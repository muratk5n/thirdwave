# Week 40

Langhorns - Las Vegas Fist Fight \#music

[[-]](https://youtu.be/awWByzK0n04)

---

Electricity tech pretty much sucks at everything except in certain
end-products which shaped the experience of an entire generation of
white-collor folk. They see lights go blink-blink and they get all
excited, and want to use that thing that makes things go blink-blink
for everything.. This is unrealistic.

---

Electricity based heating is incredibly inefficient (surprise). 

---

If green heating takes priority two things need to happen; 1) encourage
production of small, portable, H2/NH3 heating units, provided cheaply to
the world (otherwise they'll just burn wood, coal). Lavo was
[already working](https://revolution-green.com/unsw-develop-hydrogen-storage-renewables/)
on such a tech to power ovens (using a heat-exchange chemical reaction)
with simple H2 canisters. 2) For home heating, massive H2 pipeline
infra needs to be built which can provide homes
the fuel, they can use that for heating, through CHP.

---

Fortescue is from AU which has plenty of renewable potential of its
own. Then why go to Jordan..? These guys must be thinking four steps
ahead.. When the whole world wakes up to the potential of this stuff,
everyone will try to grab opportunities from sunny countries; well
Fortescue is in there now, locking in commitments... Europeans are in
North Africa. Saudi Arabia is already working with Japan.

"Jordanian government officials have met with a delegation from
Fortescue Metals Group to discuss investment opportunities in green
hydrogen and ammonia"

[[-]](https://www.pv-magazine-australia.com/2021/04/14/fortescue-delegation-meets-with-jordanian-government-to-explore-green-hydrogen-opportunities/)

---

Actually it was the academia that discovered GPUs could be used for
common numerical computation. First algorithm to run faster on the GPU
was researched [here](https://www.researchgate.net/publication/220782520_LU-GPU_Efficient_Algorithms_for_Solving_Dense_Linear_Systems_on_Graphics_Hardware).

"GPU coding happened thanks to the company NVidia"

---

Jon Stew new show is all serious.. During interviews I keep waiting
for that bizarre turn in the convo, like, 'you say there is no money
for this bill, but have you ever tried to put panties on your head?',
and the guy giving this blank look.. Yet the moment never arrives..

---

"[4/2021] Ramped-up domestic production of green hydrogen and ammonia
makes perfect sense for South Korea. Last month a deal was signed
between Australia-based Origin Energy and steelmaker POSCO for the
supply of green hydrogen in the form of green ammonia, produced at
Origin’s to-be-developed, hydro-powered ammonia production facility in
Bell Bay, Tasmania. Although POSCO is aiming for the import of
zero-carbon feedstock to be only temporary, the sheer scale of their
goal to produce 5 million tonnes of clean hydrogen in South Korea by
2050 is readily apparent"

[[-]](https://www.ammoniaenergy.org/articles/south-korean-update/)

---

MarketWatch: "Opinion: Explaining why ‘green hydrogen’ is our best (maybe only)
option for getting to net-zero carbon by 2050 and halting climate
change"

[[-]](https://www.marketwatch.com/story/explaining-why-green-hydrogen-is-our-best-maybe-only-option-for-getting-to-net-zero-carbon-by-2050-and-halting-climate-change-11633548333)

---

If co2 increases are during the winter, then priority should be to fix
heating, making that process renewable.. Surprise (!) H2, NH3 are the
best solutions for that as well. See CHP, Combined Heat and Power.

---

"Once it's added to the atmosphere, [carbon] hangs around, for a long
time: between 300 to 1,000 years"

[[-]](https://climate.nasa.gov/news/2915/the-atmosphere-getting-a-handle-on-carbon-dioxide/)

---

Clearly the increases are due to Northern Hemisphere
winter.

Then... 🤔 if everyone had a home in both hemispheres, went from one
to the other escaping colder season, there would be no CO2 increase..

Kidding

---

Monthly atmo carbon content [graph](../../2015/08/temp-increase.md#carbon).
It increases every year (except during warmer seasons when
it is flat).

Contrary to certain wisdom, co2 contentration during covid shutdowns
kept going up.

---

From Southern District of New York? Like in *Billions*.  Where is Chuck
Rhoades?

---

Clearly the judge was biased; not possible to request a new judge?

---

The [latest](../../2021/10/donziger-chevron.md#oct2021) on Donziger.  Poor
guy had to sit there and listen to a "federal judge compare him to a
mule who needed to be beaten with a piece of wood". This is unreal.

---

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

Electric transmission is incredibly inefficient \#deelectrify

---

Generate renewable fuel from fossil, CCS at the source, transmit.
H2 pipelines [work](https://pbs.twimg.com/media/EvdKNhvXAAE9Rr2?format=png&name=small).

Producing from green is better of course.. Politics will decide the
balance. But transmission must be green, and molecule based.

---

Renewable fuel pipelines wouldn't have this problem in case of
leak. No env damage (you'd be putting more H2 into H2O.. it's like,
who cares?).

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

Such colorful words.. but underneath it all, there is nothin

---

Which power indicator was used for that analysis?

---

???

"The EU is designed to hide the weakness of France and the power of Germany"

---

Natural Gas prices are up.. some claim this drove coal prices up,
ppl switching to coal from NG.

[Stat](../../2019/05/stats.md#natgas)

---

Asking a socmed company to decide themselves to not make something go
viral.. that's like asking McDonalds to sell less burgers.. Tough
ask. Can they determine when something has high DMSI but "can be
dangerous"? The answer is no, because the AI tasked with that job
doesn't work (she said this many times, it's true, even a lot of weak
AI is extremely shoddy). Good testimony though.. there was lots of
useful info in it.

"During the hearing, [Facebook whistleblower] Haugen mentioned that
Facebook CEO Mark Zuckerberg decided to not remove downstream MSI, or
Meaningful Social Interactions, because, rumor has it, peoples'
bonuses were tied to it. Haugen was formerly a product manager on
Facebook's civic integrity team, which focused on election
issues. Facebook got rid of her team shortly before the Jan. 6 riots,
and she quit her job in April.

The downstream MSI is a problematic tool because it predicts when
something might go viral — get a lot of views, shares, and comments —
and then it pushes that content out to more users"

[[-]](https://mashable.com/article/mark-zuckerberg-facebook-whistleblower-msi-bonuses)

---

Most companies cannot use, approach the DARPA model.. preferring an
actor-geek CEO instead, who will acquire, acqu-hire, or madly toss
together actually known tech in a bowl hoping something will come out
of it while trying to look "brave" in the process.

---

Any coffee fine enough for French press cld be "brewed" in a simple
cup. Add coffee, boiling water, wait, pour into another cup through a
sieve 🤷‍♂️

---

Makes sense.. lot of sunshine

"Jordan's Government Is Putting Its Focus On The Green Hydrogen Opportunity"

[[-]](https://fuelcellsworks.com/news/jordans-government-is-putting-its-focus-on-the-green-hydrogen-opportunity/)

---

Only the rare researcher can do both well.

"@OdedRechavi

Combining research with teaching"

[[-]](https://twitter.com/OdedRechavi/status/1443644844400955398)

---

Me? I said this before, I know [Italian karate](https://drive.google.com/uc?export=view&id=1TOO0EUwob6eso4RcXmU5kouLRi2YHXbc).

---

You can't win with ka-raze. You need to know karate.

---

Get this, MT is 55; he can still win that fight

"Mike Tyson keen to fight Logan Paul, with $100 million payday"

---

"New Zealand to End 'Zero Covid-19' Strategy"

---

If all lithium on Earth was mined and turned into batteries, it could
only handle 10% of todays energy requirements. H2, ammonia storage can
provide limitless storage capacity.

---


"Fumio Kishida, who was elected [as PM] by Japan’s Parliament, called
for more aggressive distribution of wealth to those with lower and
middle incomes"

---

I can't say I don't like this 🌌🛸👨‍🚀🖖

"Captain Kirk: Bezos' Blue Origin to send William Shatner into space"

---

Bathymetry 😶

---

Hyundai is a BUY

---

Translation: dont act like a cynical combmuncher - or you might get
treated as such

"The most worrisome factor is that China's delay might reflect not a
holdup in the preparation of its NDC, but a well-rehearsed plan to
leverage its climate change commitments into other areas where the
Biden administration has increased pressure on Beijing...

First, the weaponization of climate change measures might be seen by
the Biden administration as cutting off the last possibility of
cooperation with China, making the bilateral relationship much more
hostile. This is also a possibility in the case of Europe, given the
increasing importance of climate change in European citizens'
priorities"

[[-]](https://asia.nikkei.com/Opinion/Will-China-use-climate-change-as-a-bargaining-chip	)

---

I guess nothing interesting happens in the Anglosphere wout France
getting screwed in the process somehow.. Invason of Iraq: France [lost](../../2019/11/americas-secret-war-friedman.md#france)
Eastern Europeans, they sided with US, snubbed. And now the AU "sub
snub".

---

Addn'l gems here on DARPA, gov, and innovation -
[1](../../2021/10/entrepreneuel-state-mazzucato.html),
[2](../../2021/10/mission-economy.html),
[3](../../2021/10/the-value-of-everything.html)

---

There was a manager at DARPA in 2013 who took a chance on mRNA tech;
lined up bunch of research deps for that goal... Who is that guy?
What is his background? In which setting could he do what he did?

---

Private companies are good for delivering end-products based on
existing research. But pushing for risky research, not the right
address. I look at all the inno originating from DARPA.. They funded,
managed so much.

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hyundai Motor Group&#39;s Chairman, Euisun Chung, has announced that it will become the first global automaker to apply hydrogen fuel cells to all commercial vehicle (CVs) models by 2028. <a href="https://twitter.com/Hyundai_Global?ref_src=twsrc%5Etfw">@Hyundai_Global</a> <a href="https://t.co/0NTEc3woWq">pic.twitter.com/0NTEc3woWq</a></p>&mdash; Autocar India (@autocarindiamag) <a href="https://twitter.com/autocarindiamag/status/1435127959916924934?ref_src=twsrc%5Etfw">September 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"New Rules from #European Parliament on Energy Infrastructure: “Boost
Hydrogen & Carbon Capture, Phase Out Natural Gas”. No more financial
support for natural gas projects. Funds should support hydrogen,
CCS"

[[-]](https://bit.ly/3upBRH5)

---

"Storing Hydrogen Safely: Fraunhofer-Institut für Windenergiesysteme
IWM Evaluates Materials For Tubular Storage Systems in the joint
project H2Wind"

[[-]](https://bit.ly/2Yp71Tb)

---

Coal prices are through [the roof](../../2019/05/stats.md#coal)

---

JC was not a miscast! He was better than this new guy.. The key to
impressions is to catch a key characteristic. JC's angle is a
pent-up-anger shtick which of course reminds you of *Pet Detective*,
or *Liar Liar*, it was good.

TDB: "Last season, Saturday Night Live navigated its way through the
transition from Trump to Biden, first by miscasting Jim Carrey
opposite Alec Baldwin.. 47th season [opened w]ith one of its brand new
cast members, James Austin Johnson as the 46th president"

---

Europe's answer to DARPA, Joint European Disruptive Initiative -
[JEDI](https://www.jedi.foundation/)

\#F24

---

Darpa funded the first mRNA tech in 2013 - the basis of today's
Moderna and Pfizer vax

\#F24

---

I have to say this is a fantastic application of mathematics to a
real-world problem. Based on two numbers the formula generates
near accurate counts for the entire grid structure. V cool.

---

Poisson distr is,

$$ f(x) = P(X=x) = e^{-\lambda}\frac{\lambda^{x}}{x!} $$

which gives probability of 1 event, 2 events, in a certain block of
time. But in geo you have to think little differently. You divide
London into grids, and count how many bombs fell on each, then count
how many grids had 1 bomb, 2 bombs, etc. Reproducing such counts from
formula,

```python
N = 576.
m = 537/N
c = N*np.exp(-m)
expb = [c*1, c*m, c*m**2/2, c*(m**3)/(3*2)]
[np.round(e,2) for e in expb]
```

```text
Out[1]: [226.74, 211.39, 98.54, 30.62]
```

Real counts were 229, 211, 93, 35, etc. Pretty close. I am sure a
statistical test wld agree. Clustering disproved. 

---

Why the Poisson distribution usage in this [post](../../2021/08/bermuda.html)?
Event counts tend to be distributed that way.. Let's take the London
bombing [example](https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/abs/an-application-of-the-poisson-distribution/F75111847FDA534103BD4941BD96A78E).
They were wondering if bombings were clustering at specific places.
Cld be important.. Maybe Nazis were focusing bombing somewhere? Poisson
is for natural counts, then if that is proven, clustering is disproved.

---

Maybe they are Israelis from America. Their great-great-great
grandfather was kicked out by a Palestenian's great-great-great
grandfather, and, like, now they are totally back. 🤣

---

US teenagers there..? "Like, totally, a game changer, I liked eeiiiit"

---

Laboratory grown meat served in a restaurant (they grow the meat right
next door actually), Israel.

<iframe width="340" src="https://www.youtube.com/embed/CzEDkMnJ5Bo?start=17" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

The tech is [too noisy](../../2021/03/unrivaled-beckley.md#sub)

"China has nuclear subs too"

---

Affirmative action works

"California outlawed the all-white-male boardroom. That move is
reshaping corporate America"

---

BBC: "Climate change: Stop smoke and mirrors, rich nations told"

---

"An ecologically minded experiment to make Paris a cycling capital of
Europe has led to a million people now pedaling daily — and to rising
tensions with pedestrians."

---

