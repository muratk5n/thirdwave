# Week 9


Business Green: "UK Infrastructure Bank makes first green hydrogen
investment.. Public investment bank announces £30m of funding for
hydrogen power unit maker GeoPura The UK Infrastructure Bank (UKIB)
has announced its first ever green hydrogen investment, confirming a
£30m investment in a manufacturer of hydrogen power units.

The deal forms part of a £56m fund raising round completed by GeoPura
to support the roll out of hydrogen power units that can replace
emissions-intensive diesel generators. GeoPura is aiming to deploy a
fleet of more than 3,600 hydrogen power units by 2033 from its hubs in
Nottingham, Matlock, Sheffield, and Newcastle. The firm is also hoping
to become a supplier of renewable hydrogen, as part of a joint venture
with JG Pears to undertake green hydrogen production at the site of an
old power station in the East Midlands.

---

Nobel Prize–winning economist Gary Becker's mentor was Milton
Friedman. And Becker was a mentor to the junk bond felon Mike
Milken. Dam cuh

---

Even Swedes got in on the action.. 

Africa News: "[2023/09] Two former executives at a Swedish oil company
go on trial in Stockholm on Tuesday accused of complicity in war
crimes committed by Sudan's regime between 1999 and 2003. Swede Ian
Lundin and Swiss national Alex Schneiter are accused of asking Sudan's
government to make its military responsible for security at the site
of one of Lundin Oil's exploration fields, which later led to aerial
bombings, killing of civilians and burning of entire villages,
according to the prosecution"

---

"[2001] The scorched earth: Oil and war in Sudan.. [A] report.. shows
how the presence of international oil companies is fuelling the
war... In the name of oil, government forces and government-supported
militias are emptying the land of civilians, killing and displacing
hundreds of thousands of southern Sudanese. Oil industry
infrastructure - the same roads and airstrips which serve the
companies - is used by the army as part of the war. In retaliation,
opposition forces have attacked government-controlled towns and
villages, causing further death and displacement"

---

Chevron in Sudan? Say no more. There is your culprit.

"There is chaos in Sudan. Do you think involvement of Chevron contributed... "

---

Butler, *War is a Racket*: "[1935, A key] step in this business of
smashing the war racket is to make certain that our military forces
are truly forces for defense only.  At each session of Congress the
question of further naval appropriations comes up. The swivel-chair
admirals of Washington (and there are always a lot of them) are very
adroit lobbyists. And they are smart. They don’t shout that 'We need a
lot of battleships to war on this nation or that nation.' Oh,
no. First of all, they let it be known that America is menaced by a
great naval power. Almost any day, these admirals will tell you, the
great fleet of this supposed enemy will strike suddenly and annihilate
our 125,000,000 people. Just like that. Then they begin to cry for a
larger navy.  For what?..

The ships of our navy.. should be specifically limited, by law, to
within 200 miles of our coastline. Had that been the law in 1898 the
Maine would never have gone to Havana Harbor. She never would have
been blown up. There would have been no war with Spain with its
attendant loss of life. Two hundred miles is ample, in the opinion of
experts, for defense purposes. Our nation cannot start an offensive
war if its ships can’t go farther than 200 miles from the coastline.
Planes might be permitted to go as far as 500 miles from the coast for
purposes of reconnaissance. And the army should never leave the
territorial limits of our nation"

---

The `corr` function returns values between -1 and 1. Negative value
for rates and prices make sense, lower rates do push house prices up.
But excessive wealth concentration has 5 times the effect compared to
any rate changes.

---

Rate rises did not help lowering house prices. Analysis below shows
the highest correlation is between high wealth and house prices, not
between rates and house prices. 

```python
df = u.get_fred(2000,['FEDFUNDS','MSPUS','WFRBST01134']).interpolate()
df.columns = ['rate','house price','top 1% wealth']
df.corr()
```

```text
Out[1]: 
                   rate  house price  top 1% wealth
rate           1.000000    -0.121352      -0.327207
house price   -0.121352     1.000000       0.766769
top 1% wealth -0.327207     0.766769       1.000000
```

---

Inequality skews demand towards the upside. A median house cannot cost
nearly half a million fucking dollars. This is serious, as in
pitchfork level serious.

---

NBC News: "New data shows the median sale price for a home rose to
nearly $380,000 in January — the seventh increase in a row"

---

Euronews: "Spain is banning some short-haul domestic flights as part
of its plan to reduce carbon emissions... Flights with a rail
alternative that takes less than two and a half hours will no longer
be allowed, 'except in cases of connection with hub airports that link
with international routes'"

---

H2 Fuel News: "GenH2 Unveils Groundbreaking Liquid Hydrogen Technology
in Milestone UAV Flight"

---

FDR took the biggest step against gold, way before Nixon. Progressive
president, time of crisis, government could not tie its own hands by
basing its dealings on some stupid rare metal, makes sense.

---

History.com: "On June 5, 1933, the United States went off the gold
standard, a monetary system in which currency is backed by gold, when
Congress enacted a joint resolution nullifying the right of creditors
to demand payment in gold...

On April 5, 1933, Roosevelt ordered all gold coins and gold
certificates in denominations of more than $100 turned in for other
money. It required all persons to deliver all gold coin, gold bullion
and gold certificates owned by them to the Federal Reserve by May 1
for the set price of 20.67 dollars per ounce...

In 1934, the government price of gold was increased to $35 per ounce,
effectively increasing the gold on the Federal Reserve’s balance
sheets by 69 percent...

The government held the $35 per ounce price until August 15, 1971,
when President Richard Nixon announced that the United States would no
longer convert dollars to gold at a fixed value, thus completely
abandoning the gold standard"

---

Mapping time, there is some data out there for the Sudan civil
war. Frontline between RSF/SAF below. The borders delineate RSF
controlled territory.

[[-]](mbl/2024/sdndata/map1.html)

---

I see... Egypt supplies drones to them, no?

Sudan War Monitor: "Sudan army breaks Omdurman siege"

---

"@laptopkitten@kitty.social

British people like Doctor Who because it fulfills their fantasy of
getting to go on adventures. Americans like Doctor Who because it
fulfills their fantasy of having a doctor"

---

"@aphyr@woof.group

I know id.me is supposed to make tax filing more secure but I do not
have the fucking patience for a login system that requires username,
password, 2FA TOTP, and *then* has the gall to ask me to fill out a
giant form with all my personal information and join a queue to video
chat with someone to show them my ID docs???

what the fuck"

---

\#Ronson \#CultureWar

[[-]](https://cdn.fosstodon.org/media_attachments/files/111/984/661/679/214/981/original/3b53db7de50ea0d8.jpeg)

---

Jon Ronson: "Culture wars are so often.. opium of the masses, people
scream at each other about trans rights while the rich get richer"

---

Herman, *Degraded Capability*: "[2000] Nato’s fiftieth birthday
celebration was held in Washington on 23-25 April 1999. The bombing of
Yugoslavia had been going on for a month. The outcome was still
uncertain, but dissension was muted and triumphalism was the
prescribed tone. Thanks to Kosovo, Nato had asserted its new role as a
‘humanitarian’ strike force unlimited by geographical boundaries or
provisions of international law.

No humanitarian mission had been necessary to persuade major US
private corporations to put up the $8 million to pay for the birthday
party, or to incite a dozen chief executive officers of major Pentagon
contractors to pay 250,000 each to serve as official
sponsors. Corporate America was well aware of the importance of Nato
as a source of long-term, guaranteed profits. US Congressmen had been
heavily lobbied by a special ‘US Committee to Expand Nato’, presided
over by Lockheed’s chief executive. No wonder: Nato’s expansion will
require the Central Eastern European countries to strain their budgets
in order to procure US military equipment. Poland, for instance, is
expected to buy 100-150 newfighter planes, which could be either the
Lockheed F-16 (20 million) or the Boeing F-18 (40—60 million dollars
each)"

---

Businesswire: "Graforce is setting new standards in hydrogen
production and carbon dioxide removal with its cross-cutting plasma
technology (Plasmalysis). By harnessing the plasma catalytic effect, a
unique property of ionized plasma, this technology significantly
enhances chemical reactions' efficiency and reduces renewable power
consumption by 80% compared to conventional hydrogen production
methods. Plasmalysis splits natural gas and biogas into hydrogen and
solid carbon, and converts ammonia or NH4-liquids into hydrogen and
nitrogen"

---

"The Adani Group.. is reportedly engaged in advanced discussions with
sovereign funds in West Asia to secure up to $2.6 billion for its
airport expansion and green hydrogen initiatives"

---

Times of Israel: "Israel livid as Brazil’s Lula says Israel like
‘Hitler,’ committing genocide in Gaza"

---

Korea JoongAnd Daily: "Hyundai to invest $1.1 billion in Brazil for hydrogen shift"

<img width='340' src='https://files.mastodon.social/cache/preview_cards/images/088/914/901/original/421b8f983b077a5d.jpg'/> 

---

Oil Price: "Last month, Toyota chair Akio Toyoda said he thinks the
share of battery cars on the global market will peak at 30%, with the
remaining 70% taken up by hydrogen and internal combustion
engines. BMW chief executive officer Oliver Zipse is similarly bullish
about the technology as one component of a cleaner transportation
future"

---

Rescue scenarios, for a person, a small group, is becoming a thing in
recent action movie stories.. The approach keeps most of the politics
out, the story becomes more about simpler things - people, comrades,
friends, civilians in need.. How many movies can you make about "big
bad government about to get you". I for one am tired of that take. I
welcome this change.

---

"@falcennial@mastodon.social

I think curiosity more likely informed the cat"

---

Steve Seagulls - Thunderstruck \#music

[[-]](https://m.youtube.com/watch?v=0Gg9kU8Mjpo)

---

H2 Central: "Renewable hydrogen production in Spain will be around 2.5
million tonnes per year in 2030, according to the average scenario
estimated by Enagás based on data collected from companies interested
in participating in hydrogen transport infrastructure. The company has
registered a total of 650 projects, 65% of which are for production,
20% for consumption and the remaining 15% for marketing. Two hundred
and six companies participated in the “call of interest” announced by
Enagás in the last quarter of 2023"

---

Investing in foreign lands is supposed to be riskier.. Don't be a
whiny wanker... aren't you the fearless, adventurer enterpreneur? Take
the risk.

"Ew but how can corporations work in foreign lands without 'protection'"

---

Matt Kennard's *Silent Coup* describes this system in detail. ISDS can
be used for anything that rankles global corps, one government was
taken to court for raising the minimum wage.

---

The Guardian: ‘Litigation terrorism’: the obscure tool that
corporations are using against green laws.. a US mining firm sued
Mexico for billions – for trying to protect its own seabed.. What do
you get if you cross the planet’s richest 1%, a global legal system
adapted to their investment whims, and the chance to squeeze billions
from governments? The answer is 'Investor-State Dispute Settlements',
or ISDS, alternatively dubbed 'litigation terrorism' by Joseph
Stiglitz.. ISDS is a corporate tribunal system, where a panel of
unelected lawyers decides whether a company is owed compensation if
the actions of national governments leave its assets 'stranded'.

In hearings, which are often held behind closed doors, ISDS documents,
claims, awards, settlements – even the content of cases – need not be
made public, regardless of any public-interest considerations. Last
week the Guardian revealed how Odyssey Marine Exploration, a US-based
subsea mineral extraction company, was using an ISDS panel to sue
Mexico for $2.36bn (£1.87bn) after the government moved to prevent it
dredging off the Pacific coast"

---

"@fkamiah17@toot.wales

Remember the weeks of coverage and outrage when Nôtre Dame burned
down? Just a few which have been destroyed during the [ISR] genocide.

Great Omari Mosque - 2,500 years old

Qasr al-Basha - 800 years old

Church of St. Porphyrius - 1,600 years old

Hammam al-Sammara - circa 1,000 years old"

---

NYT: "Ukraine’s Deepening Fog of War.. Two years after Russia’s
full-scale invasion, Ukrainian leaders are seeking a path forward in
the face of ferocious assaults and daunting unknowns"

---

02/17 - 02/25, Russia took Robotyne back. They moved past Avdiivka
nearing Orlivka. Also approaching Ivanivska, major gains.. Looking bad
for Ukraine in every direction.

[[-]](ukrdata/map7.html)

---

CNBC: "Russia was ridiculed at the start of the war. Two years on, it
has reasons to be confident"

---

Butler: "[from a speech before the American Legion which made the
papers]. I spent thirty-three years and four months in active military
service, and during that period I spent most of my time being a
high-class muscle man for Big Business, for Wall Street and the
bankers. In short, I was a racketeer, a gangster for capitalism. I
helped make Honduras right for the American fruit companies in 1903. I
helped purify Nicaragua for the International Banking House of Brown
Brothers in 1902–1912. I helped make Mexico and especially Tampico
safe for American oil interests in 1914. I brought light to the
Dominican Republic for the American sugar interests in 1916. I helped
make Haiti and Cuba a decent place for the National City Bank boys to
collect revenues in. I helped in the raping of half a dozen Central
American republics for the benefit of Wall Street. In China in 1927 I
helped see to it that Standard Oil went on its way unmolested. Looking
back on it, I might have given Al Capone a few hints. The best he
could do was to operate his racket in three districts. I operated on
three continents"

---

Butler is one of the most decorated soldiers of US Army. He commanded
a Marine Expeditionary Force during the late 1920s, named a major
general later. He is one of the few people who have been twice awarded
the Medal of Honor, received the Marine Corps Brevet Medal, the
highest Marine decoration at the time for officers. He figured out
what was going on however, wrote about it. His book *War Is a Racket*
was republished recently, its intro written by Jesse Ventura.

---

General Smedley D. Butler: "[1930] There are only two things we should
fight for. One is the defense of our homes and the other is the Bill
of Rights. War for any other reason is simply a racket"

---

ProPublica: "The Rising Cost of the Oil Industry’s Slow
Death.. Unplugged oil and gas wells accelerate climate change.. Until
wells are properly plugged, many leak oil and brine onto farmland and
into waterways and emit toxic and explosive gasses, rendering
redevelopment impossible"

---

"@evacide@hachyderm.io

Did I mention that the data broker industry must be destroyed? Because
yeah"

---

Al-Monitor: "Shipping insurance rates soar on Red Sea missile attacks"

---

F24: "France under pressure to suspend military sales to Israel as war
in Gaza grinds on"

---
