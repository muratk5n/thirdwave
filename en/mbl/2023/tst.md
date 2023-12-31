# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.rottentomatoes3("Aquaman and the Lost Kingdom")
```

```text
Out[1]: {'tomatometer score': 35, 'audience score': 79}
```


```python
u.boxofficemojo("Aquaman and the Lost Kingdom")
```

```text
Out[1]: 
{'Domestic Opening': '$27,700,000',
 'Domestic': '$27,700,000',
 'International': '$80,200,000',
 'Worldwide Total': '$107,900,000',
 'Release Date': 'December 20, 2023'}
```











```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2023-12-24   -17.115031
2023-12-25   -17.116581
2023-12-26   -16.112096
2023-12-27   -16.577882
Name: net, dtype: float64
```




