import pandas as pd, zipfile, random, folium

with zipfile.ZipFile('nuforc-ufo.zip', 'r') as z:
      df =  pd.read_csv(z.open('scrubbed.csv'))

clat,clon=33, 40

m = folium.Map(location=[clat, clon], zoom_start=4, tiles="Stamen Terrain")
for index, row in df.iterrows():
    try: 
        year = pd.to_datetime(row['datetime']).year
        if year<2010: continue
        if random.choice(range(12))!=0: continue
        folium.CircleMarker(location=[row['latitude'], row['longitude']],
                            tooltip=row['comments'],
                            radius=6,
			    color='red',
                            weight=1).add_to(m)        
    except:
        pass

m.save('ufo-out.html')
