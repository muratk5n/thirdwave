

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.sm_kurds()
plt.savefig('/tmp/out.jpg')
```












```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1129.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

