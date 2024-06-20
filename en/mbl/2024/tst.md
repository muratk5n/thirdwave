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
2024-05-12   -17.743053
2024-05-13   -17.500206
2024-05-14   -17.481513
Name: net, dtype: float64
```


