from pygeodesy.sphericalNvector import LatLon
import numpy as np, folium

clat,clon=33, 30
m = folium.Map(location=[clat, clon], zoom_start=2, tiles="Stamen Terrain")

# larger box
big = LatLon(37.37121348080846, -95.92924913128172),\
      LatLon(33.07997873234234, -55.89200093297422),\
      LatLon(15.600825365750481, -63.333267906537074), \
      LatLon(17.030873110570198, -98.71084233003333)

# the triangle
berm = LatLon(32.273, -64.899), LatLon(25.700, -80.218), LatLon(18.579, -66.061)

fin = open("MarCas_Part1/vcas.txt")

s = []
for line in fin.readlines():
    tokens = line.split('\t')
    if len(tokens[11])==0: continue
    if len(tokens[4])==0: continue
    t9 = tokens[9].strip().split(" ")
    t11 = tokens[11].strip().split(" ")
    if len(t9)<2 or len(t11)<2: continue
    try:
        if tokens[8] != "N" or tokens[10] != "W": continue
        if len(t9[1])==0: t9[1]="0.0"
        if len(t11[1])==0: t11[1]="0.0"
        lat1,lat2=t9[0],t9[1]
        lon1,lon2=t11[0],t11[1]
        lat = "%d.%d" % (int(lat1),int(float(lat2)))
        lon = "%d.%d" % (int(lon1),int(float(lon2)))
        p = LatLon(float(lat), -float(lon))
        newlat,newlon = float(lat), -float(lon)
        if p.isenclosedBy(berm): 
            folium.CircleMarker(location=[newlat,newlon],radius=1.0,color='blue',weight=1).add_to(m)
        elif p.isenclosedBy(big):
            folium.CircleMarker(location=[newlat,newlon],radius=1.0,color='red',weight=1).add_to(m)
    except:
        continue

m.save('bermuda-out.html')
    
