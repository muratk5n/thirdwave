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
2024-07-01   -18.710026
2024-07-02   -19.425364
2024-07-03   -20.015083
Name: net, dtype: float64
```








