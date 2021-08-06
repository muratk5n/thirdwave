import pandas as pd, datetime, numpy as np
from io import BytesIO
import urllib.request as urllib2
import folium

clat,clon=33, 30

m = folium.Map(location=[clat, clon], zoom_start=2, tiles="Stamen Terrain")

THRESHOLD = 400.0

df = pd.read_csv('https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_7d.csv')
for index, row in df.iterrows():
    print (index)
    if row['brightness'] < THRESHOLD: continue
    folium.CircleMarker(location=[row['latitude'], row['longitude']],
                        radius=1.0,
			color='red',
                        weight=1).add_to(m)

m.save('fires-out.html')
