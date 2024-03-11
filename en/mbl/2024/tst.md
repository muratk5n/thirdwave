# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.sat_img(48.85859253797154, 2.2945835762002353, 17, "/tmp/out.jpg")
```







```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2024-03-05   -18.195010
2024-03-06   -18.693528
2024-03-07   -18.240259
2024-03-08   -17.940489
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



