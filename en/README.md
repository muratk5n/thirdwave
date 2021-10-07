<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

NYT: "[Sinema] doesn’t engage with Washington reporters in a serious
way, doesn’t hold open-to-the-public events in Arizona and has
effectively cut off communication with the local progressive groups
that worked to get her elected in 2018"

[[-]](https://www.nytimes.com/2021/10/05/us/politics/kyrsten-sinema-arizona-democrat.html)

---

In annual terms, bill aims to spend merely half of what US spends for
military every year. Even on that some throw up their hands go OMG!

"@ParkerMolloy

Pretty remarkable how little the actual contents of the reconciliation
bill are being discussed in the news. Instead, it’s just anchors
saying the words '$3.5 trillion!' over and over"

---

Generate renewable fuel from fossil, CCS at the source, transmit.
H2 pipelines [work](https://pbs.twimg.com/media/EvdKNhvXAAE9Rr2?format=png&name=small).

Producing from green is better of course.. Politics will decide the balance. 

---

Renewable fuel pipelines wouldn't have problems in case of leak. No
env damage (you'd be putting more H2 into H2O.. it's like, who
cares?).

USA Today: "California oil spill: Pipeline wasn't shut down for more
than 3 hours after pressure failure alert, feds say..  The U.S. Coast
Guard said divers located a split in the pipeline more than a
foot-long. Investigators believe it could be the source of the leak"

---

France has an efficient economy... This is key, esp. during wartime.

---

The GDP Per Capita x GDP has them at roughly in the same
vicinity... DE is nearly twice but, look at US, in a different league
altogether.

```python
import pandas as pd
df = pd.read_csv('../../2020/07/gdpw.csv')
df = df[df['country'].isin(['France','Germany','United States']) ]
df['gdp'] = df.gdpcap * df.population
df['mbindex'] = (df.gdpcap * df.gdp)/1e14
print (df[['country','mbindex']])
```

```text
          country       mbindex
13  United States  12898.099255
24        Germany   1883.637224
32         France   1117.358002
```

---

Which power indicator was used for that analysis?

---

???

"The EU is designed to hide the weakness of France and the power of Germany"

---

Natural Gas prices are up.. some claim this drove coal prices up,
ppl switching to coal from NG.

[Stat](2019/05/stats.md#natgas)

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


