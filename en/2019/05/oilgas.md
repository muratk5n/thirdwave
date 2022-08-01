# Oil and Gas 

### Fields

Large oil and gas fields along with their BOE estimated reserves at
the time of discovery.

[Data Source](https://github.com/alexis-ribal/giant-oil-and-gas-field-discoveries/)

[Data 1](oilgas-2018.csv), [Data 2](oilgas-plus.csv)

[Code](oilgas.py)

[Output](oilgas-out.html)

<a name='pipelines'/>

### Pipelines

All units are converted to kboe/d meaning kilo (thousand) barrels of
oil equivalent per day.

[Data Source](https://globalenergymonitor.org/)

[Data](pipelines.csv)

[Output](pipelines.html)

<a name='straits'/>

### Transport Chokepoints, Straits

```python
import folium, pandas as pd, json
df = pd.read_csv('straits.csv',sep=';')
m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")
for index, row in df.iterrows():
    points = json.loads(row['Path'])
    ts = "%s, %0.2f mboe/day" % (row['Location'],row['Volume'])
    folium.PolyLine(points, color='red', tooltip=ts, weight=4.0).add_to(m)
    
m.save('straits-out.html')
```

[Output](straits-out.html)



























