# Week 42

"Europe’s Largest Electrolysis Plant Under Construction... Everfuel is
set for full production of green hydrogen at Phase I of the flagship
HySynergy project in Fredericia, Denmark"

[[-]](https://bit.ly/3m1RsKf)

---

I like that everyone gets coin tho it needs to happen continuously
expanding the money base, inflating away stashed wealth while
providing UBI. Also iris image capture -> id generation doesn't sound
secure.

[Worldcoin](https://worldcoin.org/)

---

AFP: "The World Health Organization said Thursday that 80,000 to
180,000 health care workers may have been killed by Covid-19 up to May
this year, insisting they should be prioritised for vaccination"

---

This supersonic stuff is fine and dandy but if there are nuke-powered
nuke-armed subs in play, retaliation after a surprise attack is still
possible. Then you are back to M.A.D.

---

Chris Joss is French? He got the funk

---

Chris Joss - Superjam \#music

[[-]](https://youtu.be/t_1fJLG9WZM)

---

"Putin takes tougher anti-COVID measures as deaths soar"

---

Not the only reason for vax hesitancy but yes \#M4A

[[Comment]](https://pbs.twimg.com/media/FCJWaFEUUAcrDXN?format=jpg&name=medium)

---

I bet the script was written by a major scifi fan; used stuff from SG
Atlantis where Momoa played in, there JM constantly punks another
character, they had a similar act in *Dune*.

---
 
*Dune* looked great cinematically. Acting top notch. There is a Part 2
in the works? 

---

Good for Barbados

"Barbados has elected its first president, a key step in preparations
to become a republic and remove Britain's Queen Elizabeth II as head
of state of the Caribbean island"

[[-]](http://u.afp.com/wZe6)

---

Hi-Fi Companions A Night In Trimisoara \#music

[[-]](https://youtu.be/jGw3EdlthWQ?t=58)

---

Literally ran that code while writing this post. So right now 25 mil
ratings, for 58K movies, by anonymous 280K users are in notebook's
memory. This is not a drill. We have some fine computing capabilities
compared to even few decades ago..

---

How to? Full zip file is [here](https://grouplens.org/datasets/movielens/latest/),
unzip, then for example read all ratings with,

```python
from scipy.sparse import csr_matrix
import pandas as pd
r = pd.read_csv("ratings.csv")
m = csr_matrix((r.rating, (r.userId , r.movieId)))
```

Let's check the rating of user Id 2 for movie Id 2707

```python
m[2,2707]
```

```text
Out[1]: 3.5
```

*Arlington Road* apparently. Rating was 3.5 (out of 5.0)

.. and go from there. 

---

Big Tech marketing calls similarly rudimentary, or shoddy approaches
"AI", this is wrong.

---

:) No it is not "AI". Just simple linear algebra

---

Algo chose this movie by [geek] reducing the user-movie rating matrix
through singular value decomposition and searching in the reduced
space for users matching my record, and recommending their top liked
movies. Since the matrix is sparse `csr_matrix` can be used, speeds up
the process [/geek].

---

My DIY recommender chose *Equalizer 2*. It was good 

---

Alec Baldwin, daam.. F-ing gangsta

---

"@astreaos

no emoji can replicate the sheer joy that this guy :D radiates"

---

The fluidic theories of course need to be tied to the rest of phy. An
advice to their theoreticians while they do that; feel free to ignore
parts of "known physics" as needed. Much of recent physics is a mess..
"Theory doesn't fit with CMB" shld be able to trigger "does that
matter?". That "cosmic background" could well be misinterpreted
signals from f-ing Jersey shore (instruments were [near
there](https://bit.ly/2CMq76V)) and birdshit on the antennas.

---

"NY Governor & @PlugPowerInc Announces Construction Start at Largest
Green Hydrogen Plant in North America"

[[-]](https://bit.ly/3DUehpg)

---

The Guardian: "‘Case closed’: 99.9% of scientists agree climate
emergency caused by humans"

---

[MSNBC](https://pbs.twimg.com/media/FCHB0KBXsAAgte5?format=jpg&name=small)
dropped the ball.

---

"As of Tuesday morning, 82% of S&P 500 companies that have reported
earnings beat expectations"

---

[This](https://pbs.twimg.com/media/FCH7BhcXoAMcbXR?format=jpg&name=small)
just looks so bad.. Imagine amount of copper, steel used in the
construction. A single gas pipeline can replace all of that, *and* perform better.

---

I see, there have been fluidic space theories, trying to explain
gravity, one including dark matter, dark energy..  Good stuff..

---

An air bubble in water rises up to surface.. There is more pressure at
the bottom of it than at the top. More pres at the bottom bcz more
fluid there relative to top, more weight, creating pressure
difference.

If space is seen as fluidic, planet gravitational pull can be
explained similarly perhaps?  This fluid is extremely dense (according
to a yet unknown measure), denser further from bodies, and relative to
that planet bodies are like air, so "bubbles", ie other bodies are
pushed towards it, explaining the pull..? 🤔

---

It's open season on Facebook

---

Using coffee beans ground into a fine powder, then boiled in a little
[brass pot](https://pbs.twimg.com/media/FB9mjc0XMAU_YNS?format=jpg&name=small)
is called different names by countries, with many laying claim on its
invention. But that style of coffee making was first invented in Yemen; so it
should be called Yemenese coffee.

---

"@ivadixit

I’m just remembering that my second year in America, someone asked me
to 'validate their parking,' which was my first time hearing the
phrase, and after blinking stupidly in silence for a full five seconds
I said 'Well parking is really hard but I’m sure you did it really
well'"

---

"[Hy Stor] Energy Developing First-Ever U.S. Zero Carbon Green Hydrogen
Storage Hub..  Mississippi Clean Hydrogen Hub Represents Largest Green
Hydrogen Project of its Kind in the U.S"

[[-]](https://bit.ly/3pcB9MJ)

---

"Welspun Group Corp: First Company from India to Join the H2 Pipe
Joint Industry Project on Hydrogen Pipelines"

[[-]](http://bit.ly/3jgF1bz)

---

Heat pumps are better than purely electrical (resistance) heating as
they use some gas inside, also clean, but will still cause an uptick
in electricity usage.. Depending on the price of electricity in a
country that can hurt budgets. Everything about electricity, from its
delivery, to its storage, is problematic. If renewable gas is piped
into homes it can simply upgrade gas boilers to use the new gas,
instead of natgas.

---

NYT: "Russia's Low Vaccination Rates Leads to Record-Breaking Toll"

---

Reuters: "Centre-left wins Italian mayoral run-offs as right flounders"

---

[More](../../2021/09/computing-ai.html#car) on the shortcomings

---

FB has top talent; They have Yann Freaking LeCun -- One of the architect of the
so-called "return" of the neural net approaches.

---

The tools, the science of this domain is nowhere near being effective,
undeserving of the AI moniker (they are "preliminary weak AI" at
best), and they will not get better using the current methods being
deployed today.

"Facebook claims it uses AI to identify and remove posts containing
hate speech and violence, but the technology doesn't really work,
report says"

[[-]](https://www.businessinsider.co.za/facebook-ai-doesnt-work-to-remove-hate-speech-and-violence-2021-10)

---

Sounds like defunding the poh-lice

"[Berkeley] city council passed 'BerkDOT,' a first-in-the-nation
measure to shift traffic enforcement to unarmed Department of
Transportation workers. In the summer of 2020, cities across America
made similar commitments: to curtail the use of force, shrink police
budgets, and fund fleets of civilian officers. But Berkeley was the
first to target the traffic cop. By doing so, it is rethinking police
power at its root. Traffic stops are by far the most common reason
that police officers initiate contact with members of the public; they
account for 84 percent of encounters, according to data from the
Bureau of Justice Statistics. In fact, before cars, ordinary citizens
rarely came in contact with law enforcement. As we rebuilt cities
around the automobile, historians contend, drivers came to expect to
be policed. And communities of color have paid the highest price"

[[-]](https://www.theatlantic.com/ideas/archive/2021/10/end-police-violence-get-rid-traffic-cop/620378/)

---

Politico: "Republican governors crusading against vaccine mandates are
facing significantly lower approval ratings on their handling of the
coronavirus pandemic than their counterparts"

[[-]](https://www.politico.com/news/2021/10/17/governors-covid-vaccine-mandates-approval-516112)

---

The Daily Beast: "The net worth of American billionaires continues to
skyrocket, putting their collective wealth at more than $5 trillion,
according to a new study"

---

<iframe width="340" src="https://www.youtube.com/embed/SKVMPN2Biw8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

"HYVIA Unveils its First Prototype of the @renaultgroup Hydrogen Fuel
Cell Powered Master Van H2-Tech"

[[-]](https://bit.ly/3aCgTvC)

---

Holywood is obsessed with Batman.. There is an unending stream of
movies made abt the character.. They couldn't even wait for the dust
settle on the last actor (B. Affl), they immediately served a new
actor (the vampire guy).

I suspect propaganda. B. Wayne is rich (BAff version even said as much
in one movie when asked about his powers, answering with "I'm
rich"). BM in the comics is supposed to be an innovator himself, a
detective, but in recent incarnations his toys, BW glamor are more
front and center. The message is this; government is failing (in fact
it always fails, it can't not fail), trust the billionaire to solve
problems for you.

---

Umpteenth Batman movie?

---

Yeaa but water isn't compressing there, really.. molecules are just
sort of moving out of the way to let the fork through, that is what's
going on

"But I can put a fork in water! Easy!"

---

It's true. A tree trunk, which is solid, can be compressed to smaller
size. But water cannot. It is counter-intuitive at first, but actually
makes sense if one thinks about it.

---

That I could believe.. Anyone studying fluids wld understand. Incompressibility 

"It is well known that underwater explosion cause more damage than the
same amount of explosive detonated in the air"

[[-]](https://www.sciencedirect.com/science/article/pii/S221491471830120X)

---

18 tons teq in the sea caused 3.9. But 1000 tons on land caused 3.3?

---

Interesting.. Lebanon 2020 explosion registered as 3.3 magnitude
earthquake, it was estimated to be 1 kilotons of TNT equivalent.

<img width="240" src="https://pbs.twimg.com/media/FB7MshSXMAgA4dn?format=png&name=small"/>

---

"The capacity of the German natural gas network is more than 200,000
GWh, which meets the requirements for several months. In comparison,
the capacity of all the German pumped storage power plants only
amounts to about 40 GWh"

[[-]](https://www.researchgate.net/publication/301254520_Underground_and_pipeline_hydrogen_storage)

---

The pipeline system itself can be considered as storage; Even when we
are not pumping in new H2, the pipes themselves still have gas in
them. Same is true for natgas.

---

"@Faackshunter

They're gonna try and epstein [Donziger], fuck"

[[Latest]](https://twitter.com/Faackshunter/status/1450266152425250819)

---

F24: "Three German parties reach preliminary deal to form next govt"

---

Just teasing the Canadians.. Good people.. The Shat is Canadian, most
don't know.. D. Sutherland, Leslie Nielsen, Jim Carrey, lota actors.
I guess US is already invaded by Canadians.

---

Operation US Invasion is nigh

---

"Canada is investing in an improved communications intelligence
(COMINT) and signals intelligence (SIGINT) capability, known as
Project Strongbow, for the Royal Canadian Navy"

---

The presence of such massive supply at the consumer's doorstep can
spur development of more end-use products; eg carmakers they will
speed up FCEV production, we'll probably see more products around
portable canisters, etc. Supply is key. Aplenty will attract aplenty.

---

H2 transition can be in stages; Gov can first encourage production,
and distribution of H2 to cities via pipelines. If homes do not have
CHP, gas heating units, then gas is converted to electricity at a
local hub, the last mile remains the same. Later as people convert
their units at home, they can get the gas directly from city pipeline.

---

Tyson Fury was named after Mike Tyson? Nice

---

"@SofiaHCBBG

This is contagion. China developers in October: 

* Fantasia: Oct. 4 default. Two directors resign 
* Evergrande: Oct. 11 coupon not received 
* Xinyuan: will pay just 5% of Oct. 15 note 
* Sinic: Won't pay principal/interest due Oct. 18 
* Modern Land: asks for 3-month extension"

---


Most of those ew-money-printing-bad-so-bad-poop-fiat-gold-gold-gold
crowd u see in "certain media" are serving the interests of an
anti-dollar lobby, non-leading powers jealous their currency is not
the main one. Printing per-se isn't bad, the issue is who you print it
*for*. There is always printing. Plus developed countries aren't
foolish enough to end up like bleeping Venezuella. Then if there is
inflation, we can suspect wage increases, or supply issues, or both.

---

It happens to be one of the core tenets of econ.. time to hit the books?

Cld also be supply issues of course

"You said wage rises causes inflation.. I dont understand"

---

NYT: "[Senator Manchin], the Democrat from coal-rich West Virginia
whose vote is crucial to passage of the bill, has told the White House
that he strongly opposes the clean electricity program... As a result,
White House staffers are now rewriting the legislation without that
climate provision, and are trying to cobble together a mix of other
policies that could also cut emissions"

---

Malt is good.. I started seeing power bars with it, some exclusively
marketed to contain malt. There is dark malt powder for bread makers.
It cld go well in protein shakes too Im guessing.

AP News: "Malt Makes a Comeback, Packing Powerful Nutritional Benefits"

---

Beans alone do not supply the 9 essential aminos, but rice and beans
do (no wonder the combo is a staple in some cuisines). Rice and peas
too..

---

These news cld be interpreted it either way. If RU ever wanted to turn on
CH, they now gained valuable intelligence about them, learned their
weapons, sub tactics.

"[Oct] Chinese, Russian navies conduct co-ordinated anti-submarine drill in Sea of Japan"

"[August RU/CH] drills also marked the first time Russian soldiers had used Chinese weapons"

---

A regular 48-inch hydrogen pipeline [can carry](https://gasforclimate2050.eu/wp-content/uploads/2020/07/2020_European-Hydrogen-Backbone_Report.pdf)
13 Gigawatts. Little back-of-the envolope calculation; One person in the
developed world consumes 10 KW, this means a *single* H2 pipeline
can supply energy to 1.3 million people. 

That is a city the size of Ottowa, Zurich, or Belgrade.

---

One can learn abt government while in military.. It's **a** branch of
government after all.. For example how do they handle purchasing? A
new equipment is needed, what are the channels to get it done? You are
given a rifle, a canteen, whatever, how is that tracked?  Maybe that
information can help you understand the post office, or FEMA, or name
it, any other government agency. Even as a grunt, we might dismiss it
being at the bottom of the hierarchy, but in many ways everything
revolves around the grunt, his ass needs to be carried to and from the
"theather of action", provided food for, resting env, the grunt will
experience all that, first hand. I'd call that relevant experience.

"Why do you say military service is useful experience for politicians?"

---

