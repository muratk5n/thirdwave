import pandas as pd
import folium

m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")

def plot_rows(df):
    for index, row in df.iterrows():
        color = 'red'
        if 'Gas' in row['FIELD_TYPE']:
           color = 'blue'
        folium.CircleMarker(
            [row['LAT_DD'], row['LON_DD']], 
            color=color,
            tooltip=row['FLD_NAME'] + " " + str(int(row['EUR_MMBOE'])) + " mmboe (" + row['FIELD_TYPE'] + ")",
            radius=3
        ).add_to(m)

df = pd.read_csv('oilgas-2018.csv')
plot_rows(df)
df = pd.read_csv('oilgas-plus.csv')
plot_rows(df)
        
m.save('oilgas-out.html')
