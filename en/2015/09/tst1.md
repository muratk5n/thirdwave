


```python
import pandas as pd
df = pd.read_csv('fsi.csv')
df['Year2'] = df.apply(lambda x: pd.to_datetime(x['Year']).year, axis=1)
df = df[df.Country.isin(['United States','France','Turkey'])]
c = 'P2: Public Services'
df2 = df[['Country','Year2',c]]
df2=df2.pivot(index='Year2', columns='Country', values=c)
df2.plot(title=c)
plt.savefig('fsi1.png')
```


```python
c = 'P1: State Legitimacy'
df2 = df[['Country','Year2',c]]
df2=df2.pivot(index='Year2', columns='Country', values=c)
df2.plot(title=c)
plt.savefig('fsi2.png')
```


















