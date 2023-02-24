
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.usnavy(); u.sm_plot_list1(38, 24, 2.0, np.array(df[['name','lat','lon']]))
plt.savefig('/tmp/out.jpg',quality=40)
```












```python
u.sm_plot_ukr('ukrdata/fl-0212.csv','ukrdata/fl-221115.csv',[])
plt.savefig('/tmp/out.jpg')
```









