import time as timelib, geocoder, folium
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pandas as pd, numpy as np, json
from pandas_datareader import data
from shapely.ops import unary_union
import geopandas as gpd, re, datetime
import urllib.request as urllib2
from io import BytesIO

def get_pd(): return pd

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

def map_loc(names, outfile):
    coords = [geocoder.osm(x).latlng for x in names]
    m = folium.Map(location=coords[0], zoom_start=6)	
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
    "Polígono 97",
    "Polígono 106",
    "Polígono 109",
    "Polígono 110",
    "Polígono 118",
    "Polígono 119",
    "Polígono 122",
    "Polígono 124",
    "Polígono 125",
    "Polígono 127",
    "Polígono 130"
]

def prepare_sahel_suriyak():
    """
    Data from https://www.google.com/maps/d/u/0/viewer?mid=19IxdgUFhNYyUIXEkYmQgmaYHz6OTMEk
    97,106,109,110,118,119,122,124,125,127,130
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
    
    rrr = list(res.geoms[0].exterior.coords)

    c = np.array(rrr)
    plt.plot(c[:,0].T,c[:,1].T)
    plt.savefig('/tmp/out.jpg')    
    
    fout = open("/tmp/out.json","w")
    fout.write(str(rrr).replace("(","[").replace(")","]"))
    fout.close()


regs = [
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
    "Zaporizhia-Russian Armed Forces",
    "Kherson-Russian Armed Forces",
    "Nykolaiv-Russian Forces"]

def prepare_ukraine_suriyak():
    """
    Data from https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV
    Code searches coordinate blocks by name. Must rename some like Central Donetsk,
    or East Luhansk inside the kml file which repeat, I add 2, 3, at the end. 
    """
    content = open("/tmp/ukraine.kml").read()
    polys = []
    for i,reg in enumerate(regs):
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
    
    rrr = list(res.geoms[0].exterior.coords)

    rrr = rrr[0:-3700]
    c = np.array(rrr)
    plt.plot(c[:,0].T,c[:,1].T)
    plt.savefig('/tmp/out.jpg')    
    
    fout = open("/tmp/out.json","w")
    fout.write(str(rrr).replace("(","[").replace(")","]"))
    fout.close()

if __name__ == "__main__": 

    prepare_ukraine_suriyak()
    #prepare_sahel_suriyak()
    