
<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>


<img width="340" src="https://pbs.twimg.com/media/E86S1JPWEAEYADp?format=jpg&name=small"/>

---

"@Lj_mir

'Ashraf Ghani, the Afghan President who has apparently just fled to
Tajikistan (which was invaded by the Taliban...) [writing](https://pbs.twimg.com/media/E84zo8EWYAkw_sc?format=jpg&name=small)
for the Los Angeles Times [in 1989]'"

---

Actually Dubya WH worked through local warlords. Bama WH made a major
surge; so if you go by the numbers, it was Obama who invaded
Afghanistan.

Clearly both methods failed. 

---

I dont think there was a 'good way' of getting out of Afghanistan.

---

Tali wins.. All that after dropping them bombs.. Remember
[MOAB](https://taskandpurpose.com/news/much-actually-achieve-dropping-moab-afghanistan/)?

Trump tried to tame Afghanistan for a while too apparently.. Didn't work.

---

"PhD Student from Leibniz Institute for Catalysis Discovers a New Type
of $H_2 O$ Splitting.. Mechanism of a new type of water splitting with
which photolysis [the decomposition or separation of molecules by the
action of light] can be made inexpensive"

[Link](https://bit.ly/2VPa2v1 )

---

Data lists top grossing releases every month, *Black Panther* 2018 did
better than *Infinity War*. They can't not make sequels to this movie,
hire a new lead at some point.

---

Movie releases

```python
df['Releases'].plot()
```

<img width="340" src="https://pbs.twimg.com/media/E85eSi-X0AQZ65s?format=png&name=small"/>

Decrease in movies releases.. it's a supply issue too

---

Box office cumulative gross (in millions), since 2018

Data from [BoxOfficeMojo](https://www.boxofficemojo.com/month/by-year/2018/?grossesOption=calendarGrosses)

```python
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('boxoff.csv',sep='\t')
df.loc[:,'dt'] = df.apply(lambda x: pd.to_datetime(x.Month + " " + str(x.Year)), axis=1)
df.loc[:,'Cumulative_Gross'] = df.apply(lambda x: float(x['Cumulative_Gross'][1:].replace(",","")), axis=1)
df = df.sort_values('dt')
df.loc[:,'Cumulative_Gross'] = df['Cumulative_Gross'] / 1e6
df = df.set_index('dt')
df[['Cumulative_Gross']].plot()
```

<img width="340" src="https://pbs.twimg.com/media/E85cA4vX0AEgont?format=png&name=small"/>

There were months with a bil gross. Then the pandemic hit.

It was sorta recovering (half a bil) in July 2021, but then the
Delta variant

---

Piedmont Park, Atlanta, nice scenery.

---

A lot of compsci approaches I am looking at (for a certain domain)
feel old school... Fit for single CPUs.. Wanna bypass it
all, jump straight into high paralelization.

---

"Over the past two decades improvements in the arithmetic capabilities
of processors have significantly outpaced advances in random access
memory. Algorithms which have traditionally been compute bound—such as
dense matrix-vector products—are now limited instead by the bandwidth
to/from memory"

---

Industrial Age society, the Second Wave began in Western Europe with
the Industrial Revolution, and subsequently spread across the
world. Key aspects of Second Wave society are the nuclear family, a
factory-type education system and the corporation. The Third Wave is
the post-industrial society based on hi-tech with all its benefits and
adverse effects causing major attitude shifts in society. Institutions
are built around methods of production, so when a new wave arrives,
older structures around governance, education, health start to crumble
despite the best efforts of people working in them.

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


