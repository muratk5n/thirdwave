import pandas as pd
import folium

m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")

df = pd.read_csv('oilgas-2018.csv')

for index, row in df.iterrows():
    color = 'red'
    if row['FIELD_TYPE']=='Gas':
       color = 'blue'
    folium.CircleMarker(
        [row['LAT_DD'], row['LON_DD']], 
        color=color,
        tooltip=row['FLD_NAME'] + " " + str(int(row['EUR_MMBOE'])) + " mmboe",
        radius=2
    ).add_to(m)

m.save('oilgas-out.html')
