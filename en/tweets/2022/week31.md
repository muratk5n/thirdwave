# Week 31 

H2 Central: "The government informed that the draft Hydrogen Mission
document has been prepared. In his Independence Day speech last year,
Prime Minister Narendra Modi had announced the launch of the National
Hydrogen Mission...

According to the [Minister of State for New and Renewable Energy] the
draft mission proposes a framework for demand creation, a basket of
measures to support production and utilisation of green hydrogen and
support for indigenous manufacturing.

Besides, it also includes research and development work, pilot
projects, enabling policies and regulations, and infrastructure
development"

---

The Australia Today: "In a research paper published in the prestigious
journal *Materials Today* [Deakin University researchers] have offered
a novel way to separate, store and transport huge amounts of hydrogen
gas safely and with almost no wastage..

The traditional oil refinery methods make up 15 per cent of the
world’s energy use [which] uses a high-energy ‘cryogenic distillation’
process to separate crude oil into different gases that are further
used by consumers as petrol and household gas.

IFM researchers in their papers have outlined a completely different
mechanochemical way of separating and storing gases that use a tiny
fraction of the energy and create zero waste...

The researchers say that the special ingredient in their process is
boron nitride powder"

[[-]](https://www.theaustraliatoday.com.au/indian-australian-scientist-contributes-to-breakthrough-research-that-could-make-hydrogen-safer-to-use/)

---

H2 Central: "World's first vessel powered by an H2-storing salt gets
construction green light..The world’s first ship to be powered using a
solid form of hydrogen — said to be far safer and easier to store than
compressed or liquid H2 — is due to go into operational trials at the
Port of Amsterdam next June... The *Neo Orbis* passenger vessel —
designed to operate in Amsterdam’s canals and in the channel between
the city and the North Sea — will be powered by hydrogen released from
a salt called sodium borohydride (NaBH4)"

[[-]](https://www.rechargenews.com/energy-transition/solid-hydrogen-worlds-first-vessel-powered-by-an-h2-storing-salt-gets-construction-green-light/2-1-1269510?a=)

---

Collated post on underground H2 storage.

[[-]](2022/02/h2-underground.html)

---

Newatlas: "EAT's silicon-based powder doesn't require you to start off
with any hydrogen at all – and getting the hydrogen back out is even
easier... The Si+ powder can be made using a (preferably renewable)
energy source, as well as metallurgical-grade silicon – which itself
can be made from sand, or from crushed-up recycled solar panels and
electronics. EAT's process results in a porous silicon powder that's
completely safe and easy to transport...

When you need the hydrogen, you dump the Si+ powder into water, mix it
around a bit, and ... that's pretty much it. At a wide range of
ambient temperatures between 0-80 °C (32-176 °F), hydrogen gas will
start bubbling out. The chemical equation, says EAT, looks like this:
Si + 2H2O -> SiO2 + 2H2. Thus, apart from the hydrogen gas, all that's
left over is silicon dioxide, also known as silica, or the major
constituent of sand"

---

Hyzon has good PR department; Kudos. 

"@hyzonmotors

More than 6 billion \#Google searches will be made globally today. The
Hyzon team dug into these searches to find what the world wonders most
about hydrogen. Among the top 10 is pollution-related & we share what
a #hydrogen vehicle does actually emit"

---

"@HydrogenCentral

Shell and Shenergy Form Joint Venture to Develop Hydrogen Refuelling
Network in China"

---

Transport only clean molecules \#H2 \#NH3

"Methane at Sea: Finding the Invisible Climate Killer.. T&E's
investigation into so-called ‘green’ liquid natural gas (LNG) ships
uncovers significant amounts of invisible methane being released into
the atmosphere"

[[-]](https://www.transportenvironment.org/discover/methane-finding-the-invisible/)

---

Recharge: "Australian start-up Hysata that says it has developed the
world’s most efficient electrolyser has attracted A$42.5m ($29.4m) in
an oversubscribed Series A funding round.. The Hysata electrolyser
operates at 95% system efficiency (41.5 kWh/kg), delivering a giant
leap in performance and cost over incumbent technologies"

---

Tree Energy Solutions snagged Marco Alvera, the author of
[this book](2022/06/the-h2-revolution-alvera.html), prev CEO of
Snam. First project of TES is the Wilhelmshaven Green Energy Hub in
Germany, set to supply 250 TWh/year carbon-neutral energy of which H2
is a big part of. 250 TWh/y means 28 GW, not a small thing.

---

This level is pretty standard for most countries.. Electricity is already
not the preferred energy transfer medium. Suboptimal.

---

Electricity as percentage of oveall energy consumption

```python
import util; util.get_bp_country("China")[3]
```

```text
Out[1]: 19.49
```

```python
util.get_bp_country("US")[3]
```

```text
Out[1]: 17.06
```

---

US imports of Chinese goods back to trend (in millions).. 

```python
import util; util.plot_fred(1990, "IMPCH")
```

```text
                   IMPCH
DATE                    
2022-03-01  47373.521578
2022-04-01  41772.201093
2022-05-01  43864.418558
```

[[-]](https://pbs.twimg.com/media/FZLpzsNWIAweDZa?format=png&name=small)

---

If latest GDP figure repeats before the next election, and net
popularity doesn't change it's a loss for Biden if he runs again. But
a mere -10% (an improvement) and GDP growth of 1% would give an
advantage to him, or to the "next Dem nominee".

[[-]](2015/04/predicting-presidential-elections.html#2024)

---

Note that US transport did not fly over the South China Sea, scared
the plane could get shot down there.

---

SOH Taiwan visit didn't seem to help.. Just like the famed 90s
"Tinnamen visit" clearly did nothing for democracy in China. Publicity
stunt?

---

"@Bundeskanzler [Scholz]

At @Siemens_Energy I could see with my own eyes: The serviced turbine
is there and ready for use at any time. It only has to be requested
from Russia. So there are no technical reasons to reduce gas supplies"

---

WION: "Rafael Grossi, the UN nuclear chief has shot out a warning to
the world leaders, stating that Ukraine's Zaporizhzhia nuclear power
plant..  'is completely out of control.. Every principle of nuclear
safety has been violated. What is at stake is extremely serious and
extremely grave and dangerous,' said Grossi"

---

Guessing once artillery fired nearby its location is pinpointed by
this system, for an immediate counterfire.. Probably too late for UKR
but it could be useful for someone else..

---

Effective at what range? 

Jane's Defense: "Microflown Avisa applies 3D shockwave detection for
improved counter-artillery capability"

---

Paper: "Cost of long-distance energy transmission by different
carriers.. This paper compares the relative cost of long-distance,
large-scale energy transmission by electricity, gaseous, and liquid..
carriers. The results indicate that the cost of electrical
transmission per delivered MWh can be up to eight times higher than
for hydrogen pipelines"

[[-]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8661478/)

---

He referenced the paper above

"@BrianGitt

Capital cost of long-distance energy transmission ($/mile-MW):

Electrical lines = $1,502

Hydrogen pipeline = $166

Natural gas pipeline  = $97

Oil pipeline = $16"

---

"@H2Societies

Just a single company - Air Products - has over 600 miles of hydrogen
pipeline in operation around the US Gulf Coast"

---

Ammonia Energy: "Mitsui & Co. and CF Industries will jointly develop a
greenfield facility that will produce CCS ammonia on the US Gulf
Coast. The partners are targeting a reduction of at least 60%
emissions compared to conventional ammonia production, with the
selection of a technology provider in its final stages..

[CF said:] 'Our work with Mitsui has reinforced our shared belief that
blue ammonia will play a critical role in accelerating the world’s
transition to clean energy and that demand for blue ammonia will grow
meaningfully in the second half of this decade. We believe that the
United States offers considerable advantages for blue ammonia
production due to access to plentiful and low-cost natural gas, the
regulatory and legal framework in place, and the geology suitable for
permanent carbon sequestration.'

In November last year we reported that, thanks to planned upgrades at
their existing Donaldsonville and Yazoo City plants, CF Industries was
targeting CCS ammonia production of 1.25 million tonnes per year from
2024"

---

[General Authority for Suez Canal Economic Zone] Signs MOU with Indian
Renew Power for 220,000 Tons of Green Hydrogen Production – $8B
Investment... 'The site initially will be set on an area of ​​600,000
square meters in the Sokhna integrated Zone, bringing the production
capacity of the two phases of green hydrogen to 220,000 tons and 1,100
million tons of green ammonia.' [SCZONE chairman] Zaki added"

---

H2 Central: "Hydrogen turbines – GE Gas Power awarded $4,2M in funding
from ARPA-E.. [The] funding is focused on two projects entitled
'Lifted-flame combustion for high-hydrogen reheat gas turbines' and
'Manufacturing high-yield investment castings with minimal energy.'
Both initiatives will be led by GE Gas Power and conducted at GE’s
Global Technology Center in Greenville, South Carolina... As part of
these projects, GE will conduct cutting-edge research for gas turbine
decarbonization"

---

OCI is a Netherlands based chemical company.. NL is becoming huge in
H2 energy and regulation would be strict.. The ammonia is certainly
clean. My only worry is not being able to generate clean fuels fast
enough, but in terms of tech, there is a pathway to a clean energy
future through both green and blue H2/NH3.

---

First shipment from this venture arrived to Japan recently 

"[06/2021: A] joint venture between Adnoc and OCI, will join the
development of a large blue ammonia plant in the UAE’s downstream
centre in Ruwais... The blue aspect refers to hydrogen derived from
natural gas feedstocks. The plant will have a production capacity of
1,000 kilotonnes a year"

---

"@H2Europe

The #hydrogen start-up [Tree Energy] has secured €65 million in its
latest funding round.  @malvera1, the CEO, affirmed that the company
is looking to become one of the world’s largest buyers of #renewable
energy. Belgium-based company seeks to expand the use of renewable
energy across Europe"

---

Then this silicon-based powder sort of becomes the fuel, the thing
that gets stored, transported etc; since it can take H2 out of any
water easily.

H2 Fuel News: "Si+ material to make hydrogen fuel transportation and
storage safer.. The silicon-based powder acts as a solid-state H2
making it safer to both store and transport... The breakthrough was
announced by the EPRO Advance Technology (EAT) renewable energy
company...

'EAT has developed a revolutionary porous silicon material, known as
Si+, which has the ability to generate ultra-pure hydrogen from a
water source and which acts as a solid-state hydrogen generating
material – one that is compact, robust, and easily transportable' said
a media release issued by the company"

---

The "Mandela Effect"? Most think Mandela died in prison instead of in 2013.
That is an "effect".. I think it's just people being dumb (or
uninformed). It's fine, really.. Does the man on the street need to
know everything? No. That's why we have professions.

---

More dark comedy.. 

Al Monitor: "Palestinian family encircled by Israeli settlement.. An
eight-metre high metal fence surrounds the Gharib family home in the
occupied West Bank. To reach it they must pass through a gate remotely
controlled by Israeli security forces"

[[-]](https://pbs.twimg.com/media/FZFdyBCXwAQFYKg?format=jpg&name=small)

---

Portable food: dried poultry mixed with fruit/veg. Protein, vita,
CLA/fat all in one place.

[[-]](../../2022/07/dried-turkey-veg.html)

---

CNBC: "The death of easy money: Why 20% annual returns are over in
crypto lending.. '$3 trillion of liquidity will likely be taken out of
markets globally by central banks over the next 18 months,' said.. a
global crypto and digital asset strategist at Bank of America"

---

WION: "Lebanon: People queue up to buy bread, six breads sell for $20
on black market"

---

Yahoo News: "Truss surges ahead, wins key backers in UK leadership
race"

---

Let's sanction US for its sanctions

"U.S. Eyes Sanctions Against Network It Believes Is Shipping Iranian Oil"

---

If China consumes a lot of dirty coal, and the entire world depends on
them to produce stuff, then to lower emissions maybe countries should
not depend on China for so many products. Should the the environmental
footprint of a country define which tariffs get applied to it?

---

The Danish Strait - dam. It's busy up there..

---

Malacca is *closer* to the optimal path I bet corps shaving off cents
from their cost needed that path. 

---

Is "the Malacca Strait worry" overblown? There are alternatives..
Sunda and Lombok Strait are both available and actually spacier for
ship traffic. 

---

Straits, Chokepoints

[[-]](../../2019/05/oilgas.html#straits)

---

The now militarized Spratly Islands are smack in the middle of
international waters

---

But China says, no, [all that shit](https://pbs.twimg.com/media/FZIt5JHXgAA4COR?format=png&name=small) 
is mine

---

UN recognized maritime borders in the SCC based on 12 mile
rule.. Looks fair

[[-]](https://pbs.twimg.com/media/FZItfqnWIAAxvOd?format=png&name=small)

---

Claims on the South China Sea.. from [paper](https://www.researchgate.net/publication/342610470_Hydrocarbon_reserves_of_the_South_China_Sea_Implications_for_regional_energy_security).
Pretty much everyone's claimed sea space overlap and of course,
there is oil and gas involved.

[[-]](https://pbs.twimg.com/media/FZGH3_eWIAI0Vqz?format=png&name=small)

---

WION: "Russia Pummels Ukraine's Mykolaiv, Killing Top Businessman"

---

H2 View: "Hopes for hydrogen in the US have been heightened after the
breakthrough Tax and Climate Bill was agreed on seeing the US Senate
offer a $3 per kg in tax credits, that look to make green hydrogen
cheaper to produce than grey.".

---

H2 View: "Hydrogen mixing gas turbine project takes slice of $4.2m
funding [from US Advanced Research Projects Agency-Energy]"

---

The Lighthouse: "Designer bacteria could fuel the future with cheap
hydrogen.. Macquarie synthetic biologists have made a breakthrough in
renewable energy production by creating genetically-engineered
sugar-loving bacteria that can produce on-demand, zero-emission
hydrogen fuel..

The genetic engineering of the microbes is partly funded by a $1.1
million grant from the Australian Government’s Renewable Energy Agency
(ARENA) and supported by industry partners BOC Australia and
Bioplatforms Australia.

'This is renewable energy that uses a two-part system; first, the
bacteria consume the sugar and as it digests the sugar it produces the
hydrogen gas,' [researcher] explains...

Farming bacteria to produce hydrogen also has economic and
environmental advantages – in the right setting, bacteria rapidly
multiply, they are cheap to create and don’t need much space...

The University team has used genetic engineering approaches to change
the DNA of certain strains of E. coli bacteria to produce hydrogen
from sugars.

By accelerating the metabolism of the bacteria and finding the optimum
conditions for production, they have produced a strain that makes
hydrogen at rates higher than any previous published rates of
bacterial bio-hydrogen.

Many bio-hydrogen developers are using algae to produce hydrogen but
Willows says that bacteria have the advantage of much faster
production and lower inputs – they also don’t require big ponds for
cultivation.

The strain that the team has developed is also very stable, he
adds. 'We have bacteria that we made more than four months ago that
are still producing hydrogen at the same rate,” he says. “They are not
growing or dividing – this is exciting as all of the enzymes that are
required within the bacterial cell seem to be stable for about three
or four months, or possibly longer.'

Unlike ethanol – a fuel that must grow new yeast for each new batch –
Macquarie’s bacterial hydrogen producers can keep brewing gas without
a fresh biological agent added for each batch"

[[-]](https://lighthouse.mq.edu.au/article/september2/designer-bacteria-could-fuel-the-future-with-cheap-hydrogen)

---

Cows produce methane naturally.. Surely much can be done through bio
for H2 production.

---

Utility Dive: "Carbon capture projects, regional CO2 pipeline design
to get $2.6B in DOE funding proposal.. The Department of Energy plans
to offer 2.54 billion to help finance six carbon capture and storage,
or CCS, demonstration projects at coal- and gas-fired power plants as
well as at industrial facilities, according to a notice of intent
issued Wednesday"

---

That is around 300 mmboe.. They have [larger fields](https://muratk5n.github.io/thirdwave/en/2019/05/oilgas.html#fields)
over there, but it's not nothing.

Al Monitor: "More gas discovered off coast of Abu Dhabi.. The
discovery in the Offshore Block 2 Exploration Concession off the cost
of Abu Dhabi amounts to 1-1.5 trillion standard cubic feet of gas. The
field is operated by the Italian energy giant Eni"

---

Hopefully Wagner doesn't sabotage that pipeline. 

---

[Link](https://pbs.twimg.com/media/FY2MsoEXoAMjv5-?format=jpg&name=small)

---

Now we're talkin. This is some NStream level shit.

```python
int((30*1e9*10.55) / (1e6*365*24)), 'GW'
```

```text
36 GW
```
---

Xinhuanet: "Algeria, Niger, Nigeria ink deal to build trans-Saharan
gas pipeline..  [who] signed on Thursday a memorandum of
understanding.. for the construction of a gas pipeline across the
Sahara Desert that will supply Europe with additional gas.. [The
pipeline] is expected to span 4,000 km and could send up to 30 billion
cubic meters of natural gas per year"

---

CNBC: "Air travel chaos.. [We] spoke to several pilots flying for
major airlines, all of whom described fatigue due to long hours and
what they said was opportunism and a desire to cut costs as part of a
toxic 'race to the bottom' culture pervading the industry and
worsening the messy situation that travelers are facing today...

'Leading into the summer, it was absolute carnage because airlines
didn’t know what they were doing. They didn’t have a proper plan in
place. All they knew they wanted to do was try and fly as much as
humanly possible – almost as if the pandemic had never happened,' [a]
pilot said.

'But they forgot that they’d cut all of their resources.'"

---

Mind Soup - Dawn Of Caspian \#music

[[-]](https://youtu.be/8albXL68H-M?t=82)

---

Peter Voit (Not Even Wrong Blog): "There’s a new book out this month,
'Before the Big Bang: The Origin off the Universe from the Multiverse'..

I spent a few minutes today looking through the book in the bookstore,
trying to figure out where to find the details of the 'spectacularly
vindicated with observational evidence.' I didn’t see any references
in the book..  For many years I’ve spent a significant amount of time
reading books and papers purporting to offer scientific evidence for a
multiverse, trying to carefully understand the author’s arguments and
write about them here.. Few physicists though seem to care that bogus
claims and pseudo-science about the multiverse have overrun their
field and become its public face. I’ve come to the conclusion that
best to not waste more time on this"

[[-]](https://www.math.columbia.edu/~woit/wordpress/?p=12997)

---

*Accident Man*, my kinda thing.. Rated R.

---

*A Quiet Place*, not my kind of thing.. Recommender tad off on this
one. But cinematically wonderful, has its own pace, well acted.

---

The Independent: "Brexit bad for business, says Tory mayor Andy
Street’s comments come after Tory leadership contenders insisted
Brexit has provided opportunities"

---

That looks nice \#taipei

[[-]](https://pbs.twimg.com/media/FY8Go4GWIAENqVW?format=jpg&name=small)

---

Possible Taiwan invasion: Analyst says Nov-March too windy, May-June
has fog, July-September Typhoon season.. That leaves April or October.

---

US "one China policy" might have a hidden gag in it.. bcz CH
nationalists who lost the civil war and ran to Taiwan also considered
themselves 'the one true government of China'.

---

Politico: "Hungary expects to agree on a new deal with Russia this
summer that would provide the country with an additional 700 million
cubic meters of gas, Prime Minister Viktor Orbán said Friday"

---

RU reorg of its mil worked for them.. they saw major US air power in
display in Desert Storm, and in later conflicts, saw units that can
communicate effectively, be deployed anywhere... How do you fight
that? Disrupt communications through major jamming capab, develop
strong air defense, and center it around the type of war *they* would
fight - against a neighbor, mostly on land. Tactics feed into tanks
and artillery, even snipers pass intel to them, air defense protects
them, and they attack with overwhelming force, not with the precision
of US military, but still through sheer numbers it is effective.

---

It wont; RU can still hit transport with anti-ship missiles in Crimea,
and Kherson. See [here](https://pbs.twimg.com/media/FY5ZWQKWIAE2LD_?format=jpg&name=small).

"Ukraine retaking of the Snake Island will help ease the blockade of
grain shipments"

---

Davis: "Ukraine’s Big ‘Million Man’ Offensive Against Russia Is A
Mistake... As someone who has fought in large tank battles and spent
years participating in large-scale mechanized war games in Europe, I
cannot stress how difficult a task it is for an army to mount an
offensive operation when it has lost a sizeable portion of its
experienced leaders, is filled with large numbers of raw recruits, and
have a patchwork of limited armored vehicles and ammunition...

The danger in shooting for a miracle and trying the offensive anyway
is that Ukraine would risk suffering even more casualties, losing more
irreplaceable equipment, and in the end potentially suffering the loss
of even more territory than they had at the beginning of the
battle. All Russia would have to do is absorb the blows, yield only
when required to avoid encirclement, and then when the Ukrainian side
had expended its striking power, launch a counter-offensive to drive
the weakened troops further west"

[[-]](https://www.19fortyfive.com/2022/07/ukraines-big-million-man-offensive-against-russia-seems-like-a-mistake/)

---
