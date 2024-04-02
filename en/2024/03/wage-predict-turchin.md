# Predicting Wages, Turchin

In *Age of Discord* Turchin shows an approach to predict wages, the formula is

$$
W_{t+\tau} = \alpha \left( \frac{G_t}{N_t} \right)^\alpha
             \left( \frac{D_t}{S_t} \right)^\beta C_t^\gamma
$$

Where $W$ is the real wage, $G/N$ is the real GDP per capita, $D/S$ is
the balance of labor demand and supply, and $C$ stands for the effect of
non-market forces (culture).

Take log products become sums

$$
\log W_{t+\tau} = A + \alpha \log \left( \frac{G_t}{N_t} \right) +
                  \beta \log \left( \frac{D_t}{S_t} \right) + \gamma \log C_t +
		  \epsilon_t
$$

The formula above is now regression-able. 

Using frequency of certain words to gauge "the culture" of an era, below is
the word "greed" via Google Books.

```python
df = pd.read_csv('gr-ngram.csv',header=None)
df['DATE'] = pd.to_datetime(["%d-01-01" % x for x in list(range(1800,2020))])
df = df.set_index('DATE')[0] 
df.plot(title="Count for the Word 'Greed' in Published Work")
```

![](https://cdn.fosstodon.org/media_attachments/files/112/163/022/078/112/717/original/1c08b53962c6a725.jpg)

We put it all together below

```python
import impl as u, pandas as pd
# gdpcap wage prod lab_force minwage
df  = u.get_fred(1970,['A939RC0A052NBEA','LES1252881600Q','OPHNFB','CLF16OV','FEDMINNFRWG'])
df = df.interpolate()
df2 = pd.read_csv('gr-ngram.csv',header=None)
df3 = df.copy()
idx = list(range(1800,2020))
idx = ["%d-01-01" % x for x in idx]
df2['DATE'] = pd.to_datetime(idx)
df2 = df2.set_index('DATE')
df2.columns = ['greed']
df3['greed'] = df2
df3 = df3.interpolate()
df3.columns = ['G','W','Prod','S','M','greed']
df3['C'] = df3['greed'].rdiv(1) 
df3['D'] = df3.G / df3.Prod
df3 = df3.resample('A').first()
df3['W'] = df3.W.shift(1)

import statsmodels.formula.api as smf
results = smf.ols('np.log(W) ~ np.log(M) + np.log(G) + np.log(D/S) + np.log(C)', data=df3).fit()
print (results.rsquared)
```

```text
0.8857859038760916
```

```python
df3['Wpred'] = df3.apply(lambda x: par['Intercept'] +
                                   np.log(x['M'])*results.params['np.log(M)'] +
                                   np.log(x['G'])*results.params['np.log(G)'] +
                                   np.log(x['D']/x['S'])*results.params['np.log(D / S)'] +
		                   np.log(x['C'])*par['np.log(C)'],axis=1)
df3['Wpred'] = np.exp(df3['Wpred'])
pred = df3[df3.index > '1980-01-01']
pred[['W','Wpred']].plot()
```

![](https://cdn.fosstodon.org/media_attachments/files/112/162/971/234/257/641/original/4b72a8f22a65f36e.jpg)

