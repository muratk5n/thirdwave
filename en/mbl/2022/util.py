import pandas as pd, datetime, numpy as np, requests
import requests, urllib.parse, json
from pandas_datareader import data, wb
import matplotlib.pyplot as plt, math
import simplegeomap as sm, util
import datetime, time as timelib, re
import urllib.request as urllib2
from io import BytesIO
import pandas_ta as ta

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

def rottentomatoes(movie,tv=False):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    if not tv:
       url = url + "/m/" + rel
    else:
       url = url + "/tv/" + rel       
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    if not tv:    
       regreg = re.findall('audiencescore="(.*?)"',res)
       audiencescore = int(regreg[0])
       regreg = re.findall('tomatometerscore="(.*?)"',res)
       tomatometerscore = int(regreg[0])
       return {"tomatometer score": tomatometerscore, "audience score": audiencescore}
    else:
       tom = re.findall('<span.*?data-qa="tomatometer">\n(.*?)</span>',res,re.DOTALL)
       tom = tom[0].strip()
       aud = re.findall('<span.*?data-qa="audience-score">\n(.*?)</span>',res,re.DOTALL)
       aud = aud[0].strip()
       return {"tomatometer score": tom, "audience score": aud}
   
def boxofficemojo(q):
    q = q.replace(" ","+").lower()
    url = "https://www.boxofficemojo.com/search/?q=" + q
    res = urllib2.urlopen(url).read().decode('utf-8')
    reres = re.findall('a-size-medium a-link-normal a-text-bold" href="(.*?)"',res)
    url2 = "https://www.boxofficemojo.com" + reres[0]
    res2 = urllib2.urlopen(url2).read().decode('utf-8')

    regex2 = 'a-section a-spacing-none.*?Budget.*?money">(.*?)<'
    budget = re.findall(regex2,res2,re.DOTALL)[0]
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
            "Budget": budget, "Release Date": reldate}


def rent_housing():
    import pandas as pd, datetime
    from pandas_datareader import data

    today = datetime.datetime.now()
    start=datetime.datetime(2000, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    cols = ['CUUR0000SEHA','MSPUS']
    df = data.DataReader(cols, 'fred', start, end)
    df = df.interpolate()

    df['incrent'] = (df.CUUR0000SEHA-df.CUUR0000SEHA.shift(12))/df.CUUR0000SEHA.shift(12)*100
    df['inchouse'] = (df.MSPUS-df.MSPUS.shift(12))/df.MSPUS.shift(12)*100

    print (df[['incrent','inchouse']].tail(3))
    
    plt.figure()
    ax1 = df.incrent.plot(color='blue', grid=True, label='rent inc %')
    ax2 = df.inchouse.plot(color='red', grid=True, label='house price inc %',secondary_y=True)
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)

def sen_az_538():
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/senate_polls.csv')
    df1 = df[(df.candidate_name == 'Blake Masters')  ]
    df2 = df[(df.candidate_name == 'Mark Kelly') ]
    v1 = np.array(df1[['candidate_name','end_date','pollster','pct']].head(1))
    v2 = np.array(df2[['candidate_name','end_date','pollster','pct']].head(1))
    return list(v1[0]), list(v2[0])

def gov_ny_538():
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/governor_polls.csv')
    df1 = df[(df.candidate_name == 'Kathy C. Hochul')  ]
    df2 = df[(df.candidate_name == 'Lee M. Zeldin') ]
    v1 = np.array(df1[['candidate_name','end_date','pollster','pct']].head(1))
    v2 = np.array(df2[['candidate_name','end_date','pollster','pct']].head(1))
    return list(v1[0]), list(v2[0])

def gov_fl_538():
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/governor_polls.csv')
    df1 = df[(df.candidate_name == 'Ron DeSantis')  ]
    df2 = df[(df.candidate_name == 'Charlie Crist') ]
    v1 = np.array(df1[['candidate_name','end_date','pollster','pct']].head(1))
    v2 = np.array(df2[['candidate_name','end_date','pollster','pct']].head(1))
    return list(v1[0]), list(v2[0])

def sen_pa_538():
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/senate_polls.csv')
    df1 = df[(df.candidate_name == 'John Fetterman')  ]
    df2 = df[(df.candidate_name == 'Mehmet Oz') ]
    v1 = np.array(df1[['candidate_name','end_date','pollster','pct']].head(1))
    v2 = np.array(df2[['candidate_name','end_date','pollster','pct']].head(1))
    return list(v1[0]), list(v2[0])

def sen_ga_538():
    df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/senate_polls.csv')
    df1 = df[(df.candidate_name == 'Herschel Junior Walker')  ]
    df2 = df[(df.candidate_name == 'Raphael Warnock') ]
    v1 = np.array(df1[['candidate_name','end_date','pollster','pct']].head(1))
    v2 = np.array(df2[['candidate_name','end_date','pollster','pct']].head(1))
    s = float(df1['sample_size'].head(1))
    return list(v1[0]), list(v2[0])

def d(k,n): m=k/n; return m,1.96*np.sqrt(m*(1-m)/n)

def pollint(a,b,n):
   m,t = d(a,n)
   int1 = list(np.round([m-t,m+t],2))
   m,t = d(b,n)
   int2 = list(np.round([m-t,m+t],2))
   return int1,int2

def gfp_compare(country,file1,file2):
    df1 = pd.read_csv(file1); cols = df1.columns
    df1 = df1[df1.country.isin([country])]
    df2 = pd.read_csv(file2)
    df2 = df2[df2.country.isin([country])]

    r1 = df1[cols[2:32]].squeeze()
    r2 = df2[cols[2:32]].squeeze()

    chg = ((r2-r1)/r1)*100
    filt = np.abs(chg) > 5.0
    df = pd.concat((chg[filt],r1[filt]),axis=1)
    df.columns = ['% Change','Previous']
    return df

def spy_earnings():
    url = "https://www.spglobal.com/spdji/en/documents/additional-material/sp-500-eps-est.xlsx"
    hdr = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request(url,headers=hdr)
    file = BytesIO(urllib2.urlopen(req).read())
    df = pd.read_excel(file,sheet_name="QUARTERLY DATA",skiprows=6,header=None)
    df.columns = ['date','op_ex_ps','eps','cash_div_ps','sales_ps','book_val_ps','capex_ps','price','divisor']
    df = df.set_index(pd.to_datetime(df.date))
    return df

def yf_profit(ticker):
    df = yf.get_income(ticker)
    return df[['grossProfit','totalRevenue','grossProfitMargin']]    

def yf_eps(ticker):
    df = yf.get_earnings(ticker)
    df = df[['startdatetime','epsestimate','epsactual']]
    df = df.dropna().head(3)    
    return df

def sm_plot_kurd1(geo):
    clat,clon=37, 42; zoom=0.6
    sm.plot_countries(clat,clon,zoom,outcolor='lavenderblush')
    sm.plot_elevation(clat,clon,zoom)
    d = json.loads(open("kurd1.json").read())
    sm.plot_line(np.array(d['duhok']),color='red')
    sm.plot_line(np.array(d['erbil']),color='red')
    sm.plot_line(np.array(d['suleymaniah'],),color='red')    
    pars = [(40,38,'Asia Minor'),(46,37,'Iran'),(43,35,'Iraq'),(40,36,'Syria')]
    for x in pars: plt.text(*x,color='red')
    eps = -0.3
    for i,(lat,lon) in enumerate(geo):
        plt.text(lon+eps,lat+eps,i+1)
        plt.plot(lon,lat,'go')

def sm_plot_ukr3(file,oldfile,geo):
    sm_plot_ukr1(file,geo)    
    clat,clon=48, 37; zoom = 0.6
    sm.plot_water(clat,clon,zoom)
    df = np.array(pd.read_csv(oldfile,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_line(df,color='green',linestyle='solid')
                
def sm_plot_ukr2(file,oldfile,geo):
    sm_plot_ukr1(file,geo)    
    df = np.array(pd.read_csv(oldfile,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_line(df,color='gray',linestyle='solid')
        
def sm_plot_ukr1(file,geo):
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
    eps = 0.1
    for i,(lat,lon) in enumerate(geo):
        plt.text(lon+eps,lat-eps,i+1)
        plt.plot(lon,lat,'g+')
    
def bp_hydro_elec_perc(country):
    fin = '../../2022/01/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index == df.index.max()]
    elec = float(df['elect_twh'])
    prim = float(df['primary_ej'])*277.778
    h = float(df.hydro_twh)
    return np.round(h*100/elec,2), np.round(h*100/prim,2)

def sm_plot_cities(clat,clon,zoom,country,cities,eps=0.1):
    sm.plot_countries(clat,clon,zoom)
    for i,city in enumerate(cities):
       c = sm.find_city(city,"greece")
       if (len(c)==1):
           lat,lon,n=float(c[0][9]),float(c[0][8]),c[0][1]
           plt.text(lat+eps,lon+eps,i+1)
           plt.plot(lat,lon,'ro')
    
def country_bp(country):
    df, prod_perc, tot, elec = util.get_bp_country(country)
    print (df)
    print ('\nProduction As Percentage of Consumption\n')
    print (prod_perc)
    print ('\nElectricity',np.round(elec,2),'%')
    print ('\nTotal\n')
    print (np.round(tot*1000 / (365*24),2),'GW')

def get_bp_country(country,year=None):
    fin = '../../2022/01/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    if not year:
        df = df[df.index == df.index.max()]
    else:
        df = df[df.index == year]
        
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

def plot_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    print (df.tail(3))
    df.plot(); plt.savefig('out.png')
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

def sm_ukraine():
    clat,clon=48.70665, 37.5; zoom = 0.27

    ukr = json.loads(open("ukrdata/ukraine1.json").read())
    ru = np.array(ukr['front']['20220430'])
    sm.plot_countries(clat,clon,zoom,outcolor='lavenderblush')
    sm.plot_line(ru,color='red',linestyle='dashed')
    for city in ['donetsk','luhansk','volnovakha','lyman']:
       c = sm.find_city(city,"ukraine")[0]
       plt.text(float(c[9]),float(c[8]),c[1])

def sm_india():
    clat,clon=18, 77; zoom = 3.0
    sm.plot_countries(clat,clon,zoom)
    plt.text(78,20,"India")
    for city in ['lakshadweep','minicoy','andaman','nicobar']:
       c = sm.find_city(city,"india")
       if (len(c)==1):
           lat,lon,n=float(c[0][9]),float(c[0][8]),c[0][1]
           plt.text(lat,lon,n)
           plt.plot(lat,lon,'rd')

def sm_kurds():
    clat,clon=37.377413, 42.78591;zoom=0.6
    fig, ax = plt.subplots() 
    sm.plot_countries(clat,clon,zoom,ax=ax)
    d = json.loads(open("kurd1.json").read())
    sm.plot_region(np.array(d['duhok']),color='green',alpha=0.1,ax=ax)
    sm.plot_region(np.array(d['erbil']),color='green',alpha=0.1,ax=ax)
    sm.plot_region(np.array(d['suleymaniah'],),color='red',alpha=0.1,ax=ax)
    sm.plot_elevation(clat,clon,zoom,ax=ax)
    pars = [(40,38,'TR'),(46,37,'Iran'),(43,35,'Iraq'),(40,36,'Syria')]
    for x in pars: ax.text(*x)
    lon,lat = d['qandil']; plt.plot(lat,lon,'rd')
    lon,lat = d['sinjar']; plt.plot(lat,lon,'rx')    

def elev_at(lat,lon):
    data = '[[%f,%f]]' % (lat,lon)
    response = requests.post('https://elevation.racemap.com/api',
                             headers={'Content-Type': 'application/json',},
                             data=data)
    res = response.text
    return int(json.loads(res)[0])

def eq_at2(lat,lon,radius,ago):

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
        res.append([sd,s,lat,lon])

    df = pd.DataFrame(res).sort_values(by=0)
    df.columns = ['date','mag','lat','lon']
    df = df.set_index('date')    
    return df

def eq_at(lat,lon,radius=2000,ago=20):
    lat1,lon1 = to_bearing(lat,lon,np.deg2rad(45),radius)
    lat2,lon2 = to_bearing(lat,lon,np.deg2rad(225),radius)
    minx=np.min((lon1,lon2))
    maxx=np.max((lon1,lon2))
    miny=np.min((lat1,lat2))
    maxy=np.max((lat1,lat2))
    df = get_eq(minx,maxx,miny,maxy,days=ago)
    return df
    
def get_eq(minx,maxx,miny,maxy,days,today = datetime.datetime.now()):    
    start = today - datetime.timedelta(days=days)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=3.0&orderby=time&limit=300'
    req = req % (start.isoformat(), today.isoformat(),miny,maxy,minx,maxx)
    qr = requests.get(req).json()
    res = []
    for i in range(len(qr['features'])):
        lat = qr['features'][i]['geometry']['coordinates'][1]
        lon = qr['features'][i]['geometry']['coordinates'][0]
        rad = qr['features'][i]['geometry']['coordinates'][2]
        d = datetime.datetime.fromtimestamp(qr['features'][i]['properties']['time']/1000.0)
        s = np.float(qr['features'][i]['properties']['mag'])
        diff = (today-d).days+1
        res.append([d,s,lat,lon,rad,diff])

    df = pd.DataFrame(res).sort_values(by=0)
    df.columns = ['date','mag','lat','lon','rad','ago']
    df = df.set_index('date')
    
    return df

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

def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

def fetch_ukr_war_map(dt):
    base = "https://www.understandingwar.org/sites/default/files/DraftUkraineCoT"
    sd = dt.strftime("%B%-d,%Y")
    url = base + sd + ".png"
    print (url)
    outfile = "/tmp/isw-ukr-%d%d%02d.png" % (dt.year,dt.month,dt.day)
    import urllib.request as urllib2
    request = urllib2.Request(url)
    pic = urllib2.urlopen(request)
    with open(outfile, 'wb') as localFile:
        localFile.write(pic.read())        

def pollution(lat,lon):
    """
    Register with Openweathermap site and get a API key, place it
    in a file called .owm under .key directory. For limited use
    it is free.
    """    
    url = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    weatherapi = open(".key/.owm").read() # your api key goes in that file    
    payload = { 'lat': str(lat), 'lon': str(lon), 'appid': weatherapi }
    r = requests.get(url, params=payload)
    res = [json.loads(x.decode()) for x in r.iter_lines()]
    aqi = res[0]['list'][0]['main']
    comp = res[0]['list'][0]['components']
    return aqi, comp

def gdp_download():
    countries = ['ABW', 'AFG', 'AGO', 'AIA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ASM', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEN', 'BES', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLX', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'CAF', 'CAN', 'CCK', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CXR', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LTU', 'LVA', 'MAC', 'MAF', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MUS', 'MWI', 'MYS', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SHN', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VNM', 'VUT', 'WLF', 'WSM', 'XXB', 'YEM', 'ZAF', 'ZMB', 'ZWE']
    res = []
    for i,c in enumerate(countries):
        try:
            print (i,c)
            dat = wb.download(indicator='NY.GDP.PCAP.KD', country=[c], start=2014, end=2016)
            gdp = list(dat['NY.GDP.PCAP.KD']) 
            res.append([c, gdp[0], gdp[2]])
            #if len(res) > 5: break
        except:
            print ('error')

    df = pd.DataFrame(res)
    df.columns = ['code','gdp2014','gdp2016']
    df.to_csv('gdp1416.csv',index=None)    

def biden_approval():
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df

def trump_approval():
    url = "https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df[df.subgroup=='All polls']
    df = df[df.pollster=='Gallup']
    df = df.sort_index()
    df['net'] = df['approve'] - df['disapprove']
    return df


if __name__ == "__main__": 

    df = biden_approval()
    print (df.net.tail(10))
    df.net.plot()
    plt.show()

