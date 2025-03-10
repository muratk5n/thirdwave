# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_yahoo_tickers(2020, ["DX-Y.NYB"]).plot(title='Dollar')
plt.savefig('/tmp/out.jpg')
```




