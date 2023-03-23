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









