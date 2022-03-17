from io import BytesIO
import uuid, pandas as pd, numpy as np, urllib.request as urllib2
import math, random, datetime, folium
from zipfile import ZipFile
from scipy import sin, cos, tan, arctan, arctan2, arccos, pi

how_far = 700.0

base_conflict_url = "http://data.gdeltproject.org/events"

conf_cols = ['GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',\
             'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',\
             'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',\
             'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', \
             'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
             'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
             'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', \
             'IsRootEvent','EventCode', 'EventBaseCode','EventRootCode',\
             'QuadClass', 'GoldsteinScale','NumMentions','NumSources', \
             'NumArticles', 'AvgTone','Actor1Geo_Type', 'Actor1Geo_FullName',\
             'Actor1Geo_CountryCode', 'Actor1Geo_ADM1Code','Actor1Geo_Lat', \
             'Actor1Geo_Long', 'Actor1Geo_FeatureID','Actor2Geo_Type', \
             'Actor2Geo_FullName','Actor2Geo_CountryCode', 'Actor2Geo_ADM1Code',\
             'Actor2Geo_Lat', 'Actor2Geo_Long','electrification']

def spherical_distance(lat1, long1, lat2, long2):
    phi1 = 0.5*pi - lat1
    phi2 = 0.5*pi - lat2
    r = 0.5*(6378137 + 6356752) # mean radius in meters
    t = sin(phi1)*sin(phi2)*cos(long1-long2) + cos(phi1)*cos(phi2)
    return r * arccos(t) / 1000.
    

fout = "/tmp/conflict-%s.html" % uuid.uuid4()
now = datetime.datetime.now()
dfs = []
clat,clon = "49.3357;32.1835714".split(';')
clat,clon=float(clat),float(clon)
m = folium.Map(location=[clat, clon], zoom_start=7, tiles="Stamen Terrain")

def dist(x):
    return spherical_distance(np.deg2rad(clat),np.deg2rad(clon),np.deg2rad(x['Actor2Geo_Lat']),np.deg2rad(x['Actor2Geo_Long']))

for i in range(5):
    d = now - datetime.timedelta(days=i+1)
    sd = "%d%02d%02d" % (d.year, d.month, d.day)
    url = base_conflict_url + "/%s.export.CSV.zip" % sd
    try: 
        r = urllib2.urlopen(url).read()
        file = ZipFile(BytesIO(r))
        csv = file.open("%s.export.CSV" % sd)
        df = pd.read_csv(csv,sep='\t',header=None)    
        urls = df[57]        
        df2 = df[range(len(conf_cols))]
        df2 = pd.concat((df2,urls),axis=1)    
        df2.columns = conf_cols + ['url']
        df3 = df2[(df2.EventCode==190)|(df2.EventCode==195)|(df2.EventCode==194)]
        df3.loc[:,'dist'] = df3.apply(dist, axis=1)
        df3 = df3[df3.dist < how_far]
        dft = df3[['EventCode','Actor1CountryCode','Actor1Name','Actor2Name','Actor2Geo_Lat','Actor2Geo_Long','url']].copy()
        dfs.append(dft)
    except:
        print (url, 'missing')
        continue

df4 = pd.concat(dfs,axis=0)

df4 = df4.sample(n=50, random_state=1)

for index, row in df4.iterrows():
    if str(row['Actor2Geo_Lat'])=='nan': continue
    if str(row['Actor1CountryCode'])=='nan': continue
    folium.Marker(
        [row['Actor2Geo_Lat'], row['Actor2Geo_Long']], popup="<a href='%s' target='_blank' rel='noopener noreferrer'>Link</a>" % (row['url']), tooltip=row['Actor1CountryCode']
    ).add_to(m)


m.save('conflict-ukr-out.html')

