# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
df = u.get_fred(1980,["TTLHHM156N","POPTOTUSA647NWDB"])
df.columns = ['housing','population']
df.asfreq(freq='A',method='bfill').pct_change().mean()*100
```

```text
Out[1]: 
housing       1.142863
population    0.893067
dtype: float64
```














```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2023-12-10   -17.583314
2023-12-11   -17.578400
2023-12-12   -17.317512
2023-12-13   -16.980148
Name: net, dtype: float64
```




