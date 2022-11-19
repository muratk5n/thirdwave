

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.boxofficemojo("Constantine")
```

```text
Out[1]: 
{'Domestic Opening': '$29,769,098',
 'Domestic': '$75,976,178',
 'International': '$154,908,550',
 'Worldwide Total': '$230,884,728',
 'Release Date': 'February 8, 2005'}
```

```python
u.rottentomatoes("Constantine")
```

```text
Out[1]: {'tomatometer score': 46, 'audience score': 72}
```


















```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1115.csv','ukrdata/alt1-1002.csv',geo)
plt.savefig('/tmp/out.png')
```

