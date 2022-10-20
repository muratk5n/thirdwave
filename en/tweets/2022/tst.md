

```python
import util as u
u.gfp_compare('Germany','../2021/gfp-2021.csv','gfp-2022.csv')
```

```text
Out[1]: 
                                 % Change  Previous
Tot Military Personnel (est.)   -7.441860  215000.0
Reserve Personnel              -50.000000   30000.0
Manpower Composition            12.500000      16.0
Total Aircraft Strength        -11.982882     701.0
Transports                     -40.277778      72.0
Trainers                        15.625000      32.0
Tanker Fleet                  -100.000000       7.0
Helicopters                    -15.088757     338.0
Tanks                            9.016393     244.0
Armored Vehicles                75.228137    5260.0
Frigates                        20.000000      10.0
```













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
