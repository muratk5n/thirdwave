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

TILE = "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png"

baci_dir = "/opt/Downloads/baci"

def get_pd(): return pd

def elev_at(lat,lon):
    data = '[[%f,%f]]' % (lat,lon)
    response = requests.post('https://elevation.racemap.com/api',
                             headers={'Content-Type': 'application/json',},
                             data=data)
    res = response.text
    return int(json.loads(res)[0])

def get_yahoo_ticker2(year, ticker):
    d1 = datetime.datetime.strptime(str(year) + "-09-01", "%Y-%m-%d").timestamp()
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

def map_coords(coords, zoom, outfile):
    m = folium.Map(location=coords[list(coords.keys())[0]], zoom_start=zoom)	
    folium.TileLayer(tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png",
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for key,val in coords.items():
        folium.Marker(val, popup=folium.Popup(key, show=True)).add_to(m)
    m.save(outfile)


def trump_approval():
    import matplotlib.dates as mdates
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/approval_averages.csv')
    df2 = df[['pct_estimate','answer','date']]
    df2 = df2[df['politician/institution'] == 'Donald Trump']
    df2 = df2.pivot_table(columns='answer',index='date')
    df2['net'] = df2['pct_estimate']['Approve'] - df2['pct_estimate']['Disapprove']
    print (df2['net'])
    df2['net'].plot(grid=True,title='POTUS Net Approval - ' + datetime.datetime.now().strftime("%m/%d"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.savefig('/tmp/approval.jpg')

    
def boxofficemojo(q):
    q = q.replace(" ","+").lower()
    url = "https://www.boxofficemojo.com/search/?q=" + q
    res = urllib.request.urlopen(url).read().decode('utf-8')
    reres = re.findall('a-size-medium a-link-normal a-text-bold" href="(.*?)"',res)
    url2 = "https://www.boxofficemojo.com" + reres[0]
    print (url2)    
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

def get_coords_for_label(content, reg):
    q = "<Placemark>.*?" + reg + "(.*?)</Placemark>"
    print (q)
    res = re.findall(q, content,re.DOTALL)
    res = res[0]
    res2 = re.findall("<coordinates>(.*?)</coordinates>", res,re.DOTALL)
    tmp = res2[0].split(",0")
    coords = [x.strip().split(",") for x in tmp if len(x.strip()) > 8]
    coords = [[float(x),float(y)] for x,y in coords]
    return coords


def prep_isr_suriyak():
    # =======================================================================
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Palestine-Lebanon Map.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')                
    fout = open("/tmp/isr.kml","w")
    fout.write(content)
    fout.close()
    
def map_isr_suriyak():
    prep_isr_suriyak()
    isr_regs = ["Polígono 17"]
    
    content = open("/tmp/isr.kml").read()

    rrrs = []
    for i,reg in enumerate(isr_regs):
        coords = get_coords_for_label(content, reg)
        rrrs.append(coords)
    print (len(rrrs[0]))
    total = []
    #total += rrrs[0][0:200]
    #total += rrrs[0][400:600]
    total += rrrs[0][700:910]
    total += rrrs[0][0:535]
    rrrs[0] = total
        
    for x in rrrs:
        xx = np.array(x)
        plt.plot(xx[:,0].T,xx[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
        
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()


def prep_sahel():
    ###########################################################################33333333
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Sahel.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 1<",
                             content,count=1)

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 2<",
                             content,count=1)
        
    fout = open("/tmp/sahel.kml","w")
    fout.write(content)
    fout.close()

def map_sahel_suriyak():
    """
    Data from https://www.google.com/maps/d/u/0/viewer?mid=19IxdgUFhNYyUIXEkYmQgmaYHz6OTMEk
    """
    prep_sahel()

    sudan_regs1 = [
        "RSF-N.Kordofan",
        "RSF- White Nile",
        "RSF-Khartoum",
        "RSF-Gezira",
        "RSF-W.Kordofan",
        "RSF-S.Darfur",
        "RSF-N.Darfur",
        "RSF-C.Darfur",
        "RSF-W. Darfur 1",
        "RSF-W. Darfur 2",
        "RSF-E.Darfur",
        "RSF-W.Kordofan"]
    
    content = open("/tmp/sahel.kml").read()

    rrrs = []              
    polys = []              
    for i,reg in enumerate(sudan_regs1):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)

    sudan_regs2 = [
        "RSF-Sennar",
        "RSF-Blue Nile"]
    
    content = open("/tmp/sahel.kml").read()

    polys = []              
    for i,reg in enumerate(sudan_regs2):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)

    
    for x in rrrs:
        plt.plot(x[:,0].T,x[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
    
    np.set_printoptions(threshold=sys.maxsize)
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr.tolist()))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()


def prep_ukraine():
    ###########################################################################33333333
    
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Guerra Ruso-Ucraniana 2022.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 1)",
                             content,count=1)

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 2)",
                             content,count=1)

            content = re.sub("Donetsk People's Republic \(Central Donetsk\)",
                             "Donetsk People's Republic (Central Donetsk 1)",
                             content,count=1)

            content = re.sub("Donetsk People's Republic \(Central Donetsk\)",
                             "Donetsk People's Republic (Central Donetsk 2)",
                             content,count=1)

            content = re.sub("N.Kharkov-Russian Armed Forces\<",
                             "N.Kharkov-Russian Armed Forces 1<",
                             content,count=1)

            content = re.sub("N.Kharkov-Russian Armed Forces\<",
                             "N.Kharkov-Russian Armed Forces 2<",
                             content,count=1)

            content = re.sub("Kursk-Russian Armed Forces<",
                             "Kursk-Russian Armed Forces 1<",
                             content,count=1)

            content = re.sub("Kursk-Russian Armed Forces<",
                             "Kursk-Russian Armed Forces 2<",
                             content,count=1)
                    
    fout = open("/tmp/ukraine.kml","w")
    fout.write(content)
    fout.close()

    
def map_ukraine_suriyak():
    """
    Data from https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV
    """
    prep_ukraine()
    
    regs = [
        "S..Zaporizhia-Russian Armed Forces",
        "E..Zaporizhia-Russian Armed Forces",
        "Luhansk People's Republic \(North Luhansk\)",
        "Luhansk People's Republic \(East Luhansk 1\)",
        "Luhansk People's Republic \(East Luhansk 2\)",
        "Luhansk People's Republic \(West Luhansk\)",
        "Luhansk People's Republic \(South Luhansk\)",
        "Donetsk People's Republic \(Central Donetsk 1\)",
        "Donetsk People's Republic \(Central Donetsk 2\)",
        "Donetsk People's Republic \(East Donetsk\)",
        "Donetsk People's Republic \(West Donetsk\)",
        "Donetsk People's Republic \(South Donetsk\)",
        "E.Kharkov-Russian Armed Forces",
        "Kherson-Russian Armed Forces",
        "Nykolaiv-Russian Forces"]
    
    reg_ext1 = "N.Kharkov-Russian Armed Forces 1"
    reg_ext2 = "N.Kharkov-Russian Armed Forces 2"
    reg_ext3 = "Kursk-Russian Armed Forces 1"
    reg_ext4 = "Kursk-Russian Armed Forces 2"    
    
    content = open("/tmp/ukraine.kml").read()

    rrrs = []
    
    cext1_coords = get_coords_for_label(content, reg_ext1)
    rrrs.append(np.array(cext1_coords))
    cext2_coords = get_coords_for_label(content, reg_ext2)
    rrrs.append(np.array(cext2_coords))
    cext3_coords = get_coords_for_label(content, reg_ext3)
    cext4_coords = get_coords_for_label(content, reg_ext4)


    polys = []
    polys.append(Polygon(cext3_coords))
    polys.append(Polygon(cext4_coords))
    res = unary_union(polys)    
    cext3_cext4 = list(res.exterior.coords)
    cext3_cext4 = np.array(cext3_cext4)[350:1000]
    rrrs.append(cext3_cext4)
          
    polys = []
    for i,reg in enumerate(regs):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    rrr = rrr[0:-3700]
    c = np.array(rrr)
    rrrs.append(c)

    for x in rrrs:
        plt.plot(x[:,0].T,x[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
    
    np.set_printoptions(threshold=sys.maxsize)
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr.tolist()))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()

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
    #print('$', f"{amt:,}")
    return amt
    
if __name__ == "__main__": 

   #baci_process_total_exports()
   scrape_gfp()
   pass
