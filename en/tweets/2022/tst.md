

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_bp_country("United Kingdom",2012)
```

```text
Out[1]: 
(             Year
 wind_twh     2012     0.896391
 solar_twh    2012     0.061142
 nuclear_twh  2012     3.179830
 hydro_twh    2012     0.239783
 oil_twh      2012    38.303440
 gas_twh      2012    34.731184
 coal_twh     2012    20.463374
 biogeo_twh   2012     2.124856
 ethanol_twh  2012     0.000000
 dtype: float64,
     Perc Commodity
 0  63.96       Oil
 1  42.52       Gas
 2   1.87      Coal,
 2214.1140180691764,
 15.25)
```

```python
u.get_bp_country("United Kingdom",2021)
```

```text
Out[1]: 
(             Year
 wind_twh     2021     3.628167
 solar_twh    2021     0.697069
 nuclear_twh  2021     2.581697
 hydro_twh    2021     0.282269
 oil_twh      2021    39.023356
 gas_twh      2021    43.310718
 coal_twh     2021     3.288407
 biogeo_twh   2021     7.188318
 ethanol_twh  2021     0.000000
 dtype: float64,
     Perc Commodity
 0  78.24       Oil
 1  42.49       Gas
 2  14.52      Coal,
 1776.6412760753542,
 15.54)
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

