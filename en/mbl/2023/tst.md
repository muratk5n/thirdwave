
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```






```python
u.rottentomatoes_mov("Ant Man 3")
```



```python
#u.rottentomatoes_mov("Ant Man 3")
u.boxofficemojo("Ant Man 3")
```

```text
Out[1]: 
{'Domestic Opening': '$106,109,650',
 'Domestic': '$177,446,000',
 'International': '$196,154,352',
 'Worldwide Total': '$373,600,352',
 'Release Date': 'February 15, 2023'}
```

```python
u.mov_profit(200, 373)
```

```text
Out[1]: -76.2
```
















```python
u.sm_plot_ukr('ukrdata/fl-0304.csv','ukrdata/fl-221115.csv',[],clat=48.5,clon=38,zoom=0.2)
plt.savefig('/tmp/out.jpg')
```









