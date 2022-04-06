<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

Video on the First Light technology

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">⚛️ It says the method is simpler and more energy efficient than rival approaches, and it has reached this point at record rates of progress… <a href="https://t.co/6ZP23dfSO2">pic.twitter.com/6ZP23dfSO2</a></p>&mdash; Telegraph Business (@telebusiness) <a href="https://twitter.com/telebusiness/status/1511292001530036224?ref_src=twsrc%5Etfw">April 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Simple fuel, projectile, molecule based approach is much better than
bitch-electric, bitch-magnet, bitch-laser approaches. Heat, pressure,
mass, molecules, protons, neutrons - these form the crux of what's out
there, ie reality.

"Breakthrough achieved faster and cheaper than traditional fusion
approaches.. First Light is taking a unique projectile fusion approach
to solve [the] challenge, which it believes offers the fastest,
simplest and cheapest route to commercial fusion power. This means
that instead of using complex and expensive lasers or magnets to
generate or maintain the conditions for fusion, First Light’s approach
compresses the fuel inside a target using a projectile travelling at
tremendous speed"

[[-]](https://firstlightfusion.com/media/fusion)

---

This Dr. Tatsuya Kodama does good work; does research on solar
beam-down and H2 generation through high heat, wout electrolysis, has
Oz CSIRO ties.

[[-]](https://pbs.twimg.com/media/FPpiN4eXEAQTllx?format=jpg&name=small)

---

H2 View: "[European Investment Bank] and ICO invest €88m to develop
one of the largest green hydrogen production plants for industrial use
in Europe"

---

Their punch bowl is being taken away no more parteh

CNBC: "Key people from the Fed just spooked the markets - here's what
they said.. Fed Governor Lael Brainard and San Francisco Fed President
Mary Daly both issued comments that showed they both envision higher
rates and, in the former's case, an aggressive drawdown of the assets
the central bank is holding on its balance sheet..

Investors didn't particularly like what they heard, sending major
averages considerably lower on the day"

---

Unforscene - Dirty and Dark \#music

[[-]](https://youtu.be/FXw3r6r9R28)

---

T. Frank: "Frederick Dutton, Democratic Party power
broker.. identified workers, the core of the New Deal coalition, as
'the principal group arrayed against the forces of change'... The
culture in those years was saturated with depictions of blue-collar
bigots doing scary things like shooting the main characters in Easy
Rider and rioting in support of the Vietnam War...

Still, a man like Dutton should have known better. A glance at the
union placards carried by marchers at Martin Luther King’s 1963 March
on Washington —or at the way the United Auto Workers lobbied for the
Civil Rights Act of 1964 —or at the 1968 strike of black sanitation
workers in Memphis—should have been enough to suggest that the Archie
Bunker stereotype was not the whole story. Besides, what kind of
Democrat gives up on basic economic issues in order to focus on
matters of 'the psyche' and 'the soul'? This was not politics; it was
psychotherapy. Worse: it was aristocratic hauteur disguised as
enlightenment"

---

Why not? The job may not involve high skill but there is clearly a
demand for it.

"Truck drivers should not make the same amt of money as software
developer"

---

Are they unionized? They could push for workplace rules.

Rollling Stone (via Jon Oliver): "There are about 3.5 million truck
drivers in America, yet trucking companies have long claimed there’s a
shortage of drivers that threatens to derail — OK, further derail —
the supply chain. Except, the actual problem isn’t too few truckers,
it’s too few truckers willing to put up with all the terrible bullshit
truckers are forced to put up with"

---

Subtract imports from GDP (to see locally produced goods with locally
worked hours), divided total hours worked with it - gives numbers of
hours worked per unit GDP. Ratio has been decreasing for the past 70
years.

The reason for that decrease IMO is either technology, or too much
efficiency is being squeezed out of employees at the expense
of.. something. Maybe at Amazon you won't be allowed to take a
bathroom break.


```python
import pandas as pd, datetime
from pandas_datareader import data
today = datetime.datetime.now()
start=datetime.datetime(1945, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
df = data.DataReader(['GDPC1','B4701C0A222NBEA','IMPGS'], 'fred', start, end)
df = df.interpolate()
df['hrs_per_dollar'] = df.B4701C0A222NBEA/(df.GDPC1-df.IMPGS)
print (df['hrs_per_dollar'].tail(4))
df['hrs_per_dollar'].plot()
```

```text
DATE
2021-01-01    15.413216
2021-04-01    15.265204
2021-07-01    15.244684
2021-10-01    15.118662
Freq: QS-OCT, Name: hrs_per_dollar, dtype: float64
```

[Graph](https://pbs.twimg.com/media/FPfMHYJWUAAsACj?format=png&name=small)

---

Data disagrees - see above

"Productivity is stagnant"

---

Left Voice: "In a Historic Victory, Staten Island Workers Form the
First U.S. Amazon Union"

---

AMZN, Blue Origin can do some good in space industry.. When are
they building O'Neill Cylinders?

[[-]](2020/09/space-exploration-goals-colonization.md#oneill)

---

AFP: "Amazon has secured deals to launch up to 83 rockets carrying its
internet satellites into low earth orbit, in what is believed to be
the largest such procurement in the history of the space industry"

---

AFP: "Amazon has announced deals with Arianespace, Blue Origin and
United Launch Alliance to take thousands of satellites into orbit for
a space internet network called Project Kuiper"

---

😂 

"1984: Chlolesterol, and now the bad news..

2014: Eat Butter"

[[-]](https://pbs.twimg.com/media/FPk32mnWQAYJ8oA?format=jpg&name=small)

---

Leaving a sinking ship?

"Jen Psaki to leave White House for MSNBC gig"

---

Left Voice: "Greek Railroad Workers Block Delivery of U.S. Tanks to
Ukraine"

---

Can cause a contagion

CNBC: "Russia debt default prospect resurfaces as U.S. blocks bond
payment"

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


