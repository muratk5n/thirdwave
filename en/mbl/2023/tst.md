
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.biden_approval()
```

```python
df.net.plot()
plt.savefig('/tmp/out.jpg')
```











```python
u.sm_plot_ukr('ukrdata/fl-0212.csv','ukrdata/fl-221115.csv',[])
plt.savefig('/tmp/out.jpg')
```









