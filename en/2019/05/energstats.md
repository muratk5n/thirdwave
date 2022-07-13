# Energy Stats

### Oil Price (Futures, Continuous Contract, Front Month)

```python
import pandas as pd, datetime, time as timelib
import urllib.request as urllib2, io

end = datetime.datetime.now()
start = datetime.datetime(1980, 1, 1)
start = int(timelib.mktime(start.timetuple()))
end = int(timelib.mktime(end.timetuple()))
base_fin_url = "https://query1.finance.yahoo.com/v7/finance/download"
url = base_fin_url + "/CL=F?period1=" + str(start) + "&period2=" + \
      str(end) + "&interval=1d&events=history&includeAdjustedClose=true"
r = urllib2.urlopen(url).read()
file = io.BytesIO(r)
df = pd.read_csv(file,index_col='Date',parse_dates=True)['Close']

print (df.tail(5))
plt.plot(df.tail(1).index, df.tail(1),'ro')
df.plot()
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
plt.savefig('oil.png')
```

```text
Date
2022-06-13    120.930000
2022-06-14    118.930000
2022-06-15    115.309998
2022-06-16    117.589996
2022-06-17    109.300003
Name: Close, dtype: float64
```

![](oil.png)

<a name="opec"></a>

### Opec Oil Production

```python
import pandas as pd, requests
from datetime import date

api_key = open('.key/.eiakey').read()
url = 'https://api.eia.gov/series/?api_key=' + api_key + '&series_id=STEO.COPR_OPEC.M' 
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
df[1].plot()
print (df[1].tail(5))
plt.legend(['Oil Production Per Month (mil barrels per day)'])
plt.savefig('opec.png')
```

```text
Date
2022-02-01    28.575000
2022-03-01    28.215000
2022-04-01    28.590000
2022-05-01    28.294654
2022-06-01    28.786941
Name: 1, dtype: float64
```

![](opec.png)

<a name="natgas"></a>

### World Natural Gas Price

```python
import pandas as pd, datetime, time as timelib
import urllib.request as urllib2, io
end = datetime.datetime.now()
start=datetime.datetime(2010, 1, 1)
start = int(timelib.mktime(start.timetuple()))
end = int(timelib.mktime(end.timetuple()))
base_fin_url = "https://query1.finance.yahoo.com/v7/finance/download"
url = base_fin_url + "/NG=F?period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&events=history&includeAdjustedClose=true"
r = urllib2.urlopen(url).read()
file = io.BytesIO(r)
df = pd.read_csv(file,index_col='Date',parse_dates=True)['Adj Close']
df.plot()
plt.plot(df.tail(1).index, df.tail(1),'ro')
print (df.tail(7))
plt.savefig('natgas.png')
```

```text
Date
2022-07-05    5.523
2022-07-06    5.510
2022-07-07    6.297
2022-07-08    6.034
2022-07-11    6.426
2022-07-12    6.163
2022-07-13    6.662
Name: Adj Close, dtype: float64
```

![](natgas.png)

<a name='engconsumption'/>

### World Energy Consumption by Source, Monthly (twh)

```python
import pandas as pd, requests
from datetime import date

api_key = open('.key/.eiakey').read()

sources = ('coal','TOTAL.CLTCBUS.M'),('hydro','TOTAL.HVTCBUS.M'),\
	   ('natgas','TOTAL.NNTCBUS.M'),('oil','TOTAL.PMTCBUS.M'),\
	   ('nuclear','TOTAL.NUETBUS.M'),('solar','TOTAL.SOTCBUS.M'),\
	   ('wind','TOTAL.WYTCBUS.M')

dfall = []
descs = []
for desc,lab in sources:
    url = 'https://api.eia.gov/series/?api_key=' + api_key + '&series_id=' + lab
    r = requests.get(url)
    json_data = r.json()
    df = pd.DataFrame(json_data.get('series')[0].get('data'))
    df = pd.DataFrame(json_data.get('series')[0].get('data'))
    df['Year'] = df[0].astype(str).str[:4]
    df['Month'] = df[0].astype(str).str[4:]
    df['Day'] = 1
    df['Date'] = pd.to_datetime(df[['Year','Month','Day']])
    df = df.set_index('Date')
    df = df.rename(columns={1: desc})
    df = df[df.index > '2000-01-01-']
    df[desc] = df[desc].rolling(10).mean() * 0.293    
    descs.append(desc)
    dfall.append(df)

dfall = pd.concat(dfall,axis=1)
pd.set_option('display.max_columns', None)

dfall[descs].plot()
plt.title('Monthly World Energy Consumption (twh)')
plt.savefig('energy-sources.png')
```

![](energy-sources.png)

Looking at YoY increases per source

```python
dfeng = dfall[descs]
source = 'solar'
dfeng[source+'prev'] = dfeng[source].shift(-12)
dfeng[source+'yoy'] = (dfeng[source]-dfeng[source+'prev']) / dfeng[source+'prev'] * 100.0
print (dfeng[source+'yoy'].dropna().head(5))
```

```text
Date
2021-06-01    24.957553
2021-05-01    24.686058
2021-04-01    24.301684
2021-03-01    24.618614
2021-02-01    24.098390
Name: solaryoy, dtype: float64
```

<a name='gasolineState'/>

### US Retail Gasoline Prices per State

```python
import util

states = \
[("PET.EMM_EPM0_PTE_SCA_DPG.M","CA"),
 ("PET.EMM_EPM0_PTE_STX_DPG.M","TX"),
 ("PET.EMM_EPM0_PTE_SFL_DPG.M","FL"),
 ("PET.EMM_EPM0_PTE_SNY_DPG.M","NY"),
 ("PET.EMM_EPM0_PTE_NUS_DPG.M","USA")]
retail = [ (s[1],float(util.get_eia(s[0]).tail(1))) for s in states]
dfs = pd.DataFrame(retail); dfs.columns = ['state','price']
print (dfs)
```

```text
  state  price
0    CA  6.294
1    TX  4.670
2    FL  4.809
3    NY  4.954
4   USA  5.032
```

<a name='lng'/>

### LNG Traffic per Year

In billion cubic meters 

```python
import pandas as pd
df = pd.read_csv('lng.csv',sep=';',index_col=0)
df.plot(); plt.savefig('lng.png')
```

![](lng.png)

