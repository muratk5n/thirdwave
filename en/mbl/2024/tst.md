# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
df = u.get_fred(2018,['FEDFUNDS','MSPUS'])
df = df.interpolate()
u.two_plot(df.FEDFUNDS, 'rate', df.MSPUS, 'median houses')
plt.savefig('/tmp/out.jpg')
```

















```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2024-02-13   -17.669385
2024-02-14   -16.998960
2024-02-15   -16.935314
2024-02-16   -16.556731
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



