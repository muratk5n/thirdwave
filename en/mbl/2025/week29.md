# Week 29

"@ProPublica@newsie.social

Over the years, Texas legislators have declined to pass at least three
bills that would create siren or alert systems, a tool that Kerr
County officials tried to secure for years before the July 4 flooding."

---

15 News: "[2023] Ice Cube warns rap record labels encourage criminal
behavior and help fuel private prisons.. 'if you follow the money, you
go high enough, you start to see... Okay, let’s take Rap music. The
same people who own the labels own the prisons.' Ice Cube said, adding
later that there are a 'lot of dots to connect.. It's not about making
somebody write the lyrics, it's about being there as guardrails to
make sure certain songs make it through and certain songs
don’t,'.. Ice Cube then later explains that sometimes record companies
micromanage albums and that 'some records are made by committee' so
that they can push 'a narrative.' This is, according to the rapper, an
example of social engineering meant to ensure that American prisons
stay full"

---

In an ideal world the exchange rate would help fix imbalances (and a
Bancor system would fix it decisively), but impurities in the system
complicate matters... Many countries have dollar denominated debt,
depreciation of their currency has adverse effect on that debt, even
though depreciation would help exports. Non-diversified economies rely
on imports and exports that are "price inelastic".. And overtly
agressive financial markets can effect currencies beyond any economic
fundamentals.

Globalists likely prefer the existing system because imbalances are
fixed by placing troubled countries in debt, which makes them a slave,
fine. If a bailout is needed, they can always force politicians of the
developed world which foot the bill, sometimes on public's dime,
globalists don't care because it's not their money, they don't pay tax
anyway. If bailout cannot be arranged, still fine, they can buy public
property during an emergency fire sale. They always win.

---

That makes sense, if you are buying more than you are selling, that
reduces the demand for your currency, its price will fall which can be
inflationary. Both variables influence the exchange rate and interest
rates, with IR being the lowest in the chain, basically countries
*must* set the rate to certain values which the rest of the economy
demands. Especially for developing countries interest rates must be
set to certain levels to stabilize their exchange rate.

If a country is in a rut in terms of its exchange rates and high rates,
it must fix its current account balance.

---

CAB and pi have the highest influence, E and i have the lowest.

```python
pagerank_reversed = nx.pagerank(G.reverse())
for node, pr in sorted(pagerank_reversed.items()):
    print(f"Node {node}: {pr:.4f}")
```

```text
Node E: 0.2354
Node cab: 0.2915
Node i: 0.2116
Node pi: 0.2614
```

---

It's a jumble of relations.. A lot of variables seem to effect many
other variables. But there could be a way to solve the jumble, if we
can detect a general "outflow" of this graph from which a certain
node(s) point to other nodes more. We are looking for cascading
effects too, if A effects B which effects C, A's influence is greater
than B.

Description above sounds like PageRank but we actually need its
reverse, called CheiRank. PR is for incoming links to a node (page),
we need outgoing links (influences) from a node. We can simply reverse
graph and compute PR.

---

I believe it will look like that below

<img width='200' src='mbl/2025/argfin1.jpg'/>

---

Focusing on highly significant ones, we could create a dependency graph 

```python
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ('i', 'E'),
    ('i', 'pi'),
    ('E', 'pi'),
    ('E', 'cab'),
    ('cab', 'pi'),
    ('cab', 'i'),
    ('pi', 'cab'),
    ('pi', 'E')
])

nx.draw(G,with_labels=True,node_size=2500)
plt.savefig('argfin1.jpg')
```

---

We could retrieve causal significance between all pairs of variables (lower is better)

```python
import statsmodels.tsa.stattools as t, itertools
vars = ['E','i','cab','pi']
gr = [(x,y,t.grangercausalitytests(df[[x,y]],maxlag=1,verbose=False)) for x,y in itertools.product(vars,vars) if x!=y]
```

```python
[(x,y,list(tmp.values())[0][0]['ssr_ftest'][1]) for x,y,tmp in gr]
```

```text
Out[1]: 
[('E', 'i', np.float64(0.0002792139878687578)),
 ('E', 'cab', np.float64(0.9979766387184925)),
 ('E', 'pi', np.float64(2.215610311531833e-09)),
 ('i', 'E', np.float64(0.28212834795173775)),
 ('i', 'cab', np.float64(1.0739219996856827e-05)),
 ('i', 'pi', np.float64(0.7974862665835333)),
 ('cab', 'E', np.float64(9.775588747152808e-05)),
 ('cab', 'i', np.float64(8.341879238550786e-37)),
 ('cab', 'pi', np.float64(1.599736120930462e-09)),
 ('pi', 'E', np.float64(2.9549773728066783e-47)),
 ('pi', 'i', np.float64(6.99784340132411e-50)),
 ('pi', 'cab', np.float64(2.7202463202869524e-07))]
```

---

The variables are

- Interest Rate (i)
- Inflation (pi)
- Current Account Balance (CAB)
- Exchange Rate (E)

We could look at some data.. (below).. For Argentina,

```python
import pandas as pd
df = pd.read_csv('arg-fin.csv',index_col='date')
df[['cab','E','pi','i']].corr()
```

```text
Out[1]: 
          cab         E        pi         i
cab  1.000000  0.202825  0.124310  0.085886
E    0.202825  1.000000  0.957765  0.832089
pi   0.124310  0.957765  1.000000  0.936008
i    0.085886  0.832089  0.936008  1.000000
```

CAB and E are pretty highly correlated.. but how about causation?

[Data](https://www.dropbox.com/scl/fi/f7yr0c48zz3zgoqcutv8w/arg-fin.csv?rlkey=lju20eubk9lxzs1gdb21u8fu8&st=a19ro1le&raw=1)

---

Which of the variables have a causal relationship? Interest Rate,
Inflation, Current Account Balance, Exchange Rate. Good question

---

Ethan Peck so wants to get out of that SNW shit show, he'll take any
role in movie biz. He had a small supporting role in *The Unholy
Trinity* (good work)... he'll quit the sad role they fashioned for him
the moment he makes it in big at movies imo.

---

I thought *Strange New Worlds* was getting little better, but I
watched first ep of new season, it sucked.

---

Neolib playbook says supply-sider actions "pay for themselves" by
"spurring growth". That clearly did not work here. FR state lost
revenue, and it is now in financial dire straits.

---

"[T]he French corporate income tax (CIT) rate has gradually decreased
from the original rate in 2017, a rate of 33.3%, to 2022, now a rate
of 25% (a drop of 8.3% in five years)."

---

The question is why is France in debt

---

NYT: "France Proposes Cutting Two Public Holidays to Avert Budget
Crisis.. Drastic measures are necessary “before we are crushed by the
debt,” the country’s prime minister warned."

---

BBC: "UK and 27 nations accuse Israel of 'drip feeding' aid to Gaza
civilians as they condemn 'horrifying' killings"

---

"Aaron Bastani Meets Jean-Luc Mélenchon"

[[-]](https://youtu.be/6WFTiA_H67g?t=3294)

---

"How 5 Companies Are Keeping The World At War"

[[-]](https://www.youtube.com/embed/lDB3L23UMCQ?start=242&end=652)

---

Stephen Gruyère is being let go? I don't think Gruyère is fired for
being not funny, he has been not funny for a while now and they still
kept him. But he platformed Mamdani, that could've triggered his
firing.. In corporate mindset he exercised the ultimate sin - gave the
enemy a chance.

---

The Lever: "So much for preventing government waste. After months of
warnings from federal workers were ignored, 500 metric tons worth of
emergency, high-nutrition biscuits intended for global disaster relief
are instead marked for incineration, The Atlantic reports. Thanks to
the Department of Government Efficiency, which all but eliminated the
U.S. Agency for International Development, routine foreign aid
expenses — including deliveries — now require approval from the very
top. Yet employees’ requests to distribute the biscuits were ignored,
and now they're nearing expiration, leading the Trump administration
to order their incineration."

---

Yandex Translate by Image works well.. It finds words in image
translates them, even overlaying the translated text on top, in place
of the foreign text.

[[-]](https://translate.yandex.com/en/ocr)

---

Thoughts and prayers to you asshole

HTW: "Israeli PM Netanyahu falls ill with food poisoning, to work from
home for three days"

---

"ZeroAvia scores 45 fresh patents for hydrogen aviation
engines.. Aviation startup ZeroAvia says it’s been granted a “raft” of
45 new patents key to the development of practical large hydrogen
aviation engines – and the company says it has 200 more H-related
patents in the pipeline!

The news comes just weeks after ZeroAvia and Scottish regional airline
Loganair announced a new, hydrogen-electric “turboprop” replacement
motor capable of up to 5MW of shaft horsepower (~6,700 hp). United
States Patent and Trademark Office (USPTO) no. 12,341,225 covers an
integrated hydrogen-electric engine design land is key to the
development of a modular multi-MW hydrogen-electric engine for the ATR
42 and 72 model aircraft — which Loganair owns more than twenty of."

---

The Lever: "Affordable Care Act (ACA) marketplaces across the country
are projected to see the largest rate hikes in more than five years,
driving up out-of-pocket premiums for individual plan policyholders by
more than 75 percent on average, according to data compiled by the
Kaiser Family Foundation. More than 21 million Americans who don’t
have employer-sponsored health insurance rely on the ACA marketplace
for coverage."

---

DJT net approval reaching the previous record low. The Epstein saga is
surely partly to blame. The subject was incredibly clumsily handled.

[[-]](https://cdn.fosstodon.org/media_attachments/files/114/886/305/349/113/191/original/951aabf3c1917aa6.jpg)

---

IC: "Huckabee and MTG attack Israel over anti-Christian Pogroms"

---

\#Ukraine

07/07 - 07/18

[[-]](ukrdata/map27.html)

---

"How WW1 Created the Middle East Conflicts"

[[-]](https://m.youtube.com/watch?v=tjnBmH8b0Ko)

---

\#Xi \#China

[[-]](https://youtu.be/D-YSUTNj17M?t=44)

---

These neolib pro-market dimwits truly have no other trick than this
supply-sider bullshit. The 'letting banks offer higher-risk mortgages
to borrowers' sounds too pre-2008.

Here we see the result of confining self to a smaller solution set.
They decided *not* to rebalance wealth inequality from get-go, well,
what is left to play with?

The iPaper: "[Chancellor] Reeves wants your savings on stock
market.. The Chancellor pledged to take a more pro-risk approach to
regulations in a bid to boost economic growth.. As well as announcing
laxer financial regulations, for example letting banks offer
higher-risk mortgages to borrowers on modest incomes, the Chancellor
insisted that 'it is clear that we must do more', adding: 'In too many
areas, regulation still acts as a boot on the neck of businesses,
choking off the enterprise and innovation that is the lifeblood of
growth'"

---

"@GossiTheDog@cyberplace.social

My opinion on $1bn being defunded from US cyber defence budget and 1bn
being added added to US cyber offense budget:

People don’t even know what Netscalers they own.  That’s the reality.

Critical US gov systems aren’t patched almost a month in despite
binding orders to patch.

If US start attacking other countries, US citizens will end up dealing
with impacts of ransomware, wipers etc - defense just isn’t strong
enough."

---

ProPublica: "Since 2011, cloud computing companies that wanted to sell
their services to the U.S. government had to establish how they would
ensure that personnel working with federal data would have the
requisite 'access authorizations' and background
screenings. Additionally, the Defense Department requires that people
handling sensitive data be U.S. citizens or permanent residents. This
presented an issue for Microsoft, which relies on a vast global
workforce..

Microsoft’s foreign workforce is not permitted to access sensitive
cloud systems directly, so the tech giant hired U.S.-based 'digital
escorts,' who had security clearances that authorized them to access
sensitive information, to take direction from the overseas
experts. The engineers might briefly describe the job to be completed
— for instance, updating a firewall, installing an update to fix a bug
or reviewing logs to troubleshoot a problem. Then the escort copies
and pastes the engineer’s commands into the federal cloud.

The problem, ProPublica found, is that digital escorts don’t
necessarily have the advanced technical expertise needed to spot
problems.

'We’re trusting that what they’re doing isn’t malicious, but we really
can’t tell,' said one current escort."

---

All TR needs to do is replacing the defunct current identity with a
new culture / geo based citizen label.

---

SDF (Kurds in NE Syria) rebuff Syria integration. Hadn't US picked up
the SDF leader Abdi by helicopter bringing him to Damascus for a deal
back in March? What happened to that deal?

Ambassador Tom Barack (to TR), seemingly calling the shots on Syria,
talks about Syria integration, tells SDF to watch their step. Perhaps
encouraged by that HTS attacks Druze, the smaller problem, testing the
waters for the big fish (the Kurds). Then Israel responds to that with
an attack on Damascus, HTS.

TR talks Syria integration, but internally gets ready to elevate
Kurdish, Arab identity at its own state level which makes people think
they are making TR palatable for Syrian Arabs and Kurds so they can be
swallowed up one day. Former TR Kurdish seperatist leader Ocalan looks
to be on board with that.

Is TR fomenting trouble by talking integration, causing chaos, then
preparing for an easier meal later?

Some in TR label now as a "foundational moment" where a new nation is
born, ushering in more representation and democracy. But major
opposition leader is in jail, along with others who could cause
trouble.

It is also not clear how while demoting a defunct identity
(Turkishness) elevating minority groups in their place a la Lebanon
can make things better. To see the result of that we can just look to,
well, Lebanon. Will there be a Sunni party, Alevite party, Kurd party
and during election time Sunnis vote for the Sunni party, Kurds for
the Kurd party, so on, and that can promote a merit based governance?

---

The Lever: "How Republicans Rejected A Texas Flood Warning
System.. Lawmakers spent years rejecting Kerr County’s demands for a
disaster warning system."

---

TASS: "Pakistani PM asks Putin to help resolve conflict with India"

---

TASS: "Trump hopeful Gaza ceasefire deal can be 'straightened out'
within a week"

---

AUKUS was a stupid deal..

The Guardian: "Pentagon launches review of US-UK-Australia Aukus
security alliance.. Future of $240bn defense pact in doubt as Trump
administration reviews it to see if it aligns with ‘America first’
agenda"

---

Trump says once (on self-driving cars) "we will not allow those things
on American roads". Notice the word *American* roads, which supposedly
gives the opposition a nationalist (rightist) character. But, the car
is American, its producer is American, its software is American.  The
issue is already within national boundaries. The faux right-wing
characterization falls flat on its face.

---

I remember some in MAGA were against self-driving cars bcz it would
steal jobs from the working class. So.. you are against a business
interest?

---

Politico: "How the GOP Regulars Won Over Donald Trump.. Much has been
made of Trump’s lock-step mastery of Congress, but House and Senate
leaders still set the boundaries... Projecting American force against
the country’s traditional adversaries in concert with U.S. allies and
signing a tax bill that nearly could have been written by the Wall
Street Journal editorial page, Trump demonstrated that the GOP still
defaults to a muscular abroad and business-friendly at home posture."

---

MAGA is in the wrong party. They try to package economic left with
nationalism (it sounds right-wing), but doesn't always work. The
ideology is internally inconsistent.

---

DJT wanted to tax the rich but the Rep congress clearly nixed the idea

[[-]](https://www.reuters.com/world/us/trump-says-he-is-ok-with-republicans-raising-taxes-rich-2025-05-09/)

---

MAGA has economic left elements in it. The official left needs to take
them back.

---

Two types of people, who otherwise could like it, bash on this movie.
One is Zaslaw haters who killed Woke at WB. Other is neocon,
anti-government pro-rich billionaire bootlicker section of the
right-wing because billionaires were made to look bad in this movie
(via Luthor). Both groups will be crushed at the box office and they
will be sorry.

---

Cornsweat version is more relatable and still strong male. I saw him
in the recent Twister movie, he played it butch... That's when I knew
he could pull off the new role.

---

Cavill depicted a warrior-like SM version. Snyder likes that stuff
anyway (director of *300*). He likes the epic, stoic,
brooding.. Cavill is like from south Britain right, a Catholic,
basically a paisan a Mediterrenian Superman, we consider him as one of
us... He did a Greek warrior movie before too.. This new guy is more
apple pie, it fit the hopeful, sunny new tone.

---

"@elithebearded@fed.qaz.red

.. 'Stereotype' is a printer's term. Moveable type is expensive. You
don't want to keep it tied up longer than needed, so you make a mould
from the set type and cast a plate from that.

The 'stereotype' is the mould.

A 'cliché' is what the French called plate made from that mould, it's
onomatopoeia from the sound of removing the plate from the mould.

'Boilerplate' is widely repeated text from the round stereotype
castings of newspaper columns ready to throw on a drum press."

---

```python
u.boxofficemojo("Superman")
```

```text
Out[1]: 
{'Domestic Opening': '$122,000,000',
 'Domestic': '$122,000,000',
 'International': '$95,000,000',
 'Worldwide Total': '$217,000,000'}
```

I am looking forward for more movies from this universe.

---

Gunn's Supes was good. This character's problem was mostly being
unrelatable. Gunn made him relatable, the hero is beaten down a lot
but gets up, continues.. To stress the point Gunn even made SM give a
"I am relatable" speech ("I am human", "just like you"!). There was
spectacle, the film provided sufficient grandiosity in its action,
scenery to entice more asses on more seats, likely triggering
word-of-mouth.

---

Levant24: Ongoing negotiations between the Syrian government and the
US-backed Syrian Democratic Forces (SDF) have hit a roadblock, with
officials and sources close to the talks blaming the impasse on the
SDF’s unwillingness to compromise on key issues outlined in the March
10 agreement.

Despite active mediation by US Special envoy to Syria Tom Barrack, and
the participation of European observers, including France, the latest
round of discussions concluded without major breakthroughs. According
to sources speaking to Levant 24, the government reiterated its
commitment to national unity and the integration of all local
institutions and military forces under a centralized Syrian state,
while rejecting demands for decentralization or federalism.

A One-Sided Stalemate

The SDF, continues to insist on preserving its military structure and
advancing its model of decentralized governance in northeastern
Syria. Damascus views these positions as incompatible with Syrian
sovereignty and the provisions of the agreement signed in
March between President Ahmad al-Shara and SDF commander Mazloum Abdi.

---

Netanya is a stooge of the private complex. He does their bidding,
creates "demand" for their products, in return he is greeted as a
champ in Washington even though he has innocent people's blood in his
hands.

---

NYT: "We found that at key stages in the war, Netanyahu’s decisions
extended the fighting in Gaza longer than even Israel’s senior
military leadership deemed necessary. This was partly a result of
Netanyahu’s refusal — years before Oct. 7 — to resign when charged
with corruption, a decision that lost him the support of Israel’s
moderates and even parts of the Israeli right. In the years since his
trial, still ongoing, began in 2020, he instead built a fragile
majority in Israel’s Parliament by forging alliances with far-right
parties. It kept him in power, but it tied his fate to their extremist
positions, both before the war and after it began.

Under political pressure from those coalition allies, Netanyahu slowed
down cease-fire negotiations at crucial moments, missing windows in
which Hamas was less opposed to a deal. He avoided planning for a
postwar power transition, making it harder to direct the war toward an
endgame. He pressed ahead with the war in April and July 2024, even as
top generals told him that there was no further military advantage to
continuing. When momentum toward a cease-fire seemed to grow,
Netanyahu ascribed sudden significance to military objectives that he
previously seemed less interested in pursuing, such as the capture of
the southern city Rafah and later the occupation of the Gaza-Egypt
border. And when an extended cease-fire was finally forged in January,
he broke the truce in March in part to keep his coalition intact."

[[-]](https://www.nytimes.com/2025/07/11/magazine/benjamin-netanyahu-gaza-war.html)

---

Dessler: "Texas flood was a warning about climate change... The
physics is straightforward: For every degree Celsius our planet warms,
the atmosphere holds about 7% more water vapor. When a storm occurs in
our warmed world, the air converging into the storm carries more
moisture, leading to more intense rain events. In fact, “more intense
rainfall” is one of the oldest predicted consequences of climate
change and has since been confirmed in observational datasets."

---

They feed you toxic corporate food, then sell you corporate toys to
profit from the resulting condition.

"Barbie launches doll with type 1 diabetes in a bid for ‘inclusivity
and representation’.. Mattel launches Barbie doll with type 1 diabetes
to promote inclusivity and representation for children with the
condition."

---

"@Natasha_Jay@tech.lgbt

Why do we say 'slept like a baby'? Babies wake up every two hours
crying.

I want to sleep like my cat. 14 hours, no responsibilities, zero
regrets."

---

*Iron Heart* is ok... entertaining. A. Ramos, Thorne were cast
well. The show is properly diverse, not annoyingly Woke.

---

Saw *Thunderbolts* - not a good movie, that means reviews were
misleading (*rotten*).

---

United Nations: "This report investigates the corporate machinery
sustaining Israel’s settler-colonial project of displacement and
replacement of the Palestinians in the occupied territory. While
political leaders and governments shirk their obligations, far too
many corporate entities have profited from Israel’s economy of illegal
occupation, apartheid and now, genocide. The complicity exposed by
this report is just the tip of the iceberg; ending it will not happen
without holding the private sector accountable, including its
executives."

[[-]](https://www.un.org/unispal/document/a-hrc-59-23-from-economy-of-occupation-to-economy-of-genocide-report-special-rapporteur-francesca-albanese-palestine-2025/)

---

\#Sudan 06/01 - 07/10

Not much going on, RSF lost a little more.. Except.. what's with that
new little RSF area in the North?

[[-]](sdndata/map05.html)

---
