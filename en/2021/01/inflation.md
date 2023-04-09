# Inflation

Unless the government is literally printing money and handing out
directly to people (which has happened in some countries), and/or
supply-chain related issues are present, inflation is almost always
highly correlated with wages. People need to have more money so they
spend more, on an unchanging set of goods and services, which causes
prices to increase. 

Wages come from employers. Businesses work on credit, and credit is
newly printed money. Therefore when businesses hand out salaries they
are handing out new money. That could result in inflation, if there is
too much credit out there, then the economy "stars to heat up"
i.e. inflation.

Note that bank credit does not originate from bank customers' savings,
they are printed money, so money base expands. The system works
because even though the money base grows (through credit), the economy
*grows into that* base (credit was used to invest, hire ppl etc); more
products, services are circulating, but more money does not chase
after the same amount of goods, it chases after more amt of goods - no
inflation.

Bank credit is "printed money", brought into existence out of thin
air.. Just type bunch of numbers on a computer, boom. New money. There
is good reason for creating money and not simply lending out savings;
If only savings were lent out, growth + same money base = deflation.

If the set of goods of services in an economy grows (more production)
in tandem with the money base in that economy, there would not be
inflation. Sadly keeping this due in perfect sync is an extremely
tough job. The Central Bank has only one tool at its disposal to tune
this - the (short term) interest rate. By raising rates during econ
that is heating up, the idea is to raise borrowing costs and slow the
economy. The effect is extremely indirect, the aim is companies to
borrow less, to expand less, therefore pay employees less. It sounds
harsh but this is the system in play. 

Are government deficits inflationary? If new, more money reaches
citizens directly, it could be... If new money goes to corporations,
then no. [Research](https://www.researchgate.net/publication/227368010_Inflation_and_Budget_Deficit_What_is_the_Relationship_in_Portugal)
on this area found a lagged response in inflation for government spending
where it existed. The true determinant seemed to be unit labor costs.

Post 2008 bailouts provides the perfect example; money was dumped on
corporations, their profits soared. But the end-result was not
inflationary.  People's wages were stagnating.

Take pre-1973. Some argue "government spending for the Vietnam war
caused inflation".

See article [here](https://www.thebalancemoney.com/vietnam-war-facts-definition-costs-and-timeline-4154921)
I took data from it directly, shifted source vars one year ahead to see
causal effects better,

```python
import pandas as pd, io

s = """
YEAR    DEFICIT GROWTH  INFLATION  UNEMPLOYMENT
1965    $1B     6.5%    1.9%       4.0%
1966    $4B     6.6%    3.5%       3.8%
1967    $9B     2.7%    3.0%       3.8%
1968    $25B    4.9%    4.7%       3.4%
1969    -$3B    3.1%    6.2%       3.5%
1970    $3B     0.2%    5.6%       6.1%
1971    $23B    3.3%    3.3%       6.0%
1972    $23B    5.2%    3.4%       5.2%
1973    $15B    5.6%    8.7%       4.9%
"""
s = s.replace("%","").replace("$","").replace("B","")
df = pd.read_csv(io.StringIO(s),sep='\s*').set_index("YEAR")
df['GROWTH'] = df.GROWTH.shift(1)
df['UNEMPLOYMENT'] = df.UNEMPLOYMENT.shift(1)
df['DEFICIT'] = df.DEFICIT.shift(1)
df.corr()
```

```text
               DEFICIT    GROWTH  INFLATION  UNEMPLOYMENT
DEFICIT       1.000000  0.123867   0.490311      0.264804
GROWTH        0.123867  1.000000   0.138173     -0.504883
INFLATION     0.490311  0.138173   1.000000     -0.138800
UNEMPLOYMENT  0.264804 -0.504883  -0.138800      1.000000
```

There is strong correlation with gov spending and inflation, but also
between growth and unemployment which makes sense, wages are major
contribution to inflation.

Doc mentions gov spending wasn't entirely for the war; LBJ did some
social spending (money went to ppl direct).

Inflation wasn't too high pre-73. Starting 73 it was but oil shortages
started then.

The draft might have played a role; >2 mil was drafted into Vietnam,
1% of population, that means more money was spent on people. Now
population of >300 mil has mil active personnel less than 1.5 mil. Gov
still deficit spends but if it all goes to Reytheon, Lockheed, from
there to some offshore haven, then to stocks - no inflation.

In summary, more newly printed money in more hands can be
inflationary. One rich person can only buy so many cars. But a million
with increased wages can buy millions of products, bidding up their
prices which for unchanged set of products will cause inflation.

<a name='autocorr'/>

Autocorrelation

There is another troubling aspect to inflation, by just being there,
inflation can create more inflation. This is what economists mean when
they say inflation time series is "autocorrelated", ie a value today
is correlated with another value yesterday, signaling yesterday's
value alone effects inflation today. It is easy to see why, pricing is
imperfect, producers, landlords see higher prices, they increase
prices to match, they mostly overshoot. This is partly why Central
Banks raise rates as well to quash that self-reinforcing effect.

We can check for the presence of autoocorrelation statistically using
the Durbin-Watson test, or Ljung-Box Q-statistic. Investopedia: "The
Durbin-Watson statistic will always have a value ranging between 0 and
4.. [v]alues from 0 to less than 2 point to positive autocorrelation".

```python
from pandas_datareader.data import DataReader # get data from FRED
cpi = DataReader('CPIAUCNS', 'fred', start='1971-01', end='2016-12')

import statsmodels.formula.api as smf
from statsmodels.stats.stattools import durbin_watson
inf = np.log(cpi)
results = smf.ols('CPIAUCNS ~ 1', data=inf).fit()
print (durbin_watson(results.resid))
```

```text
9.222098132626528e-05
```

Hints at autocorrelation

Ljung-Box

```python
import statsmodels.tsa.stattools as tsa
acf,confint,qstat,pvalues = tsa.acf(results.resid, nlags=4, alpha=95,qstat=True, unbiased=True)
print (acf)
print (pvalues)
```

```text
[1.         0.99585547 0.99164499 0.98737151 0.98305291]
[1.02286496e-121 5.63735022e-239 0.00000000e+000 0.00000000e+000]
```

Low pval means presence of autocorrelation.

Marginal Revolution University

<iframe width="340" src="https://www.youtube.com/embed/gi7jx5IJtik" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Why inflate

<iframe width="340" src="https://www.youtube.com/embed/E6A_WpUY2LI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

