
```python
import impl as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(2021,['DGS3MO','DGS6MO','DGS1','DGS2','DGS3','DGS5','DGS7','DGS10','DGS20','DGS30'])
inv = df.tail(1).T
inv.columns = ['Treasury Curve']
inv.plot()
plt.savefig('/tmp/out.jpg')
```





