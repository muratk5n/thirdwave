# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df1 = u.get_wlt_sp()
df2 = u.get_yahoofin(1990,"^GSPC")
```

```python
u.two_plot(df1['Top 10%'],'Top 10%',df2, 'SP 500')
plt.savefig('/tmp/out.jpg',quality=30)
```









```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2023-12-26   -16.112096
2023-12-27   -16.577882
2023-12-28   -16.313949
2023-12-29   -16.151800
Name: net, dtype: float64
```




