import sys, os, matplotlib.pyplot as plt, pandas as pd
import re, zipfile, json, numpy as np, datetime, folium
import urllib.request, textwrap, math, requests
from timeit import default_timer as timer
from multiprocessing import Process
from shapely.geometry import Polygon
from shapely.ops import unary_union
from pandas_datareader import data
from functools import lru_cache
from datetime import timedelta
import matplotlib.dates as mdates
from pygeodesy.sphericalNvector import LatLon

TILE = "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png"

baci_dir = "/opt/Downloads/baci"

def get_pd(): return pd

def get_json(): return json

def trump_approval():
    # https://www.realclearpolling.com/polls/approval/donald-trump/approval-rating
    # LV = Likely Voters, RV = Registered Voters
    df = pd.read_csv('djt_approval.csv',index_col='Date')
    df.index = pd.to_datetime(df.index,format='%d-%m-%Y')
    df['net'] = df.Approve - df.Disprove
    df['net'].plot(grid=True,title='POTUS Net Approval - ' + datetime.datetime.now().strftime("%m/%d"))
    plt.savefig('/tmp/approval.jpg')

def beckley(country1, country2):   
   df1 = pd.read_csv('imf1.csv',sep='|',index_col="Country")
   df2 = pd.read_csv('pop1.csv',index_col="country")
   
   gdp1 = df1.loc[country1,"2024"]
   pop1 = df2.loc[country1,"pop2023"]

   gdp2 = df1.loc[country2,"2024"]
   pop2 = df2.loc[country2,"pop2023"]

   m1 = (float(gdp1)/float(pop1))*float(gdp1)*1e6
   m2 = (float(gdp2)/float(pop2))*float(gdp2)*1e6
   print (np.round(m1 / m2,2))
   
def flip_c(arg):
    return [[x[1],x[0]] for x in arg]

def eq_at(lat,lon,radius,ago,today=datetime.datetime.now()):

    lat1,lon1 = to_bearing(lat,lon,np.deg2rad(45),radius)
    lat2,lon2 = to_bearing(lat,lon,np.deg2rad(225),radius)
    minx=np.min((lon1,lon2))
    maxx=np.max((lon1,lon2))
    miny=np.min((lat1,lat2))
    maxy=np.max((lat1,lat2))
    today = datetime.datetime.now()
    start = today - datetime.timedelta(days=ago)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=5.0&orderby=time&limit=3000'
    req = req % (start.isoformat(), today.isoformat(),miny,maxy,minx,maxx)
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        sd = d.strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        diff = (today-d).days+1
        res.append([sd,s,lat,lon,diff])

    df = pd.DataFrame(res).sort_values(by=0)
    df.columns = ['date','mag','lat','lon','ago']
    df = df.set_index('date')
    res = dict((k + " magnitude:" + str(v['mag']),
                [v['lat'],v['lon']]) for k,v in df.iterrows())    
    return res

def elev_at(lat,lon):
    data = '[[%f,%f]]' % (lat,lon)
    response = requests.post('https://elevation.racemap.com/api',
                             headers={'Content-Type': 'application/json',},
                             data=data)
    res = response.text
    return int(json.loads(res)[0])

def get_yahoo_ticker2(year, ticker):
    d1 = datetime.datetime.strptime(str(year) + "-01-01", "%Y-%m-%d").timestamp()
    d2 = datetime.datetime.now().timestamp()    
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%s?period1=%d&period2=%d&interval=1d&events=history&includeAdjustedClose=true" 
    url = url % (ticker,int(d1),int(d2))
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )    
    r = urllib.request.urlopen(req).read()
    res = json.loads(r)
    ts = res['chart']['result'][0]['timestamp']
    adjclose = res['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    ts = [datetime.datetime.fromtimestamp(x).strftime("%Y-%m-%d") for x in ts]
    df = pd.DataFrame(adjclose,index=pd.to_datetime(ts),columns=[ticker])
    return df

def get_yahoo_tickers(year,tickers):
    res = []; cols = []
    for ticker in tickers:
        p = get_yahoo_ticker2(year,ticker)
        res.append(p)
    
    dfall = pd.concat(res,axis=1)
    dfall.columns = tickers
    return dfall

def map_usnavy(outfile):
    df = usnavy()
    m = folium.Map(location=[0,0], zoom_start=3) 
    for i,row in df.iterrows():
        folium.Marker([row['lat'],row['lon']], popup=folium.Popup(row['name'])).add_to(m)
    m.save(outfile)    

def usnavy():
    ships = json.loads(open("usnavy.json").read())
    headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}
    base = 'https://www.vesselfinder.com/vessels/'
    data = []
    for s in ships['data']:
        resp = requests.get(base + s[2], headers=headers)  
        res = re.findall(r'"ship_lat":(.*?),"ship_lon":(.*?),"ship_cog":(.*?),"ship_sog":(.*?),',resp.text)
        if len(res)>0:
           row = list(s) + list(res[0])
           data.append(row)
    df = pd.DataFrame(data)
    df.columns = ['code','name','code2','lat','lon','bearing','speed']
    return df

def scrape_gfp():
    reg = '<span class="textLarge textYellow textBold textShadow">(.*?)</span>.*?<span class="textWhite textShadow">(.*?)\t*?</span>'
    countries = ['United States of America','Switzerland','Norway','Ireland','Qatar','Singapore','Denmark','Australia','Sweden','Netherlands','Austria','Finland','Germany','Belgium','Canada','United Arab Emirates','United Kingdom','New Zealand','Israel','France','Japan','Italy','Kuwait','Spain','Slovenia','Bahrain','Portugal','Saudi Arabia','Estonia','Czech Republic','Greece','Slovakia','Lithuania','Latvia','Uruguay','Oman','Hungary','Venezuela','Chile','Panama','Poland','Croatia','Romania','Argentina','Malaysia','Russia','Grenada','Kazakhstan','China','Mexico','Turkey','Bulgaria','Brazil','Montenegro','Cuba','Lebanon','Botswana','Dominican Republic','Gabon','Thailand','Serbia','Libya','Turkmenistan','Peru','Colombia','South Africa','Ecuador','Belarus','Suriname','Bosnia and Herzegovina','Namibia','Iraq','Paraguay','Iran','Albania','Azerbaijan','Georgia','Guatemala','Jordan','Armenia','Mongolia','Algeria','Sri Lanka','El Salvador','Indonesia','Bolivia','Tunisia','Angola','Bhutan','Moldova','Morocco','Philippines','Ukraine','Vietnam','Egypt','Laos','Honduras','Ghana','Zimbabwe','Nicaragua','Nigeria','India','Kenya','Bangladesh','Zambia','Cameroon','Uzbekistan','Cambodia','Pakistan','Myanmar','Kyrgyzstan','Mauritania','Tanzania','Nepal','Sudan','Yemen','Mali','Tajikistan','Ethiopia','Chad','Burkina Faso','Liberia','Uganda','Sierra Leone','Madagascar','Afghanistan','Mozambique','Central African Republic','Niger','Somalia']
    sl = []
    for c in countries:
        ck = c.replace(" ","-").lower()
        url = "https://www.globalfirepower.com/country-military-strength-detail.php?country_id=%s" % ck        
        print (url)
        resp = requests.get(url)
        fout = open("/tmp/gfp.html","w")
        fout.write(resp.text)
        fout.close()
        content = open("/tmp/gfp.html").read()        
        res = re.findall(reg, content, re.DOTALL)
        d = {}
        d['country'] = c
        for x in res:
            a,b = x[0],x[1]
            b = re.sub('\s\t.*?','',b)
            b = re.sub('<span class.*?$','',b)
            b = re.sub('\s*<br />.*?','',b)
            a = a.replace("*","")
            a = a.replace(":","")
            b = b.replace("Stock:","")
            d[a] = b

        row = pd.Series(d)
        sl.append(row)
        
    df = pd.concat(sl,axis=1)
    df = df.T
    df.to_csv('gfp-2025.csv')
      
def download_dataframe(url, outdir):
    fname = os.path.basename(url)
    baseurl = os.path.dirname(url)
    target_file = outdir + "/" + fname
    url = baseurl + "/" + fname
    if not os.path.isfile(target_file):
        r = requests.get(url, allow_redirects=True)
        fout = open(target_file, 'wb')
        fout.write(r.content)
        fout.close()
    df = pd.read_csv(target_file)
    print (len(df), 'rows downloaded')
    return df
        

def map_eq(lat, lon, radius, ago, outfile="/tmp/out.html", today=datetime.datetime.now()):

    lat1,lon1 = to_bearing(lat,lon,np.deg2rad(45),radius)
    lat2,lon2 = to_bearing(lat,lon,np.deg2rad(225),radius)
    minx=np.min((lon1,lon2))
    maxx=np.max((lon1,lon2))
    miny=np.min((lat1,lat2))
    maxy=np.max((lat1,lat2))
    today = datetime.datetime.now()
    start = today - datetime.timedelta(days=ago)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=1.0&orderby=time&limit=3000'
    req = req % (start.isoformat(), today.isoformat(),miny,maxy,minx,maxx)
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        sd = d.strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        diff = (today-d).days+1
        res.append([sd,s,lat,lon,diff])

    df = pd.DataFrame(res).sort_values(by=0)
    df.columns = ['date','mag','lat','lon','ago']
    df = df.set_index('date')    

    m = folium.Map(location=[lat,lon], zoom_start=6) 
    folium.TileLayer(tiles=TILE,
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for i, row in df.iterrows():
        folium.CircleMarker([row['lat'],row['lon']],
                            color='red',
                            tooltip=str(row['mag']) + " (" + str(row['ago']) + " days ago)",
                            radius=2.0).add_to(m)        
    m.save(outfile)    

def to_bearing(lat,lon,brng,d):
    R = 6378.1 #Radius of the Earth
    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    return lat2,lon2

def map_coords(coords, lines={}, zoom=5, colors={}, outfile="/tmp/out.html"):
    m = folium.Map(location=coords[list(coords.keys())[0]], zoom_start=zoom)	
    folium.TileLayer(tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png",
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for key,val in coords.items():
        folium.Marker(val, popup=folium.Popup(key, show=True)).add_to(m)
    for key,val in lines.items():
        c = colors[key] if key in colors else "blue"
        folium.PolyLine(val, color=c, popup=folium.Popup(key, show=True)).add_to(m)
    m.save(outfile)
    
def boxofficemojo(q):
    q = q.replace(" ","+").lower()
    url = "https://www.boxofficemojo.com/search/?q=" + q
    res = urllib.request.urlopen(url).read().decode('utf-8')
    reres = re.findall('a-size-medium a-link-normal a-text-bold" href="(.*?)"',res)
    url2 = "https://www.boxofficemojo.com" + reres[0]
    res2 = urllib.request.urlopen(url2).read().decode('utf-8')
    regex2 = 'a-section a-spacing-none mojo-performance-summary-table.*?Domestic.*?money">(.*?)<'
    domestic = re.findall(regex2,res2,re.DOTALL)[0]
    regex2 = 'a-section a-spacing-none mojo-performance-summary-table.*?International.*?money">(.*?)<'
    intl = re.findall(regex2,res2,re.DOTALL)[0]
    regex2 = 'a-section a-spacing-none mojo-performance-summary-table.*?Worldwide.*?money">(.*?)<'
    worldwide = re.findall(regex2,res2,re.DOTALL)[0]
    regex2 = 'Domestic Opening.*?money">(.*?)<'
    domopen = re.findall(regex2,res2,re.DOTALL)[0]
    regex2 = '<span>Earliest Release Date</span><span>(.*?)\n.*?</span>'
    reldate = re.findall(regex2,res2,re.DOTALL)[0]
    return {"Domestic Opening": domopen, "Domestic": domestic,
            "International": intl, "Worldwide Total": worldwide,
            "Release Date": reldate}

def rottentomatoes(movie):
   rel = movie.replace(" ","_").lower()
   url = "https://www.rottentomatoes.com"
   url = url + "/m/" + rel
   hdr = {'User-Agent':'Mozilla/5.0'}
   c = urllib.request.urlopen(url).read().decode('utf-8')
   scores = re.findall('criticsScore.*?\>(\d\d)%\</rt-text\>',c,re.DOTALL)
   return {"critics": scores[0], "audience": scores[1]}

def modis_fire(lat,lon,dt,threshold,outfile):
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv"
    f = 'MODIS_C6_1_Global_7d.csv'
    if not os.path.isfile("/tmp/" + f):
        data = urllib.request.urlretrieve(url + "/" + f, "/tmp/" + f)
    THRESHOLD = 420.0
    df = pd.read_csv('/tmp/MODIS_C6_1_Global_7d.csv',index_col="acq_date")
    df = df[df.index > dt]
    df = df[df['brightness'] > threshold]
    df['brightness'] = 1.0 - (df['brightness'] / df['brightness'].max())
    m = folium.Map(location=[lat,lon], zoom_start=10) 
    folium.TileLayer(tiles=TILE,
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for i, row in df.iterrows():
        folium.CircleMarker([row['latitude'],row['longitude']],
                            color='red',
                            radius=2.0).add_to(m)        
    m.save(outfile)

def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

def lineproc(file_name,chunk_i,N,hookobj,skip_lines=0):
    file_size = os.path.getsize(file_name)
    hookobj.infile = file_name # lineprocessor object
    hookobj.chunk = chunk_i
    with open(file_name, 'r') as f:
        for j in range(skip_lines): f.readline()
        beg = f.tell()
        f.close()
    chunks = []
    for i in range(N):
        with open(file_name, 'r') as f:
            s = int((file_size / N)*(i+1))
            f.seek(s)
            f.readline()
            end_chunk = f.tell()-1
            chunks.append([beg,end_chunk])
            f.close()
        beg = end_chunk+1
    c = chunks[chunk_i]
    with open(file_name, 'r') as f:
        f.seek(c[0])
        while True:
            line = f.readline()
            hookobj.exec(line) # process the line
            if f.tell() > c[1]: break
        f.close()
        hookobj.post()    

    
class TJobTotal:
    def __init__(self):
        self.infile = "" # to be set from process
        self.chunk = -1 # to be set from process
        self.V = {}
        self.header = {'t':0,'i':1,'j':2,'k':3,'v':4,'q':5}
    def exec(self,line):        
        tok = line.strip().replace(' ','').split(',')
        i,j = tok[self.header['i']], tok[self.header['j']]
        i,j = int(i),int(j)
        v = float(tok[self.header['v']])
        q = tok[self.header['q']]
        prod = tok[self.header['k']]
        key = "%d-%d" % (i,j)
        if key not in self.V:
           self.V[key] = v
        else:
           self.V[key] += v
                      
    def post(self):
        print (self.infile)
        
        fout = open(baci_dir + "/out-totals.json","w")
        fout.write(json.dumps(self.V))
        fout.close()
        
def baci_process_total_exports():
    file_name = baci_dir + "/BACI_HS22_Y2022_V202401b.csv"
    #file_name = baci_dir + "/in.csv"
    start = timer()
    N = 1 # number of parallel tasks
    ps = [Process(target=lineproc,args=(file_name, i, N, TJobTotal(),1)) for i in range(N)]
    for p in ps: p.start()
    for p in ps: p.join()
    end = timer()
    print('elapsed time', timedelta(seconds=end-start))


@lru_cache(maxsize=1) # returned types are cached
def init_baci():
   baci_cc = pd.read_csv(baci_dir + '/country_codes_V202401b.csv',index_col='country_name')
   baci_pc = pd.read_csv(baci_dir + '/product_codes_HS22_V202401b.csv',index_col='code')
   baci_p = json.loads(open(baci_dir + "/out-p.json").read())
   baci_v = json.loads(open(baci_dir + "/out-v.json").read())
   baci_totals = json.loads(open(baci_dir + "/out-totals.json").read())
   return baci_cc, baci_pc, baci_p, baci_v, baci_totals

def baci_top_product(frc, toc):
    baci_cc, baci_pc, baci_p, baci_v, baci_totals = init_baci()
    key = "%d-%d" % (baci_cc.loc[frc].country_code, baci_cc.loc[toc].country_code)
    print('$', f"{baci_v[key]*1000:,}")
    s = baci_pc.loc[int(baci_p[key])].description
    for x in textwrap.wrap(s, width=70):
    	print (x)
    
def baci_all_products(frc, toc):
    baci_cc, baci_pc, baci_p, baci_v, baci_totals = init_baci()
    key = "%d-%d" % (baci_cc.loc[frc].country_code, baci_cc.loc[toc].country_code)
    amt = baci_totals[key]*1000
    print('$', f"{amt:,}")
    #return amt
    
if __name__ == "__main__": 
    
    if sys.argv[1] == "approv":
        trump_approval()
    if sys.argv[1] == "usnavy":
        map_usnavy("/tmp/navy.html")
