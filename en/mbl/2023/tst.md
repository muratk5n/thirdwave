
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.sm_plot_kurd()
plt.plot(44.361682512831514,35.469605798313246,'+') # kirkuk
plt.savefig('/tmp/out.jpg',quality=40)
```









```python
geo = [['Soledar',48.68207521521989, 38.08963574290512,(5,20)],
       ['Bakhmut',48.59681687669557, 37.99571812076628,(-20,0)]
       ]
u.sm_plot_ukr('ukrdata/fl-0116.csv','ukrdata/fl-221115.csv',geo)
plt.savefig('/tmp/out.jpg')
```









