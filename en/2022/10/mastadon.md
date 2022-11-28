# Mastadon

Crawl Script

It hits all MD servers and gets their stats (user count, creation date)

```python
import zipfile, pandas as pd
with zipfile.ZipFile('mastacrawl1.zip', 'r') as z:
   df = pd.read_csv(z.open('mastacrawl1.csv'),header=None) 
```

```python
print (len(df))
print (f'{df[1].sum():,}','users')
```
```text
4601
7,824,386 users
```











