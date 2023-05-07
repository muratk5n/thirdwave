# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```








47.78053057704841, 37.24655291539728
   vuhledar
47.94145650439916, 37.507118165279365
   marinka
48.09170718659994, 37.61045940066837
   pervoaiske
49.04268923078684, 38.214576529855634
   kremminna




```python
u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0304.csv')
plt.savefig('/tmp/out.jpg',quality=40)
```









```python
u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0304.csv')
plt.savefig('/tmp/out.jpg',quality=40)
```















```python
u.sm_plot_ukr('ukrdata/fl-0501.csv','ukrdata/fl-0426.csv')
plt.savefig('/tmp/out.jpg',quality=40)
```























```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-05-02   -10.620722
2023-05-03   -10.101738
2023-05-04    -9.913536
2023-05-05    -9.643667
Name: net, dtype: float64
```

