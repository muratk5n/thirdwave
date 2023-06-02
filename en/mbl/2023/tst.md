# Test


```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
df = pd.read_csv('/tmp/out1.csv')
clat,clon = 57, -130
u.get_sm().plot_countries(clat,clon,zoom=3.0)
dfb = df[df['box'] == 1]; plt.plot(dfb['longitude'],dfb['latitude'],'c.')
dfb = df[df['alaska'] == 1]; plt.plot(dfb['longitude'],dfb['latitude'],'r.')
plt.savefig('/tmp/out.jpg',quality=40)
```















```python
clat=48.59;clon=37.96
u.sm_plot_ukr1('ukrdata/fl-0521.csv','ukrdata/fl-0516.csv',["West Bakhmut Sports Complex","Bakhmut Children's Hospital","West Bakhmut Residential Area","Bakhmut"],clat,clon,zoom=0.005)
plt.savefig('/tmp/out.jpg',quality=40)
```
































```python
df = u.biden_approval()['net']
df.tail(4)
df.plot()
plt.savefig('/tmp/out.jpg')
```

```text
Out[1]: 
modeldate
2023-05-29   -13.302892
2023-05-30   -13.302892
2023-05-31   -13.664731
2023-06-01   -13.694300
Name: net, dtype: float64
```

