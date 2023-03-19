
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
u.get_masto_detail("wptoots.social")
```

```text
Out[1]: (68, '2022-11-18')
```



```text
Out[1]: (8211, '2023-01-11')
```






```python
ps = ["Kramatorsk","Bakhmut","Chasiv Yar","Soledar","Kostyantynivka","Orikhovo-Vasylivka"]
u.sm_plot_ukr('ukrdata/fl-0304.csv','ukrdata/fl-221115.csv',
              ps,clat=48.6,clon=37.8,zoom=0.06)
plt.savefig('/tmp/out.jpg',quality=40)
```









