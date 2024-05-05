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
2024-05-01   -17.015128
2024-05-02   -16.741646
2024-05-03   -15.922098
Name: net, dtype: float64
```


