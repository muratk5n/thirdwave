# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
df = u.get_yahoo_tickers(2020,["FLAT"])
df.to_csv('/tmp/out1.csv')
```


```python
import pandas as pd
df = u.get_yahoo_tickers(2015, ['^GSPC','GLD','USO','SLV','EURUSD=X'])
import statsmodels.formula.api as smf
df['SPX'] = df['^GSPC']
df['EURUSD'] = df['EURUSD=X']
```








