

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
u.eq_at2(54.759676724735534, 13.031939315523639, radius=1000, ago=100).tail(4)
```

```text
Out[1]: 
                     mag      lat      lon
date                                      
2022-09-01 14:57:42  3.8  47.1173   9.4506
2022-09-10 18:58:11  3.9  47.6928   7.3592
2022-09-14 08:47:21  4.2  51.5608  16.0862
2022-10-16 07:13:19  3.4  48.3412   8.9948
```
