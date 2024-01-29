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
2024-01-23   -16.746460
2024-01-24   -16.951214
2024-01-25   -16.869463
2024-01-26   -16.422299
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



