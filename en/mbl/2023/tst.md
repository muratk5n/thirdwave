
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
df = u.eq_at(lat=38,lon=39,radius=200,ago=30)
df = df[df.mag > 5.0]
print (df[['mag','ago','lat','lon']].tail(3))
```

```text
                     mag  ago      lat      lon
date                                           
2023-02-08 14:11:52  5.4   20  37.9368  37.6607
2023-02-08 17:20:25  5.1   20  37.9629  37.4580
2023-02-27 12:04:51  5.2    1  38.2289  38.2828
```




```python
#u.rottentomatoes_mov("Ant Man 3")
u.boxofficemojo("Ant Man 3")
```



















```python
u.sm_plot_ukr('ukrdata/fl-0224.csv','ukrdata/fl-221115.csv',[])
plt.savefig('/tmp/out.jpg')
```









