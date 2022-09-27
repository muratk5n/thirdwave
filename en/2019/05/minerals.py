import pandas as pd
import folium, re, sys

def minerals():

    m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")
        
    df = pd.read_csv('mineral_iaea_geo_ur.csv',sep='|')
    for index, row in df.iterrows(): # 
        folium.CircleMarker(
            [row['Lat'], row['Lon']], 
            color='red',
            tooltip="%s, %s (%s), %s,%s" % (row['Status'], row['Amount'],row['Type'],row['Region'],row['Country']),
            radius=3
        ).add_to(m)

    df = pd.read_csv('mineral_base.csv')
    for index, row in df.iterrows(): # 
        folium.CircleMarker(
            [row['LATITUDE'], row['LONGITUDE']], 
            color='blue',
            tooltip="%s, %s, %s, %s" % (row['CRITICAL_MINERAL'],row['DEPOSIT_TYPE'],row['DEPOSIT_NAME'],row['LOCATION']),
            radius=3
        ).add_to(m)

        
    m.save('minerals-out.html')

if __name__ == "__main__": 
    minerals()
    
