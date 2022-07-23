import datetime, time as timelib
import urllib.request as urllib2
import pandas as pd, requests, datetime
from io import BytesIO
from datetime import date

def get_yahoofin(year,ticker):
    end = datetime.datetime.now()
    start = datetime.datetime(1980, 1, 1)
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

def get_bp_country(country):
    fin = 'bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index > 1980]
    
    df = df[['wind_twh','solar_twh','oilprod_kbd','nuclear_twh','hydro_twh',\
             'gasprod_ej','coalprod_ej','coalcons_ej','gascons_ej','oilcons_ej']]

    df['oil_twh'] = df.oilprod_kbd * 365 * 1700 * 1000 / 1e9
    df['coal_twh'] = df.coalprod_ej * 277.778
    df['gasprod_twh'] = df.gasprod_ej * 277.778
    df['oil_imp_twh'] = (df.oilcons_ej * 277.778) - df.oil_twh.fillna(0)
    df['gas_imp_twh'] = (df.gascons_ej * 277.778) - df.gasprod_twh.fillna(0)
    df['coal_imp_twh'] = (df.coalcons_ej * 277.778) - df.coal_twh.fillna(0)
    cols = [x for x in df.columns if '_twh' in x]
    df = df[cols].fillna(0)
    df2 = df[cols].tail(1).unstack()
    df2 = (df2 / df2.sum())*100.0
    df2 = df2.dropna()
    return df2

