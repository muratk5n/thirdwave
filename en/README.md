<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

Pinned Tweets

<iframe width="340" src="https://www.youtube.com/embed/46y3FN4fKlE" title="E-Bikes, E-Scooters Injuries Multiplying" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Bloomberg: "Biden Has ‘Almost Guaranteed’ Hydrogen’s Future..  The law
[IRA], which provides producers with tax credits of as much as $3 a
kilogram, 'almost guarantees that hydrogen will be an important energy
vector going forward,'.. [said] head of industrial transition and
clean fuels at Macquarie’s Green Investment Group"

---

Upstream: "Sinopec to back multi-billion dollar green hydrogen project
harnessing wind power in northern China"

---

"@Hypx@mastodon.social

MTA to pilot \#hydrogen-powered buses in the Bronx"

---

"@claesdevreese@mastodon.social

Leading by example? The 🇪🇺is going full #mastodon.  Own instance for
all institutions"

---

MD report, with code ref

[[-]](2022/10/mastadon.html)

---

Or 4.74 to be exact

[[-]](https://www.cbsnews.com/news/six-degrees-of-separation-facebook-says-more-like-474/)

---

Crawl is done; I count 4601 servers and 7,824,386 users. 3 hops were
enough, maybe we should have Three Degrees of Kevin Bacon.

---

Just kidding it wasn't a wise man

---

Wise man said 'if one's code is not CPU bound one can start more
processes than cores'

---

"@Hy_Economy@mastodon.social

Mecklenburg-Vorpommern, Germany, will invest 560 million in \#hydrogen - 
this is more than the 500 million Bavaria plans to invest"

---

"@Hy_Economy@mastodon.social

Apus, Germany, develops a small \#hydrogen plane. The first prototype
should perform test flights next year.

Range: 800 km

Expected time for commercialization: 4 years"

[[-]](https://mastodon.ie/@Hy_Economy@mastodon.social/109401192156043941)

---

Traversal wld be breadth-first, check double visit of nodes.. Iteration
count..? Probably [six is fine](https://pbs.twimg.com/media/FijVyYTXoAArlYU?format=jpg&name=small).

---

You could write a simple "crawler" probably that can hit all MD servers
and get their info, collect it.

---

```python
response = requests.get(url) # details on specific host
res = json.loads(response.text)
res['stats'] 
```

```text
Out[1]: {'user_count': 880513, 'status_count': 43334732, 'domain_count': 35389}
```

---

All MD servers know about related servers, code below fetched that
for one machine displayed few results.

---

```python
import requests, json
url = "https://mastodon.social/api/v1/instance"
response = requests.get(url + "/peers") 
json.loads(response.text)[:4]
```

```text
Out[1]: 
['smgle.com',
 'mstdn.nielniel.net',
 'testdon00001.mamemo.online',
 'lazybear.io']
```

---

Mastodon servers have REST APIs - easy to get info... Nice.

---


"@gregeganSF@mathstodon.xyz

'Research at Royal Perth Hospital has found that 90 per cent of people
who believe they are allergic to penicillin are not.'"

---

Arab News: "British aid worth hundreds of millions of pounds went
toward funding police corruption in Afghanistan, according to a
report"

---

Politico.eu: "Furious EU countries rage over gas price cap proposal"

---

The psyop has a rich white guy who was culturally Protestan (as most Americans are),
to be seen as first Irish-Catholic President, read: a minority who was
"representing", "taken from us much too early". Dems are made to
weep after this symbol of diversity, follow its flashy image at the
same time ensuring its centrist, rich guy policies are followed. [This photo](https://pbs.twimg.com/media/FimCFrjWIAMztMt?format=jpg&name=small)
has the worst and second worst US presidents of modern times in a
single frame, and that is by design. 

---

".. ask what you can do for your country" translates to "dont ask for services
from gov" (as Markey brilliantly [used](https://youtu.be/86-3yuzn5UU?t=156) in MA
Senate race), "the rising tide lifts all boats" sounds like trickle-down economics
(in fact some of the WH advisors at the time were actual [proponents](https://www.thedailystar.net/news-detail-126725)
of the approach). JFK escalated the war in Vietnam, f--ked it all
up in Cuba, and somehow shifted the blame *to the media* with another
statemanly sounding proclamation. It all sounded aw so eloquent
that the retro air is what people remember fondly, rather than
the empty content of the statement itself.

---

Dems are better off wout the adulation, staning for the Kennedys, it
is holding them back. The soundbytes sound fine enough, but when you
dissect 'the legacy', there isn't much there.

---

TASS: "Odessa authorities approve demolition of monument to city's
founder Catherine the Great"

---

Anwar finally gets his chance.. Man it took a long time for this guy

Al Jazeera: "Malaysia's Anwar gets to work, promising inclusive
government.. Southeast Asian nation's new prime minister says he will
govern for all as he reaches out across political divides.

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

