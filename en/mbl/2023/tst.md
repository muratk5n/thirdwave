# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
u.sm_plot_ukr('ukrdata/fl-0416.csv','ukrdata/fl-0411.csv',[],clat=48.59,clon=37.98,zoom=0.3)
plt.savefig('/tmp/out.jpg',quality=40)
```


















```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-04-04   -10.103706
2023-04-05    -9.695323
2023-04-06    -9.941157
2023-04-07   -10.351105
Name: net, dtype: float64
```

