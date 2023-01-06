import pandas as pd, datetime, numpy as np, requests
import requests, urllib.parse, json
from pandas_datareader import data, wb
import matplotlib.pyplot as plt, math
import simplegeomap as sm, util
import datetime, time as timelib, re, os
import urllib.request as urllib2
from io import BytesIO
import pandas_ta as ta


def crime_vio_state(state):
   # ['burglary','larceny','motor-vehicle-theft','arson']
   cols = ['homicide','rape','robbery','aggravated-assault']
   d = "/opt/Downloads/fbi/fbi-data"
   data = []
   for i in range(1999,2022):
      f = d + '/csv/%d.csv' % i
      if os.path.exists(f) == False: continue
      df = pd.read_csv(f,na_values=['-',' '],skipinitialspace=True)
      df = df[df.state.str.lower() == state.lower()]
      df = df[cols]
      df = df.fillna(0)
      data.append([i,df.sum().sum()])
   df = pd.DataFrame(data)
   df.columns = ['year','crime']
   df = df.set_index('year')
   pop = pd.read_csv(d + '/uspop.csv',index_col=0)
   df['pop'] = pop
   df['rate'] = (df['crime'] / df['pop']) * 100000
   return df

def covid_hospitalization():
   df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv',parse_dates=True)
   df = df[df.indicator == 'Daily hospital occupancy per million']
   df = df[['date','entity','value']]
   df.columns = ['date','country','Daily hospital occupancy per million']
   df = df.set_index('date')
   return df

def boxofficemojo(q):
    q = q.replace(" ","+").lower()
    url = "https://www.boxofficemojo.com/search/?q=" + q
    res = urllib2.urlopen(url).read().decode('utf-8')
    reres = re.findall('a-size-medium a-link-normal a-text-bold" href="(.*?)"',res)
    url2 = "https://www.boxofficemojo.com" + reres[0]
    print (url2)
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

