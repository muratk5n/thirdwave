

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(1970,"POPTOTUSA647NWDB")
df.columns = ['pop']
df = df.reset_index()
df['year'] = df.apply(lambda x: str(x['DATE'])[:4],axis=1)
df = df[['year','pop']]
df.to_csv('/tmp/uspopulation.csv',index=None)
```

```text
Out[1]: <Figure size 640x480 with 0 Axes>
```













```python
u.rottentomatoes("Terminator 3 Rise of the Machines")
```

```text
Out[1]: {'tomatometer score': 69, 'audience score': 46}
```

```python
u.boxofficemojo("Terminator 3 Rise of the Machines")
```

```text
Out[1]: 
{'Domestic Opening': '$44,041,440',
 'Domestic': '$150,371,112',
 'International': '$283,000,000',
 'Worldwide Total': '$433,371,112',
 'Budget': '$200,000,000',
 'Release Date': 'July 2, 2003'}
```




```python
u.rottentomatoes("Terminator Salvation")
```

```text
Out[1]: {'tomatometer score': 33, 'audience score': 53}
```

```python
u.boxofficemojo("Terminator Salvation")
```

```text
Out[1]: 
{'Domestic Opening': '$42,558,390',
 'Domestic': '$125,322,469',
 'International': '$246,030,532',
 'Worldwide Total': '$371,353,001',
 'Budget': '$200,000,000',
 'Release Date': 'May 20, 2009'}
```














```python
u.sw_border_encounter('2022-Oct/sbo-encounters-fy19-fy22.csv')
```

```text
YMD
202209    227547.0
202210    164837.0
202211    174845.0
202212    179253.0
Name: Encounter Count, dtype: float64
```









```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1129.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

