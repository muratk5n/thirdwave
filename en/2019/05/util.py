from pandas_datareader import data, wb
import datetime, time as timelib
import urllib.request as urllib2
import pandas as pd, requests, datetime
from io import BytesIO
from datetime import date
import matplotlib.pyplot as plt, re
from pygeodesy import parse3llh, fstr

def country_bp(country):
    df, prod_perc, tot, elec = util.get_bp_country(country)
    print (df)
    print ('\nProduction As Percentage of Consumption\n')
    print (prod_perc)
    print ('\nElectricity',np.round(elec,2),'%')
    print ('\nTotal\n')
    print (np.round(tot*1000 / (365*24),2),'GW')

def get_bp_country(country):
    fin = 'bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index == df.index.max()]
    elec = np.round(float(df['elect_twh']) / (float(df['primary_ej'])*277.778)*100,2)
    df = df[['wind_twh','solar_twh','nuclear_twh','hydro_twh',\
             'coalcons_ej','gascons_ej','oilcons_ej','biogeo_ej',
             'ethanol_cons_pj']]
    df['oil_twh'] = (df.oilcons_ej * 277.778)
    df['gas_twh'] = (df.gascons_ej * 277.778)
    df['coal_twh'] = (df.coalcons_ej * 277.778)
    df['biogeo_twh'] = (df.biogeo_ej * 277.778)
    df['ethanol_twh'] = (df.ethanol_cons_pj * 0.277778)
    cols = [x for x in df.columns if '_twh' in x]    
    df2 = df[cols].fillna(0).unstack()
    total = df2.sum()
    df2 = (df2 / df2.sum())*100.0
    df2 = df2.dropna()

    df3 = pd.read_csv(fin)
    df3 = df3[df3.Country == country]
    df3 = df3.set_index('Year')
    df3 = df3[df3.index == df3.index.max()]    
    df3 = df3[['oilprod_kbd','coalprod_ej','gasprod_ej']].fillna(0)
    df3['oil_twh'] = df3.oilprod_kbd * 365 * 1700 * 1000 / 1e9
    df3['coal_twh'] = df3.coalprod_ej * 277.778
    df3['gasprod_twh'] = df3.gasprod_ej * 277.778

    prod_perc = [
        (np.round(float(df3['oil_twh']) / float(df['oil_twh']) * 100,2), 'Oil'),
        (np.round(float(df3['gasprod_twh']) / float(df['gas_twh']) * 100,2), 'Gas'),
        (np.round(float(df3['coal_twh']) / float(df['coal_twh']) * 100,2), 'Coal'),
    ]
    
    return df2, pd.DataFrame(prod_perc,columns=['Perc','Commodity']), total, elec

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

def get_eia(series):
    api_key = open('.key/.eiakey').read()
    url = 'https://api.eia.gov/series/?api_key=%s&series_id=%s'
    url = url % (api_key, series)
    r = requests.get(url)
    json_data = r.json()
    df = pd.DataFrame(json_data.get('series')[0].get('data'))
    df['Year'] = df[0].astype(str).str[:4]
    df['Month'] = df[0].astype(str).str[4:]
    df['Day'] = 1
    df['Date'] = pd.to_datetime(df[['Year','Month','Day']])
    df = df.set_index('Date')
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    df = df[df.index <= today]
    df = df.sort_index()
    df = df[1]
    return df

def get_eia_week(series):
    api_key = open('.key/.eiakey').read()
    url = 'https://api.eia.gov/series/?api_key=%s&series_id=%s'
    url = url % (api_key, series)
    r = requests.get(url)
    json_data = r.json()
    df = pd.DataFrame(json_data.get('series')[0].get('data'))
    df['Date'] = pd.to_datetime(df[0])
    df['Value'] = df[1]
    df = df[['Date','Value']]
    df = df.set_index('Date')
    df = df.sort_index()
    return df
