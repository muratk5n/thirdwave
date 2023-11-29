# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```



















```python
df = u.biden_approval()['net']
print (df.tail(4))
df.plot()
plt.savefig('/tmp/out.jpg')
```

```text
end_date
2023-10-10   -13.947808
2023-10-11   -13.981538
2023-10-12   -14.447912
2023-10-13   -14.352457
Name: net, dtype: float64
```




