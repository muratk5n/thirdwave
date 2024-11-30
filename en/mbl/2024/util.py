import time as timelib, geocoder, folium, zipfile, textwrap
import matplotlib.pyplot as plt, os, shutil, sys
from shapely.geometry import Polygon
import pandas as pd, numpy as np, json, requests
from pandas_datareader import data
from shapely.ops import unary_union
import geopandas as gpd, re, datetime, math
import urllib.request as urllib2, urllib.request
from io import BytesIO

from functools import lru_cache
from timeit import default_timer as timer
from multiprocessing import Process
from datetime import timedelta
from collections import defaultdict

TILE = "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png"

def get_pd(): return pd

#url = "https://morningconsult.com/global-leader-approval"

def get_yahoo_ticker2(year, ticker):
    d1 = datetime.datetime.strptime(str(year) + "-09-01", "%Y-%m-%d").timestamp()
    d2 = datetime.datetime.now().timestamp()
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%s?period1=%d&period2=%d&interval=1d&events=history&includeAdjustedClose=true" 
    url = url % (ticker,int(d1),int(d2))
    r = urllib2.urlopen(url).read()
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

def eq_at(lat,lon,radius,ago,today = datetime.datetime.now()):

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
    return df

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


def kh_djt_538_polls():

    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/president_polls.csv')
    cols = ['poll_id','sample_size','answer','pct','end_date']

    dfs = df[df.answer == 'Harris'].copy()
    dfs['harris_share'] = dfs.sample_size * dfs.pct / 100.
    dfs['Date'] = pd.to_datetime(dfs.end_date)
    g1 = dfs.groupby('Date').sum(['sample_size','harris_share'])
    g1 = g1[g1.index > '2024-08-15']
    g1['harris_pct'] = g1.harris_share / g1.sample_size

    dfs = df[df.answer == 'Trump'].copy()
    dfs['trump_share'] = dfs.sample_size * dfs.pct / 100.
    dfs['Date'] = pd.to_datetime(dfs.end_date)
    g2 = dfs.groupby('Date').sum(['sample_size','trump_share'])
    g2 = g2[g2.index > '2024-08-15']
    g2['trump_pct'] = g2.trump_share / g2.sample_size

    dfall = pd.concat([g1,g2],axis=1)
    dfall = dfall[['trump_pct','harris_pct']]
    #dfall.drop(dfall.tail(1).index,inplace=True)
    dfall.plot(title='Trump & Harris Combined Polls - ' + datetime.datetime.now().strftime("%m/%d"))
    plt.savefig('/tmp/538.jpg')
    print (dfall.tail(4))

def get_quandl(year, series):
    import quandl, os
    fname = '%s/.nomterr.conf' % os.environ['HOME']
    conf = json.loads(open(fname).read())
    df = quandl.get(series, start_date=str(year)+"-01-01", returns="pandas",authtoken=conf['quandl'])
    return df

def boxofficemojo(q):
    q = q.replace(" ","+").lower()
    url = "https://www.boxofficemojo.com/search/?q=" + q
    res = urllib2.urlopen(url).read().decode('utf-8')
    reres = re.findall('a-size-medium a-link-normal a-text-bold" href="(.*?)"',res)
    url2 = "https://www.boxofficemojo.com" + reres[0]
    
    res2 = urllib2.urlopen(url2).read().decode('utf-8')
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


def get_modis_csv():
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv"
    f = 'MODIS_C6_1_Global_7d.csv'
    if not os.path.isfile("/tmp/" + f):
        data = urllib.request.urlretrieve(url + "/" + f, "/tmp/" + f)

def modis_fire(outfile):
    get_modis_csv()    
    THRESHOLD = 420.0
    df = pd.read_csv('/tmp/MODIS_C6_1_Global_7d.csv')
    df = df[df['brightness'] > THRESHOLD]
    df['brightness'] = 1.0 - (df['brightness'] / df['brightness'].max())
    m = folium.Map(location=[0,0], zoom_start=2) 
    folium.TileLayer(tiles=TILE,
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for i, row in df.iterrows():
        folium.CircleMarker([row['latitude'],row['longitude']],
                            color='red',
                            #opacity=row['brightness'],
                            radius=2.0).add_to(m)        
    m.save(outfile)
        

def household(since):
    df = get_fred(since, ['MEHOINUSA646N','TDSP','CPIAUCSL'])
    df = df.interpolate()
    df = df.dropna()

    cpi = float(df.tail(1).CPIAUCSL)
    df['cpi2'] = cpi / df.CPIAUCSL 
    df['household income'] = df.MEHOINUSA646N * df.cpi2     
    return df['household income']
    
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

def map_loc(names, zoom, outfile):
    coords = [geocoder.osm(x).latlng for x in names]
    m = folium.Map(location=coords[0], zoom_start=zoom)	
    folium.TileLayer(tiles="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png",
            name='subdomains2',
            attr='attribution',
            subdomains='mytilesubdomain'
    ).add_to(m)
    for name,coord in zip(names,coords):
        folium.Marker(coord, popup=name).add_to(m)
    m.save(outfile)

def two_plot(s1, col1, s2, col2):
    plt.figure(figsize=(12,5))
    ax1 = s1.plot(color='blue', grid=True, label=col1)
    ax2 = s2.plot(color='red', grid=True, label=col2,secondary_y=True)
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)

def get_top10(year):
    cols = ['WFRBLT01026', 'WFRBLN09053']
    df = get_fred(year,cols)
    df = df.interpolate()
    df['top10'] =  df['WFRBLT01026'] + df['WFRBLN09053'] 
    return df / 1e6
    
def get_wlt_sp():
    cols = ['WFRBLT01026', 'WFRBLN09053','WFRBLN40080','WFRBLB50107']
    df = get_fred(1970,cols)
    df = df.interpolate()
    df['Total'] =  df['WFRBLT01026'] + df['WFRBLN09053'] + df['WFRBLB50107'] + df['WFRBLN40080']
    df['Top 10%'] = (df['WFRBLT01026'] + df['WFRBLN09053']) * 100 / df.Total 
    return df

def get_yahoofin(year,ticker):
    end = datetime.datetime.now()
    start = datetime.datetime(year, 1, 1)
    start = int(timelib.mktime(start.timetuple()))
    end = int(timelib.mktime(end.timetuple()))
    base_fin_url = "https://query1.finance.yahoo.com/v7/finance/download"
    url = base_fin_url + "/%s?period1=" + str(start) + "&period2=" + \
          str(end) + "&interval=1d&events=history&includeAdjustedClose=true"
    url  = url % ticker
    r = urllib2.urlopen(url).read()
    file = BytesIO(r)
    df = pd.read_csv(file,index_col='Date',parse_dates=True)['Close']
    return df


def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

def biden_approval():
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='end_date')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df

def mov_profit(budget, gross):
  marketing = budget / 2
  return np.round(gross - (budget + marketing + gross*0.4),2)

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


baci_dir = "/opt/Downloads/baci"

class TJob:
    def __init__(self):
        self.infile = "" # to be set from process
        self.chunk = -1 # to be set from process
        self.P = {}
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
        if key not in self.V or v > self.V[key]:
            self.V[key] = v
            self.P[key] = prod
            
    def post(self):
        print (self.infile)
        fout = open(baci_dir + "/out-p.json","w")
        fout.write(json.dumps(self.P))
        fout.close()
        
        fout = open(baci_dir + "/out-v.json","w")
        fout.write(json.dumps(self.V))
        fout.close()
        
def baci_top_products():
    file_name = baci_dir + "/BACI_HS22_Y2022_V202401b.csv"
    #file_name = baci_dir + "/in.csv"

    start = timer()
    N = 1 # number of parallel tasks
    ps = [Process(target=lineproc,args=(file_name, i, N, TJob(),1)) for i in range(N)]
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
   return baci_cc, baci_pc, baci_p, baci_v

def baci_top_product(frc, toc):
    baci_cc, baci_pc, baci_p, baci_v = init_baci()
    key = "%d-%d" % (baci_cc.loc[frc].country_code, baci_cc.loc[toc].country_code)
    print('$', f"{baci_v[key]*1000:,}")
    s = baci_pc.loc[int(baci_p[key])].description
    for x in textwrap.wrap(s, width=70):
    	print (x)
        
##############################################################################    
##############################################################################    
##############################################################################    
        
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

    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Palestine-Lebanon Map.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')
            for i in range(1,11):
                content = re.sub("IDF \(Area of Operations\)- Lebanon<",
                                 "IDF (Area of Operations)- Lebanon %d<" % i,
                                 content,count=1)
                
    fout = open("/tmp/isr.kml","w")
    fout.write(content)
    fout.close()

def map_isr_suriyak():
    prep_isr_suriyak()
    isr_regs = [
        "IDF..Area of Operations...Lebanon 1",
        "IDF..Area of Operations...Lebanon 2",
        "IDF..Area of Operations...Lebanon 3",
        "IDF..Area of Operations...Lebanon 4",
        "IDF..Area of Operations...Lebanon 5",
        "IDF..Area of Operations...Lebanon 6",
        "IDF..Area of Operations...Lebanon 7",
        "IDF..Area of Operations...Lebanon 8",
        "IDF..Area of Operations...Lebanon 9"]
    
    content = open("/tmp/isr.kml").read()

    rrrs = []
    for i,reg in enumerate(isr_regs):
        coords = get_coords_for_label(content, reg)
        rrrs.append(coords)

    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()

##############################################################################    
##############################################################################    
##############################################################################    

sudan_regs2 = [
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
    "RSF-Sennar",
    "RSF-E.Darfur",
    "RSF-W.Kordofan"]

def prep_sahel():

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
    
    content = open("/tmp/sahel.kml").read()

    rrrs = []              
    polys = []              
    for i,reg in enumerate(sudan_regs2):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)
        
        #coords = np.array(coords)
        #print (coords)
        #rrrs.append(coords)

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


##############################################################################    
##############################################################################    
##############################################################################    

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

def prep_ukraine():

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
    
if __name__ == "__main__": 

    #map_ukraine_suriyak()
    #map_sahel_suriyak()
    map_isr_suriyak()
    #kh_djt_538_polls()
    
