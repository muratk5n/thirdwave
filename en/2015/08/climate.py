import pandas as pd, gc, netCDF4, psutil 
import csv, numpy as np
import matplotlib.pyplot as plt

def average_regions():
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

    tmp_clims = np.zeros(time.shape[0])
    time_idxs = np.array(range(time.shape[0]))
    res = []
    for region in range(anom.shape[1]):
        base_temps = clim[monidxs, region]
        real_temps = base_temps + anom[:, region]
        tmp = pd.Series(real_temps)
        tmp = tmp.replace('--', np.nan)
        tmp = tmp.interpolate(method='linear',limit_direction='backward')
        res.append(list(tmp))

    arr = np.array(res)
    df = pd.DataFrame(res)

    avg = pd.DataFrame(df.median(axis=0))
    avg['year'] = avg.apply(lambda x: year(time[x.name]),axis=1)
    avg['mon'] = avg.apply(lambda x: month(time[x.name]),axis=1)
    avg['mon'] = avg['mon'] + 1
    avg['dt'] = avg.apply(lambda x: pd.to_datetime("%d-%02d-01" %(x.year,x.mon)), axis=1)
    avg[['dt',0]].to_csv('global_temperature.csv',index=None)
    avg = avg.set_index('dt')
    avg = avg[0]
    avg = avg[avg.index > '1900-01-01']  
    avg = avg.rolling(50).mean()
    avg.plot()
    plt.savefig('berkeley-temp.png')

if __name__ == "__main__":  
    average_regions()
