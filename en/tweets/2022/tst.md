

```python
import util as u
# bakhmut, svatove, novokeiry
geo = [[48.59086903747, 38.00222462226],[49.41519908195, 38.17381415982],[47.01290896691535, 33.60127980381953]]
u.sm_plot_ukr3('ukrdata/alt1-1010.csv','ukrdata/alt1-1002.csv',geo)
plt.savefig('/tmp/out1.png')
```

```python
import util as u
u.yf_eps("WMT")
```

```text
Out[1]: 
              startdatetime  epsestimate  epsactual
4  2022-08-16T07:02:00.000Z         1.62       1.77
5  2022-05-17T07:02:00.000Z         1.48       1.30
6  2022-02-17T07:11:00.000Z         1.50       1.53
```
