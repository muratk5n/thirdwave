# Week 44

Python is, of course, freely available and open-source.

---

```python
import pyfiglet; print (pyfiglet.figlet_format("PYTHON ROCKS"))
```

```text
 ______   _______ _   _  ___  _   _   ____   ___   ____ _  ______  
|  _ \ \ / /_   _| | | |/ _ \| \ | | |  _ \ / _ \ / ___| |/ / ___| 
| |_) \ V /  | | | |_| | | | |  \| | | |_) | | | | |   | ' /\___ \ 
|  __/ | |   | | |  _  | |_| | |\  | |  _ <| |_| | |___| . \ ___) |
|_|    |_|   |_| |_| |_|\___/|_| \_| |_| \_\\___/ \____|_|\_\____/ 
                                                                   

```

---

Python! 🐍 🐍 🐍 🐍 (it is the language we use on this blog)

Github: "Remember when people said AI would replace developers? Our
data tells a different story... In 2024, Python overtook JavaScript as
the most popular language on GitHub, while Jupyter Notebooks
skyrocketed—both of which underscore the surge in data science and
machine learning on GitHub"

---

Non-profits are solid orgs.. Management guru Peter Drucker wrote
entire books on them. They are not paid attention to enough, all the
attention is on for-profit entities because they give the bigger
contribution to politicians (they basically own them). Non-profits
need to band together and create their own PAC otherwise for-profit
types will make an hellhole out of your country. Can't let those
fuckers run the roost.

---

O'Nolan previously worked for Wordpress, the famous CMS platform. The
post below is timely bcz Wordpress parent co Automattic CEO Mullenweg
is apparently losing his shit, his for-profit brain is going cuckoo
damaging the WP devs and the brand in the process, so the Ghost
example is a good contrast to all that.

---

John O'Nolan: "Non-profit structures are particularly well suited to
companies that specifically want to serve public community interests,
like schools, hospitals, local news orgs, and — yes — open source
projects... In the US, non-profits are heavily regulated in their
operations, and exempt from income tax...

[Non-profits] don't have owners. And that's what matters. People often
think that 'non-profit' means that the company can't make a profit. It
actually means that the company doesn't have any owners who can
personally take the profits. Any revenue earned can only be
reinvested.

Non-profit structures are particularly well suited to companies that
specifically want to serve public community interests, like schools,
hospitals, local news orgs, and — yes — open source
projects. Non-profit orgs still employ people and pay salaries, and
they're generally audited by the government to ensure they're
operating correctly and within reason.

At [non-profit publishing platform] Ghost..our annual accounts are
subject to a mandatory audit every single year. A shareholder of a
for-profit company may decide to cut costs to the detriment of the
organisation because they're motivated to increase profits and grant
themselves larger dividends at the end of the year.

In a company making cardboard boxes, that's no big deal. Some
short-term money will be made and then the company will probably
fail. The market adapts. In an organisation whose mission is to serve
a community, though, the effects of decisions like this often have
greater consequences.

The primary purpose of the non-profit structure is to protect against
this and ensure that any decisions made benefit the organisation and
its community, not its owners. Ghost has no incentive to slash costs
and drive up profits, because it has no owners. It will always be
independent.

The organisation exists for-purpose, rather than for-profit"

[[-]](https://john.onolan.org/democratising-publishing/)

---

Govs need to invest in social infrastructure, bidness always makes use
of freely available infra e.g. educated populace, bridges, roads,
networks. Someone else needs to do the heavy lifting for them, they
only connect some "stuff on top", and create binness. We need them the
way you need cory catfish in an aquirium, but they do not
fundamentally innovate, they exploit. They are bottom feeders. But the
biz propaganda since the 80s became so extreme, they forgot the true
source of their income. They destroyed social infra and literally
killed the goose that laid golden eggs. They believed their own
bullshit.

---

Eurodollars are dollars deposited in a U.S. bank or foreign bank
outside the US... There is a futures contract on them via CME, "the
interest [on the contract] will be paid by anyone who borrows $1
million for a potential three-month duration at the LIBOR interest
rate. It allows the trader to speculate on a future interest rate of
three months". And, ED market is extremely liquid.

---

Lower rates at any time indicates econ trouble, econ is not heating
up, not growing, hence low rates. Low rates in the future, all the
time, forever means econ in duldrums. Good for asset prices, bad for
people. CB lowering rates more will not help, econ saw some of the
lowest rates post 2008, econ still sucks. Econ is fundamentally
broken. "Biz friendly environment" is no cure. Since 2008 US there's
been no shortage of biz friendly administrations yet the curve
flattened and flattened. People who work on shit jobs will not have
extra cash to spend, whatever they spend will go to the wealthy, or
China anyway. Redistribution is needed, direct aid on the one hand,
highly taxed wealth on the other. Money is zero-sum. Somebody needs to
lose for somebody to gain. Hammer time.

---

Since 2008 crisis the treasury curve has been flattening, save for a
few upticks. Buying ED means betting on rate fall. There is an uptick
now but it will be followed by a fall. Expect to see negative values
by 2026.

```python
df = u.get_fred(2008,['DGS2','DGS10'])
df = df.interpolate()
df['inv'] = df.DGS10 - df.DGS2
df['inv'].plot(grid=True,title='Treasury Curve')
```

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/113/390/079/227/717/251/original/daf9143e9ae2bf9d.jpg'/>

---

Investopedia: "The eurodollar market traces its origins to the Cold
War era of the 1950s when the Soviet Union started to move its
dollar-denominated revenue (derived from selling commodities like
crude oil) out of U.S. banks. This was done to prevent the United
States from being able to freeze its assets. Since then, eurodollars
have become one of the largest short-term money markets in the world
and their interest rates have emerged as a benchmark for corporate
funding"

---

Due to inequality econ fundamentally cannot get better. In financial
market terms that means curve flattening.. Wanna make money on the
country's doom? Can buy a "green" Eurodollar future contract (matures
a few years ahead) and ED price is inverse of interest rate btw, you
buy for the fall. Now I understand why \#Stevenson's writing tone in
his autobio is sometimes so gloomy. He came from poverty, became rich
while betting on a future that would make econ even worse for ppl who
still lived in that poverty. The ED idea is from his book.

---

You entered that BEV business and you are getting destroyed. The tech
was a useless little experiment kicked off by a misinformed,
half-brained US administration, it would have not persisted if its
prez was not hailing from a minority, and the rest of the world was
not such a copycat.  Cascading stupidity in action. But you followed it,
now chickens have come home to roost.

Bangkok Post: "Volkswagen on Wednesday said its third-quarter
operating profit plunged 42% as weak performance in the core passenger
car unit and high costs, including for model revamps, hit the
automaker"

---

"@therightarticle@mas.to

Spain cancels arms deal with Israeli company worth billions"

---

Randa Abdel-Fattah: "Palestinians have tried every
single avenue [to resist non-violently]. BDS is a peaceful movement
that was called by the civil society. It is criminalized in the US. I
just got back from there, and we would had panel discussions, they
tried to shut us down. We protest, 8000 people in the Great March of
Return [in Gaza], protested peacefully, we were shot at with live
ammunition. We go to social media, and advocate there, we get shut
out, silenced on social media. Every single avenue - international law
for instance, US will veto and shut that route down. All these
peaceful avenues are pursued by Palestinians and that is never good
enough. No form of resistance is good enough, it is only acceptable if
you are a dead Palestinian"

---

EurekAlert!: "A team from the Technical University of Berlin, HZB,
IMTEK (University of Freiburg) and Siemens Energy has developed a
highly efficient alkaline membrane electrolyser that approaches the
performance of established PEM electrolysers. What makes this
achievement remarkable is the use of inexpensive nickel compounds for
the anode catalyst, replacing costly and rare iridium"

---

Bus News: "New Flyer of America has received its largest hydrogen fuel
cell bus order to date.. The 40-foot buses will contribute to
SamTrans’ transition to a zero-emission fleet, replacing diesel buses
and supporting California’s goal of reaching 100% zero-emission
transit by 2040"

---

H2 Central: "Solar hydrogen-based microgrid to power Indian Army’s
off-grid locations in Ladakh"

---

Emily Bender: "'Virtual Employees' and Remixing Machines Devalue Human
Work.. According to Katie Prescott in The Times.. Microsoft CEO Satya
Nadella is out there arguing that copyright laws need to be reworked
to enable 'transformative' technology. I wouldn't want to argue that
US copyright laws are perfect or even good the way they are, but the
revisions needed are ones that protect the interests of creative
workers against corporations, not revisions that further the interests
of corporations at the expense of creative workers"

---

"@fuck_cars_bot@botsin.space

'Absolutely great system 👍 a train would definitely be worse than
this right?'"

[[-]](https://files.botsin.space/media_attachments/files/113/384/789/417/861/259/small/8639be79c2935172.jpeg)

---

Stevenson says in his book he was executing a trillion worth of
financial trades each day. A *trillion*. One trader. Think about that.

---

"@lauren@mastodon.laurenweinstein.org

The way things are going, we're going to end up with \#Mastodon as the
only social media platform left standing that not only isn't
controlled by billionaires, but by its very nature cannot be
effectively controlled by billionaires. In this respect we've come
full circle to the days before widespread public access to the
Internet, when individual sites used the public telephone network and
low speed modems to create ad hoc data networks for email and public
discussions.

Everything old is new again"

---

Jack White - Archbishop Harold Holmes \#music

[[-]](https://youtu.be/0FAr1HHb6TU)

---

Would I have an Andrew Carnegie or a Napoleon in my country's past?
Napoleon. Hands down.

---

A Royale with E.coli

---

Informed Comment: "BDS and its Allies are Exposing the Companies Fueling the Genocide in Gaza"

[[-]](https://www.juancole.com/2024/10/exposing-companies-genocide.html)

---

The ethnic stuff was fine.. I started watching live US comedy in NYC,
and I've heard worse. I heard Hispanic, black, white comedians roast
all kinds of ethnic groups. It is a good thing - there is a normative
side to it, but it is an antidote to shitlib multiculturalism (culture
cannot be "multi", it is like Highlander - there can only be one).

---

Hinchcliffe killed it

---

Informed Comment: "It took nearly a year for French President Emmanuel
Macron to confront the uncomfortable truth: the path to peace in Gaza
cannot be paved with more weapons to Israel. His recent remarks, sharp
and unapologetic, reflected the urgency of shifting away from military
escalation. 'I think that today, the priority is that we return to a
political solution, that we stop delivering weapons to fight in Gaza,'
Macron declared, laying bare his stance. He was unequivocal in his
message, adding, 'If you call for a ceasefire, it’s only consistent
that you do not supply weapons of war.'. Although Macron clarified
that France does not supply Israel with offensive arms, his pointed
comments seemed aimed at the United States, which remains Israel’s
primary arms provider"

---

Congressman, stock trader.. same thing

---

January 6, Shmanuary 6.... Bunch of stock traders nearly got their
asses kicked. Who gives a shit?

---

Selydove is gone

[[-]](https://cdn.fosstodon.org/media_attachments/files/113/385/967/128/799/458/original/d030ad496f7237be.jpg)

---

Why are people throwing a fit on the WaPo non-endorsement? Not only it
is good journalistic practice, an endorsement is also useless. "Biased
liberal coastal elite" image would, did in the past turn people off.

---

"In a major step for sustainable steel manufacturing, Greensteel
Australia has been awarded a contract by global steelmaking technology
leader Danieli to build a 600,000-tonne-per-year rolling mill that
will be powered entirely by green hydrogen.

The first-of-its-kind green steel facility is to be located in New
South Wales, Australia, and will create a global benchmark for
zero-emissions steel production. Danieli, an Italian-based metal
processer and supplier, will partner with Greensteel Australia to
develop the plant and is targeting commencement of operations by late
2026"

---

It's so good.. eat it and you will die

---

[Recipe](mbl/2024/montrecip1.txt)

---

Favorite intl meal? *Tagine de veau aux fonds d'artichauts*, from
Montignac. Lamb Vindaloo is also high up there.

---

"@jon@vivaldi.net

Microsoft really does not want you to try another browser. I wonder why? 

Time to defy Microsoft and install Vivaldi!"

[[-]](https://social-cdn.vivaldi.net/system/media_attachments/files/113/362/133/402/386/453/small/5c82fa745b785860.png)

---

The Go! Team - Bust-Out Brigade \#music

[[-]](https://youtu.be/unK1yGbL9nk)

---

\#Suburbia

[[-]](https://files.botsin.space/media_attachments/files/113/364/500/611/994/942/original/3e4661a959ce470c.png)

---

Countries have businesses. In US, businesses have a country.

---

Home ownership rate (the ratio of owner-occupied units to total
residential units) is 93% for China, 89% for Russia, 65.7% for US.
After decades of "ownership society" propaganda you got beat by two
former communist states. Why? Because the kind of vapid capitalism you
practice increases inequality.

---

Zelensk possibly wants an end to the war, his victory plans could be
purposely over-the-top in its resource demands so once denied VZ can
say "well u dont give me what I need, then let me make peace". It
could work but US corp media will muzzle that framing, hence no public
pressure will build. The war will go on as long as there are profits
to be made. This has been the case for nearly all recent American
wars.

---

AP: "Microsoft fires employees who organized vigil for Palestinians
killed in Gaza"

---

"@PabloMartini@climatejustice.social

Israeli troops murder four British Oxfam engineers. Why is this not
all over the UK news outlets? Why is it being hidden from us?"

---

Kerry Burgess: "Very concerning that there is a news blackout in the
United Kingdom on the murder by Israel of the 4 British Oxfam
engineers who were attempting to fix a water supply in Gaza. They were
in a marked vehicle and had notified and obtained permission from the
IDF prior to commencing work"

---

In line w/ international law.. is that because they are sent to Kursk,
which is Russia according to intl law, so they are sent to *defend*,
not to the new areas where Russia is attacking, inside Ukranian
territory? That makes sense I guess in pure legalistic terms.

Le Monde: "[UA mil] told the War Zone website that some 2,600 of the
first North Korean soldiers will be sent to the Kursk region"

---

TASS: "North Korea cannot confirm media reports that the country has
sent its servicemen to Russia, but even if that were true, it would be
in line with the norms of international law, Vice Foreign Minister Kim
Jong Gyu said"

---

Patriotic Millionaires UK: "Did you catch the Metro? 🗞️ 🚇

This week, commuters in Westminster were greeted with our msg on the
front page of the Metro: 'Tax us, the super rich.'

To fix the foundations of our country it's time for those us who can
afford to pay more to do so"

---

Today's Disney is no different. Woke agenda is distraction, indirect
capitalist propaganda which lulls people into thinking the culture war
is supreme when in fact the real war has been waged in economic realm
and it's been already lost for the working class. They are now dancing
in your grave via a Captan America who "fights the government", making
gov look bad so big co continues to evade tax and your serfdom is
entrenched.

---

Walt was a rapacious capitalist? It's funny how completely opposite
his daughter is, Abigail Disney.

[[-]](https://www.theguardian.com/commentisfree/2024/apr/18/world-leaders-raise-taxes-rich-people-inequality-abigail-disney)

---

"@MikeDunnAuthor@kolektiva.social

Today in Labor History October 24, 1947: Walt Disney testified before
the House Un-American Activities Committee, naming many of his own
employees as communists, including Herbert Sorrell, David Hilberman
and William Pomerance, because of their activism as union
organizers. In 1993, the New York Times wrote that Disney had been
passing secrets to the FBI from 1940 until his death in 1966. In
return, J. Edgar Hoover let Disney film in FBI headquarters in
Washington and made Disney a 'full Special Agent in Charge Contact.'

In 1971, Ariel Dorfman and Armand Mattelart published 'How to Read
Donald Duck,' a book-length essay critiquing Disney comics as
capitalist propaganda for U.S. corporate and cultural imperialism. It
became a bestseller throughout Latin America and is still considered a
seminal work in cultural studies. It was first published in
Valparaiso, Chile when Allende was in power. Pinochet banned it and
conducted public book burnings [with it]"

---

"@Gargron@mastodon.social [MD founder]

Mastodon is financed by crowdfunding instead of venture capital not
because we don't know that venture capital exists, not because we
don't have bills to pay, and not because venture capital isn't willing
to give money to new social media platforms. VCs don't want a
sustainable business, they want a big exit. Every VC-backed business
is on a timer to deliver or die"

---

Vox: "Michael Becker, a professor of international human rights law at
Trinity College, Dublin, said, overall, the above incidents and others
mean 'South Africa has an ever-expanding repository of evidence that
it can put before the [ICJ] as further evidence of genocidal intent,'
which includes evidence suggesting Israel 'has not meaningfully sought
to comply' with the ICJ’s orders so far"

---

Vox: "Ernesto Verdeja, a professor of political science and peace
studies at the University of Notre Dame, said it could be 'called a
genocide, even in a narrow legal sense, for several months now' given
the accumulation of Israeli attacks clearly and consistently targeting
the civilian population in Gaza."

---

Vox: "'Any early hesitation I had about applying the 'genocide' label
to the Israeli attack on Gaza has dissipated over the past year of
human slaughter and the obliteration of homes, infrastructure, and
communities,' said Adam Jones, a professor of political science at the
University of British Columbia who has written a textbook on
genocide..  'whatever peace constituency existed in Israel seems to
have vanished, and there is a growing consensus for genocidal war,
mass population transfer, and long-term eradication of Palestinian
culture and identity'"

---

F24: "Israeli airstrike on Tehran caused ‘minimal damage’ Iran says"

---

NYT: "Israel’s Retaliatory Attack on Iran Appears Carefully Calibrated"

---

Firstpost: "Georgia's pro-Russia ruling party celebrates early victory"

---

Fox News: "In a show of support for former President Trump, a group of
Muslim leaders in Michigan, a swing state, officially endorsed his
candidacy."

---
