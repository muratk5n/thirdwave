

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.sen_ga_538()
```

```text
Out[1]: 
(['Herschel Junior Walker', '11/17/22', 'Fabrizio/Impact', 47.0],
 ['Raphael Warnock', '11/17/22', 'Fabrizio/Impact', 51.0])
```

```python
u.rottentomatoes("Strange World")
```

```text
Out[1]: {'tomatometer score': 73, 'audience score': 59}
```




```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1123.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

