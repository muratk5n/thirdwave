# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
u.boxofficemojo("Blackhat")
```

```text
Out[1]: 
{'Domestic Opening': '$3,901,815',
 'Domestic': '$8,005,980',
 'International': '$11,646,077',
 'Worldwide Total': '$19,652,057',
 'Release Date': 'January 15, 2015'}
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
2023-03-29   -10.400897
2023-03-30   -10.605330
2023-03-31   -10.766547
2023-04-01   -10.761750
Name: net, dtype: float64
```

