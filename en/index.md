
"@Floofer@mk.catgirlsfor.science

A pizza is basically a real life pie chart that shows the amount of
pizza left"

---

H2 Central: "West Virginia Hydrogen Hub Coalition Applauds Appalachian
Hydrogen Hub’s Continued Success.. Senator Manchin said: 'West
Virginia and Appalachia have a long history of powering our great
nation, and I am pleased the Appalachian Regional Clean Hydrogen Hub’s
tireless efforts have been rewarded by the Department of Energy'"

---

Mozilla Mastodon instance is up

[[-]](https://mozilla.social/public/local)

---

Need to stress the approach can fail sometimes

Seeking Alpha: "1953 and 1957 [recessions], were not preceded by yield
curve inversions. So this concept is not perfect by any means"

---

"The curve" has indeed inverted (longer maturity treasuries have lower
yield than shorter ones) which some take as a signal of recession. 

[[-]](2021/01/stats.html#tcurve)

---

DGW Magazine: "Engine maker INNIO plans to convert a German power
plant to 100% green hydrogen by 2035"

---

Euractiv: "Germany ‘not opposed’ to nuclear-made hydrogen, says will
import from France"

---

Some banks need to fail, it is a sign the system is punishing bad
management. See the plot below, \# of bank bankruptcies per year, data
from FDIC. Notice the two years when there were **zero** bank
closures.  2005, and 2006. What happened afterwards? 🤔

```python
url = 'https://www.fdic.gov/bank/historical/bank/bfb-data.csv'
df = pd.read_csv(url,parse_dates=['Closing Date'])
df['year'] = df['Closing Date'].dt.year
dfg = pd.DataFrame(index=range(2001,2023))
dfg['closures'] = df.groupby('year').size()
dfg.fillna(0).plot(grid=True)
```

<img width='340' src='mbl/2023/bank1.jpg'/> 

---

## Reference

[Nations and Nationalism, Culture, Narratives](0119/2013/02/nations-and-nationalism.html)

[The Fundamentals of Industrial Ideologies](0119/2011/04/fundamentals-of-industrial-ideologies.html)

[Education, Workplace](0119/2017/09/education-workplace.html)

[Science and Technology](0119/2018/09/science-technology.html)

[Democracy, Parties](0119/2016/11/democracy.html)

[Economy](2021/01/economy.html)

[Globalization](0119/2018/09/globalization.html)

[Rome, The First Wave, Religion](0119/2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2022/01/climate.html)

[Reports](2021/01/reports.html)

[The Middle East](0119/2019/07/middleeast.html)

[TR](../tr/index.html)

## Browse

[Members, Donations](2022/08/members.html)

[By Year](years.html)

[Search](search.html)

[Microblog Archive](mbl/index.html)

[PDF](https://drive.google.com/uc?export=view&id=1FSi-1MnqXVq_PVTEXzzflwN8-7h92N_R)

Also on 
[Mastodon](https://masto.ai/@muratk3n),
[Codeberg](https://muratk5n.codeberg.page/en/),
[Github Pages](https://muratk5n.github.io/thirdwave/en/)

