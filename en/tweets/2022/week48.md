# Week 48 


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

[[-]](../../2022/10/mastodon.html)

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

Al Jazeera: "Malaysia's Anwar gets to work.. Southeast Asian nation's
new prime minister says he will govern for all"

---

Politico.eu: "After six years of chaos and recrimination since Britons
voted to leave the European Union, there are signs the country is
showing an unexpected outbreak of common sense in its approach to the
bloc.

In his first weeks in office, Prime Minister Rishi Sunak -a Brexiteer
himself- has sent clear signals that he wants a more constructive
relationship with Brussels and Paris, and to avoid a trade war with
Britain's biggest economic partner"

---

Al Monitor: "Amazon to open online grocery store in UAE"

---

"@hydrogenLOHC

\#Delegation Trip to Austria and Italy! Here are the main take-aways

1) When it comes to decarbonization, the new language is “hydrogen”
(besides \#renewableenergy) 💙

2) \#Hydrogen will partly be transported via pipelines (e.g. European
Hydrogen Backbone Initiative \#EHB) – so we must take the right steps
and find the right partners now 

3) The \#energytransition is a joint goal ➡️ only achievable through
international cooperation – hydrogen is a perfect example!

4) Our \#LOHC technology = a great solution for transporting
\#greenhydrogen via ship to Italy, where the hydrogen could be injected
into pipelines💪 

And: \#Hydrogen will come from all over the world, so we need all
transport options and act in a #technology-open manner!"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hyper:Fuel Mobile Stations™ the power of the stars.<br><br>Hydrogen is the most abundant element in our universe. It fuels each star in our galaxy and every NASA rocket to date.. <br><br>Now it can power your car!<a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/refuel?src=hash&amp;ref_src=twsrc%5Etfw">#refuel</a> <a href="https://twitter.com/hashtag/recharge?src=hash&amp;ref_src=twsrc%5Etfw">#recharge</a> <a href="https://twitter.com/hashtag/NASA?src=hash&amp;ref_src=twsrc%5Etfw">#NASA</a> <a href="https://twitter.com/hashtag/starpower?src=hash&amp;ref_src=twsrc%5Etfw">#starpower</a> <a href="https://twitter.com/hashtag/losangelesautoshow?src=hash&amp;ref_src=twsrc%5Etfw">#losangelesautoshow</a> <a href="https://t.co/4Gl7rCdz1g">pic.twitter.com/4Gl7rCdz1g</a></p>&mdash; Hyperion Motors, Inc (@hyperionmotor) <a href="https://twitter.com/hyperionmotor/status/1595587623783141376?ref_src=twsrc%5Etfw">November 24, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

For two teams we can look at their past K games, within that calc goal
avg, passes per minute, bad passes per minute, fouls per minute,
number of completed passes per minute in the attacking 30%/20% of the
field (see how detailed it is), it goes on... Taking such stats for
two teams even eyeballing one can probably gauge a winner. "AI" just
automates that, adds another layer of (let's be honest here) extremely
simple linear regression, and reports a result.

[[-]](https://github.com/GoogleCloudPlatform/ipython-soccer-predictions/blob/master/predict/wc-final.ipynb)

---

A lot of soccer games can be predictable. If you feed in gazillion of
base data points through "feature engineering" than even simple stupid
logistic regression will predict something. There are companies
providing such raw, so-called touch-by-touch data. See
[Opta](https://www.statsperform.com/opta-event-definitions/).

---

"@Hy_Economy@mastodon.social

Germany and France plan to strengthen that corporation regarding
\#hydrogen. Part of this should be the construction of a hydrogen
pipeline network"

---

"Ronaldo makes history.. he becomes the first.. to score in five
different FIFA World Cups"

---

"England draws 0-0 with the USA" \#Qatar

---

😂 US-England \#worldcup

[[-]](https://twitter.com/griffin_dahl/status/1596219000761245696)

---

RFK was ok on some left issues, but fell short... Supported the war in
Vietnam in the beginning, and promised to send 50 fighter jets to
Israel if elected president. That's why that Palestenian assassin was
radicalized and shot him literally one year after the Six-Day War.
Why support the civil right movement but be ok with Palestenians
getting bombed go bits?? Half-assed left - the perennial problem of
America. That is why RFK is dead.

---

