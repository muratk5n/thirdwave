# Week 9

Physics is in dire straits. No one should underestimate how bad things
are.

---

America oscillates between two extremes, either too industrious
(getting shit to work), or too dreamy (a distant walhalla, gold rush,
dot.com). Industrious gets you "shut up and compute" of quantum
mechanics ignoring every bizarreness of it, dreamification gets you
stupidest theories presented as real physics many worlds, multiverses,
string theory among others. There doesn't seem to be a middle point
between the two extremes, as in conceptually sound and wide-reaching
base formulations that will explain experimental results. Eurasia
would not get mired in this bullshit if they were in the driving
seat. We've lost precious time with the New World.

---

The native culture of the land, pushing its inhabitants to incessant
dreamification probably did not help.

---

The sci rut started either 50 or 100 years ago, I still blame US for
the current state of science. They've been the stewards of the
bleeding edge research since WWII.

---

Masse: *Nature of Physical Fields and Forces*: "Newton’s force law can
be used to derive Poisson’s gravitational field equation. Moreover,
since Newton’s force law of gravity is not a function of time,
Poisson’s field equation of gravity only applies to gravitational
fields that are stationary. Therefore, Poisson’s field equation of
gravity and Newton’s force law of gravity must be mathematically
equivalent for a stationary gravitational field... The physical
interpretation of Poisson’s field equation of gravity is, however,
very different from the physical interpretation of Newton’s force law
of gravity. Rather than the action-at-a-distance interpretation of
gravity obtained from Newton’s force law of gravity, Poisson’s field
equation is based upon and must be interpreted in terms of the
existence of a physical medium consisting of contiguous particles
about any material body [aether!]"

---

Having a proper imperial past that descends from a militocracy would
help to get the right context on Ukraine, Georgia, Syria.. Empires
care about their borders, "what I control" vs "what the other guy
controls". You worry abt "trouble at the far flung edges" they can
spread and reach the middle. When I read my history I see statements
like "words of unrest reached [from a distant outpost] Sublime Porte
(the Otto palace), and they mobilized in a hurry". It is that "oh
shit" moment that many do not get. We are alert, borders have been
fought over for centuries, shed blood over.. This is not some
"McDonalds franchise" where you worry about "market share" and all you
care about is parachuting into some country beyond the border to open
a store there, and start selling products. The border is
life-or-death.

---

Many in US have trouble relating to conflicts around the world IMO
because you've never been a proper empire. You are not one now, and
you've never been. The short amount you were ruled by an Anglo king
does not count, you need a continental king for the proper experience.

---

HuffPost: "House Adopts Republican Budget That Calls For Medicaid Cuts"

---

TDB: "Trump Rescues Johnson From Humiliating Vote Flop After GOP
Chaos.. In the days leading up to the vote, several moderate GOP
lawmakers also voiced reservations, worried that the resolution could
impact key entitlement programs such as Medicaid, Pell Grants, and
SNAP. Ultimately, leadership was able to sway them by assuring that
these programs would remain untouched"

---

CNN: "The United States joined Russia to vote against a UN General
Assembly resolution condemning Russia’s war against Ukraine Monday in
a stunning shift from years of US policy"

---

Onshoring, reducing immigration will help, but won't be enough.

---

Pro-business anti-government policies are useless. Growth will remain
meager, asset prices will go through the roof unless inequality is
addressed. The rich needs to be taxed at higher rates. US needs a new
New Deal.

---

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/114/059/969/209/830/627/original/bd0faf1198db4a5b.jpg'/>

---

"@evanchaney@mastodon.social

Apple’s #privacy policy for #Siri now says Apple can retain
transcripts of and related inputs to your interactions with Siri for 2
years or more. The “Delete Siri & Dictation History” button only
deletes _local_ copies of your transcripts. The only way to opt out is
to turn off both Siri and dictation"

---

UAS Weekly: "Heven Drones introduces its latest hydrogen-powered UAV,
the Raider, at IDEX 2025, featuring a 1,000 km range and 10-hour
endurance"

<img width='340' src='https://files.mastodon.social/cache/preview_cards/images/134/204/087/original/63d6bd16cf373118.jpg'/>

---

Lookie. Orban misses Merkel.

[[-]](https://www.youtube.com/embed/7DaVBp3IUO0?start=1998&end=2089)

---

There was an internal power struggle in the CDU years ago, and today's
chancellor-to-be Merz was ousted by Merkel. The wording at the time
was he was "cut down at a young age", "executed". Now he is back bcz
Merkel is out, you see? Dude might have nursed some anger since; if he
tries to be the un-Merkel bcz of it, that's would be dumb. The
immigration issue aside, AM had the right approach towards the
East. She was an "Ossie" herself.

---

Merz wants to "lead Europe" for a massive UA aid package so they can
continue fighting?

---

"Steve Bannon warned Republicans that cutting Medicaid would hurt
Trump's base, as many MAGA supporters rely on the program"

---

Politico: "Republicans [David Valadao, Ken Calvert, Mike Lawler,
Pennsylvania’s Robert Bresnahan, Dan Newhouse] have a lot to lose if
Congress cuts Medicaid.. GOP lawmakers expected to vote soon on
slashing the insurance program for low-income people represent tens of
millions reliant on it"

---

[Link](https://www.youtube.com/embed/1b9EZBYqibs?start=81&end=116)

---

I remember the Oval Office press briefing for the announcement, guess
who was there to shower BHO with praise and receive his munee - the
same melon headed son of a bitch we like to dislike - Netanyahoo.  The
linchpin of MILC, military-industrial-Likud-complex.

---

👇 👇 👇 

Reuters: "[2016/09] U.S., Israel sign $38 billion military aid
package"

---

They must have scared Bama so badly he kowtowed to MIC until the last
second of his admin.

---

BHO admin started fine but capitulated midway, they got scared, gave
in. Trump era shows a tug-of-war between MIC and WH, we'll see how
things work out this time around.

---

Looking at the graph it is clear after 2012 MIC had a bonanza (Syria,
Libya, overall unrest in ME). Higher upward trend seen beginning 2017
but meager growth between 2018-2020, steep fall at 2020 is
understandable, but steady upward trend continued thanks to bought out
officials doing MIC's bidding on Ukraine and other places, like Tony
Blink Blink 737, and "Raytheon Lord" Austin. Biden obviously had his
own "entanglements" in Ukraine.

---

```python
tickers = ['RTX','LMT','BA','GD','NOC']
df = u.get_yahoo_tickers(2000,tickers)
cap = {'RTX':157.5,'LMT':122.4,'BA':115.7,'GD':76.3,'NOC':70.6}
recent = df.tail(1).to_dict("records")[0]
df_cap = df * dict((x,cap[x]/recent[x]*1e9) for x in tickers)
df_cap.sum(axis=1).plot(title='MIC Combined Market Cap')
```

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/114/057/775/435/730/965/original/f30428ed5f338f9f.jpg'/>

---

Macron - Trump meeting, and no one got handcucked this time? Very
strange.

---

😂 Let's not go there

"Is there anything more German than our old pure Austrianness?"

---

Hear it from the Austrian military, Markus Schwarzenegger explains it
all \#AustrainMil \#Ukraine

[[-]](https://www.youtube.com/embed/IDRjughhXMg?start=1019&end=1069)

---

Eventually they will take it all back. But it doesn't matter when imo,
RU kills Ukrainian soldiers over there, or kills them over somewhere
else... their strategy is the same, is one of de-militarization,
removing UA as a threat.

Reuters: "Russia says it has taken back major chunk of Kursk region"

---

Rail Journal: "Italy's first hydrogen train on test.. The Alstom
Coradia Steam H train is undergoing refuelling trials at Rovato"

<img width='200' src='https://cdn.railvis.com/hub/news/IMF1RK0ZLKQHHAPF.jpg'/>

---

"@cnbusinessforum@mstdn.business

[\#TRADESHOW] The 3rd #World #Hydrogen #Energy #Industry #Expo (#WHE
2025) will take place from August 8–10, 2025, at the #China #Import
and #Export #Fair Complex (Area A) in #Guangzhou"

---

"Ohio transit agency to switch to green hydrogen for fuel cell buses"

---

The Korea Herald: "Seoul to offer increased subsidy for
hydrogen-powered buses from March"

---

Interesting Engineering: "Honda hydrogen fuel cell with 3x power
density to boost car performance"

---

The New Stack: "According to the federal government, WebAssembly could
and should be integrated across the cloud native service mesh sphere
to enhance security... The use of WebAssembly could become mandatory
to meet security-compliance requirements while solving other ongoing
security conundrums as Wasm becomes more widely adopted"

---

I was joking abt the Justin Baldoni thing earlier. He was most likely
unjustly blamed, is the real victim, the target of a Me Too type of
smear campaign.

---

Carrier Strike Group near Greece?


```python
u.map_usnavy(outfile="map03.html")
```

[[-]](map03.html)

---

Market Screener: "[US] administration is piling pressure on Iraq to
allow Kurdish oil exports to restart or face sanctions alongside Iran,
eight sources with direct knowledge of the matter told Reuters. A
speedy resumption of exports from Iraq's semi-autonomous Kurdistan
region would help to offset a potential fall in Iranian oil exports,
which Washington has pledged to cut to zero as part of Trump's
'maximum pressure' campaign against Tehran."

---

D'Alembert's Principle? Also a restatement of the second law.

---

How did I find about Richard Masse's work? I was looking for a way to
explain how to derive the Lagrangian form of least action, the famous
$T - V$ formula from basic principles. I saw a derivation starting
from $\int mvds$, Euler's method, they call mass times velocity times
distance as "action", based on Maupertuis. But neither method sound
fundamental.  Feynman does a great job motivating $T - V$ in his
lectures (Vol II), he articulates extremely well why he thinks the
method works, but he is essentially putting lipstick on a pig. He is
rationalizing, the choice of this particular formula is arbitrary. It
is pulled out of the air, in a "let's see if this works" kind of
experiementation (obviously it did), explained later.

Then I searched for books on the subject, Masse's came up.  His
approach was Newton's second law is more fundamental, derive
Lagrangian from there, but still, not fundamental enough. This is
where his eather formulation comes in, he can derive the second law
from it.

---

BMW Blog: "Toyota’s 3rd-Gen Fuel Cell: The Tech That Could Power BMW’s iX5 Hydrogen"

---

Ash Sarkar: How WOKE Politics is DESTROYING the Left!

[[-]](https://www.youtube.com/embed/zo3URITmjsQ?start=609&end=861)

---

"@cdarwin@c.im

German newsmagazine Der Spiegel reported that the Max Planck Society
one of the world’s top scientific research institutions is
experiencing an uptick in applications from American scientists. [Its
president said the society regards the U.S. as 'a new talent pool' at
a time when the Trump administration seeks to cut billions in funding
to the National Institutes of Health.

There’s a deep historical irony in these recent developments: During
the Third Reich, it was the Max Planck Society then known as the
Kaiser Wilhelm Society that lost its best and brightest to the
U.S. and other countries"

---

Politico: "As Eric Adams melts down, Andrew Cuomo forges ahead.. The
former governor has put together the structure of a campaign and is
courting New York power players"

---

"@EndIsraeliApartheid@mastodon.social

The BBC has faced significant backlash following its removal of the
documentary 'Gaza: How To Survive A Warzone,' which focused on the
experiences of Palestinian children in the Gaza Strip"

---

The Guardian: "[2021] Literally meaning 'alternative-less',
*alternativlos* was Angela Merkel’s own version of a line usually
associated with Margaret Thatcher: 'There is no alternative.' But if
'TINA' was specifically used to close down debates over alternatives
to the market economy, Merkel’s government declared all type of policy
decisions *alternativlos*.. [eg open border immigration policy]. Her
use of the phrase also inspired the naming of the first party to the
right of her CDU to make it into the Bundestag: Alternative für
Deutschland [AfD]"

---

F24: "Germany's snap elections: CDU leads, far-right AfD set for
record gains"

---

Ash Sarkar: How WOKE Politics is DESTROYING the Left!

[[-]](https://www.youtube.com/embed/zo3URITmjsQ?start=609&end=861)

---

Sounds like a good plan so far

The New Arab: "Egypt’s diplomatic plan for Gaza's future is set to be
presented to US President Donald Trump after receiving approval at key
upcoming summits in Riyadh and Cairo... According to a high-ranking
Egyptian diplomat based in Washington, the initiative from Cairo
is divided into two phases, which are estimated to cost tens of
billions of dollars.

The first phase spans ten years and primarily focuses on rebuilding
Gaza's infrastructure, housing, and residential sectors. The plan
includes the redistribution of population clusters in Gaza,
particularly by easing the density of the population in northern Gaza
and creating less populated zones near illegal Israeli settlements.

The second phase, still open for Arab discussion and refinement, would
start the process of establishing a Palestinian state, focusing on
creating links between Gaza, the West Bank, and Jerusalem...

Another key element of the first phase is the regulation of
weapons. Cairo's approach seeks to address concerns from international
donors financing Gaza's reconstruction while respecting Palestinian
armed groups' demands of retaining their arms until a Palestinian
state is established...

Another crucial aspect of this stage involves the establishment of an
Arab-led committee, with Egypt at the helm, tasked with resolving
disputes between local security forces and militant factions"

---

Masse: "Having concluded that time in our Universe is a result of the
flow of aether into matter, we see that time cannot be modified in any
way (shortened or lengthened). Time is then uniform and absolute
throughout our Universe and is independent of the kinematic properties
and spatial position of any observer. Since absolute motion
(acceleration) exists in our Universe, it is to be expected that
absolute time must also exist.  Time is not relative, and time does to
alter with the motion of any reference system.

We see, therefore, that Einstein’s special theory of relativity, with
its kinematically dependent time, cannot be correct. We also see that,
while Newton was correct in postulating the existence of absolute
time, he was incorrect in assuming that such time is independent of
anything external.  Aether provides not only the absolute frame of
reference in our Universe, but also (together with matter) the
absolute time in our Universe. Time is not, then, a fundamental entity
of our Universe"

---

The Guardian: "Nigeria sues crypto giant Binance for $81.5bn in
economic losses and back tax..  Authorities blame Binance, the world’s
largest crypto exchange, for Nigeria’s currency woes and detained two
of its executives in 2024 after crypto websites emerged as platforms
of choice for trading the local naira currency"

---

The Huge Flaw in the Many Worlds Interpretation \#Barandes

[[-]](https://youtu.be/i1yAfpnErUU)

---

We need boring scifi. A new show can focus on truly unknown, but
knowable stuff.. One episode they can discover how gravity
works. Another fixes quantum mechanics. Forget abt these multiple
universes, time travel. Try to imagine how stuff works in one universe
with boring time (it only flows forward).

---

Who made this PDF? Two pages in one sheet, heavy graphics.. I had to
`ghostscript` to decrease image quality, then a little `mutool poster
-x 2 input.pdf output.pdf` to split pages in half. 

---

News 12: "Officials: Fire rips through high rise building in Melrose
[New York].. As of Jan. 30, there have been 12 fires and 3 injuries
due to lithium-ion batteries"

---

Politico: "China says it backs new US and Russian [consensus] on
Ukraine war"

---
