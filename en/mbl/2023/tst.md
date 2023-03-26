# Test code

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.boxofficemojo("Terminator Dark Fate")
```

```text
Out[1]: 
{'Domestic Opening': '$29,033,832',
 'Domestic': '$62,253,077',
 'International': '$198,866,215',
 'Worldwide Total': '$261,119,292',
 'Release Date': 'October 23, 2019'}
```


```python
u.boxofficemojo("Shazam 2")
```

```text
Out[1]: 
{'Domestic Opening': '$30,111,158',
 'Domestic': '$38,956,765',
 'International': '$34,600,000',
 'Worldwide Total': '$73,556,765',
 'Release Date': 'March 15, 2023'}
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

