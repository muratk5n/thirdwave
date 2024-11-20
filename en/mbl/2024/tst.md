# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(1980, ["FGEXPND","GDP"])
```

```python
dfd= np.abs(df.diff())
dfd['FGEXPND'] = np.abs(df['FGEXPND'])
print (dfd)
dfd.corr()
```

```text
             FGEXPND      GDP
DATE                         
1980-01-01   583.861      NaN
1980-04-01   608.694    7.510
1980-07-01   639.968   59.131
1980-10-01   657.298  129.074
1981-01-01   680.243  138.649
...              ...      ...
2023-07-01  6527.403  513.882
2023-10-01  6619.838  329.270
2024-01-01  6772.827  327.102
2024-04-01  6864.587  392.645
2024-07-01  7048.543  333.210

[179 rows x 2 columns]
Out[1]: 
          FGEXPND       GDP
FGEXPND  1.000000  0.698573
GDP      0.698573  1.000000
```




