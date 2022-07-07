import pandas as pd, requests, datetime
from datetime import date

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


