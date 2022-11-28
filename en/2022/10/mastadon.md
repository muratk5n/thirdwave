# Mastadon

Mastodon is free and open-source software for running self-hosted
social networking services. Each user is a member of a specific
Mastodon instance (also called a server), which can interoperate as a
federated social network, allowing users on different instances to
interact with each other. This is intended to give users the
flexibility to select a node whose policies they prefer, but keep
access to a larger social network.

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

[Code](masta.py)











