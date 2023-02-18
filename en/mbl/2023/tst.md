
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.rottentomatoes_tv("Star Trek Discovery")
```

```text
Out[1]: {'tomatometer score': '84%', 'audience score': '36%'}
```








```python
u.sm_plot_ukr('ukrdata/fl-0212.csv','ukrdata/fl-221115.csv',[])
plt.savefig('/tmp/out.jpg')
```









