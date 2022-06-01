import pandas as pd, datetime, numpy as np
import requests, urllib.parse, json
from pandas_datareader import data, wb

def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(1970, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

