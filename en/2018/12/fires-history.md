# Forest Fire Historical Data

Annual count for worldwide fires; based on FIRMS [data](https://firms.modaps.eosdis.nasa.gov/country/)

Downloaded select years, 2000,05, etc. the code below scans
all countries, counts number of fire (pixels) above a certain
brightness threshold. 

```python
import pandas as pd, zipfile, datetime
THRESHOLD = 450.0
count = 0
for y in [2000,2005,2010,2015,2020]:
    with zipfile.ZipFile('modis_%d_all_countries.zip' % y, 'r') as z:
          zfiles =  z.namelist()
          for zf in zfiles:
              if ".csv" not in zf: continue
              df =  pd.read_csv(z.open(zf))
              df = df[df.brightness > THRESHOLD]
              count += len(df)          
    print ('year', y, ":", count)
```

```
2000 : 144
2005 : 4100
2010 : 7533
2015 : 11607
2020 : 16365
```

Looks bad.. The number of fires increase at each period, in two actually
doubling.

