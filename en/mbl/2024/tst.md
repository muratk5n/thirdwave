# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(1980, ['DRCCLACBS'])
```

```python
df.plot(title='Delinquency Rate on Credit Card Loans')
plt.savefig('/tmp/out.jpg')
```




https://fred.stlouisfed.org/series/DRCCLACBS







