import pandas as pd
import folium, re, sys

def plot_rows(df, m):
    for index, row in df.iterrows(): # 
        color = 'red'
        if 'Gas' in row['FIELD_TYPE']:
           color = 'blue'
        folium.CircleMarker(
            [row['LAT_DD'], row['LON_DD']], 
            color=color,
            tooltip=row['FLD_NAME'] + " " + str(int(row['EUR_MMBOE'])) + " mmboe (" + row['FIELD_TYPE'] + ")",
            radius=3
        ).add_to(m)

def fields():
    m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")
    df = pd.read_csv('oilgas-2018.csv')
    plot_rows(df,m)
    df = pd.read_csv('oilgas-plus.csv')
    plot_rows(df,m)
    m.save('oilgas-out.html')

def get_linestring(content):
   points = []
   c = content.replace("LINESTRING","").replace("(","").replace(")","")
   res = c.split(",")
   for x in res:
      cs = x.split()
      if len(cs)<2: continue
      points.append((float(cs[1]), float(cs[0])))
   return points
    
def pipelines():
    df = pd.read_csv('pipelines.csv',sep=';')
    m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")
    for index, row in df.iterrows():
       if 'Cancelled' in row['Status'] or 'Shelved' in row['Status']: continue
       segments = []
       ts = row['PipelineName'] + " " + row['StartCountry']+"-"+row['EndCountry'] + " "
       if 'nan' not in str(row['Capacity']):
          ts += str(row['Capacity']) + " " + str(row['CapacityUnits']) + " "          
          if "MMcf/d" in str(row['CapacityUnits']):
              ts += str(int(float(row['Capacity'])*1e6/(5800*1000))) + " kboe/d "
          if "bcm/year" in str(row['CapacityUnits']) or "bcm/y" in str(row['CapacityUnits']):
              ts += str(int(float(row['Capacity'])*1e9/(170*365*1000))) + " kboe/d "
       ts += "(" + row['Status'] + ") "
       if "MULTILINESTRING" in row['WKTFormat']:
          c = row['WKTFormat'].replace("MULTILINESTRING","")
          linestrings = c.split("),")
          for x in linestrings:
             xx = x.replace("(","").replace("(","").replace(")","")
             res = get_linestring(xx)
             segments.append(res)
       elif 'LINESTRING' in row['WKTFormat']:
          points = get_linestring(row['WKTFormat'])
          segments.append(points)
       for points in segments:
          if len(points)==0: continue
          folium.PolyLine(points, color='blue', weight=2.0, tooltip=ts).add_to(m)

    df = pd.read_csv('oilgas-2018.csv')
    plot_rows(df,m)
    df = pd.read_csv('oilgas-plus.csv')
    plot_rows(df,m)
          
    m.save('pipelines.html')

if __name__ == "__main__": 
    pipelines()
    
