# Week 17

"All credit is printed money". Guy thinks he discovered the 8th wonder
of the world w/ that observation. That doesn't solve the
problem. Money, printed or not, can pile up on someone's account, now
the wealthy, causing massive inequality reducing everyone's living
standards. Excess wealth will chase assets, if it buys mortgage debt
it will increase the price of the underlying asset which is precisely
what happened before the GFC. Now the median house nearly costs half a
million *freaking* dollars.

Governments must tax for rebalancing. Useless observations like one
above are so inane they create opportunities for ideological arbitrage
which the wealthy will happily exploit. They will push faux leftist
spending wout taxation - all printed money flows to them anyway, and
they remain wealthy.

---

\#Ukraine 04/15 - 04/25

[[-]](mbl/2025/ukrdata/map17.html)

---

Economic Times: "Vincent Lyne, a researcher from the University of
Tasmania's Institute for Marine and Antarctic Studies, claims to have
located the missing Malaysian Airlines flight MH370. The plane, which
disappeared in 2014 with 239 people on board, was allegedly flown
intentionally into a 20,000-foot-deep chasm in the Indian Ocean known
as the Broken Ridge. Lyne's research..  suggests that the
disappearance was a result of meticulous planning and not an
accident... [Lyne] believes the plane was intentionally flown into a
deep chasm in the Indian Ocean. [He] suggests that previous searches
missed the mark due to incorrect assumptions about the aircraft's
final moments... Lyne identified a 6000-meter hole at the eastern end
of the Broken Ridge as the likely resting place of MH370. He described
the area as a hazardous ocean habitat filled with deep pits of fine
sediments and narrow, steep sides surrounded by enormous hills.

Lyne's theory contradicts the earlier notion of a rapid plunge due to
lack of fuel. Instead, he proposed a 'controlled ditching' akin to
Captain Chesley 'Sully' Sullenberger's 2009 landing on the Hudson
River, with the plane's wings, flaps, and flaperon damages supporting
this scenario"

---

Researcher Lyne disputes the last moments of the plane, the data on
the "7th arc" (which most pre-2018-data analysis used), says that last
ping should not be trusted.

---

They were going to search the Godfrey and Lyne points, plus that white
region in the map.

---

```python
import json, requests
qr = requests.get("https://trise5631.github.io/areas2.js").text
jres = json.loads(qr.replace("parseAreas(","").replace("})","}"))

cs = {"Lyne": list(reversed(jres["areas"]["LYNE"][0]))}
atsb = u.flip_c(jres["areas"]["ATSB"])
OI2018 = u.flip_c(jres["areas"]["OI2018"])
GCM = u.flip_c(jres["areas"]["GCM"])
a =  u.flip_c(jres["areas"]["OI2025A"])
b =  u.flip_c(jres["areas"]["OI2025B"])
polys = {"atsb": atsb, "OI2018": OI2018, "OI2025A": a, "OI2025B": b, "Godfrey": GCM}
u.map_coords([-19,110],cs, polys, zoom=4, colors={"Godfrey": "#FFFFFF", "OI2025A": "#FFFFFF", "OI2025B": "#FFFFFF"}, outfile="map07.html")
```

[[-]](mbl/2025/map04.html)

---

Found its raw data, almost in json

[[-]](https://trise5631.github.io/areas2.js)

---

This was the tracking page for the MH 370 search

[[-]](https://www.mh370-caption.net/index.php/armada-tracking/)

---

Oh well.. 

Arab News: "Search for long-missing flight MH370 suspended.. 'They
have stopped the operation for the time being, they will resume the
search at the end of this year' Transport Minister Anthony Loke said"

---

Mining Weekly: "Hydrogen combustion truck undergoes proof-of-concept
trials.. equipment manufacturer Komatsu has partnered with German
hydrogen engine startup KEYOU to develop a conceptual 'world’s first'
12-cylinder, hydrogen-powered rigid-frame mining haul truck"

---

"The pope would often end his speeches calling people to pray for him,
a sinner, he would say, like anyone else"

---

The Telegraph: "Trump to let Putin keep land seized from Ukraine.. The
condition is part of a seven-point plan to end the war.. Point three
requires Ukraine to refrain from seeking membership of Nato, though
the country would still be free to join the EU. Point four covers
territory, with America offering de jure recognition of Russian
sovereignty over Crimea.. [T]he nuclear power station at Zaporizhzhia,
the largest in Ukraine and currently held by Russian forces, would be
transferred to American control. Under point six, Ukraine would sign
the minerals deal allowing US companies access to the country’s
natural resources. Point seven raises the possibility of a new
relationship between America and Russia, saying that all US sanctions
would be lifted and the two countries could begin to co-operate on
energy"

---

Semafor: "Bannon warned the alternative was someone like Luigi
Mangione, the man charged with killing United Healthcare CEO Brian
Thompson last year. 'He’s treated like Robin Hood,' Bannon said. 'That
should scare you to the marrow of your bones, because that’s the
alternative if the system keeps going like it is'"

---

H2 View: "Doosan Fuel Cell and KOSPO Team Up to Deliver Dynamic Grid
Solutions with Hydrogen Fuel Cells"

---

H2 View: "Haffner promises sub-€3/kg hydrogen from new biomass reforming unit"

---

H2 Fuel News: "BYD Enters Hydrogen Fuel Cell Market with Launch of
Hydrogen-Powered Bus.. BYD is making waves again—this time by rolling
out its very first hydrogen-powered bus. Known around the world for
leading the charge in electric vehicles, BYD’s foray into hydrogen
fuel cells shows it’s not just sticking to batteries. Instead, the
company’s broadening its game plan with a bigger focus on
zero-emission technology"

---

Business Insider: "A new class action lawsuit accuses Tesla of
intentionally manipulating the mileage shown on its electric vehicles'
odometers to more quickly void its warranties. Other Tesla drivers not
involved in the litigation have told Business Insider they believe
they've experienced the same phenomenon..

California driver Nyree Hinton filed the class action lawsuit against
the company on April 2, accusing Tesla of using algorithms and energy
consumption metrics to manipulate and misrepresent the actual mileage
traveled by Tesla vehicles"

---

The Asashi Shukimbun: "The Japan Atomic Energy Agency said it plans to
start producing clean hydrogen using heat from its High Temperature
Engineering Test Reactor (HTTR) in Ibaraki Prefecture close to Tokyo
by 2028..

The national nuclear research and development agency is hoping to
start producing hydrogen at the HTTR, an experimental high-temperature
gas-cooled reactor (HTGR), in the second half of fiscal 2028. There
are hopes that HTGRs can produce hydrogen in voluminous amounts on a
stable basis because heat at higher temperatures can be extracted from
an HTGR compared with a light-water reactor, which is the mainstream
nuclear reactor"

<img width='340' src='https://files.mastodon.social/cache/preview_cards/images/143/641/491/original/24181029b743d850.jpg'/>

---

"@stroughtonsmith@mastodon.social

The European Commission finds Apple’s Core Technology Fee is against
the law. It's also too onerous on developers, and too complicated for
users, and Apple has not proved these measures are just and
valid. Apple now has a chance to defend its reasoning before a final
ruling on fines & consequences"

---

AAah now we find out why they included the scene. It's anti-deportation,
pro-open-border propaganda. No wonder the show sucks.

The Holywood Reporter: "Andor dared to go to the darkest places Star
Wars could offer. An Imperial Officer abusing his untouchable status
to [assault] an undocumented migrant, while his troops are rounding up
other undocumented citizens. This is the real world seeping into Star
Wars storytelling; this is the world WE live in, reflected in the
galaxy far, far away, this is Star Wars at its most political, its
most potent"

---

There was a scene in ep 3 where an imperial officer abused a woman?

---

Watched one ep, it still sucks

---

New *Andor* season..?

---

The Guardian: "The world’s coral reefs have been pushed into
'uncharted territory' by the worst global bleaching event on record
that has now hit more than 80% of the planet’s reefs, scientists have
warned.

Reefs in at least 82 countries and territories have been exposed to
enough heat to turn corals white since the global event started in
January 2023, the latest data from the US government’s Coral Reef
Watch shows"

---

Pope RIP

---

Fault line from paper

[[-]](https://www.nature.com/articles/ncomms2999)

---

[Link](this_is_fine_eq.jpg)

---

All near the fault line.. Nothing to worry about. All dandy.

```python
fl = u.get_json().loads(open("tr_faultline1.json").read())
u.map_coords([40,28],dfq, lines=fl, zoom=9, outfile="map07.html")
```

[[-]](map07.html)

---

There's been much talk about "the big one" that is predicted to hit
Stanpoli at some point. Are these the signs of the big one?

---

Homie got shook? 

\#Earthquake

```python
dfq = u.eq_at(41, 29, 500, 3); u.map_coords([41, 29], dfq, zoom=9, outfile="map06.html")
```

[[-]](map06.html)

---

[Perovskites](../../2022/06/the-h2-revolution-alvera.html#peros)

---

Zeihan: "[T]he absolute lowest grade for silicon as an actual
industrial input is 99.95 percent pure.  Getting there requires a
blast furnace, which typically requires a lot of coal.  Overall, the
process isn’t all that complicated—you basically just bake the quartz
until anything that is not silicon burns away—which means some 90
percent of this firststep processing tends to be done in countries
like Russia and China, countries with a lot of surplus industrial
capacity that don’t [care] about environmental issues...

The 99.95 percent purity of 'standard' silicon isn’t anywhere enough
[for solar panels]. A second round in the blast furnace gets the
silicon up to 99.99999 percent pure. Round two is far more
sophisticated than round one’s bake-it-pure. China’s GCL Group is the
only Chinese entity that can manage such precision at scale, making it
responsible for one-third of global supply. The rest comes from a
smattering of developed-world companies.  This pure silicon is
incorporated into the solar cells that make solar panels do their
thing"

---

CleanTechnica: "China’s coal-fired electricity generation took an
unexpectedly sharp turn downward in the first quarter of 2025,
signaling a potentially profound shift in the world’s largest
coal-consuming economy. This wasn’t merely a seasonal dip or economic
distress signal; rather, it represented a clear and structural turning
point. Coal generation fell by approximately 4.7% year over year,
significantly outpacing the overall grid electricity supply decline of
just 1.3%. However, electricity demand, a better measure, went up by
1%. What gives?...

China put in place a Whole County Rooftop Solar Promotion
Program. Developers had to bid on an entire county’s rooftop solar at
once, committing to putting solar on 50% of government buildings, 40%
of public institutions, 30% of commercial and industrial rooftops, and
20% of rural homes. That’s paid off massively in the densely populated
southeast of the country where demand is highest and free space is
lowest...

As a result, tens of terawatt-hours (TWh) of electricity generated by
these rooftop systems are effectively invisible when interpreting
China’s national grid-supplied electricity data. This has profound
implications: the reported 1.3% decline in grid electricity generation
does not represent true reduced consumption, but rather a substitution
effect—electricity generated behind the meter directly displacing
grid-supplied power... Given that China’s reported 1.3% drop in
grid-delivered electricity in early 2025 equates to roughly 30 TWh
less generation, it’s reasonable to conclude that this hidden solar
growth alone might account for much, if not all, of the decline"

---

BBC: "US sets tariffs of up to 3,521% on South Asia solar panels"

---

"@luckytran@med-mastodon.com

From the first #EarthDay: Students in St. Louis marched wearing masks
to protest smog and air pollution.

The inaugural 1970 protests drew millions, and led to the creation of
the EPA and clean air standards"

<img width='340' src='https://cdn.masto.host/medmastodoncom/media_attachments/files/114/383/009/754/943/226/original/64abfaa939a5b210.png'/>

---

Firstpost: "Far-right Reform UK to beat Labour to be largest party if
elections are held today: Survey"

---

YNet: "The Houthi rebels were positioning landmines around the port of
Hodeidah and other populated areas in anticipation of a ground
offensive by Yemen's government forces, with the support of the United
States, the Saudi-owned Asharq Al-Awsat reported on Saturday"

---

Left to their own devices businesses will become monopolistic,
globalize, employ slave labor, destroy nature while doing so, cheat,
steal, tax-evade.. It is in their nature.

---

Scared of being in the "kill zone" - I believe that is the definition
of monopolistic power.

---

Kurt Andersen: "[2020] Google does more than 90 percent of all
Internet searches, forty times as many as its closest competitor. As
far as venture capitalists are concerned, digital start-ups looking to
compete with the Internet colossi, no matter how amazing their new
technology or service or vision, ultimately have two alternatives: to
be acquired by Google or Facebook, or to be destroyed by Google or
Facebook. If the latter seems likelier—being in the 'kill zone,' in
the Valley term of art—the VCs tend not to invest in the first place"

---

Politico: "This week marks a moment of truth for Washington’s push to
rein in Big Tech — a yearslong and often fruitless battle to curb the
power of the world’s richest companies... After years of empty threats
from Congress, two major antitrust cases have landed two companies in
court at once"

---

Dems need to ditch Clinton and Obama as examples to be followed and
stop pretending they were good Presidents.

---

Politico: "Doug Sosnik is a longtime Democratic strategist best known
for being a top adviser to Bill Clinton. He’s a self-described member
of the party’s centrist wing. But he says it’s now time for Democrats
to take a page from the progressive left’s playbook.. 'We’re out of
power. We can’t get anything done,' he said. But at least we need to
be able to articulate a coherent narrative about the future that can
appeal to the middle class.'"

---

CNBC: "China vows retaliation against countries that follow U.S. calls
to isolate Beijing"

---

Arab News: "China on Monday hit out at other countries making trade
deals with the United States at Beijing’s expense, promising
countermeasures against those who 'appease' Washington in the
blistering tariff war. While the rest of the world has been slapped
with a blanket 10 percent tariff, China faces levies of up to 145
percent on many products"

---

Ledbetter, *Unwarranted Influence*: "The last years of [Ike's]
presidency were marked by deep, often bitter conflicts with Congress
over the military and national security... These conflicts came to a
head in the fall of 1957, with the one-two punch of the Soviet Sputnik
launch and the near-simultaneous release of a report arguing that the
United States would soon fall behind the Soviets in the production of
atomic weapons...

The launch of the Sputnik satellite on October 4, 1957, hit the
Eisenhower White House like a targeted missile. Whether it represented
a scientific breakthrough for the Soviet Union is a matter that can
still be debated. But as a public relations coup, it unsettled the
administration more than any other event... 

While the public was focused on the two Sputnik launches, Washington’s
elite was arguably more devastated by the release of an exceptionally
well-timed panel study — delivered four days after the second Sputnik
orbit — that appeared to show the Soviet military threat was even
greater than the administration thought. Entitled 'Deterrence &
Survival in the Nuclear Age,' it was known informally as the Gaither
Report, after its panel chairman, H. Rowan Gaither of the RAND
Corporation. The report —classified top secret— cited 'spectacular
progress' in Soviet military development after World War II.  The
Soviets, the authors claimed, had enough fissionable material for
fifteen hundred atomic weapons and had 'probably surpassed' the United
States in the production of nuclear-tipped intercontinental
missiles. They proposed a massive military spending program that
would...  match the alleged Soviet offensive capabilities..

The period following the Sputnik-Gaither crisis demonstrates
Eisenhower’s military-industrial-complex critique in its early
stages. [W]ho was behind the faulty intelligence and calls for
military buildup in the Gaither Report? The leadership consisted of
known and trusted Eisenhower advisors, but there could be no hiding
the fact that the billions in increased military spending called for
by the panel would benefit many of the very people making the
recommendations. Two of the report’s principal directors were Robert
C. Sprague, who headed his own business of military electronics, and
William C. Foster of the Olin-Mathiesen Chemical Company, a producer
of gunpowder and ammunition"

---

The supposed Tishrin Dam handoff (from SDF to HTS) is not yet visible.

\#Frontlines \#Syria - 03/24 - 04/19

[[-]](syrdata/map03.html)

---

