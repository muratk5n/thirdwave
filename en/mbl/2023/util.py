from metpy.calc import dewpoint_from_relative_humidity, wet_bulb_temperature
from metpy.units import units
import datetime, time as timelib, re, os, glob, numpy.linalg as lin
import pandas_ta as ta, random
import pandas as pd, datetime, numpy as np, requests
import urllib.parse, json, io, geocoder, zipfile
import matplotlib.pyplot as plt, math
import simplegeomap as sm, util
import urllib.request as urllib2, itertools
from pandas_datareader import data, wb
from io import BytesIO

from scipy.ndimage import gaussian_filter
from siphon.catalog import TDSCatalog
import netCDF4, numpy as np, numpy.linalg as lin, math

from scipy.interpolate import NearestNDInterpolator

def get_sm(): return sm

def get_pd(): return pd

def ukr_data_json():
    for f in sorted(glob.glob(os.environ['HOME']+ "/Documents/tw/en/mbl/2023/ukrdata/fl-*.csv")):        
        if "221115" in f or "none" in f: continue
        print (f)
        df = pd.read_csv(f,header=None)
        outfile = f.replace(".csv",".json")
        res = df.to_numpy().tolist()
        fout = open(outfile, "w")
        fout.write(json.dumps(res))
        fout.close()


def plot_silam(fin,var,t,clat,clon,zoom):
    outdir = "/opt/Downloads"
    base_url = "https://silam.fmi.fi/thredds/fileServer/dailysilam_glob06_v5_8/files/"
    target_file = outdir + "/" + fin
    url = base_url + "/" + fin
    if not os.path.isfile(target_file):
        r = requests.get(url, allow_redirects=True)
        open(target_file, 'wb').write(r.content)
    f = netCDF4.Dataset(target_file)
    x,y = np.meshgrid(np.linspace(-180,180,600),np.linspace(-90,90,297))
    z = f.variables[var][t,0,:,:] 
    z = z * 1e8
    z = np.log(z)
    sm.plot_continents(clat, clon, zoom, incolor='black', outcolor='white', fill=False)
    plt.pcolormesh(x,y,z,cmap='OrRd')

def get_modis_csv():
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv"
    f = 'MODIS_C6_1_Global_7d.csv'
    if not os.path.isfile("/tmp/" + f):
        data = urllib.request.urlretrieve(url + "/" + f, "/tmp/" + f)

def modis_fire(clat,clon,zoom):        
    get_modis_csv()    
    THRESHOLD = 400.0
    df = pd.read_csv('/tmp/MODIS_C6_1_Global_7d.csv')
    df = df[df['brightness'] > THRESHOLD]
    df['brightness'] = 1.0 - (df['brightness'] / df['brightness'].max())
    sm.plot_continents(clat,clon,zoom=zoom,incolor='green', outcolor='white', fill=False)
    for i, row in df.iterrows():
        plt.plot(row['longitude'],row['latitude'],'r.',alpha=row['brightness'])

def wbt(T,H):
    #T = 46; H = 50
    P = 1000
    dew = dewpoint_from_relative_humidity(T * units.degC, H * units.percent)
    return wet_bulb_temperature(P * units.hPa, T * units.degC, dew)
    
def sm_plot_ukr6():    
    fig, ax = plt.subplots() 
    clat=44;clon=25;zoom = 0.8
    sm.plot_countries(clat,clon,zoom=zoom,incolor='papayawhip',outcolor='azure',ax=ax)
    sm.plot_water(clat,clon,zoom=zoom,ax=ax)
    geo = ['Izmail']
    d = json.loads(open("ukrdata/geo.json").read())
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm_plot_list2(data=ps,ax=ax)
    
def sm_plot_list2(data, ax=None, elev=None):
    if not ax: fig, ax = plt.subplots()
    offsets = [[random.randint(-60,60), random.randint(-60,60)] for i in range(len(data))]
    for i,row in enumerate(data):
       lat,lon = float(row[1]),float(row[2])
       label = row[0]
       style = tuple(offsets[i])
       ax.annotate(
         label, 
         xy = (lon, lat), xytext = style,
         textcoords = 'offset points', ha = 'right', va = 'bottom',
         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
         arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          
    
def plot_khali(zoom=0.5,show_elevation=False):
    clat,clon = 54.2, 23.2
    fig, ax = plt.subplots() 
    d = json.loads(open("ru.json").read())
    sm.plot_countries(clat,clon,zoom,ax=ax,force_include=['RUS'])
    if show_elevation:
        sm.plot_elevation(clat,clon,zoom,ax=ax)
    sm.plot_line(np.array(d['suwalki']),ax=ax,color='red')
    ax.text(20,52,'Poland')
    ax.text(20.8,54.6,'Khaliningrad')
    ax.text(26,53,'Belarus')
    ax.text(24,55,'Lithuania')    

def ru_areas():
    res = []
    for f in sorted(glob.glob(os.environ['HOME']+ "/Documents/tw/en/mbl/2023/ukrdata/fl-*.csv")):
        if "221115" in f or "none" in f: continue
        df = pd.read_csv(f,header=None)
        df = np.array(df)
        a = poly_area(df[:,:2])
        d = re.findall('fl.*(\d\d\d\d).csv',f)[0]
        res.append([pd.to_datetime('2023'+d),a])
    res = res[3:]
    df= pd.DataFrame(res)
    df.columns = ['dt','area']
    df = df.set_index('dt')
    return df*10000

def poly_area(pts):
    ps = np.array([0.5 * lin.det(np.vstack((pts[i], pts[i+1]))) for i in range(len(pts)-1)])
    s = np.sum(ps)
    p1,p2 = pts[-1],pts[0]
    s += 0.5 * lin.det(np.vstack((p1,p2)))
    return np.abs(s)

def masto_stat():
    url = "https://api.joinmastodon.org/statistics"
    r = requests.get(url)
    df = pd.DataFrame([[pd.to_datetime(x['period']),x['user_count'],x['active_user_count']] for x in json.loads(r.text)])
    df.columns = ['dt','users','active']
    df = df.set_index('dt').astype(float)
    f,x = plt.subplots(2)
    df['users'].plot(ax=x[0])
    df['active'].plot(ax=x[1])
    print (df.tail(3))    

def sm_plot_ukr5():
    fig, ax = plt.subplots() 
    d = json.loads(open("ukrdata/geo.json").read())
    clat,clon=55.2, 15.5;zoom=0.085
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_line(np.array(d["nordstream1"]),ax,color='blue',linestyle='dashed')
    sm.plot_line(np.array(d["nordstream2"]),ax,color='blue',linestyle='dashed')
    lat,lon = d['nsleak1']; ax.plot(lon,lat,'rd')
    lat,lon = d['nsleak2']; ax.plot(lon,lat,'rd')
    ax.text(14.8,55.1,"Bornholm")
    return d

def elev_at(coords):
    #data = '[[%f,%f]]' % (lat,lon)
    data = str(coords)
    print (data)
    response = requests.post('https://elevation.racemap.com/api',
                             headers={'Content-Type': 'application/json',},
                             data=data)
    res = response.text
    return int(json.loads(res)[0])

def sm_plot_ukr4(newfile,oldfile,geo,w,h,zoom=0.01,fsize=(8,12)):
    
    fig, ax = plt.subplots(w,h,figsize=fsize)
    ax = ax.reshape(w,h)
    fig.tight_layout(pad=2.0)
    cities = json.loads(open("ukrdata/geo.json").read())    
    geo2 = np.empty((w,h),dtype=list) # reshape does not keep internal [], so handcode
    for i,j in itertools.product(range(w),range(h)):
        geo2[i,j] = geo[j+(h*i)]

    for i in range(w):
        for j in range(h):
            c = geo2[i,j][0]
            if c=='Main':
                clat,clon = 48, 36
                cs = [x[0] for x in geo if 'Main' not in x]
                sm_plot_ukr1(newfile,oldfile,cs,clat,clon,zoom=0.5,ax=ax[i,j])
                sm.plot_line(np.array(cities['dnipro1']),ax=ax[i,j],color='cyan',linestyle='solid')
            else:
                clat,clon = cities[c]
                sm_plot_ukr1(newfile,oldfile,geo2[i,j],clat,clon,zoom=zoom,ax=ax[i,j])
                sm.plot_line(np.array(cities['dnipro1']),ax=ax[i,j],color='cyan',linestyle='solid')
                

def pollution(lat,lon):
    """
    Register with Openweathermap site and get a API key, place it
    in a json file called .twkeys.json under your $HOME directory. The
    file should look something like '{ "weatherapi": "[key]" .. }
    """    
    url = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    params = json.loads(open(os.environ['HOME'] + "/.twkeys.json").read())
    payload = { 'lat': str(lat), 'lon': str(lon), 'appid': params['weatherapi'] }
    r = requests.get(url, params=payload)
    res = [json.loads(x.decode()) for x in r.iter_lines()]
    aqi = res[0]['list'][0]['main']
    comp = res[0]['list'][0]['components']
    return aqi, comp

def sm_plot_ukr3():    
    fig, ax = plt.subplots() 
    clat=49;clon=35;zoom = 1.0
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    cities = json.loads(open("ukrdata/geo.json").read())
    sm.plot_line(np.array(cities['dnipro1']),ax,color='cyan',linestyle='solid')
    geo = ["Kakhovskaya Reservoir","Dnieper Reservoir","Srednedneproskoe Reservoir",
           "Kremenchug Reservoir","Kanevskoe Reservoir","Kiev Reservoir","Zaporizhzhya Nuclear Power Plant"]
    
    df = pd.read_csv("ukrdata/fl-0521.csv",header=None)
    df = np.array(df)
    df[:, [1, 0]] = df[:, [0, 1]]    
    sm.plot_line(df,ax,color='red')
    offsets = [[random.randint(-100,100), random.randint(-100,100)] for i in range(len(geo))]
    for i,label in enumerate(geo):
      lat,lon = cities[label]
      style = tuple(offsets[i])
      ax.plot(lon, lat, color='red', marker='o', markersize=4)
      ax.annotate(
          label, 
          xy = (lon, lat), xytext = style,
          textcoords = 'offset points', ha = 'right', va = 'bottom',
          bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
          arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          

def sm_plot_yugo1():
    clat,clon=42, 20;zoom=1.0
    fig, ax = plt.subplots()    
    d = json.loads(open("yugo.json").read())
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_line(np.array(d['Kosovo']),ax,color='cyan',linestyle='solid')
    ax.text(20, 44.23,"Serbia")
    ax.text(17, 44.16, "Bosnia")
    ax.text(16.5, 42.3, "Montanegro")
    ax.text(16.263, 45.587, "Crotia")
    ax.text(19, 41.256987256111785, "Albania")
    ax.text(20.5, 42.59487952393303, "KS")

def sm_plot_tr1():
    fig, ax = plt.subplots() 
    d = json.loads(open("tr.json").read())
    clat,clon=41, 29;zoom=0.1
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_line(np.array(d['canal']),ax,color='cyan',linestyle='solid')
    geo = ["Durusu", "Sazlidere Dam","Kucukcekmece"]
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm_plot_list1(clat,clon,zoom,data=ps,ax=ax)

def sm_plot_nile2():
    fig, ax = plt.subplots() 
    d = json.loads(open("africa.json").read())
    clat,clon=13, 29;zoom=2.0
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_water(clat,clon,zoom=zoom,ax=ax)
    df = pd.read_csv('../../2022/01/oilgas-2018.csv')
    fields = df[df.ISO == 'SDN'][['LAT_DD','LON_DD']]
    fields = np.array(fields)
    plt.plot(fields[:,1],fields[:,0],'r.')        
    geo = ["Ethiopia", "Sudan","South Sudan"]
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm.plot_line(np.array(d['South Sudan Border']),ax,color='green',linestyle='solid')
    sm_plot_list1(clat,clon,zoom,data=ps,ax=ax)
    

def sm_plot_libya2(geo):
    fig, ax = plt.subplots() 
    d = json.loads(open("libya.json").read())
    clat,clon=26, 17;zoom=3.0
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_region(np.array(d['haftar']),ax,color='blue',alpha=0.5)
    sm.plot_region(np.array(d['westgov']),ax,color='lightpink')
    df = pd.read_csv('../../2022/01/oilgas-2018.csv')
    fields = np.array(df[df.ISO == 'LBY'][['LAT_DD','LON_DD']])
    plt.plot(fields[:,1],fields[:,0],'r.')
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm_plot_list1(clat,clon,zoom,data=ps,ax=ax)


def sm_plot_libya1(geo):
    fig, ax = plt.subplots() 
    d = json.loads(open("libya.json").read())
    clat,clon=26, 17;zoom=3.0
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_region(np.array(d['haftar']),ax,color='blue',alpha=0.5)
    sm.plot_region(np.array(d['westgov']),ax,color='lightpink')
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm_plot_list1(clat,clon,zoom,data=ps,ax=ax)


def sm_plot_ukr2(file,oldfile):
    fig, ax = plt.subplots(2,3,figsize=(12, 6))
    fig.tight_layout(pad=2.0)
    zoom = 0.01

    clat=47.78053057704841;clon=37.24655291539728
    sm_plot_ukr1(file,oldfile,['Vuhledar'],clat,clon,zoom=zoom,ax=ax[0,0])

    clat=47.94145650439916;clon=37.507118165279365
    sm_plot_ukr1(file,oldfile,['Marinka'],clat,clon,zoom=zoom,ax=ax[0,1])

    clat=48.09170718659994;clon=37.61045940066837
    sm_plot_ukr1(file,oldfile,['Pervomaiske'],clat,clon,zoom=zoom,ax=ax[1,0])

    clat=49.04201323402742;clon=38.21594879135994
    sm_plot_ukr1(file,oldfile,['Kreminna'],clat,clon,zoom=0.1,ax=ax[1,1])

    clat=48.59;clon=37.98
    sm_plot_ukr1(file,oldfile,['Khromove','Bakhmut'],clat,clon,zoom=0.01,ax=ax[0,2])

    clat=clat=47.6;clon=35.124
    sm_plot_ukr1(file,oldfile,['Zaporizhzhya Nuclear Power Plant'],clat,clon,zoom=0.2,ax=ax[1,2])
    sm.plot_water(clat,clon,zoom=zoom,ax=ax[1,2])
    
def sm_plot_ukr1(file,oldfile,geo,clat=48,clon=37,zoom=0.6,ax=None,show_fortifications=False):
    if not ax: fig, ax = plt.subplots() 
    cities = json.loads(open("ukrdata/geo.json").read())
    sm_plot_ukr_base(file,geo,clat,clon,zoom,ax) 
    df = np.array(pd.read_csv(oldfile,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_line(df,ax,color='gray',linestyle='solid')

    if show_fortifications:
        fs = cities['fortifications']
        for f in fs: sm.plot_line(np.array(f),ax,color='black',linestyle='solid')
        
    sm.plot_line(np.array(cities['dnipro1']),ax=ax,color='cyan',linestyle='solid')
    
    offsets = [[random.randint(-60,60), random.randint(-60,60)] for i in range(len(geo))]    
    for i,label in enumerate(geo):
      lat,lon = cities[label]
      style = tuple(offsets[i])
      ax.plot(lon, lat, color='red', marker='o', markersize=4)
      ax.annotate(
        label, 
        xy = (lon, lat), xytext = style,
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          

def sm_plot_nile1():
    fig, ax = plt.subplots() 
    d = json.loads(open("africa.json").read())
    clat,clon=15, 34;zoom=3.0
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_water(clat,clon,zoom=zoom,ax=ax)
    geo = ["Ethiopia", "Sudan", "Egypt", "GERD","Khartoum"]
    ps = np.array([[x, d[x][0], d[x][1]] for x in geo])
    sm_plot_list1(clat,clon,zoom,data=ps,ax=ax)
       
def get_masto_detail(host):
    response = requests.get("https://%s/api/v1/instance" % host,  timeout=3)
    res = json.loads(response.text) # this converts the json to a python list of dictionary
    cd = pd.to_datetime(res['contact_account']['created_at'])
    return res['stats']['user_count'],cd.strftime('%Y-%m-%d')

        
def sm_plot_ukr_base(file,geo,clat,clon,zoom,ax):
    df = np.array(pd.read_csv(file,header=None))
    df[:, [1, 0]] = df[:, [0, 1]]
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax,incolor='papayawhip',outcolor='azure',force_include=['RUS'])
    sm.plot_line(df,ax,color='red')
    
    df = np.array(pd.read_csv('ukrdata/donetsk.csv',header=None))
    sm.plot_line(df,ax,color='pink')
    ax.text(37,48,'Donetsk',color='gray')

    df = np.array(pd.read_csv('ukrdata/kherson.csv',header=None))
    sm.plot_line(df,ax,color='pink')
    ax.text(33,46.5,'Kherson',color='gray')

    df = np.array(pd.read_csv('ukrdata/zaporizhia.csv',header=None))
    sm.plot_line(df,ax,color='pink')
    ax.text(35,47,'Zaporizhia',color='gray')
    ax.text(38.3,49,'Luhansk',color='gray')
    

def plot_africa_ru_us(ru,us):
    country_dict = sm.get_country_name_iso3()
    geo = sm.get_country_geo()
    colors = {}
    for x in ru: colors[country_dict[x]] = "red"
    for x in us: colors[country_dict[x]] = "yellowgreen"
    plt.figure(figsize=(10, 8))
    clat,clon=5.0910, 24.828
    zoom = 8.0
    fig, ax = plt.subplots() 
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax,country_color=colors)
    for k in colors:
        lat,lon = geo[k]
        if "TGO" in k:
            ax.text(lon-2,lat-5,k)
        else:            
            ax.text(lon-2,lat,k)

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

def get_bp_country(country,year=None):
    fin = '../../2022/01/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index == 2021]
        
    df = df[['primary_ej','elect_twh','coalcons_ej','gascons_ej','oilcons_ej']]
    df['oil_twh'] = (df.oilcons_ej * 277.778)
    df['gas_twh'] = (df.gascons_ej * 277.778)
    df['coal_twh'] = (df.coalcons_ej * 277.778)
    df['primary_twh'] = (df.primary_ej * 277.778)
    cols = [x for x in df.columns if '_twh' in x]    
    df2 = df[cols].fillna(0).unstack()
    
    return df2


def renew_perc_bp(country):
    fin = '../../2022/01/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index == df.index.max()]
    return np.round(float(df['renewables_ej']) / (float(df['primary_ej']))*100,2)

def sm_usnavy(clat, clon, zoom):
    df = usnavy()
    sm_plot_list1(clat, clon, zoom, np.array(df[['name','lat','lon']]))

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
    d = json.loads(open("tr.json").read())
    d = d['eq']['deaths']
    res = [[str(x[0]) + " " + str(x[1]), geocoder.osm(x[0]).latlng] for x in d[k]]
    res = [[x[0],x[1][0],x[1][1]] for x in res]
    print ("Total :", np.sum(np.array([x[1] for x in d[k]])))
    sm_plot_list1(38, 38, 0.5, res)

def sm_tr_eq_buildings(k):
    d = json.loads(open("tr.json").read())
    d = d['eq']['buildings']
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

def sm_plot_list1(clat, clon, zoom, data, ax=None, elev=None):
    if not ax: fig, ax = plt.subplots()
    offsets = [[random.randint(-60,60), random.randint(-60,60)] for i in range(len(data))]
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    if elev: sm.plot_elevation(clat,clon,zoom=zoom,levels=elev,ax=ax)
    for i,row in enumerate(data):
       lat,lon = float(row[1]),float(row[2])
       label = row[0]
       style = tuple(offsets[i])
       ax.annotate(
         label, 
         xy = (lon, lat), xytext = style,
         textcoords = 'offset points', ha = 'right', va = 'bottom',
         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
         arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))          

def sm_plot_azearm4(geo):
    d = json.loads(open("azerbarm1.json").read())
    clat,clon=40, 46;zoom=0.25
    sm.plot_countries(clat,clon,zoom)
    sm.plot_line(np.array(d['nagornarm1']),color='lightgreen')
    sm.plot_line(np.array(d['lachin']),color='red')
    ps = np.array([[x, d[x][1], d[x][0]] for x in geo])
    sm_plot_list1(clat,clon,zoom,ps)
       
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
    import rottentomatoes as rt 
    return {"tomatometer score": rt.tomatometer(movie)['value'],
            "audience score": rt.audience_score(movie)['value']}

def rottentomatoes2(movie):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    url = url + "/tv/" + rel       
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    aud = re.findall('audiencescore=\"(.*?)\"',res,re.DOTALL)
    tom = re.findall('tomatometerscore=\"(.*?)\"',res,re.DOTALL)
    return {"tomatometer score": int(tom[0]), "audience score": int(aud[0])}


def rottentomatoes3(movie):
    rel = movie.replace(" ","_").lower()
    url = "https://www.rottentomatoes.com"
    url = url + "/m/" + rel
    hdr = {'User-Agent':'Mozilla/5.0'}
    res = urllib2.urlopen(url).read().decode('utf-8')
    
    tom = re.findall('"audienceScore":{.*?}',res,re.DOTALL)
    d1 = json.loads("{" + tom[0] + "}")
    tom = re.findall('"tomatometerScoreAll":{.*?}',res,re.DOTALL)
    d2 = json.loads("{" + tom[0] + "}")
    return {"tomatometer score": d2['tomatometerScoreAll']['value'], "audience score": d1['audienceScore']['value'] }

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
  from yahoofinancials import YahooFinancials
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
      slist.append(pd.DataFrame.from_dict(data_qt['balanceSheetHistoryQuarterly'][ticker][i]))
  df = pd.concat(slist,axis=1).T
  df = df.sort_index(ascending=True)
  return df

def biz_cash(ticker):
  yahoo_financials = YahooFinancials(ticker, concurrent=True, max_workers=8, country="US")
  data_qt = yahoo_financials.get_financial_stmts('quarterly', 'cash')
  slist = []
  for i in range(len(data_qt['cashflowStatementHistoryQuarterly'][ticker])):
      slist.append(pd.DataFrame.from_dict(data_qt['cashflowStatementHistoryQuarterly'][ticker][i]))
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

def sliding_window(image, stepSize, windowSize):
  for y in range(0, image.shape[0], stepSize):
    for x in range(0, image.shape[1], stepSize):
      yield np.resize(image[y:y + windowSize[1], x:x + windowSize[0]],windowSize)
      #yield image[y:y + windowSize[1], x:x + windowSize[0]]

def ecmwf_wind(clat,clon,zoom,M=100,N=60,show_ike=False):
    import ecmwf.data as ecdata
    from ecmwf.opendata import Client
    
    client = Client("ecmwf", beta=True)
    parameters = ['10u', '10v','2t']
    filename = '/tmp/medium-2t-wind.grib'

    client.retrieve(
        date=0,
        time=0,
        step=12,
        stream="oper",
        type="fc",
        levtype="sfc",
        param=parameters,
        target=filename
    )

    data = ecdata.read(filename)

    t2m = data.select(shortName= "2t")
    u = data.select(shortName= "10u")
    v = data.select(shortName= "10v")

    lons = u.longitudes()
    lats = u.latitudes()
    udata = u.values()
    xi = np.linspace(min(lons), max(lons), M)
    yi = np.linspace(min(lats), max(lats), N)
    Xi, Yi = np.meshgrid(xi, yi)
    interp = NearestNDInterpolator(list(zip(lons,lats)), udata)
    uzi = interp(Xi, Yi)

    lons = v.longitudes()
    lats = v.latitudes()
    vdata = v.values()
    xi = np.linspace(min(lons), max(lons), M)
    yi = np.linspace(min(lats), max(lats), N)
    Xi, Yi = np.meshgrid(xi, yi)
    interp = NearestNDInterpolator(list(zip(lons,lats)), vdata)
    vzi = interp(Xi, Yi)

    fig, ax = plt.subplots()
    sm.plot_continents(clat,clon,zoom,incolor='green', outcolor='white', fill=False,ax=ax)
    
    if show_ike:
        W = (3,3)
        # lat,lon 111 kilometers/deg
        lonlen = 111*((min(lons)-max(lons))/M)
        latlen = 111*((min(lats)-max(lats))/M)
        cell_area = latlen * lonlen
        xs = []; ys = []; ikes = []
        for xx,yy,uu,vv in zip(sliding_window(Xi,1,W),sliding_window(Yi,1,W),
                               sliding_window(uzi,1,W),sliding_window(vzi,1,W)):
           u_wind = uu.flatten()
           v_wind = vv.flatten()
           x_coord = xx.flatten()
           y_coord = yy.flatten()
           wspeedsquare = u_wind**2+v_wind**2
           IKE = np.sum(0.5*wspeedsquare*cell_area*W[0]*W[1]) / 1e6
           xs.append(np.mean(x_coord))
           ys.append(np.mean(y_coord))
           ikes.append(IKE)
        
        ikeinterp = NearestNDInterpolator(list(zip(xs,ys)), ikes)
        ikezi = ikeinterp(Xi, Yi)
        plt.pcolormesh(Xi,Yi,ikezi,cmap='Reds')
        
    ax.quiver(Xi,Yi,uzi,vzi)    

def berlin1():
    # Prager Platz
    # 52.49318629735666, 13.333060825694803
    # adenauerplatz
    # 52.49986790660432, 13.307533743044464
    # Neukolln
    # 52.44068295147736, 13.445288470596834
    # Potsdamer Platz
    # 52.509791308054666, 13.375978712119096    
    url = "https://gist.github.com/CliffordAnderson/49f26b694e2f1e41ac5c17433aa310fe/archive/9e78f341e21f9a8b53f35a92dff9727f312abeeb.zip"
    r = urllib2.urlopen(url).read()
    file = io.BytesIO(r)
    with zipfile.ZipFile(file, 'r') as z:
       content = z.open('49f26b694e2f1e41ac5c17433aa310fe-9e78f341e21f9a8b53f35a92dff9727f312abeeb/berlin-wall.geojson').read()    
    res = json.loads(content)
    print (res['features'][1]['geometry']['coordinates'][:10])    

def ike_ncei(lat,lon,day,month,year,hour):

    # form grid which has NE, and SW cornes brg kilometers away
    # from center lat,lon
    brg = 1000
    upper_right = to_bearing(lat,lon,np.deg2rad(45),brg)
    lower_left = to_bearing(lat,lon,np.deg2rad(225),brg)

    north = int(upper_right[0])
    south = int(lower_left[0])
    east = int(upper_right[1])
    west = int(lower_left[1])

    side = np.cos(np.deg2rad(45))*brg*2
    area = side*side*1e6

    dt = datetime.datetime(year, month, day, hour)

    base_url = 'https://www.ncei.noaa.gov/thredds/catalog/model-narr-a-files/'
    cat = TDSCatalog(f'{base_url}{dt:%Y%m}/{dt:%Y%m%d}/catalog.xml')
    ds = cat.datasets.filter_time_nearest(dt)
    ncss = ds.subset()

    query = ncss.query()
    query.lonlat_box(north=north, south=south, east=east, west=west)
    query.all_times()
    query.add_lonlat()
    query.accept('netcdf')
    query.variables('u-component_of_wind_isobaric',
                    'v-component_of_wind_isobaric')

    data = ncss.get_data(query)
    u_wind_var = data.variables['u-component_of_wind_isobaric']
    v_wind_var = data.variables['v-component_of_wind_isobaric']
    u_wind = u_wind_var[0, 0, :, :].squeeze() 
    v_wind = v_wind_var[0, 0, :, :].squeeze() 

    gi,gj = u_wind.shape
    cell_count = gi*gj
    cell_area = area / cell_count

    wspeedsquare = u_wind**2+v_wind**2
    wspeedsquare = wspeedsquare.reshape(-1)
    wspeedsquare = wspeedsquare[wspeedsquare > 30.0]
    IKE = np.sum(0.5*wspeedsquare*cell_area) / 1e12
    return IKE

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
    df = pd.read_csv(url,parse_dates=True,index_col='end_date')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df

if __name__ == "__main__": 
    #print (ru_areas())
    #modis_fire(0,0,18)
    
    #df = biden_approval().net
    #print (df.tail(5))
    #df.plot()
    #plt.savefig('/tmp/out.jpg',quality=40)

    ukr_data_json()
      
