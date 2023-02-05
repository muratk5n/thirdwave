# US Military

```python
import pandas as pd, folium
import util as u
```

<a name='bases'/>

### US Bases around the World

Data from [here](https://github.com/meflynn/troopdata), itself based
on David Vine's work.

```python

clat,clon=33.01136975577918, 40.98527636859822

m = folium.Map(location=[clat, clon], zoom_start=7, tiles="Stamen Terrain")

df = pd.read_csv("https://raw.githubusercontent.com/meflynn/troopdata/master/data-raw/basedata.csv",encoding = "ISO-8859-1", engine='python')
df = df[['countryname','basename','lat','lon']]
df = df.dropna()

for index, row in df.iterrows():
    folium.Marker([row['lat'], row['lon']],tooltip=row['basename'] + " " + row['countryname']
                  ).add_to(m)


m.save('usbases-out.html')
```

[Output](usbases-out.html)

### Navy

<a name='navy'/>

```python
import pandas as pd, folium
m = folium.Map(location=[33,40], zoom_start=7, tiles="Stamen Terrain")

df = u.usnavy()

for index, row in df.iterrows():
    folium.Marker([row['lat'], row['lon']],tooltip=row['name'] + " " + row['bearing'] + " " + row['speed']
                  ).add_to(m)

m.save('usnavy-out.html')
```

[Output](usnavy-out.html)

<a name='nuke'/>

### Nuclear Bomb, Missile Sites

```python
import pandas as pd, folium

df = pd.read_csv('nuke.csv')

clat,clon=33, -111
m = folium.Map(location=[clat, clon], zoom_start=4, tiles="Stamen Terrain")

def split_nth(s, sep, n):
    n_split_groups = []
    groups = s.split(sep)
    while len(groups):
    	  n_split_groups.append(sep.join(groups[:n]))
    	  groups = groups[n:]
    return n_split_groups

for index, row in df.iterrows():
    descr = str(row['description'])
    descr = "<br>".join(split_nth(descr, " ", 5))
    s = str(row['bombs'])  + " bombs, " + descr
    s = s.replace("nan","")
    folium.Marker(        
        [row['latitude'], row['longitude']], tooltip=s
    ).add_to(m)
    
m.save('nuke-out.html')    
```

[Output](nuke-out.html)

