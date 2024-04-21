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
2024-04-16   -16.184816
2024-04-17   -17.292626
2024-04-18   -17.184241
2024-04-19   -17.034775
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



