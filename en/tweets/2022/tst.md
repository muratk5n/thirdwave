

https://www.boxofficemojo.com/search/?q=black+panther

https://www.boxofficemojo.com/title/tt1825683/



```python
u.boxofficemojo("Black Panther")
```

```text
Out[1]: 
{'Domestic Opening': '$202,003,951',
 'Domestic': '$700,426,566',
 'International': '$681,822,260',
 'Worldwide Total': '$1,382,248,826'}
```

```python
u.boxofficemojo("Black Panther Wakanda Forever")
```

```text
Out[1]: 
{'Domestic Opening': '$181,339,761',
 'Domestic': '$220,692,647',
 'International': '$187,200,000',
 'Worldwide Total': '$407,892,647',
 'Release Date': 'November 9, 2022'}
```







```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.rotten_tomatoes("Black Panther 2018")
```



```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1115.csv','ukrdata/alt1-1002.csv',geo)
plt.savefig('/tmp/out.png')
```

