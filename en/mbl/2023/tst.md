# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```
















```python
#u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0426.csv')
u.sm_plot_ukr2('ukrdata/fl-0501.csv','ukrdata/fl-0404.csv')
plt.savefig('/tmp/out.jpg',quality=40)
```
























```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-04-23   -10.651749
2023-04-24   -10.352707
2023-04-25   -11.497941
2023-04-26   -10.667035
Name: net, dtype: float64
```

