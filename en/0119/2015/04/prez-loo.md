# Prez Prediction, Past Elections, Leave-One-Out Check

We will use this model to predict past elections (by canceling out
that year's so it cannot tilt the prediction in any way). We will also
use it for the 2016 election prediction.

```python
from io import StringIO
import numpy as np
import statsmodels.formula.api as smf
import pandas as pd
s="""year,gdp_growth,net_approval,two_terms,incumbent_vote
2012,1.3,-0.8,0,52
2008,1.3,-37,1,46.3
2004,2.6,-0.5,0,51.2
2000,8,19.5,1,50.3
1996,7.1,15.5,0,54.7
1992,4.3,-18,1,46.5
1988,5.2,10,1,53.9
1984,7.1,20,0,59.2
1980,-7.9,-21.7,0,44.7
1976,3,5,1,48.9
1972,9.8,26,0,61.8
1968,7,-5,0,49.6
1964,4.7,60.3,0,61.3
1960,-1.9,37,1,49.9
1956,3.2,53.5,0,57.8
1952,0.4,-27,1,44.5
1948,7.5,-6,1,52.4
"""

df = pd.read_csv(StringIO(s))
regr = 'incumbent_vote ~ gdp_growth + net_approval + two_terms + net_approval:two_terms'
results = smf.ols(regr, data=df).fit()

def f(year):
    df2 = df[df['year'] != year]
    results2 = smf.ols(regr, data=df2).fit()
    conf = results2.conf_int()
    pred = np.array(df[df['year'] == year])[0][:-1]; pred[0] = 1.
    pred = np.array(list(pred) + [pred[-1]*pred[-2]])
    res = np.dot(pred, conf)
    return res, np.sum(res)/2.0

print ('\nbush/clinton'); print (f(1992))
print ('\ngore/bush'); print (f(2000))
print ('\nbush/kerry'); print (f(2004))
print ('\nmccain/obama'); print (f(2008))
print ('\nobama/romney'); print (f(2012))
```

```text

bush/clinton
(array([45.5545006 , 51.63342375]), 48.59396217652096)

gore/bush
(array([43.62406671, 64.45632856]), 54.04019763636963)

bush/kerry
(array([48.66180994, 54.92965126]), 51.79573059909151)

mccain/obama
(array([46.28829965, 42.88150912]), 44.58490438148577)

obama/romney
(array([48.16757318, 53.57914149]), 50.87335733434571)
```

The run on past elections is above, uses 95% confidence interval for
the coefficients.

Bush / Clinton guess points to a likely Bush loss. Clinton
won. Bush/Kerry points to a definite Bush win, he won. Mccain / Obama
says definite McCain loss, he lost. Bama / Romney, definite Bama win,
he did.

The freak event is Bush / Gore. Two things there - there was some
possibility for Bush win, and second, well.. the election was
stolen. Plus, Gore won the popular vote (that's what the model
predicts).
