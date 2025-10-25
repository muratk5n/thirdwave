# Week 42

James Ellars: "The idea of having to 'earn a living' implies that, by
default, you don't actually deserve to be alive."

---

Buckminster Fuller: “We should do away with the absolutely specious
notion that everybody has to earn a living. It is a fact today that
one in ten thousand of us can make a technological breakthrough
capable of supporting all the rest. The youth of today are absolutely
right in recognizing this nonsense of earning a living. We keep
inventing jobs because of this false idea that everybody has to be
employed at some kind of drudgery because, according to Malthusian
Darwinian theory he must justify his right to exist. So we have
inspectors of inspectors and people making instruments for inspectors
to inspect inspectors. The true business of people should be to go
back to school and think about whatever it was they were thinking
about before somebody came along and told them they had to earn a
living.”

---

Social media companies run analysis like the one below all the
time. It's pretty standard. In order to suggest friends, they can look
for central characters, look for cliques,..

---

Mark Weinberger, no.. the ring leader cannot be Jew, it has to be Anglo.
The tail does not wag the dog. 

---

If I had to pick a shadowy surface state ring leader / MIC decision
maker from this list, I would chose Ronald D. Sugar or Alex Gorsky.

---

Betweenness centrality measures how often a corporate board director
lies on the shortest path between two other directors. A high score
identifies critical connectors or "brokers" who bridge different,
otherwise separate groups of directors/companies. People with the
highest influence would appear in the list.

---

```python
centrality = nx.betweenness_centrality(G)
centrality_by_name = {
    G.nodes[director_id].get('name', director_id): score
    for director_id, score in centrality.items()
}

sorted_centrality = sorted(
    centrality_by_name.items(), 
    key=lambda item: item[1], 
    reverse=True
)

print(f"Total directors (nodes) in the graph: {G.number_of_nodes()}")
print(f"Total connections (edges) in the graph: {G.number_of_edges()}")
print("\nTop 10 Directors by Betweenness Centrality:")
top_10_centrality = dict(sorted_centrality[:10])
print(json.dumps(top_10_centrality, indent=4))
```

```text
Total directors (nodes) in the graph: 530
Total connections (edges) in the graph: 3131

Top 10 Directors by Betweenness Centrality:
{
    "Timothy P. Flynn": 0.19139407768467753,
    "Alex Gorsky": 0.17909671845915184,
    "F. William McNabb III": 0.16453952077340997,
    "William Kennard": 0.1621896758007987,
    "Monica C. Lozano": 0.14874907198276752,
    "Mark Weinberger": 0.1377558993440156,
    "Wayne Hewett": 0.1365517916895944,
    "Ronald Sugar": 0.13566760923211765,
    "Marillyn Hewson": 0.10746758774663069,
    "Linda Gooden": 0.09421774253843748
}
```

These are the central figures... 🤔 Who are they?

---

The network

```python
from itertools import combinations
import hjson, networkx as nx, json

with open('theyrorgs.json', 'r') as f:
    orgs_data = hjson.load(f)
    
with open('theyrdirs.json', 'r') as f:
    dirs_data = hjson.load(f)
G = nx.Graph()

organizations = orgs_data.get('Orgs', {})

for org_id, org_info in organizations.items():
    director_ids = org_info.get('d', [])
    for director1_id, director2_id in combinations(director_ids, 2):
        G.add_edge(director1_id, director2_id)
directors = dirs_data.get('Dirs', {})
name_mapping = {
    dir_id: dir_info.get('n', dir_id) 
    for dir_id, dir_info in directors.items()
}
nx.set_node_attributes(G, name_mapping, 'name')    
```

---

If two people are sitting on the same board, we assume them
"connected", create the whole structure that way and run the rest of
the computation on that graph.

---

I always wanted to analyse data from the *They Rule* site
(theyrule.net), the site that tracks corporate boards and the members
on them. It turns out their raw data is in a Javascript file, in
`/static/js/main.6ef84500.js`.  Reverse engineered it - [orgs](mbl/2025/theyrorgs.json), [directors](mbl/2025/theyrdirs.json).  
With a little preprocessing, you create the social graph via
`networkx` and process its connections.

---

TAC: "Putin Meets Syria’s al-Sharaa, a Former Enemy, in Moscow"

---

Perhaps that will help in their assimilation.. well, they are already
assimilated actually, I mean will help with them *accepting* their
assimilation more, realizing they do not constitute a seperate,
identifiably distinct culture within another. According to Clotaire
Rapaille cultural transmission does not occur through ritual, or
assuming labels, it is organic and takes place through osmosis.

I believe Jews who do not accept their assimilation (a big source of
neuroticism) also provide an attack vector for Israeli propaganda, and
indirectly the fearsome military-industrial complex. Less of an attack
vector, the better for the world.

WaPo: "More U.S. Jews shield identity in public amid antisemitism
fears, Post poll finds.. A third of U.S. Jewish people say they don’t
feel safe, and two-thirds report seeing antisemitic content online at
least once a month"

---

Finance guy talking down USDT and similar stablecoin approaches..  "It
is backed by nothing which is backed by nothing". He is refering to US
treasuries which are backed by the US dollar. Both are "nothing" in
his view.

---

The Bond King speaks. This is not a drill.

CNBC: "[09/17] DoubleLine’s Jeffrey Gundlach believes holding a 25%
gold position isn’t excessive"

---

The aid flotillas were a PR nightmare for Israel. I'm glad they
attempted to reach Gaza and did not give up.

IC: "[T]he Sumud Flotilla also deserves credit for creating momentum
for the ceasefire.. Sumud began as a small fleet of hope — dozens of
boats carrying activists, doctors, and humanitarian cargo, setting
sail from ports around the world to challenge Israel’s blockade on
Gaza.

Now, after months of confrontation, detention, and diplomatic fallout,
the flotilla’s central message has unexpectedly materialized in
political reality: Israel and Hamas have agreed to a provisional
ceasefire that will allow humanitarian aid to flow freely into Gaza
and has facilitated the release of hostages and prisoners."

---

TAC: "Trump Hails 'Historic Dawn' of a New Middle East in Knesset
Speech.. The president vowed continued American support for Israel
while saying “the hand of friendship” is open toward Tehran."

---

TAC: "Trump’s Pressure on Sanctuary Cities Is Working.. The
foreign-born population in the United States declined by an
unprecedented 2.2 million in the first half of 2025."

---

The Lever: "Anthony Kennedy Is Trying To Find The Guy Who Did
This.. The retired Supreme Court Justice who authored Citizens United
is suddenly worried about the future of democracy."

---

Considering the zeitgeist is Nazism the right focus for this cinematic
universe? Extreme right-wing is not the main problem for US, or the
world, extreme wealth inequality caused by errant neoliberalism is.  A
destroyed middle-class can be led towards various outlets, fighting
symptoms is not helpful.

---

Overman was literally raised by Adolf Hitler, according to DC canon.

---

Peacemaker S2 characters were off.. like Grillo's role. Is he being
set up for something bigger (it's not him, it is an impersonator)? His
son, is he Overman (the Nazi Superman) in his universe? Not a big fan
of 'other dimension' tropes, but if the storytelling is good enough,
one could go along... PM S2 fell short there.

---

"@GossiTheDog@cyberplace.social

@canacar I don’t know if you’ve used the new Vibe Working feature, but
here it is. The data is all fabricated."

[Image 1](https://cyberplace.social/system/media_attachments/files/115/369/299/487/890/190/small/ce77356ce70a78fc.jpeg),
[Image 2](https://cyberplace.social/system/media_attachments/files/115/369/299/931/281/516/small/9af4df5fc81eeca2.jpeg),
[Image 3](https://cyberplace.social/system/media_attachments/files/115/369/300/242/728/844/small/548bd8557f615188.png),
[Image 4](https://cyberplace.social/system/media_attachments/files/115/369/300/660/964/330/small/aa863287ed52ffa2.png)

---

"@GossiTheDog@cyberplace.social

If you stand back and think for a moment, orgs.. added Copilot at $30
per user per month (more than their cyber spend), then rolled out
Copilot “vibe working” feature to produce fake briefing docs,
presentations and Excel packs based on zero subject knowledge and fake
data.. so they can buy the products it suggests while defunding
security, IT etc.

It’s properly nuts and very exciting and super dumb."

---

That is star power 

```python
u.boxofficemojo("F1: The Movie (2025")
```

```text
Out[1]: 
{'Domestic Opening': '$57,001,667',
 'Domestic': '$189,527,111',
 'International': '$439,300,000',
 'Worldwide Total': '$628,827,111'}
```
---

The movie made *some* money.. let's be fair. And it did this without
any star power...

```python
u.mov_profit(budget=225, gross=615)
```

```text
Out[1]: 31.5
```

---

```python
u.boxofficemojo("Superman")
```

```text
Out[1]: 
{'Domestic Opening': '$125,021,735',
 'Domestic': '$354,184,465',
 'International': '$261,800,000',
 'Worldwide Total': '$615,984,465'}
```

---

TASS: "Gold price hits a new all-time high, topping $4,200 per troy
ounce"

---

F24: "Coral reefs cross survival limit, in Earth's first catastrophic
climate tipping point"

---

The Lever: "Ticketmaster and its parent company Live Nation
Entertainment have drawn the ire of consumers — and the Federal Trade
Commission — for exorbitant ticket prices, misleading hidden fees, and
shady resale tactics. But losing your right to sue Ticketmaster or
join a class action lawsuit is now just a click away. Hiding in the
company’s new terms-of-use agreement, The Lever found a clause that
forces ticket buyers into arbitration, a private judicial system
rigged in favor of the company."

---

Allowing lawsuits.. that is a big deal.

F24: "Newsom on Monday signed the nation’s first law regulating
artificial intelligence chatbots.. The measure requires chatbot
operators to implement safeguards for user interactions and allows
lawsuits if failures cause harm, state senator Steve Padilla, the
bill’s sponsor, said."

---

Politico: "Shutdown polls show Democrats’ economic messaging still
falling flat"

---

Reshare

\#LPPFusion \#EricLerner \#OilGasComplex

[[-]](https://youtu.be/0sQ4Xa5z_oc?t=640)

---

"US Justice Department opens inquiry into First Brands
collapse.. First Brands, which makes filters, brakes and lighting
systems for the automotive industry, filed for bankruptcy protection
last month after its lenders began investigating irregularities in the
company's financial reporting. The company has $11.6 billion in total
liabilities..

Financial troubles at First Brands and the recent bankruptcy of
subprime lender Tricolor Holdings, have rattled debt investors and
stoked fears of broader stress in corporate debt markets, according to
bondholders and bankruptcy experts. Some of the financial firms
exposed to First Brands include Jefferies (JEF.N), opens new tab,
which disclosed $715 million in exposure through Leucadia Asset
Management, and UBS (UBSG.S), opens new tab, which is assessing
exposure on more than 500 million tied to the company."

---

TASS: "Attempt to steal Russian assets will result in EU counting its
losses.. According to Russia's Ambassador.. the response will be
proportionate"

---

IC: "Rashid Khalidi on the Gaza Ceasefire: The veil that has hidden
the true nature of the Zionist project was shredded for good"

---

Hindustan Times World: "Biden hails Trump after Hamas hostages'
release, ‘The road to this deal was not easy’.. Joe Biden commended
Donald Trump after all 20 Hamas hostages were released, saying he is
'deeply grateful and relieved that this day has come.'"

---

NYT: "A Test Now for Israel: Can It Repair Its Ties to
Americans?.. Israel’s advocates fear that its conduct of the war has
cost it the support of an entire generation of U.S. voters"

---

"@brucelawson@vivaldi.net

Anthropic stole the books I co-wrote in order to train their
planet-burning hallucination machine, so I've filed a claim. They wept
that if every plagiarised author does so, the company will go
bankrupt. Boo emdash hoo."

---

Potential experiments that can be performed to prove aether's
existence

[[-]](../../2025/10/masse3.html)

---

Some allow the conversational smarts of "AI" fool them. There are
still many things LLMs cannot do. LLM / neural net approach to AI is
one among many.

---

Dude rides scooter from Paris to Manoco, makes vlog on Youtube. Day 2,
"I made a huge mistake, this is what you get for using AI to plan your
route". He was led astray. Went to completely wrong directions thanks
to AI.

---

Is the Nobel commitee captured by the US corporate complex (esp. its
military wing)? Trump was expecting an award but it was given to an
opposition figure in Venezuella, a country US is signaling it might
invade. It's like the commitee told Trump "you wait in line, prove
your worth to us, if you invade Venezuella maybe you get your award
next year 'for bringing peace and democracy' to Venezuella"

---

The American Conservative: "[E]vents are swinging [Venezuellan
opposition figure] Machado’s way.. The latest coup comes with her
acquisition of a Nobel Peace Prize, for showing 'that the tools of
democracy are also the tools of peace' — a description that may go
down as one of the more ironic tributes, as Machado has been quick to
turn her Peace Prize award into one more weapon of war."

---

I always keep dehydrated turkey (turkey jerky!) somewhere, DIY
dehydrated product. Maybe it's my inner prepper. I keep "fruit
leathers" too this one I purchase but could make. 

---

But Zaslaw got what he wanted from Gunn; little excitement, little
extra shine on the DCU property before it is handed over to someone
else.

---

S2 is too quirky and some characters are not appealing, their writing
seems to have made them even dumber and less appealing. Show dabbles
in the shallow, the crass, often in S2... "Needle drops" are overdone,
too many slow mo walks w/ the backdrop of some overly exciting music.

---

Peacemaker S2 wasn't as good as S1. The second season was more like
the Gunn stuff I don't like, which is basically all his work except PM
S1 and Supes.

---

Crysis is a ref to an FPS game

---

Difference btw two graphs tend to increase before Crysis

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/115/365/536/814/627/273/original/189d781c57d65e8a.png'/>

---

How could stablecoin become every day currency? Organically, slowly
perhaps, or a crisis can be invented, ATM's can be down, banking
network is clogged / attacked, there is an artificial panic.. boom.
People are channeled towards this new thing, "hey it is safer". The
switch is made.

---

Right. Their tokens are backed by treasuries, the more they issue the
more treasuries they have to buy.. And now imagine stablecoins
becoming everyday currency, as in all your spending having to go
through them.. That would generate massive demand for stablecoins
therefore US debt / treasuries, wouldn't it?  Then you monetize in the
back end, $35 trillion debt, poof. Gone.

---

Fortune: "[8/9] Stablecoin issuers like Circle and Tether are gobbling
up more Treasuries than most countries"

---

\#Ukraine 10/05 - 10/13

[[-]](ukrdata/map39.html)

---

$35 trillion of debt would be a driving factor. USG could say "we
can't pay this whole thing, we will pay back only half". But that
would create panic. Via the stablecoin scheme they will spread the
debt across time, across people, turning it into everyday money, then
they can monetize this debt/money instrument at any pace they want.

---

If the US stablecoin scheme spreads all over the world, it will create
even more demand for US debt, but when the US devalues, those
countries could end up suckers, they'd pay 100 but end up with 50
worth of "stablecoin" value. The scheme has a certain appeal from US
POV. But I agree with "the rest" suspecting it, smelling something
fishy.

---

He must be referring to a recent crypto bill... it says USG will
support short-term bond / cash backed "stablecoins", the coins are
backed with US debt, US bond one-to-one, so they are legally stable
hence the name. That can help USG: If such stablecoins, eg USDT,
become widely used in US as digital money, every coin holder would
automatically become the holder of US debt, gov would be creating
massive demand for its debt, its financing becomes easier.

Reportedly there is another leg for this scheme, banks have about 4
trillion of dollars sitting at the FED, currently kept out of the
circulation, sitting there only to balance their books. The new bill
will allow the use of that cash for the issuence of new stablecoins
and that will certainly cause the dollar to depreciate. The
speculation continues, other countries sensed this coming, they are
dumping the dollar, piling up non-US assets like precious metals at a
rapid pace bcz even though there is no official "money printing" the
use of that cash is still debt monetization and more of it can arrive
later.

---

Yahoo Finance: "[9/8] Putin Advisor [Kobyakov] Accuses US of Using
Crypto, Gold to Escape Massive Debt.. According to Kobyakov, the
U.S. will ultimately place its debt into stablecoins and then devalue
it... 'Put simply: they have a $35 trillion currency debt, they’ll
move it into the crypto cloud, devalue it—and start from scratch,' he
said. 'That’s the reality for those who are so enthusiastic about
crypto'"

---

Year 2000 people who thought they had a good chance of improving their
standard of living was at about 70%. In 2015 the percentage fell to
50%. It is now at 25%. These numbers correlate with rising wealth
inequality in the populace. As a consequence few think working hard
will get them anywhere in life. The system is rigged against them.

---

A poll with the title / question: [do you think you have a] good
chance of improving [your] standard of living.  Source: Wall Street
Journal - NORC Surveys. Data replicated below.

```python
import pandas as pd, io
data = """
Year,Agree (%),Disagree (%)
1990,68,32
1995,58,42
2000,72,28
2005,65,35
2010,55,45
2015,50,50
2020,58,42
2025,25,75
"""
df = pd.read_csv(io.StringIO(data),index_col='Year')
df['Agree (%)'].plot(kind='bar')
plt.xticks(rotation=45, ha='right')
```

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/115/348/905/813/672/929/original/9974c7a8a81a20c6.jpg'/>

---

Gizmodo: "[08/22] Bank Fires Workers in Favor of AI Chatbot, Rehires
Them After Chatbot Is Terrible at the Job"
 
---

TechRepublic: "[05/19] ‘We Acted Too Quickly’: Over Half of Companies
Regret AI-Driven Layoffs, Report Finds"

---

\#LPPFusion \#EricLerner \#OilGasComplex

[[-]](https://youtu.be/0sQ4Xa5z_oc?t=640)

---

Summary: The US bombing of Serbs was a show, to cover up the Bosnian
concessions made to them later. I would not expect anything less from
a Clinton.

\#HarryBlain \#NeutralityStudies

[Excerpt 1](https://www.youtube.com/embed/-v5nnhsBXiI?start=125&end=297),
[Excerpt 2](https://www.youtube.com/embed/-v5nnhsBXiI?start=1309&end=1767)

---

Some notes from Robert Masse's criticism of the Copenhagen
Interpretation of QM

[[-]](../../2025/10/masse2.html)

---

Hinton, "the godfather of AI" is mostly talking out of his ass these
days.. What happened to one innovation of his, the so-called
"capsules"?  He had declared regular NN aproaches dead back in 2017
and was promoting it ad nauseam, capsules, that would revolutionize
everything... it didn't go anywhere. His best days are clearly behind
him. He is a just a rambling man now.. talking crazy.

---

"Long considered a system reserved for insiders, Linux is experiencing
a real boom in France. According to an analysis.. based on web traffic
data published by Cloudflare Radar, more than 2.2 million French
people regularly use Linux on their personal computers"

---

It needs to be stressed, LLMs operate in a "latent space", in the
compressed knowledge representation of the world, and when asked
something they can *always* generate something from that latent
space. I can factorize a matrix $A$ into various components even with
missing data, get a "reduced dimension" representation, and always
recreate the whole matrix from those components even fill in the
missing values whether the prediction is completely right or not. The
generation can be close, but not always necessarily accurate. This is
what they mean when the hallucination is embedded in the math.

---

Retrieval-Augmented Generation is a good idea.. you can have LLM index
your personal notes, personal documents (obviously orgs can do the
same on their internal knowledge base), just like LLMs indexed the
whole Internet and books, they can just add your stuff on top of that,
then you can "ask", or query that knowledge base silo in plain
English.

---

LLM is glorified search.. LLMs are ok at that, I never said they
weren't, but remember for regular search we don't expect perfection,
or crazy accuracy, simply the top 10 or 20 items be relevant, same is
true here.

---

Computerworld: "OpenAI admits AI hallucinations are mathematically
inevitable, not just engineering flaws"

---

Bloomberg: "Ferrari Scales Back Electric Ambitions"

---

The Guardian: "About 5 million British computer users risk becoming
vulnerable to cyber-attacks and scams after Microsoft next week stops
updating its decade-old Windows 10 system, consumer campaigners have
warned.

One in four of an estimated 21 million UK people using a device that
runs the Windows 10 software intend to continue using it after updates
cease and so will be at risk of online security breaches including
malware and viruses..

The most straightforward move is to update to Windows 11 for free. If
your PC is less than four years old, it is likely to work [but some
hardware might not be enough to run 11] ...

Another solution is to convert your computer to a different operating
system, such as Linux or Google’s Chrome OS."

---

The actress is not Israeli herself, she is a chica. LatinX.

---

NCIS has a new spinoff, *NCIS Tony and Ziva*. The character Ziva is an
Israeli. Is this part of an attempt to make the Zio look good again?

---

Truth Social exists thanks to FOSS. They took their base code from
Mastodon. Every time Il Duce posts a message on TS he is expressing
how much he likes software socialism.

---

The Internet boom of post 90s would be impossible if it had to rely on
Oracle, Microsoft commercial packages alone... Having a free software
stack as an alternative (now the main tech avenue) allowed many
projects to experiment with what worked what didn't, for
free. Startups did not immediately call up Jew Ellison to be charged
millions for gargentuan bloated Oracle database before they made any
money. They relied on open source, paid next to nothing for their
software stack.

---

