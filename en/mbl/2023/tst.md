# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```














```python
#u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0426.csv')
u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0304.csv')
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

