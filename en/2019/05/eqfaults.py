import json, folium
d = json.loads(open("gem_active_faults_harmonized.geojson").read())
m = folium.Map(location=[30, 20], zoom_start=3)
for idx in range(len(d['features'])):
    coords = d['features'][idx]['geometry']['coordinates']
    coords = [[x[1],x[0]] for x in coords]
    ts = d['features'][idx]['properties'].get('name')
    if not ts: ts = ''
    dip = str(d['features'][idx]['properties'].get('average_dip'))
    tp = str(d['features'][idx]['properties'].get('slip_type'))
    ts += " dip: " + dip
    ts += " type: " + tp
    folium.PolyLine(coords, color='blue', weight=2.0, tooltip=ts).add_to(m)
m.save('eq-fault-lines.html')
