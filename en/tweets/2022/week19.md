# Week 19 

---

H2 View: "A cooperation agreement to develop hydrogen refuelling
infrastructure capable of refuelling 100,000 hydrogen-powered vehicles
in the Nordic region has been signed.. Norwegian Hydrogen AS,
FirstElement Fuel Inc. and Mitsui & Co, announced the companies would
be working together to accelerate the expansion of the hydrogen
network across the entire Nordic region"

---

H2 View: "Aviation H2 signs major deal with FalconAir to aid in
developing hydrogen aircraft by 2023. As development of Australia’s
first hydrogen-powered plane ramps up, the company behind the
aircraft, Aviation H2, has unveiled a new major partnership with
FalconAir"

---

H2 Bulletin: "ZeroAvia Kicks Off US 19-seat Aircraft Testing and
Demonstration Program on Path to Worldwide Application of its
Powertrain Technology"

---

H2 View: "Texas, US, continues to ramp up its hydrogen capabilities
with Enbridge and Humble Midstream revealing plans to develop
low-carbon hydrogen and ammonia facilities"

---

H2 Fuel News: "Hydrogen trucks are the most eco-friendly zero-emission
vehicle, says ATRI [American Transportation Research Institute]"

---

H2 View: "Elcogen announced that it has received a €24m ($25.25m)
investment to aid the expansion of its capabilities to produce green
hydrogen, using its reversible solid oxide fuel cell (SOFC)
technology, from HydrogenOne Capital Growth Plc (HydrogenOne)... The
investment is set to allow Elcogen to drive forward its expansion of
facilities in Tallinn, Estonia, to create an automated production line
for SOFCs"

---

H2 View: "Lhyfe has officially launched its initial public offering (IPO) to
support the development of the company’s green hydrogen production
technology and ambitions... The capital increase has soared to over
€145m ($152m)"

---

Thorium on the other hand, can be found in Egypt, Australia, Canada,
US, Brazil, Asia Minor.. Molten-salt reactors show some hope; can
produce H2 easily, added bonus.

---

Wanna do more nuclear? A lot of the fuel for that also comes from
Russia Russia Russia.

---

[Link](https://drive.google.com/uc?export=view&id=1n0aVnSajhY5RR18uEk-tvTD0aRGzQc8D)

---

Saw another asshat claiming 'maybe the Sun just *reflects* GR from
everywhere else' 😂 

---

Of course, dark matter, near black hole, across a time dilation field
seeping into our universe from another. You got it all figured out
champ...

"Dark Matter could be involved here too"

---

Activity would disrupt the activity on that surface, so Gamma rays
would decrease. That's why there is strong anti-correlation. 

---

Nuclear reactions on the surface of the Sun is enough to explain
that. See 'lattice confinement fusion'. Have to accept the Sun does
have a surface, it aint bunch of 'hot gas'.

SciAm: "The Sun Is Spitting Out Strange Patterns of Gamma Rays—and No
One Knows Why.. To their surprise, the researchers found the most
intense gamma rays appear strangely synced with the quietest part of
the solar cycle"

[[-]](https://www.scientificamerican.com/article/the-sun-is-spitting-out-strange-patterns-of-gamma-rays-and-no-one-knows-why/)

---

Many-Worlds Interpretation of QM is made possible by ignoring the
measurement problem, not solving it. 'The collapse' of the
wavefunction is essentially swept under the carpet, but ignoring the
problem doesn't make it go away. 

---

Interesting, though this tool is overused these days as a literary
crutch. Ditto for 'alternate universes'.

"[Twain novel] *A Connecticut Yankee in King Arthur’s Court*.. is often
said to be the forerunner of all science fiction tales about time
travel"

---

MT depiction in Trek Next Gen was good.

---

It's weird how the image of Twain today is excessively sanitized.
Mark Twain was a vocal anti-war proponent in his day.. He even once
suggested that the stars in the flag be "replaced by skulls and
cross-bones".

"During the Spanish-American War, [Mark] Twain became a fervent
anti-imperialist, even joining the Anti-Imperialist League. His
sentiments about the war and the war in the Phillippines were
published nationwide"

---

Some accents at the UN pronounce piece as 'piss'. Have to work on that
bruh.

---

Social rentals (gov-built rent-controlled homes) as a % of total
housing; France 14%, Denmark 21%, Netherlands 37%. \#ABC \#Oz. That is
a huge number. Taking services completely outside the market structure
can work. This is the way

---

\#Documentary \#WSJ "Trucking used to be one of the very best blue
collar jobs in the US. The industry was almost fully unionized by the
teamsters union.  Unionized truck drivers were making up to 20% more
than even unionized steel workers or auto workers. It was one of the
best jobs you could get, and when you got one of those good jobs you
were likely to stay in it until you until you retired. [But] the
industry was deregulated 1980, the union was pushed out of the big
segments of the of the industry, and and wages and working conditions
followed [became worse]"

---

He had kicked out the foreigners and nationalized the oil
industry. Then boom - toppled by an 'Anglo' coup.

---

Pity. Iran's democratically elected leader Mossadeg was Time's Man of
the Year for 1952. A terrible fate befell him..

[[-]](https://pbs.twimg.com/media/FSWaDakXMAEnhI5?format=jpg&name=small)

---

Had to guide the processing towards the goal; remove small patches,
tell the segmentation algo to look at coarse objects, put a lower
limit on segment size.. lots of small nudges here and there. There is
no free lunch. There is no 'Alexa give me the interesting image blocks
and boundaries in this image'.

---

Little image processing action to reverse-eng UKR-RU frontline. Works ok

```python
from skimage.color import rgb2gray, rgb2lab, deltaE_cie76
from skimage.segmentation import felzenszwalb
from skimage.morphology import binary_closing
from skimage import io, measure

threshold = 15
img = io.imread("ua-ukr-20220504.png")
lab = rgb2lab(img[:,:,[0,1,2]])
d1 = deltaE_cie76(rgb2lab(np.uint8(np.asarray([243,178,182])) ), lab)
d2 = deltaE_cie76(rgb2lab(np.uint8(np.asarray([253,35,36])) ), lab)
flt = rgb2gray(img.copy())
flt[(d1 < threshold)] = 1; flt[(d1 >= threshold)] = 0
flt[(d2 < threshold)] = 1; 
flt = flt.astype(bool)
flt = binary_closing(flt)
seg = felzenszwalb(flt, scale=50, sigma=2, min_size=8000)
fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
axes[0].imshow(img)
axes[1].imshow(seg)
contours = measure.find_contours(seg, 0.8)
for c in contours:
    axes[1].plot(c[:, 1], c[:, 0], color='white',linewidth=2)
```

<img width="350" src="https://pbs.twimg.com/media/FSWZvWtXwAAfZVv?format=png&name=small"/>

---

Al Monitor: "Yazidis displaced anew by north Iraq violence"

---

NI is seperated by the North Channel from UK just as UK is seperated
by the English Channel from EU mainland - yet the latter went through
Brexit, severing its connection to that mainland. Well here is another
Channel and maybe another "exit".

"Northern Island is so close to UK, it's logical they want to be
closely connected"

---

Aw man but UK is such a 'leader' in the RU/UKR fight (while also
quietly enjoying the mess it helped create inside European
landmass). Can't you cut them a little slack?

Politico: "Take a chill pill, EU tells UK over Northern Ireland
protocol.. London needs to 'dial down the rhetoric' and 'find
solutions' to trade issues within the framework of the deal, European
Commission Vice President Maros Sefcovic says"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Gasgrid Finland participates in the update of <a href="https://twitter.com/ehb_europe?ref_src=twsrc%5Etfw">@ehb_europe</a> development vision – the hydrogen backbone to support the achievement of climate goals, REPowerEU plans, and developing the resilience of the European energy system. <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/EHB?src=hash&amp;ref_src=twsrc%5Etfw">#EHB</a> <a href="https://t.co/adljzgqa2X">https://t.co/adljzgqa2X</a> <a href="https://t.co/fdAbz5wzwC">pic.twitter.com/fdAbz5wzwC</a></p>&mdash; Gasgrid Finland Oy (@GasgridFinland) <a href="https://twitter.com/GasgridFinland/status/1511248215798161410?ref_src=twsrc%5Etfw">April 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

H2 View: "[A new] study has found that using a [polymer based]
photocatalyst under simulated sunlight facilitates the decomposition
of water, when loaded with an iridium catalyst, which in turn
generates hydrogen. The photocatalysts.. are of huge interest as their
properties can be tuned.. The researchers have also said that another
potential advantage of this technique.. is that ‘polymers are
printable’, which would allow for cost-effective production techniques
for scaling up"

[[-]](https://www.h2-view.com/story/study-suggests-solar-energy-potential-solution-for-green-hydrogen-production/)

---

H2 View: "European electrolyser manufacturers and the European
Commission have committed to increase their annual hydrogen
manufacturing capacity to 15.5GW by 2025 in a joint declaration"

---

"@AirLiquideUSA

In today’s \#SenateENR hearing on the [DOE] budget, @SenCortezMasto
and @SecGranholm discuss their recent visit to our new hydrogen
facility in Nevada"

[[-]](https://mobile.twitter.com/AirLiquideUSA/status/1522318903204093954)

---

H2 View: "Preliminary approval brings hydrogen-powered ships closer to
Norway.. HAV Group ASA announced that it has received preliminary
approval for its hydrogen-based energy system, pushing forward hopes
of using hydrogen fuel in commercial ships"

---

H2 View: "A pre-feasibility study has been announced that will assess
the viability to produce and transport green hydrogen in Western
Australia, using existing pipelines"

---

H2 View: "ScottishPower and Storegga announced plans to build a series
of megawatt-scale green hydrogen projects in the Scottish Highlands"

---

H2 Fuel News: "Smartpipe Technologies recently announced that it has
received a $6.6 million investment from Enbridge for the development
of innovative pipelinew technology [for H2 and CO2]."

---

"@hyzonmotors

... Hyzon fuel cell trucks will be operating with a lower total cost
of ownership than diesel trucks in California before the end of 2022"

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The launch of Anglo American’s <a href="https://twitter.com/hashtag/nuGen?src=hash&amp;ref_src=twsrc%5Etfw">#nuGen</a>™️ Zero Emission Haulage Solution haulage solution, a hydrogen-powered, ultra-class mine haul truck, is currently underway at the Mogalakwena PGM mine in Mokopane, Limpopo. <a href="https://twitter.com/hashtag/HydrogenPower?src=hash&amp;ref_src=twsrc%5Etfw">#HydrogenPower</a> <a href="https://twitter.com/hashtag/GrowSouthAfrica?src=hash&amp;ref_src=twsrc%5Etfw">#GrowSouthAfrica</a> <a href="https://t.co/EGZWTSuQmn">pic.twitter.com/EGZWTSuQmn</a></p>&mdash; Presidency | South Africa 🇿🇦 (@PresidencyZA) <a href="https://twitter.com/PresidencyZA/status/1522526875209371650?ref_src=twsrc%5Etfw">May 6, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

The energy ref is good. 

DMT: "For the uninitiated, “Halo” is a military science fiction media
[video game now adapted for the screen] .. Madrigal is home to a plant
that has the galaxy’s highest concentration of heavy hydrogen, which
can be used to power ships... Since resources are probably finite in
the 26th century as well, the UNSC is looking to put their stamp on
Madrigal"

---

They were talking about that 2012 Meet the Press appearance, Im just
kidding.. We kid here.

---

Mrs Biden is a guy? I didnt know!

Politico: "How Same-Sex Marriage Shaped Joe Biden"

---

Pompeo slammed Oz, who was previously endorsed by DJT. What's up

---

Poor guy's reply is full of spurious correlations now.

---

That's from a reply to the trending Douthat tweet; as an example for a
spurious correlation, like his 

---

😂 

"@donmoyn

Worth noting that unemployment rapidly dropped after Britney Spears
[released](https://pbs.twimg.com/media/FSFHKPDWQAEFlbU?format=jpg&name=small)
'Work Bitch'"

---

The market has been overvalued for a long time. 

CNBC: "Stock markets are set for more heavy selling this summer as
central banks around the world hike interest rates to fight spiraling
inflation, said one economist"

---

Lula can win, unseat Bolsonaro. 

The Jakarta Post: "Leftist icon Lula launches presidential campaign to 'rebuild Brazil'"

---

AP News: "[New] post-Brexit rules, which took effect after Britain
left the European Union, have imposed customs and border checks on
some goods entering Northern Ireland from the rest of the U.K. The
arrangement was designed to keep an open border between Northern
Ireland and EU member Ireland, a key pillar of the peace process.

But the rules angered many [DUP members], who maintain that the new
checks have created a barrier between Northern Ireland and the rest of
the U.K. that undermines their British identity. In February, the
DUP’s Paul Givan resigned as first minister in protest against the
arrangements, triggering a a fresh political crisis in Northern
Ireland"

---

The party that wants broken island calls themselves 'unionists' BTW;
effective word play. They actually want to 'unify' with England.

"Belfast results show [DUP] unionists can’t win vote on Brexit protocol"

---

UK limped on by playing an inner-outer game; it tried to balance both,
until it couldn't - enter Brexit. 

---

I hope Ireland is unified, leaves UK. Ditto for Scotland.
England-centric UK proved it doesn't deserve to remain as single
entity. Now solidly in the outer alliance, they flail around in
desperation f-ing shit up everywhere. 

---

Sinn Fein wants the eventual unification of Ireland, their rival DUP
is pro-England.

---

Brexit England is getting the shit kicked out of it; I like it

NYT: "Northern Ireland Turns to Sinn Fein.. Election results reflected the
demoralization of unionist voters, the disarray of their leaders and
an electorate with new priorities — much of which can be traced to
Brexit"

---

First Post: "How Narendra Modi deftly walked Ukraine tightrope to
bring India and Europe closer"

---

Al Jazeera: "Putin believes he cannot ‘afford to lose’ Ukraine war: CIA chief"

---

Politico: "The war in Ukraine has revived Washington’s once-deflated hawks"

---
