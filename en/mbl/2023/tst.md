
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



















```python
ps = [("Kramatorsk",48.73382111766231, 37.574050560223476),
      ("Bakhmut",48.596402146096274, 38.00607314033711)]
u.sm_plot_ukr('ukrdata/fl-0304.csv','ukrdata/fl-221115.csv',ps,clat=48.5,clon=38,zoom=0.1)
plt.savefig('/tmp/out.jpg')
```









