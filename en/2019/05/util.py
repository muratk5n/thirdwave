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
