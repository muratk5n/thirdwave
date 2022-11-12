
```python
import util as u
import pandas as pd
geo = [[46.65638330412107, 32.61676838804905]]
u.sm_plot_ukr2('ukrdata/alt1-1002.csv','ukrdata/alt1-1109.csv',geo)
plt.savefig('/tmp/out.png')
```




```python
u.yf_eps("TWTR")
```

```text
Out[1]: 
              startdatetime  epsestimate  epsactual
0  2022-07-22T08:00:00.000Z         0.14      -0.08
1  2022-04-28T08:06:00.000Z         0.03       0.90
2  2022-02-10T07:00:00.000Z         0.35       0.33
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
