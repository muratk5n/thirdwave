

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.boxofficemojo("Black Adam")
```

```text
Out[1]: 
{'Domestic Opening': '$67,004,323',
 'Domestic': '$165,071,691',
 'International': '$219,500,000',
 'Worldwide Total': '$384,571,691',
 'Release Date': 'October 14, 2022'}
```



```python
u.boxofficemojo("Black Panther")
```

```text
Out[1]: 
{'Domestic Opening': '$202,003,951',
 'Domestic': '$700,426,566',
 'International': '$681,822,260',
 'Worldwide Total': '$1,382,248,826',
 'Release Date': 'February 13, 2018'}
```

```python
u.boxofficemojo("Black Panther Wakanda Forever")
```

```text
Out[1]: 
{'Domestic Opening': '$181,339,761',
 'Domestic': '$393,671,128',
 'International': '$339,300,000',
 'Worldwide Total': '$732,971,128',
 'Release Date': 'November 4, 2022'}
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
u.sm_plot_ukr2('ukrdata/alt1-1129.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

