from datetime import datetime
import numpy as np
from netCDF4 import Dataset, num2date
from scipy.ndimage import gaussian_filter
from siphon.catalog import TDSCatalog
import mygeo

def ike(lat,lon,day,month,year,hour):

    # form grid which has NE, and SW cornes brg kilometers away
    # from center lat,lon
    brg = 1000
    upper_right = mygeo.to_bearing(lat,lon,np.deg2rad(45),brg)
    lower_left = mygeo.to_bearing(lat,lon,np.deg2rad(225),brg)

    north = int(upper_right[0])
    south = int(lower_left[0])
    east = int(upper_right[1])
    west = int(lower_left[1])

    side = np.cos(np.deg2rad(45))*brg*2
    area = side*side*1e6

    dt = datetime(year, month, day, hour)

    base_url = 'https://www.ncei.noaa.gov/thredds/catalog/model-narr-a-files/'
    cat = TDSCatalog(f'{base_url}{dt:%Y%m}/{dt:%Y%m%d}/catalog.xml')
    ds = cat.datasets.filter_time_nearest(dt)
    ncss = ds.subset()

    query = ncss.query()
    query.lonlat_box(north=north, south=south, east=east, west=west)
    query.all_times()
    query.add_lonlat()
    query.accept('netcdf')
    query.variables('u-component_of_wind_isobaric',
                    'v-component_of_wind_isobaric')

    data = ncss.get_data(query)
    u_wind_var = data.variables['u-component_of_wind_isobaric']
    v_wind_var = data.variables['v-component_of_wind_isobaric']
    u_wind = u_wind_var[0, 0, :, :].squeeze() 
    v_wind = v_wind_var[0, 0, :, :].squeeze() 

    gi,gj = u_wind.shape
    cell_count = gi*gj
    cell_area = area / cell_count

    wspeedsquare = u_wind**2+v_wind**2
    wspeedsquare = wspeedsquare.reshape(-1)
    wspeedsquare = wspeedsquare[wspeedsquare > 30.0]
    IKE = np.sum(0.5*wspeedsquare*cell_area) / 1e12
    return IKE
