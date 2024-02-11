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
2024-02-06   -16.601430
2024-02-07   -17.105172
2024-02-08   -17.018775
2024-02-09   -17.225691
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



