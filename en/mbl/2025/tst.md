# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_fred(2024, ['SP500']).plot()
plt.savefig('/tmp/out.jpg')
```













