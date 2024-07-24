# Week 29


US industry needs to be encouraged to move away from MS OS to Linux
based OS as soon as possible. You are better off running LOS while
running existing Windows programs through an emulation layer. If there
are programs that have problems on emulation, MS can be forced to
open-source their code. This migration needs to be actively encouraged
by the government, especially for its own computing needs.

"@mjg59@nondeterministic.computer

'Linux would have prevented this!' literally true because my former
colleague KP Singh wrote a kernel security module that lets EDR
implementations load ebpf into the kernel to monitor and act on
security hooks and Crowdstrike now uses that rather than requiring its
own kernel module that would otherwise absolutely have allowed this to
happen, so everyone please say thank you to him"

---

Soya beans? This trade relationship looks like a rel between an
advanced nation and a third-world country. 

```python
top_product('USA','China')
```

```text
$ 17,924,895,224.0
Soya beans: other than seed, whether or not broken
```

---

What is the top export from China to US?

```python
top_product('China','USA')
```

```text
$ 48,530,501,546.0
Automatic data processing machines: portable, weighing not more than
10kg, consisting of at least a central processing unit, a keyboard and
a display
```

Basically a computer "not more than 10kg", that covers a lot of ground.
48 billions worth! 

---

Little more code.. 

```python
import pandas as pd, json, textwrap

cc = pd.read_csv(u.baci_dir + '/country_codes_V202401b.csv',index_col='country_name')
pc = pd.read_csv(u.baci_dir + '/product_codes_HS22_V202401b.csv',index_col='code')
p = json.loads(open(u.baci_dir + "/out-p.json").read())
v = json.loads(open(u.baci_dir + "/out-v.json").read())

def top_product(frc, toc):
    key = "%d-%d" % (cc.loc[frc].country_code, cc.loc[toc].country_code)
    print('$', f"{v[key]*1000:,}")
    s = pc.loc[int(p[key])].description
    for x in textwrap.wrap(s, width=70):
    	print (x)
```

---

```python
u.baci_top_products()
```

```text
elapsed time 0:01:43.950638
```

---

I had shared a trade network report using this dataset. How about top
products between any two country pairs? 

"BACI provides data on bilateral trade flows for 200 countries at the
product level (5000 products). Products correspond to the "Harmonized
System" nomenclature (6 digit code)"

[[-]](http://www.cepii.fr/cepii/en/bdd_modele/bdd_modele_item.asp?id=37)

---

"@simon@fosstodon.org

Nobody got fired for buying #Microsoft and #Crowdstrike ...

that's because the HR systems are down"

---

"@danderson@hachyderm.io

I'd just like to interject for a moment. What you’re referring to as
Windows is in fact Crowdstrike/Windows, or as I’ve recently taken to
calling it, Crowdstrike plus Windows. Windows is not an operating
system unto itself, but rather another component of a fully
non-functioning Crowdstrike system, made useless by the .SYS files,
automated updates and blue screens comprising a full outage as defined
by the news"

---

"@anguinea@mstdn.social

Here’s a crazy thought:

Since there actually is no plan B, let’s stick with plan A.

\#PollsAreBS"

---

Arab News: "Germany will halve military aid for Ukraine next year"

---

EurekAlert: "A research team.. at Korea Institute of Science and
Technology (KIST).. has developed an oxidatively stable
molybdenum-based MXene as electrocatalyst support in anion exchange
membrane water electrolyzers. As it is stable against oxidative high
voltage conditions, if it is applied as a carrier for electrolysis
catalysts, it can be used as an oxygen evolution reaction electrode
material for green hydrogen production to reduce the cost of green
hydrogen production"

---

<img width='200' src='https://s3.ap-southeast-2.wasabisys.com/aussocial/media_attachments/files/112/812/497/133/648/966/small/25a5aba8e013b69f.jpg'/>

---

"@jaztrophysicist@sciences.re

A single software update bug caused by a capitalistic monopoly can
singlehandedly paralyse the whole international economy and provoke
financial panic, but sure the main risk for economic stability is
moderate left-leaning parties who want to impose a 20% tax on the rich
to fund social, health, ecological care and education"

---

"@danderson@hachyderm.io

Happy Friday, hugops to Crowdstrike, Azure, Microsoft, and uh every
fortune 1000 it would seem.

Big skynet vibes tbh, I'm kinda surprised that _more_ stuff isn't on
fire. Not yet, at least"

---

via @fuck_cars_bot@botsin.space

<img width='340' src='https://files.botsin.space/media_attachments/files/112/787/651/554/666/771/small/f1393537eb64536b.jpeg'/>

---

"@GossiTheDog@cyberplace.social

My laptop is currently idle. MDE process (`MsSense.exe`) is using 2316mb
of RAM"

---

H2 Central: "New hydrogen storage facility in Hamburg Metropolitan
Region. Storengy Deutschland announced Tuesday (June 11, 2024) plans
to build new underground caverns to store up to 15,000 tonnes of
hydrogen in Hersfeld"

---

<img width='200' src='https://rollenspiel.social/system/media_attachments/files/112/800/722/169/654/374/original/bc08ad4e5b76eab6.jpg'/>

---

I would not be surprised.. there is a lot money involved in that
[racket](https://cdn.fosstodon.org/media_attachments/files/112/811/480/690/795/566/original/5d00be1a26e69b39.jpeg),
people have killed others for less.

WION: "Ukraine could try to kill Trump.. [wrote] an exiled Ukrainian
politician who currently lives in Russia.. [Medvedchuk] was handed
over to Russia as part of a prisoner swap. He was the leader of
Platform For Life party, which is now banned in Ukraine"

---

CNBC: "A growing number of parents are refusing to give their children
smartphones — and the movement is going global"

---

CNBC: "Labour's gains in London have private equity looking to exit —
the country.. With the British parliament back from recess, the UK’s
Labour Party will start working to push through aggressive changes,
including controversial proposals that would force the rich to pay
more in taxes"

---

"@GossiTheDog@cyberplace.social

There’s finally some reviews of a Copilot+ laptop on Amazon"

[[-]](https://cyberplace.social/system/media_attachments/files/112/798/593/412/489/548/original/77aef8544ccadce1.png)

---

Noah Smith, Bloomberg: "[2017/12] It's pretty well known that
U.S. workers have lost a lot of bargaining power over the past few
decades. Wage gains, for example, haven’t kept pace with rising
productivity:

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/112/806/469/071/803/959/original/42da51bcebfce68b.jpeg'/>

Clearly, workers have been unable to take home a fair share of the new
value they were creating. Why? One big potential culprit is the
decline of labor unions"

---

Politico: "Scared to Death’: GOP Security Hawks Slam Vance
Selection.. By choosing the Ukraine-skeptic Ohio senator, Trump
accelerates his party’s rejection of its Reaganite roots.

---

\#Frontline \#RU \#UA 07/10 - 07/18

[[-]](ukrdata/map27-ext.html)

---

NYT: "Israel in Talks Over Withdrawing From Egypt-Gaza Border,
Officials Say"

---

Al Monitor: "Flies and mosquitoes feast on Gaza's waste crisis"

---

"@OhOkKay@beige.party

Finding out that most tea bags are about 20% plastic, last night I cut
open my tea bags and brewing it loose.  Wow! What a difference in
flavour. So much better. Will being doing this more often!"

---

"Why Americans Are Nuts About Peanut Butter... First of all, the
United States grows a ton of peanuts. .. Growing peanuts became a big
thing in the early 1900s when the cotton crop was suffering in the
South, and we still grow a lot of peanuts today. Peanut butter’s birth
year explains our obsession even more. In World War I, the Great
Depression, and World War II, America was in search of inexpensive,
filling, and nutritious ways to feed its people. So people turned to
peanut butter, and it stuck. Peanut butter sandwiches were given out
in food lines during the Great Depression and were part of Army
rations in both World Wars"

---

"Americans consume [on average] about twenty-two tablespoons [of
peanut butter] per person per year... Europeans on average consume
less than one tablespoon.. per person annually"

---

Do they *have* to eat peanut based products? America is so coo coo
about peanuts some ppl not being able to eat it sounds scandalous.

NBC News: "Early treatment could help ease peanut allergies in young
kids"

---

[Link](https://www.dropbox.com/scl/fi/xnvs40x81zlntzqifxgd3/tombstone_1.gif?rlkey=4fakmjulq11ue1lmi40ioev7m&st=5cqmssqz&raw=1)

---

Because both he and Kurt Russell played in two different movies about
Wyatt Earp and his movie sucked, Russell's movie *Tombstone* did
great. Costner might be jealous, he keeps making Westerns until he
makes a movie at the same level of *Tombstone*.

"Why does Kevin Costner keep making westerns?"

---

Battles around Bakhmut were an example of AW. The fact that the
frontlines "did not move" for a long time was on purpose, not due to
RU shortcomings. At one point the Wagner chief -while still alive-,
was commenting "well we could dash ahead and take Kramatorsk". But
rushing ahead taking shit is not the point.. Clearly the guy did not
get the memo. RU battle plan was about degrading UA's ability to make
war. Wag chief as a bidnessman was probably looking at the theather
like a market to incrase his share in, "I can open a corner sandwich
shop over there, I can expand..". But the RU top brass had a different
plan. He was asked to execute on a portion of that plan. He failed
(then he was died).

---

Vershinin: "[2024/03] The Attritional Art of War: If the West is
serious about the possibility of a great power conflict, it needs to
take a hard look at its capacity to wage a protracted war and to
pursue a strategy focused on attrition rather than
manoeuvre. Attritional wars require their own ‘Art of War’ and are
fought with a ‘force-centric’ approach, unlike wars of manoeuvre which
are ‘terrain-focused’. They are rooted in massive industrial capacity
to enable the replacement of losses, geographical depth to absorb a
series of defeats, and technological conditions that prevent rapid
ground movement. In attritional wars, military operations are shaped
by a state’s ability to replace losses and generate new formations,
not tactical and operational manoeuvres. The side that accepts the
attritional nature of war and focuses on destroying enemy forces
rather than gaining terrain is most likely to win...

Only after meeting these criteria should offensive operations
commence. They should be launched across a broad front, seeking to
overwhelm the enemy at multiple points with shallow attacks. The
intent is to remain inside a layered bubble of friendly protective
systems, while stretching depleted enemy reserves until the front
collapses. Only then should the offensive extend towards objectives
deeper in the enemy rear. Concentration of forces on one main effort
should be avoided as this gives an indication of the offensive’s
location and an opportunity for the enemy to concentrate their
reserves against this key point. The Brusilov Offensive of 1916, which
resulted in the collapse of the Austro-Hungarian army, is a good
example of a successful attritional offensive at the tactical and
operational level" via Col. Daniel Davis, Jacques Baud

---

Politico: "King Charles III unveiled the new U.K. Labour government’s
packed policy agenda Wednesday. It’s not going to make everyone
happy... Starmer’s agenda features big ticket items including a
shakeup of planning laws to trigger.. infrastructure investment, the
establishment of a publicly-owned energy company and a plan to bring
failing privatized railway networks back into public ownership"

---

"@ashleygjovik@mastodon.social

Let’s warm up with some of Apple’s very basic failures. Apple's
facility [in Santa Clara which they fired Gjovik complaining to gov
about] has extremely toxic gases that'd create a Bhopal-like
disaster. Apple says its env friendly & thoughtful, so Apple must have
constant monitoring? Except if the power goes out. Then all the alarms
shut off"

[[-]](https://mastodon.social/@ashleygjovik/112788551287662863)

---

*Knox Goes Away* good movie.

---

Gary Clark Jr. - Don't Owe You a Thang \#music

[[-]](https://youtu.be/t0MEODXMMrU)

---

"[The company] Savor makes delightfully rich foods without animals,
farmland, fertilizers, hormones, or antibiotics... Fat has a
recipe. We start with a source of carbon, like carbon dioxide [from
air], and use a little bit of heat and hydrogen to form chains which
are then blended with oxygen from air to make the fats & oils we know,
love and drool over. That’s how we get rich, delightful ingredients
without animal suffering, palm plantations, or dangerous
chemicals. All in the most efficient, most resilient, least polluting
way known to science"

---

Power is transmitted over dinky electrical lines.. Energy could be
transmitted via sturdy, strong (clean gas, H2) pipelines that can
provide energy ten times faster at eighth the cost.  We need to defund
the grid.

---

AP: "The storm slammed into Texas on Monday, knocking out power to
nearly 2.7 million homes and businesses and leaving huge swaths of the
region in the dark and without air conditioning in the searing summer
heat"

---

USSR was aiding the rebels while the west was supporting
apartheid.. they later changed their minds but for a while the west
was on the wrong side. 

The Conversation: "The [South African] ANC and the former Soviet
Union have a long history together. The first visit by an ANC leader
to the Soviet Union was by Josiah Tshangana Gumede, one of the
founding members of the ANC, in 1927...

After the apartheid regime was banned the ANC in 1960 it received aid
from the Soviet Union for its exiled mission in the fight to liberate
South Africa from minority white rule. This aid exceeded that from the
pan-African Organisation of African Unity- now the African Union - or
anyone else.

It was only from the end of the 1970s that [other] donations became
higher than Soviet funding.. [but o]nly the Soviet Union provided
weapons and other military aid to the ANC’s armed wing"

---

CleanTechnica: "Hydrogen Fuel Cell eVOTL And Jets Are Coming For Your
Fossil Fuels"

---

Hydrogen-Powered Air Taxi.. In a significant milestone for sustainable
aviation, a hydrogen-powered air cab has completed an 842-kilometer
flight.. Joby is one of several companies at the forefront of creating
air cab services using vertical take-off and landing (VTOL)
vehicles. Initially, the company focused on developing all-electric
aircraft with a range of approximately 160 kilometers, intended for
urban and intercity transport. Joby recently adapted a prototype of
its electric aircraft to operate on hydrogen. Equipped with a liquid
hydrogen tank and a fuel system, the modified VTOL successfully
completed a flight of 842 kilometers over Marina, California, using
only 90% of its hydrogen fuel load.

<img width='340' src='https://omniletters.com/wp-content/uploads/2024/07/Hydrogen-Powered-Air-Taxi.webp'/>

---

Techcrunch: "Tesla reportedly delays ‘robotaxi’ event to
October.. Tesla is apparently not ready to reveal its “robotaxi”
design next month, and is instead pushing the event to October,
according to Bloomberg News.. The company reportedly needs more time
to build the prototypes. It had been aiming for an August 8 event. The
company did not immediately respond to a request for comment. Tesla
shares fell more than 6% following the report"

---

"@RadicalGraffiti@todon.eu

Poster seen in Pullman, Washington"

[[-]](https://todon.eu/system/media_attachments/files/112/793/163/287/716/804/original/02b0b9a06e928268.jpg)

---

\#NATO \#Lottaz \#Freeman

[[-]](https://youtu.be/EDONLsCGmZw?t=1863)

---

CNBC: "Treasury, IRS announce 'major milestone' of $1 billion in
past-due taxes collected from millionaires"

---

Anatolian Agency: "Putin says BRICS may establish its own parliament in future"

---

The National: "Jeremy Corbyn 'in talks' with SNP over 'left-wing alliance'"

---

"@ben@werd.social

The news cycle has moved on, but just as a reminder, they’re still
bombing the shit out of Gaza and killing civilians in enormous
numbers"

---

Al-Monitor: "Hamas says pulling out of Gaza truce talks, as Israel
keeps up strikes"

---


Nutella said, back in 2015, "Microsoft's new computerized goggles,
HoloLens are the new desktop". You can find this reference on Business
Insider.

It's not just him, Bill Gates wrote a book with the title THE ROAD
AHEAD (1995) and it completely missed the Internet boom that would
follow in a few years. Let alone the road ahead, the book could not
see in front of its nose.

Gates did a little better after his CEO stint, maybe there's something
blinding about being a tech CEO. You are too mired in the market, your
market share, sales, every thought has to be shaped in service to
that, and they miss the general trend. They are easily gripped by
FOMO, blinded by hype.

---

Tadella Nutella said in 2021 "cannot overstate what a breakthrough
metaverse is" (via Zitron w/ Connover). 

---

That's not exactly a yardstick to judge any tech by, neither this CEO
or previous ones were really good about predicting tech future.

"If [so-called] AI was not a big deal why is Microsoft CEO so excited about it?"

---

AP News: "Federal judge dismisses Trump classified documents case"

---

TASS: "Biden apologizes for his call to put Trump 'in the bullseye'"

---

Good pick.. JD is good on Ukraine, economy, immigration, he is young
can carry Trump legacy forward.

---

AP News: "JD Vance is Trump's vice president pick"

---

Truthout: "[Passenger] describes how Delta Airlines threatened to kick
him off a plane over his 'Jews Say Ceasefire Now' T-shirt...

'My T-shirt displayed the text "Not in Our Name" on the front side and
"Jews Say Ceasefire Now" on the back... Before the flight had even
taken off, I was approached while I was seated on the plane by a
flight attendant who requested that I either change or cover up my
shirt because some passengers found the message offensive.. I
requested that the people who had complained about the nature of my
shirt come talk to me directly..

About 5 to 10 minutes later, a purser (also known as a chief flight
attendant or cabin manager) came to my seat and explained that I had
to cover up the shirt, because Delta had a policy against showcasing
political messages of any kind. I once again refused to cover up the
shirt. The purser then threatened to kick me off the flight unless I
obliged her wishes. Because I wanted to get to my destination, I
covered up the "Jews Say Ceasefire Now" shirt for the time being with
a nondescript white shirt. The flight took off'"

---

The Conversation: "Israel has reportedly approved its largest seizure
of land in the occupied West Bank in over three decades, according to
a report released on July 3 by Israeli anti-settlement watchdog, Peace
Now. The seizure involves more than 12 sq km of land in a key corridor
bordering Jordan.

Land that is privately owned by Palestinians in the West Bank can be
declared as 'state land' by Israel and subsequently seized. One of the
primary outcomes is the establishment or expansion of Israeli
settlements on the land, which are widely considered illegal under
international law"

---

"@ItsTrainingCatsAndDogs@kolektiva.social

Whoooooaaaa. Israel is attacking like crazy right now while everyone’s distracted"

---

F24: "Israeli strike on Gaza 'safe zone' kills more than 70, officials say"

---

The American Conservative: "'In Trump’s first term [his] realist
impulses were muted and sometimes stopped by hawkish national security
staffers who did not share his vision. But having learned that
personnel is policy, Trump will not make this mistake again'

So write Andrew Byers and Randall Schweller in *Foreign Affairs*.
Schweller, an academic at Ohio State, is a card-carrying foreign
policy realist, and is willing to put his name to a claim that we have
argued in these pages all along: Donald Trump, despite his mercurial
nature and despite the opposition from entrenched interests in
Washington, DC, is fundamentally displaying a realist instinct in his
foreign policy... [he writes] 'an "America first" agenda is an
intellectually defensible, fundamentally realist program that seeks to
ascertain and act on the United States’ national interests rather than
the interests of others'"

---

An anti M&A mindset! We can't have that!

FT: "Vance.. has been among the loudest Republican voices opposing
more US aid to Ukraine... But it is Vance’s [economy views] that has
divided the business community...

'He represents something in the country that the coastal elites and
big business have taken too long to recognise,' [a bank] lobbyist
added, in an apparent reference to Vance’s ability to channel the
anger and disenfranchisement of the working classes...

Vance has espoused a protectionist trade policy, stricter immigration
laws, higher minimum wages and a more aggressive approach to antitrust
enforcement. He made headlines earlier this year when he described
Federal Trade Commission chair Lina Khan as one of the Biden
administration officials 'doing a pretty good job'...

Those kind of comments have concerned investors in particular. One top
New York dealmaker said picking Vance as vice-president 'would not be
reassuring to the business community, and could signal an anti-M&A
mindset for the second Trump administration'"

---

Spicy

"Ohio Sen. JD Vance, a top VP contender, blames Trump rally shooting
on Biden 'rhetoric'"

---

Shooter is registered Rep?. Sounds like an extreme non-MAGA
type. After recent Biden mishaps he could have lost hope and took
matters in his own hands..  to the extent a dill weed 20 yo could of
course.

---

NBC News: "Frenzied Democratic effort to replace Biden comes to a
standstill after Trump rally shooting"

---

I'm glad. The event will help Biden a little taking focus off him. But
it will help DJT more, now there is an iconic image associated with
the event, he looked like a warrior, bloodied, while fighting against
forces arrayed against him.

Reuters: "Trump survives assassination attempt at campaign rally"

---
