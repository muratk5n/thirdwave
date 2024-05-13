import time as timelib, geocoder, folium
import matplotlib.pyplot as plt, os, shutil, sys
from shapely.geometry import Polygon
import pandas as pd, numpy as np, json, requests
from pandas_datareader import data
from shapely.ops import unary_union
import geopandas as gpd, re, datetime, math
import urllib.request as urllib2, urllib.request
from io import BytesIO

TILE = "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png"

def get_pd(): return pd

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
    
def rottentomatoes(movie):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    url = url + "/m/" + rel
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    
    tom = re.findall('"audienceScore":{.*?}',res,re.DOTALL)
    d1 = json.loads("{" + tom[0] + "}")
    tom = re.findall('"tomatometerScoreAll":{.*?}',res,re.DOTALL)
    d2 = json.loads("{" + tom[0] + "}")
    return {"tomatometer score": d2['tomatometerScoreAll']['value'], "audience score": d1['audienceScore']['value'] }

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

sudan_regs = [
    "RSF-N.Kordofan",
    "RSF- White Nile",
    "RSF-Khartoum",
    "RSF-Gezira",
    "RSF-W.Kordofan",
    "RSF-S.Darfur",
    "RSF-N.Darfur",
    "RSF-C.Darfur",
    "RSF-W. Darfur",
    "RSF-W. Darfur 2",
    "RSF-Sennar",
    "RSF-E.Darfur"
]

def prepare_sahel_suriyak():
    """
    Data from https://www.google.com/maps/d/u/0/viewer?mid=19IxdgUFhNYyUIXEkYmQgmaYHz6OTMEk
    """    
    content = open("/tmp/sahel.kml").read()
    polys = []
    for i,reg in enumerate(sudan_regs):
        q = "<Placemark>.*?" + reg + "(.*?)</Placemark>"
        print (q)
        res = re.findall(q, content,re.DOTALL)
        res = res[0]
        res2 = re.findall("<coordinates>(.*?)</coordinates>", res,re.DOTALL)
        for r in res2:
            tmp = r.split(",0")
            coords = [x.strip().split(",") for x in tmp if len(x.strip()) > 8]
            coords = [[float(x),float(y)] for x,y in coords]
            polys.append(Polygon(coords))

    res = unary_union(polys)
    rrr = list(res.exterior.coords)

    c = np.array(rrr)
    plt.plot(c[:,0].T,c[:,1].T)
    plt.savefig('/tmp/out.jpg')    
    
    fout = open("/tmp/out.json","w")
    fout.write(str(rrr).replace("(","[").replace(")","]"))
    fout.close()


regs = [
    "S..Zaporizhia-Russian Armed Forces",
    "E..Zaporizhia-Russian Armed Forces",
    "Luhansk People's Republic \(North Luhansk\)",
    "Luhansk People's Republic \(East Luhansk\)",
    "Luhansk People's Republic \(East Luhansk 2\)",
    "Luhansk People's Republic \(West Luhansk\)",
    "Luhansk People's Republic \(South Luhansk\)",
    "Donetsk People's Republic \(Central Donetsk\)",
    "Donetsk People's Republic \(Central Donetsk 2\)",
    "Donetsk People's Republic \(Central Donetsk 3\)",
    "Donetsk People's Republic \(Central Donetsk 4\)",
    "Donetsk People's Republic \(East Donetsk\)",
    "Donetsk People's Republic \(West Donetsk\)",
    "Donetsk People's Republic \(South Donetsk\)",
    "E.Kharkiv-Russian Armed Forces",
    "Kherson-Russian Armed Forces",
    "Nykolaiv-Russian Forces"]

reg_ext1 = "N.Kharkiv-Russian Armed Forces"
reg_ext2 = "N.Kharkiv-Russian Armed Forces 2"

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

def prepare_ukraine_suriyak():
    """
    Data from https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV
    Code searches coordinate blocks by name. Must rename some like Central Donetsk,
    or East Luhansk inside the kml file which repeat, I add 2, 3, at the end. 
    """
    content = open("/tmp/ukraine.kml").read()

    rrrs = []
    
    cext1_coords = get_coords_for_label(content, reg_ext1)
    rrrs.append(np.array(cext1_coords))
    cext2_coords = get_coords_for_label(content, reg_ext2)
    rrrs.append(np.array(cext2_coords))
    
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
        plt.plot(x[:,0].T,x[:,1].T)
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

    prepare_ukraine_suriyak()
    #prepare_sahel_suriyak()
    
