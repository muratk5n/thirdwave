

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/fl-0106.csv','ukrdata/fl-221115.csv',geo)
plt.savefig('/tmp/out.jpg',quality=50)
```

