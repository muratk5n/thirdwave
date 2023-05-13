# Test


```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```
















```python
u.sm_plot_libya1(["Ghadamis","Tripoli","Sirte"])
plt.savefig('/tmp/out.jpg',quality=40)
```

















```python
clat=48.59;clon=37.96
u.sm_plot_ukr1('ukrdata/fl-0511.csv','ukrdata/fl-0501.csv',['Khromove','Bakhmut Center'],clat,clon,zoom=0.005)
plt.savefig('/tmp/out.jpg',quality=40)
```















































```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-05-06    -9.643667
2023-05-07   -10.604047
2023-05-08    -9.947167
2023-05-09   -10.158535
Name: net, dtype: float64
```

