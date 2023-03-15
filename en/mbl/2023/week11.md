# Week 11

Al Monitor: "Israeli leaders trade accusations over Saudi-Iran
rapprochement via China.. Coalition and opposition leaders are trading
accusations over which government is to blame over the
relations-renewal deal between Tehran and Riyadh"

---

H2 Central: "Bloom Energy fuel cells successfully used aboard cruise
ship"

---

GP is the current, and the first left-wing President of Columbia, also
former mayor of Bogota.

Gustavo Petro: "A developed country is not a place where the poor have
cars. It's where the rich use public transportation."

---

For Prez elections the ultimate Hail Mary was from the Rep side during
the 2000 election. I don't mean to downplay the skills of other
campaigns who also won... Maybe they too had it in them to snatch a
win out of the lion's den, just snatching that shit, snatching it and
going home with the trophy.. Maybe. But we didn't see those campaigns,
we almost exclusively saw the ones who won with an advantage. I need to
base the take on data.

---

Previous share on AI+ethics debate is similar in spirit to AI+doomsday
debate. In both cases the underlying assumption / message is the tech
is *that good*. It's a good trick, sales-by-presumption. If A implies
B develop arguments as if B is already true, which telegrams A is a
done deal. These c--suckers are always selling...

---

Taxpayers are absolutely on the hook for SVIB bailout. Gov covered not
just some, but all depositors; and the bank's total deposits reach
over $170 billion - no pocket change.

But if gov works the books, spreads the damage forwards can reap some
if not all loss... it's possible. 

---

The first AUKUS announcement was happier, snappy, woo hoo we are on
top of the world baby..! This one looks more sad, dour. Two of the
three figures have low approval ratings, one is certainly on the way
out. The war in Ukraine is not going well for the "Rules-Based Order"
and the opposition is coalescing.

---

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

[[-]](../../2021/01/stats.html#tcurve)

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

<img width='340' src='bank1.jpg'/> 

---

"@joeyh@octodon.social

[Y Combinator] posted a petition to get a goverment bailout for SVB,
and the \#HackerNews post for it attracted so many people telling them
to go jump in a lake that YC flagged it right off their own website"

---

Ng is a Stanford prof, taught deep neural nets for many years. DNNs
are okay for limited, well-defined, focused use.. But notice the
subtext - ain't gonna get no AGI with them neural nets.

---

Reshare 2018.

"@AndrewYNg

AI+ethics is important, but has been partly hijacked by the AGI
(artificial general intelligence) hype. Let's cut out the AGI nonsense
and spend more time on the urgent problems: Job loss/stagnant wages,
undermining democracy, discrimination/bias, wealth inequality"

---

"Brookings’s Aaron Klein argued that total avoidance of bank failure is
not necessarily a good thing, as some banks that make bad business
model decisions deserve to fail"

[[-]](https://www.brookings.edu/2023/03/10/forum-on-the-future-of-the-federal-home-loan-bank-system-highlights-from-the-brookings-and-bu-law-event/)

---

"@wallstcynic

The chutzpah here beggars belief. The VC 'community' literally started
the SIVB run on Thursday, when it urged its portfolio companies to
pull their deposits.. which they did ($42B). And they now want the
Taxpayer to bailout their investments…?!"

---

Come to Butthead \#music

[[-]](https://youtu.be/Iht77cJGRl4)

---

I could improve the visuals, or.. I could just steal Github Pages
template. [Boom](https://muratk5n.codeberg.page/en/).

---

For the backup site I generate the visual pages (HTML) from raw content,
using Python `markdown` pkg. 

---

H2 Central: "German hydrogen firm Thyssenkrupp Nucera (TKAG.DE) has
seen customer interest soar in the U.S. as a result of the Inflation
Reduction Act (IRA) and may create local production capacity with
Italy’s De Nora (DNR.MI) if the market takes off.

Thyssenkrupp Nucera held talks about several potential green hydrogen
projects 'with very concrete timelines' during a trip to the United
States last week, Chief Executive Werner Ponikwar said in an interview"

---
