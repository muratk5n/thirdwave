# NOAA Recent Reanalysis Data


https://psl.noaa.gov/thredds/catalog/Datasets/NARR/catalog.html

https://psl.noaa.gov/thredds/catalog/Datasets/NARR/Dailies/monolevel/catalog.html?dataset=Datasets/NARR/Dailies/monolevel/uwnd.10m.2021.nc


```python
import netCDF4

#url = "uwnd.sig995.2021.nc"
url = "uwnd.10m.2021.nc"
nc = netCDF4.Dataset(url)
print (nc)
```

```text
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF4_CLASSIC data model, file format HDF5):
    Conventions: CF-1.2
    centerlat: 50.0
    centerlon: -107.0
    comments: 
    institution: National Centers for Environmental Prediction
    latcorners: [ 1.000001  0.897945 46.3544   46.63433 ]
    loncorners: [-145.5       -68.32005    -2.569891  148.6418  ]
    platform: Model
    standardpar1: 50.0
    standardpar2: 50.000001
    title: Daily NARR
    history: created Sat Mar 26 05:25:45 MDT 2016 by NOAA/ESRL/PSD
    dataset_title: NCEP North American Regional Reanalysis (NARR)
    references: https://www.esrl.noaa.gov/psd/data/gridded/data.narr.html
    source: http://www.emc.ncep.noaa.gov/mmb/rreanl/index.html
    References: 
    dimensions(sizes): time(334), y(277), x(349), nbnds(2)
    variables(dimensions): float64 time(time), float32 lat(y, x), float32 lon(y, x), float32 y(y), float32 x(x), int32 Lambert_Conformal(), float32 uwnd(time, y, x), float64 time_bnds(time, nbnds)
    groups: 
```

```python
lat = nc['lat'][:]
print (lat.shape)
lon = nc['lon'][:]
print (lon.shape)
uwnd = nc['uwnd'][:,:,:]
print (uwnd.shape)
```

```text
(277, 349)
(277, 349)
(334, 277, 349)
```



mayfield kentucky
36.728334068830755, -88.7063255602711

https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis/surface/catalog.html

https://psl.noaa.gov/cgi-bin/db_search/DBListFiles.pl?did=195&tid=96617&vid=1263





```text
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF4_CLASSIC data model, file format HDF5):
    Conventions: COARDS
    title: 4x daily NMC reanalysis (2014)
    history: created 2017/12 by Hoop (netCDF2.3)
    description: Data is from NMC initialized reanalysis
(4x/day).  These are the 0.9950 sigma level values.
    platform: Model
    dataset_title: NCEP-NCAR Reanalysis 1
    References: http://www.psl.noaa.gov/data/gridded/data.ncep.reanalysis.html
    dimensions(sizes): lat(73), lon(144), time(1380)
    variables(dimensions): float32 lat(lat), float32 lon(lon), float64 time(time), float32 uwnd(time, lat, lon)
    groups: 
```

```python
lat = nc['lat'][:]
print (lat.shape)
lon = nc['lon'][:]
print (lon.shape)
uwnd = nc['uwnd'][:,:,:]
print (uwnd.shape)
```

```text
(73,)
(144,)
(1380, 73, 144)
```

```python
print (uwnd[0,0,0])
```
```text
-3.3
```

```python
print (lat)
print (lon)
```

```text
<xarray.DataArray 'lat' (lat: 73)>
array([ 90. ,  87.5,  85. ,  82.5,  80. ,  77.5,  75. ,  72.5,  70. ,  67.5,
        65. ,  62.5,  60. ,  57.5,  55. ,  52.5,  50. ,  47.5,  45. ,  42.5,
        40. ,  37.5,  35. ,  32.5,  30. ,  27.5,  25. ,  22.5,  20. ,  17.5,
        15. ,  12.5,  10. ,   7.5,   5. ,   2.5,   0. ,  -2.5,  -5. ,  -7.5,
       -10. , -12.5, -15. , -17.5, -20. , -22.5, -25. , -27.5, -30. , -32.5,
       -35. , -37.5, -40. , -42.5, -45. , -47.5, -50. , -52.5, -55. , -57.5,
       -60. , -62.5, -65. , -67.5, -70. , -72.5, -75. , -77.5, -80. , -82.5,
       -85. , -87.5, -90. ], dtype=float32)
Coordinates:
  * lat      (lat) float32 90.0 87.5 85.0 82.5 80.0 ... -82.5 -85.0 -87.5 -90.0
Attributes:
    units:          degrees_north
    actual_range:   [ 90. -90.]
    long_name:      Latitude
    standard_name:  latitude
    axis:           Y
<xarray.DataArray 'lon' (lon: 144)>
array([  0. ,   2.5,   5. ,   7.5,  10. ,  12.5,  15. ,  17.5,  20. ,  22.5,
        25. ,  27.5,  30. ,  32.5,  35. ,  37.5,  40. ,  42.5,  45. ,  47.5,
        50. ,  52.5,  55. ,  57.5,  60. ,  62.5,  65. ,  67.5,  70. ,  72.5,
        75. ,  77.5,  80. ,  82.5,  85. ,  87.5,  90. ,  92.5,  95. ,  97.5,
       100. , 102.5, 105. , 107.5, 110. , 112.5, 115. , 117.5, 120. , 122.5,
       125. , 127.5, 130. , 132.5, 135. , 137.5, 140. , 142.5, 145. , 147.5,
       150. , 152.5, 155. , 157.5, 160. , 162.5, 165. , 167.5, 170. , 172.5,
       175. , 177.5, 180. , 182.5, 185. , 187.5, 190. , 192.5, 195. , 197.5,
       200. , 202.5, 205. , 207.5, 210. , 212.5, 215. , 217.5, 220. , 222.5,
       225. , 227.5, 230. , 232.5, 235. , 237.5, 240. , 242.5, 245. , 247.5,
       250. , 252.5, 255. , 257.5, 260. , 262.5, 265. , 267.5, 270. , 272.5,
       275. , 277.5, 280. , 282.5, 285. , 287.5, 290. , 292.5, 295. , 297.5,
       300. , 302.5, 305. , 307.5, 310. , 312.5, 315. , 317.5, 320. , 322.5,
       325. , 327.5, 330. , 332.5, 335. , 337.5, 340. , 342.5, 345. , 347.5,
       350. , 352.5, 355. , 357.5], dtype=float32)
Coordinates:
  * lon      (lon) float32 0.0 2.5 5.0 7.5 10.0 ... 350.0 352.5 355.0 357.5
Attributes:
    units:          degrees_east
    long_name:      Longitude
    actual_range:   [  0.  357.5]
    standard_name:  longitude
    axis:           X
```

mayfield kentucky
36.728334068830755, -88.7063255602711

```python
print (-88 % 360)
```

```text
272
```

```python
#print (lat[21])
#print (lon[110])
print (uwnd[2,21,110])
```

```text
-7.1999984
```

```python
print (1380/4)
```

```text
345.0
```

Bcz Dec 10 was the last
