# Oil, Gas and Minerals

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
    ts = "%s, %0.2f mboe/day, %d Vessels/Year" % (row['Location'],row['Oil'],row['Ships'])
    folium.PolyLine(points, color='red', tooltip=ts, weight=4.0).add_to(m)
    
m.save('straits-out.html')
```

[Output](straits-out.html)

<a name='minerals'/>

### Other Fossil Fuels and Minerals

Base minerals are marked in blue, uranium is marked in red, coal in black.

Uranium data is from *World Distribution of Uranium Deposits (UDEPO)*,
2009 Edition. Base minerals are from [USGS](https://mrdata.usgs.gov/pp1802).
Coal data is from [Global Energy Monitor](https://globalenergymonitor.org/projects/global-coal-mine-tracker/).

[Data 1](mineral_base.csv),
[Data 2](mineral_iaea_geo_ur.csv),
[Data 3](mineral_iaea_ur.csv),
[Data 4](mineral-coal.csv)

[Code](minerals.py)

[Output](minerals-out.html)




