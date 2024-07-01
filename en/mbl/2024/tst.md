# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



















```python
app = u.biden_approval()
app = app[app.index > '2024-01-01']
print (app.net.tail(3))
app.net.plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```

```text
end_date
2024-06-28   -17.891216
2024-06-29   -18.507328
2024-06-30   -18.970774
Name: net, dtype: float64
```


