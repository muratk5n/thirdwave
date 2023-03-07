
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```










```python
ps = ["Vuhledar","Kramatorsk","Bakhmut","Chasiv Yar","Soledar","Rai-Oleksandrivka"]
u.sm_plot_ukr('ukrdata/fl-0304.csv','ukrdata/fl-221115.csv',
              ps,clat=48.6,clon=37.8,zoom=0.06)
plt.savefig('/tmp/out.jpg',quality=40)
```









