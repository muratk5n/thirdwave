# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
sh = np.vstack([np.array(u.usnavy()[['name','lat','lon']]), ['Taiwan',23,120]])
u.sm_plot_list1(29, 131, 2.0, sh)
plt.savefig('/tmp/out.jpg',quality=50)
```










```python
ps = ["Bakhmut"]
u.sm_plot_ukr('ukrdata/fl-0404.csv','ukrdata/fl-2203.csv',
              ps,clat=48.6,clon=37.95,zoom=0.01)
plt.savefig('/tmp/out.jpg',quality=40)
```

















```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-04-04   -10.103706
2023-04-05    -9.695323
2023-04-06    -9.941157
2023-04-07   -10.351105
Name: net, dtype: float64
```

