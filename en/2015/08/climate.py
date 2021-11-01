'''
https://climateestimate.net/content/example-step1.html

https://github.com/hausfath/warming_map/blob/master/gridbox_csvs.py

https://github.com/hdrake/climatepy-tutorial/blob/master/notebooks/climate_data_tutorial.ipynb

http://berkeleyearth.org/data/

https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/
'''
import pandas as pd, gc, netCDF4, psutil 
import csv, numpy as np
import matplotlib.pyplot as plt

def preproc1():
    url='/tmp/Land_and_Ocean_EqualArea.nc'
    nc = netCDF4.Dataset(url)
    clim = nc['climatology'][:,:]
    anom =  nc['temperature'][:,:]
    time =  nc['time'][:]

    dfclim = pd.DataFrame(clim.T)
    pd.set_option('display.max_columns', None)
    dfclim2 = dfclim.reset_index()
    dfclim2 = pd.melt(dfclim2, id_vars=['index'])
    dfclim2['variable'] = dfclim2['variable'] + 1
    dfclim2 = dfclim2.set_index(['index','variable'])

    def year(float_year):
        year = int(float_year)
        return year

    def month(float_year):
        month = int((float_year % 1) * 12)
        return month

    dftime = pd.DataFrame(time)
    dftime['year'] = dftime.apply(lambda x: year(x[0]),axis=1)
    dftime['mon'] = dftime.apply(lambda x: month(x[0]),axis=1)
    dftime['mon'] = dftime['mon'] + 1

    dfanom = pd.DataFrame(anom.T)
    dfanom = dfanom.reset_index()
    dfanom2 = pd.melt(dfanom,id_vars=['index'])

    df1 = pd.merge(dfanom2, dftime, left_on='variable', right_index=True, how='left')

    df1.to_csv('/tmp/out1.csv',index=None)
    dfclim2.to_csv('/tmp/clim.csv')
    print ('stage 1 complete')

def preproc2():
    fout = open("/tmp/berkeley.csv","w")

    dfclim = pd.read_csv('/tmp/clim.csv',index_col=['index','variable'])
    dfclimdict = dfclim.to_dict()
    print (dfclimdict['value'][(200,1)])

    with open('/tmp/out1.csv') as csvfile:
         rd = csv.reader(csvfile,delimiter=',')
         headers = {k: v for v, k in enumerate(next(rd))}
         print (headers)
         for i,row in enumerate(rd):
             key = ( int(row[headers['index']]), int(row[headers['mon']]))
             if not row[headers['value']]: continue
             if key in dfclimdict['value']:
                mon = int(row[headers['mon']])          
                year = int(row[headers['year']]) 
                clim = dfclimdict['value'][key]            
                anom = np.float( row[headers['value']] )
                #print (year,mon,clim,anom)
                #fout.write("%d,%d,%f,%f\n" % ((year,mon,clim,anom)))
                fout.write("%d,%d,%f\n" % ((year,mon,clim+anom)))
                fout.flush()

    fout.close()
    print ('stage 2 complete')

def plot():
    df = pd.read_csv('/tmp/berkeley.csv',header=None)
    print (df)
    avg = df.groupby([0,1]).median().reset_index()
    avg['dt'] = avg.apply(lambda x: pd.to_datetime("%d-%02d-01" %(x[0],x[1])), axis=1)
    avg = avg.set_index('dt')
    print (avg)
    avg = avg[avg.index > '1900-01-01']  
    avg[2].plot()
    plt.savefig('berkeley-temp.png')    
    
if __name__ == "__main__": 
    #preproc1()
    #preproc2()
    plot()
    
