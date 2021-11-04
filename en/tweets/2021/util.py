import pandas as pd, datetime, time as timelib
import urllib.request as urllib2, io
import matplotlib.pyplot as plt
import pandas as pd, requests
from datetime import date

def opec_price():

    end = datetime.datetime.now()
    start = datetime.datetime(1980, 1, 1)
    start = int(timelib.mktime(start.timetuple()))
    end = int(timelib.mktime(end.timetuple()))
    base_fin_url = "https://query1.finance.yahoo.com/v7/finance/download"
    url = base_fin_url + "/CL=F?period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&events=history&includeAdjustedClose=true"
    r = urllib2.urlopen(url).read()
    file = io.BytesIO(r)
    df2 = pd.read_csv(file,index_col='Date',parse_dates=True)['Close']

    api_key = open('../../2019/05/.eiakey').read()
    final_data = []
    startDate = '2009-01-01'
    endDate = '2021-01-01'

    url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=STEO.COPR_OPEC.M' 
    r = requests.get(url)
    json_data = r.json()

    df = pd.DataFrame(json_data.get('series')[0].get('data'))

    df['Year'] = df[0].astype(str).str[:4]
    df['Month'] = df[0].astype(str).str[4:]
    df['Day'] = 1
    df['Date'] = pd.to_datetime(df[['Year','Month','Day']])
    df = df.set_index('Date')

    df3 = pd.merge(df, df2, left_index=True, right_index=True, how='left')
    df3 = df3[[1,'Close']]
    df3 = df3.dropna(axis=0)

    ax1 = df3[1].plot(color='blue', grid=True, label='Production')
    ax2 = df3.Close.plot(color='red', grid=True, label='Price',secondary_y=True)
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)
    plt.savefig('opec-price.png')

if __name__ == "__main__":
    
    opec_price()


    
