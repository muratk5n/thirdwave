import matplotlib.pyplot as plt
import simplegeomap 

def plot_africa_ru_us(ru,us):
    country_dict = simplegeomap.get_country_name_iso3()
    geo = simplegeomap.get_country_geo()
    colors = {}
    for x in ru: colors[country_dict[x]] = "red"
    for x in us: colors[country_dict[x]] = "yellowgreen"
    #plt.figure(figsize=(12, 10))
    plt.figure(figsize=(10, 8))
    #plt.figure()
    clat,clon=5.0910, 24.828
    zoom = 8.0
    simplegeomap.plot_countries(clat,clon,zoom,country_color=colors)
    for k in colors:
        lat,lon = geo[k]
        plt.text(lon-2,lat,k)

    
