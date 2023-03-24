# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```









```python
ps = ["Zalisnyanske","Orikhovo-Vasylivka","Bakhmut"]
u.sm_plot_ukr('ukrdata/fl-2203.csv','ukrdata/fl-0304.csv',
              ps,clat=48.6,clon=37.8,zoom=0.04)
plt.savefig('/tmp/out.jpg',quality=40)
```

















```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
modeldate
2023-03-21    -8.236541
2023-03-22    -8.811406
2023-03-23   -10.075967
2023-03-24    -9.677857
Name: net, dtype: float64
```

