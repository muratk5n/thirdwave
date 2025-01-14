# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
df = u.get_fred(1990, ["CATOTLTAX"])
df.plot(title="CA State Government Tax Collections")
plt.savefig('/tmp/out.jpg')
```







```python
u.modis_fire(34.11778266, -118.504923,"/tmp/fire1.html")
```









