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

def sm_plot_azearm3():
    d = json.loads(open("azerbarm1.json").read())
    clat,clon=40, 46;zoom=0.25
    colors = {"AZE": "lightcyan", "ARM":"lightyellow", "IRN":"lavenderblush", "TUR":"lavenderblush"}
    sm.plot_countries(clat,clon,zoom,country_color=colors)
    plt.text(45,40,'ARM')
    plt.text(47.5,40,'AZE')
    plt.text(46.8,39.75,'NK',color='gray')
    sm.plot_line(np.array(d['nagornarm1']),color='lightgreen')
    sm.plot_region(np.array(d['nagornarm3']),color='yellow')    
    sm.plot_line(np.array(d['lachin']),color='red')

def sm_plot_azearm2():
    d = json.loads(open("azerbarm1.json").read())
    clat,clon=40, 46;zoom=0.25
    colors = {"AZE": "lightcyan", "ARM":"lightyellow", "IRN":"lavenderblush", "TUR":"lavenderblush"}
    sm.plot_countries(clat,clon,zoom,country_color=colors)
    plt.text(45,40,'ARM')
    plt.text(47.5,40,'AZE')
    plt.text(46.8,39.75,'NK',color='gray')
    sm.plot_region(np.array(d['nagornarm21']),color='lightpink') 
    sm.plot_region(np.array(d['nagornarm22']),color='lightpink') 
    sm.plot_region(np.array(d['nagornarm1']),color='lightpink') 
    sm.plot_line(np.array(d['nagornarm1']),color='green')

def sm_plot_azearm1():
    d = json.loads(open("azerbarm1.json").read())
    clat,clon=40, 46;zoom=0.25
    colors = {"AZE": "lightcyan", "ARM":"lightyellow", "IRN":"lavenderblush", "TUR":"lavenderblush"}
    sm.plot_countries(clat,clon,zoom,country_color=colors)
    plt.text(45,40,'ARM')
    plt.text(47.5,40,'AZE')
    plt.text(46.8,39.75,'NK',color='gray')
    sm.plot_line(np.array(d['nagornarm1']),color='green')    

def biz_stock_plot(year,ticker):
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
    df.plot()

def rotom_mov(movie):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    url = url + "/m/" + rel
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    regreg = re.findall('audiencescore="(.*?)"',res)
    audiencescore = int(regreg[0])
    regreg = re.findall('tomatometerscore="(.*?)"',res)
    tomatometerscore = int(regreg[0])
    return {"tomatometer score": tomatometerscore, "audience score": audiencescore}

def rotom_tv(movie):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    url = url + "/tv/" + rel       
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    tom = re.findall('<span.*?data-qa="tomatometer">\n(.*?)</span>',res,re.DOTALL)
    tom = tom[0].strip()
    aud = re.findall('<span.*?data-qa="audience-score">\n(.*?)</span>',res,re.DOTALL)
    aud = aud[0].strip()
    return {"tomatometer score": tom, "audience score": aud}

def sm_plot_kurd():
    clat,clon=37.377413, 42.78591;zoom=0.6
    sm.plot_countries(clat,clon,zoom,outcolor='lavenderblush')
    d = json.loads(open("kurd1.json").read())
    sm.plot_line(np.array(d['duhok']),color='pink')
    sm.plot_line(np.array(d['erbil']),color='pink')
    sm.plot_line(np.array(d['suleymaniah'],),color='pink')
    plt.text(42.5,37,'Duhok',color='gray')
    plt.text(43.5,36,'Erbil',color='gray')
    plt.text(45,35.5,'Suleymaniah',color='gray')
    pars = [(40,38,'TUR'),(46,37,'IRN'),(43,35,'IRQ'),(40,36,'SYR')]
    for x in pars: plt.text(*x)

def sw_border_encounter(url):
    url = 'https://www.cbp.gov/sites/default/files/assets/documents/' + url
    hdr = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request(url,headers=hdr)
    file = BytesIO(urllib2.urlopen(req).read())    
    df = pd.read_csv(file)
    repl = {"JAN": 1, "FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,
            "JUL":7,"AUG": 8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}
    df['Mon'] = df['Month (abbv)'].replace(repl)
    df['YMD'] = df.apply(lambda x: "%s%02d" % (x['Fiscal Year'],x['Mon']),axis=1)
    g = df.groupby('YMD')['Encounter Count'].sum()
    print (g.tail(4))
    g.plot(title='Southwest Land Border Encounters')

def biz_income(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
  slist = []
  for i in range(len(data_qt['incomeStatementHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['incomeStatementHistoryQuarterly'][ticker][i]))
  df = pd.concat(slist,axis=1).T
  df['grossProfitMargin'] = df.grossProfit / df.totalRevenue * 100.0
  df = df.sort_index(ascending=True)
  return df

def biz_balance(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
  slist = []
  for i in range(len(data_qt['balanceSheetHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['balanceSheetHistoryQuarterly']['DIS'][i]))
  df = pd.concat(slist,axis=1).T
  df = df.sort_index(ascending=True)
  return df

def biz_cash(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'cash')
  slist = []
  for i in range(len(data_qt['cashflowStatementHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['cashflowStatementHistoryQuarterly']['DIS'][i]))
  df = pd.concat(slist,axis=1).T
  df = df.sort_index(ascending=True)
  return df

def biz_eps(ticker):
  df = biz_income(ticker)  
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

"""
Converts pixel values picked from a map to lat/lon coordinates. Requires
two pixels and two corresp coordinates as references

Usage:
refcoord=np.array([[lat1,lon1],[lat2, lon2]])
refpixel=np.array([[px1,py1],[px2,py2]])
pixels = [..] 
coords = u.pixel_coord(refcoord, refpixel,pixels)
"""
def pixel_coord(refcoord, refpixel,pixels):
    mlat = (refcoord[1,0]-refcoord[0,0]) / (refpixel[1,1]-refpixel[0,1])
    mlon = (refcoord[1,1]-refcoord[0,1]) / (refpixel[1,0]-refpixel[0,0])
    cs = [ [ refcoord[0,0]+(y-refpixel[0,1])*mlat, refcoord[0,1]+(x-refpixel[0,0])*mlon ] for x,y in pixels ]
    return cs
