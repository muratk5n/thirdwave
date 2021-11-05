'''
https://earthobservatory.nasa.gov/features/GISSTemperature/giss_temperature4.php

https://climateestimate.net/content/example-step1.html

https://github.com/hausfath/warming_map/blob/master/gridbox_csvs.py

https://github.com/hdrake/climatepy-tutorial/blob/master/notebooks/climate_data_tutorial.ipynb

http://berkeleyearth.org/data/

https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/
'''
import pandas as pd, gc, netCDF4, psutil 
import csv, numpy as np
import matplotlib.pyplot as plt

url='/tmp/Complete_TAVG_EqualArea.nc'
nc = netCDF4.Dataset(url)
clim = nc['climatology'][:,:]
anom =  nc['temperature'][:,:]
time =  nc['time'][:]

print (clim.shape)
print (anom.shape)
print (time.shape)

def year(float_year):
    year = int(float_year)
    return year

def month(float_year):
    month = int((float_year % 1) * 12)
    return month

monidxs = np.array(list(map(month, time)))
print (monidxs[330])
print (time[330])

tmp_clims = np.zeros(time.shape[0])
time_idxs = np.array(range(time.shape[0]))
res = []
for region in range(anom.shape[1]):
    base_temps = clim[monidxs, region]
    real_temps = base_temps + anom[:, region]
    tmp = pd.Series(real_temps)
    tmp = tmp.replace('--', np.nan)
    res.append(list(tmp))
    #if region==3: break

arr = np.array(res)
print (arr.shape)
df = pd.DataFrame(res)
print (df)
print (df.shape)

avg = pd.DataFrame(df.median(axis=0))
avg['year'] = avg.apply(lambda x: year(time[x.name]),axis=1)
avg['mon'] = avg.apply(lambda x: month(time[x.name]),axis=1)
avg['mon'] = avg['mon'] + 1
avg['dt'] = avg.apply(lambda x: pd.to_datetime("%d-%02d-01" %(x.year,x.mon)), axis=1)
avg = avg.set_index('dt')
avg = avg[0]
avg = avg[avg.index > '1900-01-01']  
print (avg)
print (avg.shape)
avg = avg.rolling(50).mean()
avg.plot()
plt.savefig('berkeley-temp.png')


