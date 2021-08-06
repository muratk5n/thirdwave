# Natural Disasters

<a name='fires'/>

### Fires

Data comes from [FIRMS](https://firms.modaps.eosdis.nasa.gov/active_fire/),
Fire Information for Resource Management System,  I read their MODIS
CSV dataset for the world, for all fires within last 7 days and filter
out fires below a certain brightness threshold. MODIS works through
satellite images, it scans for certain brighness, color on all Earth
images.

[Script](fires.py)

[Output](fires-out.html)

<a name='equakes'/>

### Earthquake Stats

```python
import requests, time, datetime
import numpy as np, math
import pandas as pd

def get_eq(minx,maxx,miny,maxy):
    today = datetime.datetime.now()
    days = 120
    start = today - datetime.timedelta(days=days)

    req = 'https://earthquake.usgs.gov/fdsnws'
    req+='/event/1/query.geojson?starttime=%s&endtime=%s'
    req+='&minlatitude=%d&maxlatitude=%d&minlongitude=%d&maxlongitude=%d'
    req+='&minmagnitude=5.0&orderby=time&limit=300'
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
    df = df.set_index(0)
    df.columns = ['mag','lat','lon','rad','ago']
    return df
```

```python
import mygeo

lat,lon = 55, -137
D = 3000
lat1,lon1 = mygeo.to_bearing(lat,lon,np.deg2rad(45),D)
lat2,lon2 = mygeo.to_bearing(lat,lon,np.deg2rad(225),D)
minx=np.min((lon1,lon2))
maxx=np.max((lon1,lon2))
miny=np.min((lat1,lat2))
maxy=np.max((lat1,lat2))
df = get_eq(minx,maxx,miny,maxy)
```

```python
import folium

m = folium.Map(location=[lat, lon], zoom_start=3, tiles="Stamen Terrain")

import folium
for index, row in df.iterrows():
    color = 'blue'; opacity = 0.5
    if float(row['mag']) > 6.0:
       color = 'red'; opacity = 1.0
    folium.CircleMarker(
        [row['lat'], row['lon']], opacity=opacity, color=color, tooltip=str(row['mag']) + " " + str(row['ago']) + " days ago"
    ).add_to(m)
    
m.save('equake-out.html')
```

[Output](equake-out.html)


