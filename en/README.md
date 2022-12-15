<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

Pinned Tweet

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hyper:Fuel Mobile Stations™ the power of the stars.<br><br>Hydrogen is the most abundant element in our universe. It fuels each star in our galaxy and every NASA rocket to date.. <br><br>Now it can power your car!<a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/refuel?src=hash&amp;ref_src=twsrc%5Etfw">#refuel</a> <a href="https://twitter.com/hashtag/recharge?src=hash&amp;ref_src=twsrc%5Etfw">#recharge</a> <a href="https://twitter.com/hashtag/NASA?src=hash&amp;ref_src=twsrc%5Etfw">#NASA</a> <a href="https://twitter.com/hashtag/starpower?src=hash&amp;ref_src=twsrc%5Etfw">#starpower</a> <a href="https://twitter.com/hashtag/losangelesautoshow?src=hash&amp;ref_src=twsrc%5Etfw">#losangelesautoshow</a> <a href="https://t.co/4Gl7rCdz1g">pic.twitter.com/4Gl7rCdz1g</a></p>&mdash; Hyperion Motors, Inc (@hyperionmotor) <a href="https://twitter.com/hyperionmotor/status/1595587623783141376?ref_src=twsrc%5Etfw">November 24, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

NeftegazRU: "Russia's own bid to become carbon neutral by 2060 is
expected to require major shifts in its energy strategy from oil & gas
to increases in nuclear and hydrogen production"

---

The draft might have played a role; >2 mil was drafted into Vietnam,
1% of population, that means more money was spent on people. Now
population of >300 mil has mil active personnel less than 1.5 mil. Gov
still deficit spends but if it all goes to Reytheon, Lockheed, from
there to some offshore haven, then to stawks, no inflation.

---

Inflation wasn't too high pre-73. Starting 73 it was but oil shortages
started then, and bunch of other stuff. Glad LBJ spent on social programs.

---

There is strong correlation with gov spending at the time and
inflation, but also between growth and unemployment which makes sense,
wages are major contribution to inflation.

Doc mentions gov spending wasn't entirely for the war; LBJ did some
social spending (money went to ppl direct, which, like wages, can
cause inflation).

---

See [doc](https://www.thebalancemoney.com/vietnam-war-facts-definition-costs-and-timeline-4154921)
here. I took data below from it, shifted source vars one year ahead
to see causal effects better. Correlation shown below,

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

---

Not all gov spending causes inflation. Not all gov spending was
for the war.

"The government spending for the Vietnam war caused inflation"

---

"@isabelzawtun@mstdn.social

Gary Numan is 13 days older than Gary Oldman. I don't even know what
to believe any more"

---

Reuters: "Egypt approves $5.5 bln green hydrogen project in Ain
Sokhna"

---

Zigwheels: "Hydrogen-powered Toyota Hilux in the works.. Toyota’s UK
arm has recently received funding from the UK Government to develop
the prototype of the hydrogen-powered Toyota Hilux"

<img width="340" src="https://pbs.twimg.com/card_img/1602731312564957184/TMA98qda?format=jpg&name=small"/>

---

I still see links to that Quanta article - "wormhole created in the
lab". What they missed; it was all computer simulation. Hey I could create
entire cities in the lab; see one [here](https://youtu.be/wjxVci-fWj4?t=85).

---

Barron's: "Buy Plug Power Stock, UBS Says. It Could Lead a Potential
$10 Trillion Hydrogen Market"

---

Andy Marsh's H2 company (Plug Power) picked up on it. [Here is](https://www.linkedin.com/posts/plug-power_plug-ceo-andy-marsh-was-honored-to-be-invited-activity-6976203348068704256-1a6S)
Marsh. This stuff isn't outside the mainstream anymore, hitjobs will
be harder to execute. Better watch out

---

*Glass Onion* - total hitjob. Talking down H2. Do these people want to
destroy the world? If one is against clean fuels, one is either
misinformed, ill-intentioned or a moron. There isn't a fourth option.

---

[There he is](tweets/2022/ejagoffthiel2.jpeg), with his best friend

---

Merry band of corksuckers around Peter Thiel - that group is like a
knitting circle, they blabber on constantly visit each others
'podcasts', give each other blowjobs.. They aren't contrarian in the
least. There is a clique, the clique has certain business interests,
whatever is suitable for those interests becomes the contrarian
viewpoint.

---

"@Hy_Economy@mastodon.social

Weimar, Germany, plans to replace all of their 37 buses with #hydogen
buses - the first three will arrive soon... They plan to use locally
produced green hydrogen to power the vehicle fleet"

---

H2 View: "Uniper, Shell announce contracts for blue hydrogen plans in Humber, UK"

---

## Reference

[Nations and Nationalism, Culture, Narratives](2013/02/nations-and-nationalism.html)

[The Fundamentals of Industrial Ideologies](2011/04/fundamentals-of-industrial-ideologies.html)

[Education, Workplace](2017/09/education-workplace.html)

[Science and Technology](2018/09/science-technology.html)

[Democracy, Parties](2016/11/democracy.html)

[Economy](2018/05/economy.html)

[Globalization](2018/09/globalization.html)

[Rome, The First Wave, Religion](2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2018/12/climate.html)

[Reports](2019/05/reports.html)

[The Middle East](2019/07/middleeast.html)

[TR](../tr)

## Browse

[Members](2022/08/members.html)

[By Year](years.html)

[Search](search.html)

[Tweet Archive](tweets/index.html)

[PDF](https://drive.google.com/uc?export=view&id=1FSi-1MnqXVq_PVTEXzzflwN8-7h92N_R)

