# Week 14 

Video on the First Light technology

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">⚛️ It says the method is simpler and more energy efficient than rival approaches, and it has reached this point at record rates of progress… <a href="https://t.co/6ZP23dfSO2">pic.twitter.com/6ZP23dfSO2</a></p>&mdash; Telegraph Business (@telebusiness) <a href="https://twitter.com/telebusiness/status/1511292001530036224?ref_src=twsrc%5Etfw">April 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Simple fuel, projectile, molecule based approach is much better than
bitch-electric, bitch-magnet, bitch-laser approaches. Heat, pressure,
mass, molecules, protons, neutrons - these form the crux of what's out
there, ie reality.

"First Light is taking a unique projectile fusion approach to solve
[the] challenge, which it believes offers the fastest, simplest and
cheapest route to commercial fusion power. This means that instead of
using complex and expensive lasers or magnets to generate or maintain
the conditions for fusion, First Light’s approach compresses the fuel
inside a target using a projectile travelling at tremendous speed"

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
of.. something. Wages? Maybe at Amazon you won't be allowed to take a
bathroom break?


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

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">👀 🛩 GTL ultralight aircraft tank just 67kg holds ~150kg of liquid <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> 💪enough for 8hr 4,500km flight with <a href="https://twitter.com/hypointinc?ref_src=twsrc%5Etfw">@hypointinc</a> system. The future of <a href="https://twitter.com/hashtag/zeroemission?src=hash&amp;ref_src=twsrc%5Etfw">#zeroemission</a> ☘️flight. H2 tech just keeps on accelerating <a href="https://t.co/0BSPCaf0UB">https://t.co/0BSPCaf0UB</a></p>&mdash; Jon Hunt (@JontheHunt) <a href="https://twitter.com/JontheHunt/status/1510898984365301763?ref_src=twsrc%5Etfw">April 4, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

H2 Fuel News: "HyPoint predicts fuel cell aircraft with 4 times range
of conventional planes.. The company expects that this will occur
because of the ultra-light cryotank developed by GTL"

---

H2 View: "One solution [for H2 storage] that has been overlooked is
liquid organic hydrogen carriers.. LOHC are organic compounds that can
absorb and release hydrogen through chemical reactions... In
principle, every unsaturated compound (organic molecules with C-C
double or triple bonds) can take up hydrogen during hydrogenation..
One m³ LOHC enables the safe storage of 57 kg H2"

---

H2 View: "France has recently announced a €7bn package to build a
carbon-free hydrogen industry. Germany issued a similar program of
€9bn and that has intensified as their reliance on Russian gas is
threatened. In July, the European Commission said it is looking to
increase its production capacity of electrolysers from 250MW today to
40GW in 2030. Similar strategies have been released by the UK,
Australia, and Asian countries. These are just some of the most recent
announcements, but they show a clear trend towards massive public
investments in the sector"

---

Businesswire: "Locosoco pleased to announce discussions are underway
with Proton Technologies, a leader in the field of Clean Hydrogen
Production that utilises existing fossil fuel infrastructure.. Proton
Technologies [tech creates] carbon-free, low-cost opportunity for
extracting hydrogen using previously expensed infrastructure and known
energy deposits.. [which allows] extraction of clean hydrogen whilst
sequestering carbon within existing oil wells"

---

We could complement the transition with CCS. Many green advocates are
fine with blue H2 generated from natgas with carbon capture (of course
solar is preferable). People who lobby, produce lit on this stuff need
to laser focus on proper engineering, and costs.

Report: "Greenhouse gas emissions need to be reduced by 43% and methane
by about a third by 2030 that can only happen if countries reduce
their dependence on fossil fuels and replace it with renewable energy"

---

WION: "United Nations warns that it's 'now or never' to avoid climate catastrophe"

---

Condemnation rituals.. Will that help? 

Maybe Japan should have just condemned Harry Truman for his war crimes
in Japan in 1945, instead of making a deal.

---

The play could be an inner-outer battle too.. Abdullah's mother is
British - some say the only reason he got the job

---

Jordan is land-locked too except a tiny sea access. 

---

What was the aim for toppling Abdullah again? He wasn't for the accords?

I know Abdul is a Trekkie (had a cameo on Voyager) nothing particularly against him

---

Trump gone, he gone.

"[King's brother] Jordan's Hamzah renounces title of prince"

---

The backdrop changed of course throughout the Craig era; there was the
2008 crisis, failures in Iraq, Syria, refugees, more crisis.. Surely
these effected the mood later.

---

*Bourne Identity*, the first movie in the series, isn't exactly a post
9/11 movie. It was written, filmed 1999/2000, due to delays it hit the
theathers 2002. That is clear to see in the content; plus the director
Liman's father was Senate chief counsel on the Iran-Contra affair, so
he was making a movie around that stuff, shady biz, underhanded
spycraft etc. Later two Bourne movies are different.

---

*Casino Royale* was a good action movie, no arguments there.

---

After many globetrotting adventures (an "outer belt" hero, Master of
all Faraway Lands) 9/11 Bond died near European landmass, after
fighting a foe played by an ethnically Egyptian actor.

---

The 9/11 Bond, "James Blonde", has died. It's interesting the first
major action scene has Bond killing, beating on colored people in a
Caribbean setting. Post 9/11 Jason Bourne would soon follow suit.

Arabs aren't black but hey, close enough, they just found the nearest
non-white folk and beat up on them. Fureigners, A-rabs and the like,
you've been warned.

---

:) James Bond's grave at Faroe Islands

Spoiler: the last movie has Bond die there. The island now uses it as
touristic attraction apparently.

[[-]](https://pbs.twimg.com/media/FOrhf5CXMAg-Z3g?format=jpg&name=small)

---

The migration that resulted due to the partition was especially bad
with deaths reaching up to a million. That too is on the Brits.

Al Jazeera: Before leaving India [1947], the British made sure a
united India would not be possible... East and West Pakistan were
hacked off the stooped shoulders of India by the departing
British.. Within months, India and Pakistan were embroiled in a war
over Kashmir, the consequences of which still affect us today. The
creation and perpetuation of Hindu-Muslim antagonism was the most
significant accomplishment of British imperial policy: the colonial
project of 'divide et impera' (divide and rule) fomented religious
antagonisms to facilitate continued imperial rule"

---

Kashmir? Britain's fault

---

It makes sense for Pak to get buddy-buddy w China, Russia; since India
rels are always on the rocks. Cant blame a guy for wanting friends,
energy deals, ports and roads for his country.

---

Additional info [here](2021/03/unrivaled-beckley.md#taiwan).

---

Al Jazeera: How hard would it be for China to invade Taiwan?

[[-]](https://youtu.be/qaYQNyJlNFk)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">In a top <a href="https://twitter.com/hashtag/H2View?src=hash&amp;ref_src=twsrc%5Etfw">#H2View</a> <a href="https://twitter.com/hashtag/hydrogennews?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogennews</a> story this week we saw that Germany’s <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> refuelling infrastructure will receive a substantial boost.<a href="https://twitter.com/Hy24partners?ref_src=twsrc%5Etfw">@Hy24partners</a> is set to provide €70m ($77m) in funding to support <a href="https://twitter.com/H2_MOBILITY_DE?ref_src=twsrc%5Etfw">@H2_MOBILITY_DE</a>.<a href="https://twitter.com/hashtag/HydrogenNow?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenNow</a><a href="https://t.co/rPitiEnVi1">https://t.co/rPitiEnVi1</a></p>&mdash; H2 View (@h2_view) <a href="https://twitter.com/h2_view/status/1510343781991817224?ref_src=twsrc%5Etfw">April 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Fermilab physics video below. Summary: Mass is an illusion. Proton,
neutrons are the shit. Higgs Boson is not a big deal.

[[-]](https://youtu.be/x8grN3zP8cg?t=81)

---

TDB: "IBM’s Watson, who trounced the greatest Jeopardy! players on the
classic game show—but needed to be hard-wired to the show’s
question-posing system. He was incapable of doing an autonomous task
that any three-year-old could do: listening for the host to finish a
question before buzzing in"

---


Sounds like bunch of unnecessary pain.. Test based restrictions are
excessive.. Left over policy from beginning of pandemic.

TDB: "On the day my wife and I were to fly home from London after a
brief visit, we took a COVID-19 test.. My wife’s test was negative. My
test was positive. She flew out.... So I was looking at 10 days of
hotels, which are not cheap in London. It’s not as if I can call a
friend here and say, “Hey, I got covid. Can I crash on your living
room sofa?”

[Gets covid] My symptoms quickly went away, and after four days I felt
fine again... But, now, how do I get back? Here’s the problem. There
is a chance that some little piece of the virus remains in my body. So
if I take another test and it’s positive, I’m stuck here again—with no
symptoms except a bleeding wallet"

---

CNBC: "Charlie Munger warns Gen Z investors.. 'It’s going to be way
harder for the group that’s graduated from college now ... to get rich
and stay rich,' Munger, 98, said. 'Think what it [used to] cost to own
a house in a desirable neighborhood in a city like Los Angeles.'"

---

Besides the need to provide bed-time stories for their shoddy
nation-building, Asia Minor Turkist propaganda was useful for British
interests; they could use it as a cudgel for the continuation of the
Great Game in Asia, eg if you can create an illusion of unity between
TR and "the Stans", some of which are "ethnically similar", u could
then be provoke those countries against their immediate neighbor.

But the act is getting old.. Plus TR's problems compound whose very
foundation was crooked (that's what you get with second rate
founders). People live in a bastardized world of their true culture
which is incompatible with national narrative that constantly leads
them astray, or at best, keeps them stagnant which is the case today
(middle-income trap). 

---

Because US was caught doing undemocratic shit, its protests on the
Egyptian coup registered less. The revelations might have even given
Sisi the PR cover he needed for the coup.

---

Timeline reminder

June 2013: An NSA contractor Edward Snowden starts sharing gov secrets
with the media. Americans learn that their government was spying
broadly on its own people.

July 2013: A military coup in Egypt removes President Morsi from
power.

---

Looking at the map, Philippines would be key for the outers to contain
China.. But what happens after Duterte?

"U.S., Philippines Hold One of Their Largest-Ever Military Exercises"

---

Orban wins again. He is lambasted on immigration, but on process we
have to accept forcing countries to accept new people if their
democratically elected government does not agree would be
undemocratic.

---

FT: "China has reaffirmed its partnership with Russia in the wake of
the Ukraine invasion and says it wants to push bilateral relations 'to
a higher level'"

---

NYT: "Syrian mercenaries deploy to Russia en route to Ukrainian
battlefields Hundreds of Syrian fighters are en route to join Russian
forces in Ukraine, effectively returning the favour to Moscow for
helping President Bashar Assad crush rebels in an 11-year civil war,
according to two people monitoring the flow of mercenaries"

---

Moldova is NATO-friendly? If they were opportunistic they would give
Russia access for Western Ukraine in return for Odessa Oblast.

---

TBH Ukraine had ownership of some prime land that was beyond its
capacity to hold onto. They needed massive deterrence, or major
forsight on diplomacy to make self less threathening to others
(RU). Ukraine had neither.

---

Moldova was screwed, historically speaking; had zero sea access until
2005, now have a *tiny* port, and had to trade land with Ukraine to
get it. Reminds me the bitch borders of Iraq drawn up by Western
powers..  Sad.

In a natural evolution of borders Moldova would have the land reaching
all the way to the Black Sea, areas currently belong to Ukraine.

[[-]](https://pbs.twimg.com/media/FPZe1sNXoAcqpvu?format=jpg&name=small)

---

Immediate UKR south is in danger being closed off to sea access for
Ukraine. No wonder Odessa is being attacked.

---

The map suggests a possible region for attack would be that pocket
shown with arrow, and yes, Severodonetsk, Rubizhne, Lysychansk,
Kreminna, Hirske, Popasna Berezove, Toshkivka - all being shelled. If
RU takes the region the red block will get bigger.

[[-]](https://pbs.twimg.com/media/FPZVQEpWYAE1r0R?format=png&name=small)

---

MSM is not even providing Liveuamap level reporting here. See the red
regions in the map. Those are RU areas; not newsworthy? 

[[-]](https://pbs.twimg.com/media/FPZWhNmX0AQ7ALF?format=png&name=small)

---

Watching the corporate media you'd think Ukraine is winning big, if
there was just some extra hardware, they'd finish the war today

---

*The Contractor*, not bad

---

H2 View: "Yara to boost the hydrogen industry with the creation of [a]
carbon-free ammonia fuel bunker network"

---

H2 View: "Lidl puts 98 green hydrogen-powered warehouse trucks into
operation in France"

---

H2 View: "Nel continues to back hydrogen refuelling infrastructure
with orders in Poland and Canada"

---

H2 Fuel News: "The research team [at Cornell] developed a nitrogen-doped,
carbon-coated nickel anode for use as a catalyst."

---

Sri Lanka has massive solar potential with mad DNI. They could be
generating renewable fuel instead they are in queues waiting for
fossil. 

---

They had a seperatist group Tamil Tigers.. A coworker of mine was from
Sri Lanka and Tamil Tiger symphatizer. The group was defeated later, I
looked it up now, in 2009, with 40,000 ethnic Tamils dead throughout
the conflict. Is Sri Lanka getting some karma blowback here?

---


"How Sri Lanka Has Fallen Into Darkness..

April is the hottest month in Sri Lanka. Just unbelievably hot, like a
fever that doesn’t break until the rains. Heat makes everybody cranky,
irritable, and I suppose violent. April is the cruelest month, as they
say.  This is the worst April in Sri Lanka’s history. I don’t mean
that worse things haven’t happened—we’ve had pogroms, a tsunami,
various insurrections, a good thirty years of war—I just mean this
catastrophe is happening to all of Sri Lanka, all at once. No one is
safe from this disaster. It affects every single home.  At a very
fundamental level, the island has just fallen into the sea...

Why did this happen? Many reasons, and one family (the Rajapaksas).
Sri Lanka was an ancient irrigation civilization and in modern times
50% of our electricity comes from water (hydro). However, after
‘liberalizing’ in the 1980s we stopped building anything
useful. Instead we built giant generators that burn fucking oil for
the rest of our needs. This has been a farce forever. Now it’s a
tragedy.  Now we’re run out of oil for this generator, foreign capital
flows have dried up, and the whole thing has been managed
abysmally. The ruling family’s elder brother ran up the credit card a
decade ago and now the younger brother is paying off those commercial
bank loans instead of providing for our families.  And so the entire
country has blackouts, every day, for hours at a time. The entire
country waits in petrol and diesel queues"

[[-]](https://indica.medium.com/how-sri-lanka-has-fallen-into-darkness-9e2d76f071bd)

---

<img width="340" src="https://pbs.twimg.com/media/FPDNAgbX0Ao5YMC?format=jpg&name=small"/>

---

A good summary on how the world soured on the dollar, bit by bit, even
the Europeans (after DJT Iran deal cancellation).

[[-]](https://inews.co.uk/news/long-reads/russia-china-us-dollar-undermine-change-world-cryptocurrency-1548200)

---

There is a sequel too.. In this one Bruce Wayne decides to lobby the
government for his tax dollars to be spent more on social help, less
on stop-and-frisk bust-head-and-crack-skull approach mostly used in
Gotham. The sequel is titled "*Batman: Defunding the Police*". It
works, Joker, Two-Face get bored after a while, they declare they wont
show up for the whole trilogy, or even the prequels. 

---

Batman movies could be much shorter.. Bruce Wayne sees lots of crime,
then he thinks about what to do.. he think.. thinks.. while the camera
moves closer; the last scene is a near shot on BW when he says "I
guess I should pay my taxes". Done. The movie ends.

---

The saddest part in the Batman movies is when they lit up that 'bat
sign', essentially making city gov look like bufoons; the
establishment sales pitch here is "wouldn't an ultra-rich twat be
better to save your ass then the elected government?"

---

The gun is symbolism for a dick basically

---

It was [another time](https://pbs.twimg.com/media/FPPRIWWWUAcqYd7?format=jpg&name=small)

---

Damn Clint! (at the end). He probably feels different about that stuff
now

"@rafaelshimunov

1973: Native American actor Sacheen Littlefeather boo'd (and cheered)
by Hollywood at the Oscars.. asking that Indigenous people not to be
dehumanized in film"

[Video](https://twitter.com/rafaelshimunov/status/1447570025494327300)

---
