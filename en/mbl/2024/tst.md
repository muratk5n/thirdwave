# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = pd.read_csv('https://projects.fivethirtyeight.com/polls/data/president_polls.csv')
```

```python
cols = ['poll_id','pollster','sample_size','answer','pct','end_date']
print (df[cols].head(30))
```

```python
u.kh_djt_538_polls()
plt.savefig('/tmp/538.jpg')
```

```text
            trump_pct  harris_pct
Date                             
2024-09-19   0.468208    0.489408
2024-09-20   0.464579    0.496868
2024-09-21   0.457992    0.481633
2024-09-22   0.450000    0.500000
```

```python
import datetime
sd = datetime.datetime.now().strftime("%m/%d")
print (sd)
```

```text
09/24
```










