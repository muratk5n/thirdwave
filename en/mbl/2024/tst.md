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
2024-01-06   -17.388328
2024-01-07   -17.382915
2024-01-08   -17.358060
2024-01-09   -17.898006
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



