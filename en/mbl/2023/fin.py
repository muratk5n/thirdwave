from pandas_datareader import data, wb
import datetime, time as timelib
import urllib.request as urllib2
import pandas as pd, requests, datetime
from io import BytesIO
from datetime import date
import matplotlib.pyplot as plt, re, json
from pygeodesy import parse3llh, fstr

def geoname(keyword, ccode):
    url = "http://www.geonames.org/search.html?q=%s&country=%s" % (keyword,ccode)    
    url = url.replace(" ","+")
    print (url)
    r = urllib2.urlopen(url).read()
    content = r.decode('utf-8')
    res = re.findall("Latitude.*?<td nowrap>(.*?)</td><td nowrap>(.*?)</td>",content, re.DOTALL)
    lats = res[0][1]; lons = res[0][0]
    lats = lats[1:] + lats[0]
    lons = lons[1:] + lons[0]
    geos = lats + "," + lons
    x = parse3llh(geos)
    res = fstr(x, prec=6).split(",")
    return float(res[0]),float(res[1])

def two_plot(df, col1, col2):
    plt.figure(figsize=(12,5))
    ax1 = df[col1].plot(color='blue', grid=True, label=col1)
    ax2 = df[col2].plot(color='red', grid=True, label=col2,secondary_y=True)
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2) 

def get_quandl(series):
    import quandl, os
    fname = '.key/.quandl'
    auth = open(fname).read()
    df = quandl.get(series, returns="pandas",authtoken=auth)
    return df
    
def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

