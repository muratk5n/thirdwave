# Russian, Chinese Militaries

```python
import pandas as pd, folium
import impl as u
```

### Bases around the World

Red: Russia, Blue: China. [Source](https://datahub.hku.hk/articles/dataset/Overseas_Military_Bases/20438805).

```python
clat,clon=33, 40

m = folium.Map(location=[clat, clon], zoom_start=3)

df = pd.read_csv("rubases.csv",sep=';')
for index, row in df.iterrows():
    folium.CircleMarker([row['lat'], row['lon']],tooltip=row['basename'],
                  color='red',radius=5.0).add_to(m)

df = pd.read_csv("chbases.csv",sep=';')
for index, row in df.iterrows():
    folium.CircleMarker([row['lat'], row['lon']],tooltip=row['basename'],
                  color='blue',radius=5.0).add_to(m)

m.save('ch-ru-bases-out.html')
```

[Output](ch-ru-bases-out.html)


