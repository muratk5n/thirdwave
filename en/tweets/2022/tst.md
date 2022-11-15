
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



```python
df = u.rent_housing()
print (df[['incrent','inchouse']].tail(3))
plt.savefig('/tmp/out2.png')    
```

```text
             incrent  inchouse
DATE                          
2022-08-01  6.740728  9.526485
2022-09-01  7.206730  8.447235
2022-10-01  7.521848  7.389046
```











```python
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1115.csv','ukrdata/alt1-1002.csv',geo)
plt.savefig('/tmp/out.png')
```


```python
u.yf_eps("WMT")
```

```text
Out[1]: 
              startdatetime  epsestimate  epsactual
6  2022-08-16T07:02:00.000Z         1.62       1.77
7  2022-05-17T07:02:00.000Z         1.48       1.30
8  2022-02-17T07:11:00.000Z         1.50       1.53
```


```python
u.yf_profit("TWTR")
```

```text
Out[1]: 
Breakdown  grossProfit totalRevenue grossProfitMargin
endDate                                              
2021-09-30     799.338      1283.82           62.2626
2021-12-31     1052.13      1567.22           67.1335
2022-03-31     693.534      1200.98           57.7471
2022-06-30     635.984      1176.66           54.0499
```
