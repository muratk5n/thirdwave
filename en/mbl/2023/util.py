import pandas as pd, datetime, numpy as np, requests
import requests, urllib.parse, json
from yahoofinancials import YahooFinancials
from pandas_datareader import data, wb
import matplotlib.pyplot as plt, math
import simplegeomap as sm, util
import datetime, time as timelib, re, os
import urllib.request as urllib2
from io import BytesIO
import pandas_ta as ta

def yf_income(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
  slist = []
  for i in range(len(data_qt['incomeStatementHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['incomeStatementHistoryQuarterly'][ticker][i]))
  df = pd.concat(slist,axis=1).T
  df['grossProfitMargin'] = df.grossProfit / df.totalRevenue * 100.0
  return df

def yf_balance(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
  slist = []
  for i in range(len(data_qt['balanceSheetHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['balanceSheetHistoryQuarterly']['DIS'][i]))
  df = pd.concat(slist,axis=1).T
  return df

def yf_cash(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'cash')
  slist = []
  for i in range(len(data_qt['cashflowStatementHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['cashflowStatementHistoryQuarterly']['DIS'][i]))
  df = pd.concat(slist,axis=1).T
  return df

def yf_eps(ticker):
  df = yf_income("DIS")  
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  shares = yahoo_financials.get_num_shares_outstanding(price_type='current')
  df = df['netIncomeApplicableToCommonShares'] / shares  
  return df

def drug_overdose_deaths():
  url = "https://data.cdc.gov/api/views/xkb8-kh2a/rows.csv?accessType=DOWNLOAD&bom=true&format=true"
  df = pd.read_csv(url)
  df = df[(df.State != 'US') & (df.Indicator == 'Number of Drug Overdose Deaths') & (df.Month == 'December')]
  df2 = df[['Year','Data Value']]
  df2['Data Value'] = df2['Data Value'].str.replace(',','')
  df2['Data Value'] = df2['Data Value'].str.replace('"','')
  df2['Data Value'] = df2['Data Value'].astype(float)
  g = df2.groupby('Year')['Data Value'].sum()
  g.plot(kind='bar',title='Deaths by Drug Overdose')
  plt.savefig('drugoverdose1.jpg',quality=30)
  
def mov_profit(budget, gross):
  marketing = budget / 2
  return gross - (budget + marketing + gross*0.4)

def covid_hospitalization():
   df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv',parse_dates=True)
   df = df[df.indicator == 'Daily hospital occupancy per million']
   df = df[['date','entity','value']]
   df.columns = ['date','country','Daily hospital occupancy per million']
   df = df.set_index('date')
   return df

def sm_plot_ukr(file,oldfile,geo):
    sm_plot_ukr_base(file,geo)    
    df = np.array(pd.read_csv(oldfile,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_line(df,color='gray',linestyle='solid')
    for label,lat,lon,s in geo:
      style=(s[0], s[1])
      plt.annotate(
        label, 
        xy = (lon, lat), xytext = style,
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
      
    
#    eps = 0.1
#    for i,(lat,lon) in enumerate(geo):
#        plt.text(lon+eps,lat-eps,i+1)
#        plt.plot(lon,lat,'g+')

    
        
def sm_plot_ukr_base(file,geo):
    df = np.array(pd.read_csv(file,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    clat,clon=48, 37; zoom = 0.6
    sm.plot_countries(clat,clon,zoom,outcolor='lavenderblush')
    sm.plot_line(df,color='red')
    
    df = np.array(pd.read_csv('ukrdata/donetsk.csv',header=None))
    sm.plot_line(df,color='pink')
    plt.text(37,48,'Donetsk',color='gray')

    df = np.array(pd.read_csv('ukrdata/kherson.csv',header=None))
    sm.plot_line(df,color='pink')
    plt.text(33,46.5,'Kherson',color='gray')

    df = np.array(pd.read_csv('ukrdata/zaporizhia.csv',header=None))
    sm.plot_line(df,color='pink')
    plt.text(35,47,'Zaporizhia',color='gray')

    plt.text(38.3,49,'Luhansk',color='gray')
    
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

