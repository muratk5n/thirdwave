




```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```












```python
u.sw_border_encounter('2022-Oct/sbo-encounters-fy19-fy22.csv')
#plt.savefig('/tmp/out.png')
```

```text
YMD
202209    227547.0
202210    164837.0
202211    174845.0
202212    179253.0
Name: Encounter Count, dtype: float64
```









```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1129.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

