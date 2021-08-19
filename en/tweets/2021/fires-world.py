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
