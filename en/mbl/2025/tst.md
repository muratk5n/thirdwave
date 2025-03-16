# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.get_fred(2007,["M2V"]).plot(title="US Money Velocity")
plt.savefig('/tmp/out.jpg')
```




