# Coronavirus Data, Analysis

# Mortality Rate

Fatality / Cases ratio is around 2.2%, the cases is for people with
symptoms. What would be the fatality rate for the broader population?
On one of those cruise ships which experienced the epidemic in an
isolated environment, they found about 1/3 rd of the people were
infected. We can assume the virus reached everyone possible on that
ship. 1/3 of mortality rate is nearly 1%. So if given the chance,
covid can kill 1% of an entire population. As a reference point,
annual growth of world population hovers around the same ratio


Code is from [2]

<a mame='mortality'/>

```python
import util
world_rate_df = util.mortality_rate()
world_rate_df['deaths / 100 confirmed'].plot(title='Worldwide Mortality Rate')
plt.savefig('mort.png')
```

```text
8/31/21    2.075917
9/1/21     2.074744
9/2/21     2.073132
9/3/21     2.071545
Name: deaths / 100 confirmed, dtype: float64
```

![](mort.png)


The SIR Model

$$
\frac{ds}{dt} = -\beta s i
$$

$$
\frac{di}{dt} = \beta s i - \gamma i
$$

$$
\frac{dr}{dt} = \gamma i
$$

Where does $R_0$ come from? Epidemic occurs if \# of infected ppl
increase, meaning $di / dt > 0$. That means (from 2nd eq above)

$$
\beta si - \gamma i > 0  \implies \frac{\beta s i }{\gamma} > i
$$

Then,

$$
\frac{\beta s }{\gamma} > 1
$$

At the beginning of the epidemic everyone is susceptible, so $s
\approx 1$. Substitute $s=1$

$$
\frac{\beta}{\gamma} = R_0 > 1
$$

To find $R_0$ from data, we fit the differential equation system above
to data, and using the found $\beta$ and $\gamma$ we calculate $R_0$.

Daily Change

<a name='daily'/>

```python
import pandas as pd, util
df = util.get_data()
```

```python
df['Germany +'] = df['Germany'].diff()
df['UK +'] = df['United Kingdom'].diff()
df['US +'] = df['US'].diff()
pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', None)
print (df[['Germany +','UK +','US +']].tail(10))
```

```text
Country/Region  Germany +     UK +      US +
8/25/21           13275.0  35618.0  148146.0
8/26/21           11688.0  38117.0  161334.0
8/27/21            1940.0  37854.0  322934.0
8/28/21            8395.0  32142.0   53071.0
8/29/21            6627.0  32992.0   38475.0
8/30/21            6823.0  26285.0  258537.0
8/31/21           18646.0  32167.0  140705.0
9/1/21            14158.0  35577.0  198025.0
9/2/21            13950.0  37982.0  153143.0
9/3/21             2899.0  42355.0  300957.0
```

<a name='Rt'/>

Reproduction Rate $R_t$

This calculation is based on [1]

```python
tau = 7 # length of time window
si_mean = 6.3 # mean of serial interval
si_std = 4.2 # standard deviation of serial interval
conf = 0.95 # confidence level of estimated Reff
c = df['US'].tail(200)
R = util.Reff(c, si_mean, si_std, tau, conf)
df2 = pd.DataFrame(R.T)
print (df2[1].tail(5))
# 0,2 indices 95% conf
df2[1].tail(70).plot()
plt.title('US')
plt.ylim(1.0,1.1)
plt.savefig('Rt-US.png')
```

```text
195    1.025505
196    1.025649
197    1.025940
198    1.026153
199    1.026227
Name: 1, dtype: float64
```

![](Rt-US.png)


Code

[util.py](util.py)

References

[1] https://github.com/tt-nakamura/Reff.git

[2] https://notebooks.ai/rmotr-curriculum/analyzing-covid19-outbreak-40c03c06

[4] https://web.stanford.edu/~jhj1/teachingdocs/Jones-on-R0.pdf


