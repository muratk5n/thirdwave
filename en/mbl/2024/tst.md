# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```
































```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
print (app.net.tail(3))
app.net.plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```

```text
end_date
2024-06-18   -17.713626
2024-06-19   -16.813872
2024-06-20   -16.596729
Name: net, dtype: float64
```


