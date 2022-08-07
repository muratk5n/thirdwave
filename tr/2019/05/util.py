from pandas_datareader import data, wb
import datetime, time as timelib
import urllib.request as urllib2
import pandas as pd, datetime, numpy as np, requests
from io import BytesIO

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

def country_bp(country):
    df, prod_perc, tot = util.get_bp_country(country)
    print (df)
    print ('\nProduction As Percentage of Consumption\n')
    print (prod_perc)
    print ('\nTotal\n')
    print (np.round(tot*1000 / (365*24),2),'GW')

def get_bp_country(country):
    fin = '../../../en/2019/05/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index == df.index.max()]    
    df = df[['wind_twh','solar_twh','nuclear_twh','hydro_twh',\
             'coalcons_ej','gascons_ej','oilcons_ej','biogeo_ej']]
    df['oil_twh'] = (df.oilcons_ej * 277.778)
    df['gas_twh'] = (df.gascons_ej * 277.778)
    df['coal_twh'] = (df.coalcons_ej * 277.778)
    df['biogeo_twh'] = (df.biogeo_ej * 277.778)
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
    
    return df2, pd.DataFrame(prod_perc,columns=['Perc','Commodity']), total
