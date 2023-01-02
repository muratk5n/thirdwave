

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.boxofficemojo("Black Adam")
```

```text
https://www.boxofficemojo.com/title/tt6443346/?ref_=bo_se_r_1
Out[1]: 
{'Domestic Opening': '$67,004,323',
 'Domestic': '$167,873,355',
 'International': '$223,400,000',
 'Worldwide Total': '$391,273,355',
 'Release Date': 'October 14, 2022'}
```

```python
gross = 390
budget = 190 + 70
print (gross - (190/2 + gross*0.40 + budget))
```

```text
-121.0
```





```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1129.csv','ukrdata/alt1-1115.csv',geo)
plt.savefig('/tmp/out.png')
```

