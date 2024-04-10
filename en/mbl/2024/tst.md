# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```
























```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2024-04-05   -15.920577
2024-04-06   -15.416099
2024-04-07   -15.414668
2024-04-08   -15.407409
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



