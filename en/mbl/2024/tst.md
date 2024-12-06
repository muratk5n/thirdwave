# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(1980, ['GDPC1','CLVMEURSCAB1GQEA19'])
```

```python
df.pct_change().dropna().mean()*100
```

```text
Out[1]: 
GDPC1                 0.623935
CLVMEURSCAB1GQEA19    0.378737
dtype: float64
```














