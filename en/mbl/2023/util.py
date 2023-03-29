import pandas_ta as ta, random, rottentomatoes as rt    
import pandas as pd, datetime, numpy as np, requests
import requests, urllib.parse, json, io, geocoder
import matplotlib.pyplot as plt, math
import simplegeomap as sm, util
import datetime, time as timelib, re, os
import urllib.request as urllib2
from yahoofinancials import YahooFinancials
from pandas_datareader import data, wb
from io import BytesIO

def get_masto_detail(host):
    response = requests.get("https://%s/api/v1/instance" % host,  timeout=3)
    res = json.loads(response.text) # this converts the json to a python list of dictionary
    cd = pd.to_datetime(res['contact_account']['created_at'])
    return res['stats']['user_count'],cd.strftime('%Y-%m-%d')

def sm_plot_ukr(file,oldfile,geo,clat=48,clon=37,zoom=0.6):
    cities = json.loads(open("ukrdata/cities.json").read())
    sm_plot_ukr_base(file,geo,clat,clon,zoom)    
    df = np.array(pd.read_csv(oldfile,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_line(df,color='gray',linestyle='solid')
    offsets = [[random.randint(-60,60), random.randint(-60,60)] for i in range(len(geo))]
    for i,label in enumerate(geo):
      lat,lon = cities[label]
      style = tuple(offsets[i])
      plt.plot(lon, lat, color='red', marker='o', markersize=4)
      plt.annotate(
        label, 
        xy = (lon, lat), xytext = style,
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          
        
def sm_plot_ukr_base(file,geo,clat,clon,zoom):
    df = np.array(pd.read_csv(file,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
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
    

def plot_africa_ru_us(ru,us):
    country_dict = sm.get_country_name_iso3()
    geo = sm.get_country_geo()
    colors = {}
    for x in ru: colors[country_dict[x]] = "red"
    for x in us: colors[country_dict[x]] = "yellowgreen"
    plt.figure(figsize=(10, 8))
    clat,clon=5.0910, 24.828
    zoom = 8.0
    sm.plot_countries(clat,clon,zoom,country_color=colors)
    for k in colors:
        lat,lon = geo[k]
        if "TGO" in k:
            plt.text(lon-2,lat-5,k)
        else:            
            plt.text(lon-2,lat,k)

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
    df, prod_perc, tot, elec = get_bp_country(country)
    print (df)
    print ('\nProduction As Percentage of Consumption\n')
    print (prod_perc)
    print ('\nElectricity',np.round(elec,2),'%')
    print ('\nTotal\n')
    print (np.round(tot*1000 / (365*24),2),'GW')

def get_bp_country(country):
    fin = '../../2022/01/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
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

def usnavy():
    ships = json.loads(open("../../mbl/2023/usnavy.json").read())
    headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}
    base = 'https://www.vesselfinder.com/vessels/'
    data = []
    for s in ships['data']:
        resp = requests.get(base + s[2], headers=headers)  
        res = re.findall(r'"ship_lat":(.*?),"ship_lon":(.*?),"ship_cog":(.*?),"ship_sog":(.*?),',resp.text)
        if len(res)>0:
           row = list(s) + list(res[0])
           data.append(row)
    df = pd.DataFrame(data)
    df.columns = ['code','name','code2','lat','lon','bearing','speed']
    return df

def sm_tr_eq_deaths(k):
    d = json.loads(open("try_sry_eq.json").read())
    d = d['deaths']
    res = [[str(x[0]) + " " + str(x[1]), geocoder.osm(x[0]).latlng] for x in d[k]]
    res = [[x[0],x[1][0],x[1][1]] for x in res]
    print ("Total :", np.sum(np.array([x[1] for x in d[k]])))
    sm_plot_list1(38, 38, 0.5, res)

def sm_tr_eq_buildings(k):
    d = json.loads(open("try_sry_eq.json").read())
    d = d['buildings']
    res = [[str(x[0]) + " " + str(x[1]), geocoder.osm(x[0]).latlng] for x in d[k]]
    res = [[x[0],x[1][0],x[1][1]] for x in res]
    print ("Total :", np.sum(np.array([x[1] for x in d[k]])))
    sm_plot_list1(38, 38, 0.5, res)

def eq_at(lat,lon,radius,ago,today = datetime.datetime.now()):

    lat1,lon1 = to_bearing(lat,lon,np.deg2rad(45),radius)
    lat2,lon2 = to_bearing(lat,lon,np.deg2rad(225),radius)
    minx=np.min((lon1,lon2))
    maxx=np.max((lon1,lon2))
    miny=np.min((lat1,lat2))
    maxy=np.max((lat1,lat2))
    today = datetime.datetime.now()
    start = today - datetime.timedelta(days=ago)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=1.0&orderby=time&limit=3000'
    req = req % (start.isoformat(), today.isoformat(),miny,maxy,minx,maxx)
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        sd = d.strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        diff = (today-d).days+1
        res.append([sd,s,lat,lon,diff])

    df = pd.DataFrame(res).sort_values(by=0)
    df.columns = ['date','mag','lat','lon','ago']
    df = df.set_index('date')    
    return df

def sm_plot_list1(clat, clon, zoom, data):
    offsets = [[random.randint(-60,60), random.randint(-60,60)] for i in range(len(data))]
    sm.plot_countries(clat,clon,zoom)
    for i,row in enumerate(data):
       lat,lon = float(row[1]),float(row[2])
       label = row[0]
       style = tuple(offsets[i])
       plt.annotate(
         label, 
         xy = (lon, lat), xytext = style,
         textcoords = 'offset points', ha = 'right', va = 'bottom',
         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
         arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          

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

def rottentomatoes1(movie):
    return {"tomatometer score": rt.tomatometer(movie)['value'],
            "audience score": rt.audience_score(movie)['value']}

def rottentomatoes2(movie):
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
  df['profitMargin'] = df.netIncome / df.totalRevenue * 100.0
  df['operatingProfitMargin'] = df.operatingIncome / df.totalRevenue * 100.0
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
  return np.round(gross - (budget + marketing + gross*0.4),2)

def covid_hospitalization():
   df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv',parse_dates=True)
   df = df[df.indicator == 'Daily hospital occupancy per million']
   df = df[['date','entity','value']]
   df.columns = ['date','country','Daily hospital occupancy per million']
   df = df.set_index('date')
   return df

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
def pixel_coord(refcoord, refpixel, pixels):
    mlat = (refcoord[1,0]-refcoord[0,0]) / (refpixel[1,1]-refpixel[0,1])
    mlon = (refcoord[1,1]-refcoord[0,1]) / (refpixel[1,0]-refpixel[0,0])
    cs = [ [ refcoord[0,0]+(y-refpixel[0,1])*mlat, refcoord[0,1]+(x-refpixel[0,0])*mlon ] for x,y in pixels ]
    return cs

def to_bearing(lat,lon,brng,d):
    R = 6378.1 #Radius of the Earth
    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    return lat2,lon2

def two_plot(df, col1, col2):
    plt.figure(figsize=(12,5))
    ax1 = df[col1].plot(color='blue', grid=True, label=col1)
    ax2 = df[col2].plot(color='red', grid=True, label=col2,secondary_y=True)
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)

def lineproc(file_name,chunk_i,N,hookobj,skip_lines=0):
    file_size = os.path.getsize(file_name)
    hookobj.infile = file_name # lineprocessor object
    hookobj.chunk = chunk_i
    with open(file_name, 'r') as f:
        for j in range(skip_lines): f.readline()
        beg = f.tell()
        f.close()
    chunks = []
    for i in range(N):
        with open(file_name, 'r') as f:
            s = int((file_size / N)*(i+1))
            f.seek(s)
            f.readline()
            end_chunk = f.tell()-1
            chunks.append([beg,end_chunk])
            f.close()
        beg = end_chunk+1
    c = chunks[chunk_i]
    with open(file_name, 'r') as f:
        f.seek(c[0])
        while True:
            line = f.readline()
            hookobj.exec(line) # process the line
            if f.tell() > c[1]: break
        f.close()
        hookobj.post()    

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

def global_leader_approval():
    url = "https://morningconsult.com/global-leader-approval"
    c = urllib2.urlopen(url).read().decode('utf-8')
    regex = 'span class="bar__name">(.*?)</span>.*?NET(.*?)</span>'
    res = re.findall(regex,c,re.DOTALL)
    res = [[x[0].replace("<span>",""),x[1].replace("&plus;","+")] for x in res]
    df = pd.DataFrame(res)
    df.columns = ['name','net']
    return df

def biden_approval():
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df
