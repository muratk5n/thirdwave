import numpy as np, io
import matplotlib.pyplot as plt
import pandas as pd, zipfile
import urllib.request as urllib2
r = urllib2.urlopen("https://raw.githubusercontent.com/zhukovyuri/VIINA/master/Data/control_latest.zip").read()
file = zipfile.ZipFile(io.BytesIO(r))
csv = file.open("control_latest.csv")
df = pd.read_csv(csv)
print ('in dataframe')
cols = [x for x in df.columns if 'ctr_'  in x]
df2 = df[cols]
df2.replace("RU",1,inplace=True)
df2.replace("UA",0,inplace=True)
df2.replace("CONTESTED",0,inplace=True)
print (df2.shape)
print ('sum')
df2.sum(axis=0).tail(600).plot()
plt.savefig('viina-control.png')







