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
2023-11-28   -15.271585
2023-11-29   -15.831821
2023-11-30   -16.551066
2023-12-01   -16.556864
Name: net, dtype: float64
```




