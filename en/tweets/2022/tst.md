

```python
# bakhmut, kramatorsk
import util as u, pandas as pd
import simplegeomap as sm

geo = [(48.599201519702945, 38.01322689318272),(48.7309677, 37.5836740)]
#u.sm_plot_ukr('ukrdata/alt1-0828.csv',geo)
#u.sm_plot_ukr('ukrdata/alt1-0913.csv',geo)
#u.sm_plot_ukr('ukrdata/donetsk.csv',[])

df = np.array(pd.read_csv('ukrdata/alt1-0913.csv',header=None))
df[:, [1, 0]] = df[:, [0, 1]]
clat,clon=48, 37; zoom = 0.6
sm.plot_countries(clat,clon,zoom,outcolor='lavenderblush')
sm.plot_region(df,color='lightblue')

df = np.array(pd.read_csv('ukrdata/donetsk.csv',header=None))
sm.plot_line(df,color='red')

eps = 0.1
for i,(lat,lon) in enumerate(geo):
    plt.text(lon+eps,lat+eps,i+1)
    plt.plot(lon,lat,'gx')



plt.savefig('/tmp/out1.png')
```




