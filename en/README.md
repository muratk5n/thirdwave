<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

Still in vacation mode; this is left-over stuff

---

Hmmmm

Oct 26: "South Africa identifies new coronavirus variant"

---

With WHO blessing apparently

Oct 19: "Scientists in South Africa are working to reverse engineer the Moderna COVID vaccine"

---

"Concentrated solar power (CSP) watchers are keeping an eye on Spain as
the country looks to auction a minimum of 200 MW of capacity before
2022.

Sara Aagesen, Spain?s Secretary of State for Energy, confirmed the
auction would go ahead before the end of this December in an
announcement on October 1"

[[-]](https://www.pacificgreen-solar.com/articles/reflections-spains-upcoming-200-mw-csp-auction)

---

Submarine cables map, as in cables that are laid under the sea

[[-]](https://pbs.twimg.com/media/FFDK09LXoAUg3hK?format=jpg&name=medium)

---

Examples abound: your mother teaches you how to talk, to walk and how
to take a shit.  Then the economy takes this finished product, a
worker, utilizes them, makes money of off them. Noone pays the mother
for her labor.

This is the dirty little secret of the free market; that it relies on
a lot of free stuff.

---

The irony is tech relies on gov funded research from academia, and
other "free stuff" all the time.

---

Interesting on academia / tech relation.. some replies are
informative. Unis make members pay for parking?

[[-]](https://mobile.twitter.com/DrStephCraig/status/1463550686445064204)

----

High NG prices create an oppo for an H2 based solution
here. Steelmaking already uses H2; in fact there are no green
alternatives other than H2 for their furnaces. 

---

I wonder what other gas, that is clean, can provide that kind of flame? 🤔

"Murano glassblowing model shattered by methane price surge"

[[-]](https://www.pbs.org/newshour/arts/murano-glassblowing-model-shattered-by-methane-price-surge)

---

Of course it is 

"The SALT deduction that benefits the rich is bipartisan"

---

Base info: Nordstream 2 can deliver 55 billion cubic meters of gas per
year. Natural gas contains 5367.27 kWh of energy per cubic meter of
gas.

Convert that to Gigawatts,

```python
kwh_year = 55*1e9 / 5367.27
print ("%0.2f" % (kwh_year / (365*24*1000)), 'GW')
```

```text
1.17 GW
```

The mega CSP plant in Chile has 110 MW capacity. That means roughly 10
of those plants will equal the Nordstream 2 pipeline. This is not bad
at all. Fantastic actually. Fossil f has been sitting there, basting,
for millions of years. But we can equal it with tech.

---

Nordstream 2 is still a major issue.. it's a huge amount of gas supply
into Europe. I wonder what the green equivalent to it would be

---

"@GregDaco

Inflation isn’t just a US thing ... 'Underneath it all, the key theme
is #COVID19 disruptions... & desynchronized global recoveries'"

---

Chocolate pizza by Dominos.. Now I've seen it all.

---

"Worldwide hydrogen supply chains have been handed a huge boost today
(Nov 23) with Australia and Germany committing to jointly strengthen
bilateral cooperation on hydrogen technology"

[[-]](https://www.h2-view.com/story/australian-germany-joint-collaboration-to-accelerate-hydrogen-supply-chains/)

---

Who should play the President in that movie? Jack Black, or Jim
Carrey. If he wants to reprise the role in *Idiocracy*, Terry Crews.

---

Movie idea: while trying to change the course of asteroid, they make
it hit Earth by mistake, end all life.

"NASA has launched a space probe to change the course of an asteroid"

---

Taspinar: "There are some countries where a single issue can explain
pretty much everything that is wrong with its domestic and foreign
policy. Turkey’s Kurdish predicament is such a case. Ankara’s historic
failure to find democratic solutions to Kurdish ethnic demands has
created a deeply insecure and chronically irrational Turkish political
culture"

[[-]](https://www.brookings.edu/blog/order-from-chaos/2021/10/13/turkeys-kurdish-obsession-explains-putins-gains-and-us-strains/)

---

That's abt 3 days worth of consumption. But the psychological effect
can matter.

"DOE To Make Available A Release Of 50 Million Barrels Of Crude Oil
From The Strategic Petroleum Reserve"

---

```python
from pandas_datareader import data
import datetime

today = datetime.datetime.now()
start=datetime.datetime(2000, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['TURB6BLTT02STSAQ','RBTRBIS']
df = data.DataReader(cols, 'fred', start, end)
df = df.dropna()
print (df.tail(5))
plt.figure(figsize=(10,6))
ax1 = df.TURB6BLTT02STSAQ.plot(color='blue', grid=True, label='Current Account as % GDP')
ax2 = df.RBTRBIS.plot(color='red', grid=True, secondary_y=True, label='XCHG')
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
plt.savefig('currxch.png')
```

```text
            TURB6BLTT02STSAQ  RBTRBIS
DATE                                 
2020-04-01         -5.612587    57.08
2020-07-01         -5.655827    56.34
2020-10-01         -5.281476    49.55
2021-01-01         -3.276163    54.04
2021-04-01          0.242710    50.84
```

<img width="300" src="https://pbs.twimg.com/media/FFDh9jkXMAAAHXd?format=jpg&name=small"/>

```python
df.corr()
```

```text
Out[1]: 
                  TURB6BLTT02STSAQ   RBTRBIS
TURB6BLTT02STSAQ          1.000000 -0.533232
RBTRBIS                  -0.533232  1.000000
```
Strong reverse correlation.

I checked Granger causality, to see the direction of the cause from
the data, early time horizon FX effects current account. Later horizon
shows account effecting currency. So in a way it's a chicked-and-egg
problem, but from Nikolas Müller-Plantenberg
[research](https://www.researchgate.net/publication/46490787_Balance_of_payments_accounting_and_exchange_rate_dynamics),
we know the primary direction is CA->FX. You need to have products to
sell so people demand your currency.

---

🤣 🤣 🤣 

[[Tweet]](https://pbs.twimg.com/media/FE1kRn6XEAA1hDB?format=jpg&name=small)

---

China is in similar power range to France. The large agro-empire past,
sometimes ending up as the odd-man-out in the Anglo world is similar
as well. 

```python
import pandas as pd
df = pd.read_csv('../../2020/07/gdpw.csv')
df = df[df['country'].isin(['United States','France','China']) ]
df['gdp'] = df.gdpcap * df.population
df['mbindex'] = (df.gdpcap * df.gdp)/1e14
print (df[['country','mbindex']])
```

```text
          country       mbindex
13  United States  12898.099255
32         France   1117.358002
85          China   1363.010190
```

---

Black brother in US are very different from an "African-African" in
culture. We know this. 

---

Just like there are no "Irish" or "Polish" in US beyond zeroth
generation, there are no Turks in Anatolia, there are no Africans in
America -- unless brother jumped off the boat (plane) and came to US
obviously.

---

:) Morgan Freeman 

[[-]](https://twitter.com/FriendlyHistory/status/1462446229858570244)

---

"@IEA_SolarPACES

China makes strong commitment to CSP. [China] announces that it will
develop at least 20 new CSP projects throughout its territory to
achieve carbon neutrality"

[[-]](https://twitter.com/IEA_SolarPACES/status/1461686943331360773)

---

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](/2013/02/nations-and-nationalism.md)

[The Fundamentals of Industrial Ideologies](/2011/04/fundamentals-of-industrial-ideologies.md)

[Education, Workplace](2017/09/education-workplace.md)

[Patents](/2018/09/patents.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave, Religion](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[Reports](/2019/05/reports.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


