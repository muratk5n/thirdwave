# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.modis_fire('fire1.html')
```











```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2024-02-23   -16.050079
2024-02-24   -15.911317
2024-02-25   -15.846404
2024-02-26   -15.488056
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



