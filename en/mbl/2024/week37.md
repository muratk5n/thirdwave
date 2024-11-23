# Week 37

The moon was not formed due to an impact.. Well shit.. this theory was
so widely believed.. it makes you wonder where else sci consensus
might have gone wrong.

Paper: "Here we critically examine the geophysical and geochemical
properties of the Moon in order to identify the extent to which
dynamical scenarios [an impact forming the Moon] satisfy these
observations... there is no unambiguous geochemical or isotopic
evidence for the role of an impactor in the formation of the Moon,
implying perfect equilibration between the proto-Earth and
Moon-forming material or alternative scenarios for its genesis"

[[-]](https://arxiv.org/abs/2408.16840)

---

"@emmatonkin@mstdn.social

Pallab Ghosh on the BBC just described this as 'one small step' - 'a
moment of history that will be remembered'

Don't see why, frankly. Rich person does stuff previously achieved by
many less wealthy people, news at 12?"

---

BBC: "Billionaire becomes first non-professional astronaut to walk in
space"

---

Green Party VP candidate drops burn, "AOC Pelosi". Pelosi did become a
curse word of sorts among the left. Wasn't Nancy for single-payer
healthcare back in day? Now she stock trades on legislation. Sad.

---

The un-inversion partly has to do with 2-year yield falling, which is
closely tied to FEDFUNDS. And lo and behold, FED is about to cut
rates soon.

---

Curve inversion rings alarm bells bcz if long-term interest rate
expectation (captured in the 10-year) is lower than short-term, it
means a crisis is expected in the future, hence lower rates.

---

Negative values are places where the curve inverted. No need to plot
all maturities 2, 5, 10, 20 etc and looking at the "shape" of that
curve. Simply subtracting 2 year treasury from 10 year treasury for
each time period is good enough. BTW the pattern shows recession does
not occur exactly at the point of inversion, but *after* the inversion
un-inverts, just when it start becoming positive, then the recession
hits.

---

How is the curve inversion going (a good indicator for recession),

```python
df = u.get_fred(1980,['DGS2','DGS10'])
df = df.interpolate()
df['inv'] = df.DGS10 - df.DGS2
df['inv'].plot(grid=True)
plt.axvspan('01-09-1990', '01-07-1991', color='y', alpha=0.5, lw=0)
plt.axvspan('01-03-2001', '27-10-2001', color='y', alpha=0.5, lw=0)
plt.axvspan('22-12-2007', '09-05-2009', color='y', alpha=0.5, lw=0)
```

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/113/136/135/805/131/113/original/022cfaec2fbef7b6.jpg'/>

---

Al-Jazeera: "Australian media reported the police operation in
Melbourne was the largest since 2000, when Australia’s second-largest
city hosted the World Economic Forum"

---

BBC: "Dozens arrested after clashes at Melbourne anti-war protest..
Police had anticipated unrest ahead of the event, which is expected to
draw over 1,000 corporations from 31 countries in the coming days. The
expo, which is not open to the public, brings together military,
defence, government, scientific and industry delegations from around
the world.

Local media reported military artillery, trucks and semi-automatic
weapons have been on display during the convention. Activists had said
they were protesting as they claim many of the weapons on-show have
been used by Israeli forces in Gaza"

---

Great.. on our way forming a Eurasian superpower. When are
we invading New York?

Firstpost: "A day after India’s External Affairs Minister S Jaishankar
said that about 75 per cent of disengagement problems with China 'have
been sorted out', China said that its troops have withdrawn from four
places in eastern Ladakh and that the situation at the border is
relatively stable"

---

"@bdm@iceshrimp.de

Apple has to pay 13 billion euros in back taxes in Ireland.. 'The
European Court of Justice (ECJ) has ruled that Ireland has granted the
tech giant Apple illegal aid amounting to around 13 billion
euros. Ireland must now reclaim this, according to the ECJ..  In 2020,
the Court of the European Union (CJEU) ruled in Apple's favor that
there was no state aid. From the CJEU's point of view, the Commission
had not been able to prove that Apple's tax agreements in Ireland from
1991 and 2007 constituted prohibited state aid. The Commission
appealed against this - successfully, as has now been established. The
ECJ fully confirmed the Commission's original decision from 2016'"

---

I guess if written well u could do an accurate Doom.. If the writing
is playful enough, it can work. Marv will then be banking on RDJ's
star power to carry this role. Playful like VVD sees Stark on TV gets
mad bcz he judges him a dumbass and double mad bcz TS also looks like
him. Parker is shocked to see his mentor's likeness in a villain. So
on.

---

"Draghi Report confirms hydrogen as a key technology and stresses the
importance of R&I to keep Europe at the forefront"

---

It's true, media isn't as gaga abt her anymore are they? Good for
Greta

Joshua Hill: "In a striking scene, Greta Thunberg was arrested on
Wednesday as she participated in an anti-genocide protest at the
University of Copenhagen, the sort that has catapulted the student
movement to the forefront of the solidarity struggle for a Free
Palestine...  [But as] I posted [.. earlier]: '..the second Greta
started making connections between climate change and capitalism,
colonialism.. the media coverage came to a screeching halt'"

---

"@RustyBertrand@kolektiva.social

People do not 'slip through the cracks' of society. They are stomped
into the cracks, bleeding and screaming and pleading for help"

---

RFK's VP pick is on Fox.. Shamrock Po? RFK is on DJT camp I guess she
now enjoys some downstream benefits.

---

I'd take the "acceptable" and move on.. I don't know which moron
advised that debate prep, but they did an aweful job. Kam performed ok
not saying it was a loss for her cuz the bar was set so low due to
Biden but next one probably won't be any better for Dems, if the
same shitlibs will be advising.

---

You mean our solar system is special? 

"[T]he galaxy rotation curve does not follow the gravitational law that
applies in our solar system. This is because the matter in the galaxy
is distributed differently than in our solar system"

---

Fleming: "General Relativity does not account for spiral galaxy
formations.. [GR] fails both in terms of not providing the force
strength necessary to retain the most distant stars and not have a
force mechanism that explains the spiral arm formation"

---

The Cradle: "US naval forces cannot remain to protect Israel
'forever': Washington... Washington has warned Tel Aviv that US naval
forces cannot indefinitely be deployed to the West Asia region to
protect Israel, Channel 13 reported on 6 September, amid continued
fear of an expanded war between Israel and Hezbollah in Lebanon. The
Israeli news channel reported a message was sent to Israel that
tensions with Hezbollah and Iran need to be reduced at some stage
because 'the [US] aircraft carriers will not be able to stay in the
area forever'"

---

Reuters: "Zelenskiy has been pleading with Kyiv's allies for months to
let Ukraine fire Western missiles including long-range U.S. ATACMS and
British Storm Shadows deep into Russian territory to limit Moscow's
ability to launch attacks..  Putin said on Thursday that such a move
would drag the countries supplying Kyiv with long-range missiles
directly into the war. He said satellite targeting data and
programming of the missiles' flight paths would have to be provided by
NATO military personnel, as Kyiv did not have the capabilities itself"

---

EIA: "U.S. electric power sector explores hydrogen cofiring at natural
gas-fired plants"

---

Firstpost: "End of Googling? Gen-z prefers searching on TikTok,
Instagram rather than using search engines"

---

Some Dem mistakes during debate: KH referenced "Goldman Sachs", as an
institution supporting her plans, that was a negative. You can spin
that as elitism vs middle-class to an low-info voter (hell even
high-info voter).

She talked about econ profs who support her plan, and cited Wharton
School of Econ. Well Trump graduated from Wharton. What was the plan
there, by hearing his school being cited as being against him, Trump
would tremble in fear and be paralyzed for the rest of the debate? Of
course not. He actually had an opening; he said "I graduated from
Wharton" and said profs there are supporting his plan. Now Kam looked
like she was one-upped, looked like she didn't know DJT was a Wharton
grad, the info was "sprung on her". DJT stirred the pot, gave one
tidbit that low-info voter could easily check another that they could
not. Couch jagoff can check Wharton but won't have any idea if the
profs there supported Trump. And since earlier one-up favored Trump,
voter can assume he was being truthful.

There were many instances like this that shitlib eco-chamber missed but
would absolutely register with the regular voter. 

---

I do not like dams esp ones built for electricity generation. Energy
cld be generated cheaply via solar or nuclear, in its various forms.

"@adapalmer@wandering.shop

The largest dam removal in history is complete.. The best thing that
happened in the world last week: after years of negotiating—and
decades of activism—the Klamath River is free of four huge dams,
reopening more than 644 kilometres of free-flowing water. It’s a
landmark moment for the Shasta Indian Nation, who are restoring 2,800
acres of their ancestral land that is above ground for the first time
in a century"

---

*Expend4bles*, perfectly fine movie.. It subverted expectations,
action was top notch.

---

"We put 7 Uber & Lyft drivers in one room and had them open their apps.

We found Uber paying different drivers different amounts for the same
ride. Lyft too.

It’s proof corporations are using secret algorithms to pay workers
less""

[[-]](https://youtu.be/OEXJmNj6SPk?t=161)

---

WION: "A 'groundbreaking' nuclear power plant is being developed by
Russia and China which is expected to support human settlements on the
Moon in future... A new report published by Russian news agency TASS,
however, has suggested that India is also likely to become a part of
this ambitious project in future."

---

Chico Mendes: "Environmentalism without class struggle is just gardening"

---

\#Bilzerian \#PBD

[[-]](https://www.youtube.com/embed/nTQmJt86h9I?start=2654&end=2789)

---

AIPAC is crawling up your ass who assigns handlers to lawmakers to
follow them closely turning legislators into their *bitch*
(indirectly for the MIC of course) and DOJ is still after "Russian
influence operations", going after a handful of tubers and some freak
company noone has even heard of?

---

Second US citizen killed by ISR. Where is DOJ? 

"Biden blasted for calling Israeli killing of US activist 'accident'"

---

"@fuck_cars_bot@botsin.space

'Top tier carbrain architecture?'"

[[-]](https://files.botsin.space/media_attachments/files/113/112/762/570/317/385/small/cf8124365a27605c.jpeg)

---

The cats and dogs thing was funny. Regular voter, sparse consumer of
politics info would like that stuff

---

Politico: "[T]here’s a widespread perception that Trump did serious
damage to his chances of winning with his undisciplined and largely
incoherent debate performance... When all the corners of elite
thinking are in agreement — whether it’s on social media, Wall Street,
the Beltway, print newsrooms or in cable TV green rooms — it’s best to
be very skeptical"

---

Netzpolitik.org: "Following a historic ruling in August, another
monopoly case against Google is beginning today in the USA... monopoly
expert Ulrich Müller explains what could happen to Google - and why
Europe should also dare to unbundle more...

When you visit a website, auctions run in the background in fractions
of a second to determine which ads will be shown on the advertising
space on that page. Google provides the largest server through which
publishers handle the auctions. It also dominates the market for the
services that advertisers use to manage their online advertising
campaigns. In between, Google also operates the largest auctioneer on
the market with AdExchange.

According to investigations by American and European competition
authorities, Google has abused this control over the various sides of
the market to its advantage for years. In the legal proceedings that
begin today on Google's monopoly position in the adtech sector, the US
Department of Justice and several states are demanding that at least
the Google service for publishers and the Google AdExchange be split
off. The EU Commission also came to the preliminary conclusion in 2023
that Google had abused its adtech market power and that structural
measures were needed"

---

Cetta, *The Quantum Dice*: "Let us consider a box that is divided into
two smaller equal boxes L and R by means of a movable wall. Assume
that inside the big box there is a (single) particle... We ask a
simple question: Where is the particle? Even though it would be
difficult to pose a simpler question, physicists are imaginative
enough as to have begotten a full range of answers to it; however,
since our interest lies in the fundamental content of those answers,
we may abstract the details and reduce them to just the two that catch
the main tendencies. So, where is the particle?..

The conventional description [is this] basic tenet of the conventional
interpretation of quantum mechanics is that the wave function affords
a complete description of each individual system... this means that
the wave function refers to the one particle inside the big box and
the answer to the above question depends on whether we have observed
the interior or not. Previous to any observation the state is
*completely* described by stating that the probability of the particle
being in any of the two boxes L or R is $\frac{1}{2}$; there is no
more to that. Thus, the particle is in a state of indeterminate
localization (delocalized) in the big box. By looking inside (making a
measurement to know its whereabouts) we perturb the system and bring
it into a new state, (objectively) localized either in box L or in box
R. The transformation of the wave function from the (pre-observation)
indeterminate localization state to the (post-observation) determinate
state constitutes the reduction or collapse of the wave function,
brought about by the observation. Whether the particle ends up in box
L or in box R after the measurement, is a matter of chance.

The assumption that the wave function refers to a single system thus
has enormous consequences. Quantities such as $\Delta x$
(uncertainties in the conventional language) become objective
restrictions on the localization of the particle, meaning that there
exist intrinsic limitations on the corresponding measurements. So,
quantum mechanics goes as far as is possible and physicists must
renounce once and for all the hope for a detailed description of the
individual. Further, since the concept of probability is being applied
to a single event and no sample space can be constructed, there is no
consistent way of viewing the result as a property of the system, and
it must be interpreted as an uncertainty of our knowledge. The
observer slips thus into the description, and the fundamental
principle that physics refers to the world rather than to our
knowledge of it, is eroded"

---

But you know what, I bet entrenched interests are behind that
wording... That way existing tech can still be sold "but smaller",
because, somehow that makes the tech safer and better 🤨 The idea is
the same tech and the same companies who earn from that tech will be
fine, *don't you worry*.

However large and small, the end result is the same for the old tech,
same amt of fuel will be used for the same amt of energy generation,
the waste problem will also remain unchanged.

---

You could build a very large helium-cooled nuclear reactor. The key
point is that such reactors are not water cooled, and use safer
nuclear fuel.

---

It is mind-boggling how ignorant MSM is... They get a few words in
their heads, "electric", "small reactor" it just circulates in there
ad infinitum, in that vast empty space, without anyone checking if
these words they parrot even make sense... It is like the the
telephone game where science tells something on one end, after a
string of MSM repeats, absolute garbage comes out on the other end.

---

RIP

F24: "US actor James Earl Jones, voice of Darth Vader and CNN, dies at 93"

---

F24: "EU court rules Google, Apple must pay billions of euros in
antitrust, tax cases.. A top European Union court on Tuesday told
Google it would have to pay a 2.4 billion fine brought forth by the
bloc's antitrust regulators seven years ago, just as the court
rejected Apple's final legal challenge against an order from the
European Commission to repay ?13 billion in back taxes to Ireland"

---

Viktor Orban: "Germany has decided to impose strict border controls to
stop illegal migration. Bundeskanzler Scholz, welcome to the club!"

---

"GeofCox@climatejustice.social

The only thing that worries me about the apparently almost universal
approval of Harris and condemnation of Trump among the 'serious' media
and 'chattering classes' - especially in Europe - is that it plays
directly into the 'metropolitan elite' vs 'ordinary people' narrative
that is a key driver of votes for [Reps]"

---

Kamala did an acceptable job..  But overall DJT did better.

\#Debate

---

The Guardian: "Wealthy, democratic countries in the global north are
using harsh, vague and punitive measures to crack down on climate
protests at the same time as criticising similar draconian tactics by
authorities in the global south." via @GeofCox@climatejustice.social

---

Yet no attention is paid to these researchers.. Is it because they are
Mexican?

Ray Fleming: "Ana Maria Cetta & Luis de la Peña have shown that QED is
an emergent property of the quantum field. Classical electromagnetics
and the physical constants also emerge from the quantum field
completing QED"

---

CNBC: "China's exports grow by 8.7% in August, beating expectations"

---

TDB: "Nancy Pelosi Ambushed Over Wall Street Wealth at Book Signing"

---

Case in point.. the news of the day was the waterfront brawl in Alabama
(remember that?). Some lady is commenting on it, Roland Martin shared
it. At first I was like "why is she acting black?". Then I realized,
she is not acting black, she is acting *Southerner*. 

[[-]](https://youtu.be/D5Fj3ALsVhw?t=1538)

---

What is known as "black culture" in US is a derivative of the Southern
culture. Obviously all immigrants contribute something into the tomato
soup and the next generation gets da whole thing, not just the little
piece your fureign ancestors added.

---

Culture forms at young age, via osmosis. Fureigners arriving at a
place will always remain fureigners until the day they die. America,
for better or worse, *does* have a culture which people assimilate
into. Whites, Blacks, Asians - they assimilate into the same
thing. 

---

I've said this before out of all TNG alien races the one that
resembles US most is not humans and their Federation. It's the
Pakled. *Samaritan Snare* ep has it.

---

The state of AI, state of quantum mechanics and the stagnation around
"the theory of everything" is purely an American phenomenon. The lack
of QM anthology, and the fact the issue has been left that way for
nearly 80 years can be blamed on the new world, as well as the
excitement around recent AI'ish AI that isn't AI... The culture code
US gives itself is DREAM, the code for technology is IT WORKS.

US also knows very well how it enyojed many of the fruits of 20th
century advanced sci. How? By importing it from Europeans.

Put all these together, the reason for QM anthology stagnation is US
scientists, even the ones trained by the best of the old world, are
too scared to touch the "sacred transmission" they'd received. They
didn't question the core, and the interpration at the time fit their
sensibilities too, there is mysterious, dreamy shit, weird and
bizarre, so they built a ring fence around that, merely surrounded it
with tech that WORKED ("shut up and compute" ideology) and left it at
that = stagnation.

"AI" is similar, it works, mysteriously, ginning up the American
*dream* (imagine what you can do with it broooo), the outputs are
seemingly human, this AI basically sells itself by being mysterious
and "working". No need to look under the hood.

In summary Us scientists are at once too amazed, and too scared to
touch anything they took earlier from the old world, and gravitate
toward more mystery (leave things unexplained = mystery) and so
naturally after eight decades stuff kinda works but noone knows why
(in "AI"'s case it doesn't even work at a smart human level, can't
plan, can't diagnose, can't do anything intelligently, only parroting
out stuff creatively). There is a 2016 word for that. Sad.

---

This is a different method than Abramovitz but it apparently works,
agrees w/ TfC.

F24: The ’13 keys’ method: How one historian has accurately predicted
almost every US election.. Historian Allan Lichtman, who has an almost
perfect record in predicting US election results, has said that
Democratic presidential nominee Vice President Kamala Harris will win
the November poll. The American University professor has correctly
predicted the results of all but one US presidential election since
1984.

---

Apparently UA army chief Syrskyi speaks Ukranian pretty badly. That's
bcz its his second language, just like for Zelensk, the first one
being Russian.

---

WION: "Chances of Israel and Hamas reaching a phased hostage-ceasefire
deal were 'close to zero', a report in Times of Israel has claimed."

---

Cetta, de la Pena: "This paper provides elements in support of the
random zero-point radiation field (ZPF) as an essential ontological
ingredient needed to explain distinctive properties of
quantum-mechanical systems. We show that when an otherwise classical
particle is connected to the ZPF, a drastic, qualitative change in the
dynamics takes place, leading eventually to the quantum dynamics...

[An] inspection of the current literature readily reveals the
existence of about two dozen different interpretations of QM, some
more popular than others, and none of them experimentally
verified. How can it be that a fundamental theory that provides the
basis for a most significant part of contemporary physics, admits such
a variety of alternative, even contradictory interpretations? No
serious physicist or philosopher of science in his five senses would
claim to come up with a better interpretation of Newtonian mechanics
or Maxwellian electrodynamics. Reformulations of a known accepted
theory may appear, of course, but fundamental theories do not accept
reinterpretations. Special relativity did not reinterpret classical
mechanics, it extended mechanics to wider domains, and together with
quantum theory helped to specify its range of applicability. We should
conclude that in the case of quantum mechanics, such variety of
interpretations is indicative of a crucial underdetermination of the
theory...

[To] understand the origin of so many different visions about the same
fundamental theory, it is convenient to place ourselves in the context
in which QM was born. We recall that the quantum formalism—its
excellent mathematical apparatus that we still use today with
success—was born in the absence of a deep understanding of the quantum
phenomenology...

It is against this background that Heisenberg worked on his version of
the theory, the matrix mechanics. Heisenberg discovered that the
quantum particles have an unavoidable random behavior. Being persuaded
of the completeness of his theory, he took this randomness for an
essential, irreducible trait that neither needs nor admits a deeper
explanation...

Unknowingly, Schrödinger’s wave theory implied the introduction of a
new element into the quantum description. The point is that electron
interference patterns are produced by the accumulation of a high
number of point-like events, each one created by a single electron. A
single particle produces an isolated, randomly located bright point on
the detecting screen, the interference—the wave manifestation—becoming
evident only after very many hits. The conclusion—normally one that
goes unnoticed—is that Schrödinger’s wave function refers not to a
single particle, but to an ensemble of them. Well interpreted,
Schrödinger theory is intrinsically statistical in nature, and deals
with ensembles rather than individual particles.  Nevertheless, the
statistical perspective of the quantum phenomenon was dismissed in
general—and adamantly opposed by the Copenhagen school in particular,
which prevails to date under different guises.. This opened the door
to another infelicitous ingredient, the observer. The introduction of
an active character in order to ’explain’ the reduction of the
distinctive quantum mixtures to the pure states observed, added a
subjective ingredient to the already odd quantum scheme.  All in all,
such variety of interpretations and re-interpretations indicates that
something of importance is missing in the theory. Having so many
variations indicates that the issue is actually not one of
interpretation, but of an essential incompleteness. The absence of an
appropriate guiding ontological element has turned the physical
situation into a mystery...

However, rather than [an] incompletenesses.. we are referring to an
essential ingredient that is missing. The point is that whatever is to
be added to the incomplete theoretical framework should be able to
address simultaneously some of its main puzzles, including not just
the nature of quantum fluctuations; atomic stability, quantum
transitions, discrete atomic spectra, wavelike phenomena and the like
should find their natural explanation in a coherent scheme.

The present paper is one of a series that deals with the development
of stochastic electrodynamics (SED) as a physical foundation for
quantum mechanics. In previous work we have shown that, by including
the zero-point radiation field (ZPF), SED allows us to arrive at a
consistent description of the stationary states and to derive the
(nonrelativistic) radiative corrections proper for QED"

[[-]](https://arxiv.org/pdf/2210.16388)

---

I see CNBC shared a list of reactors under construction, but we have
to stress HTR-PM in China, HTTR in Japan, HTGR-POLA in Poland in the
list are all helium-cooled reactors. So the main feature of these
reactors is not they are small, they are *cooled differently* which
gives them additional safety features. Proper detail was not provided
in this article.

---

CNBC: "New nuclear plant designs, called small modular reactors, could
speed deployment of carbon-free power"

[[-]](https://www.cnbc.com/2024/09/07/how-small-modular-reactors-could-expand-nuclear-power-in-the-us.html)

---

F24: "Hezbollah fires rockets, Israel strikes after attack kills
Lebanese emergency workers"

---

\#Frontline \#UA \#RU 08/30 - 09/09

[[-]](ukrdata/map34.html)

---

Paper: "The zero-point field and the emergence of the quantum..  In
this paper we present a new way of arriving at the quantum formalism,
based on the recognition of the reality of the random zero-point
radiation field (ZPF). The advantage of this approach lies in that one
sees into the quantum world from outside, which affords a perspective
wider than the one reachable from within the quantum theory
proper. Many of the usual conceptual problems that characterize
presentday quantum mechanics (QM) are thus dissolved, and new physical
elements are integrated that help to clarify its physical and
conceptual contents. At the same time, the fresh perspective proposed
invites us to cross the doorway and go beyond the strictly
quantum-mechanical realm..

When referring to the problems of QM we have in mind basically those
conceptual puzzles — frequently bordering philosophy of science, to
the annoyance of some physicists, although their nature is physical —
that have been under scrutiny and debate since the early days of the
theory, but remain basically as unsolved now as they were eighty years
ago. We recall as examples: the irreducible or unexplained
indeterminism characteristic of the theory; the fact that it predicts
probabilities, not outcomes; that it then requires a measurement
theory for its accomplishment, which means opening the door to
observers and their subjectivism, and giving birth to undefined
boundaries between the quantum and the classical world. Add to this
the loss of realism; two opposed laws of evolution (Schrodinger’s
equation and the collapse of the wave function); nonlocality and, for
many, superluminal influences and so on. There are also some strictly
technical questions, such as the lack of a clear physical explanation
of the mechanism that stabilizes the atom and leads to quantized
states (rather than a mere description of the phenomenon), or of the
mechanism that entangles two identical noninteracting particles. The
list is not short...

It is important to realize that although the ZPF could appear at first
as a sort of collection of hidden variables introduced to complete the
quantum description, this is not the case. Quite the contrary: nothing
is added to QM, but the latter emerges from a more general theory that
contains the ZPF"

[[-]](https://www.researchgate.net/profile/Ana-Maria-Cetto/publication/270725917_The_Zero-Point_Field_and_the_Emergence_of_the_Quantum/links/56211ef808ae70315b58c7f9/The-Zero-Point-Field-and-the-Emergence-of-the-Quantum.pdf)

---

Obammer, Kamaller.. the invasive R.. 

---

Just kidding.. I am using his formulation, obviously we reached the
same conclusion.  I also assign an advantage to Dems, Reps have a
chance and if anyone can pull it off, it is DJT. But I have to make a
call, so I will call it for Kamaller

---

It's like he read my mind..

Abramovitz: "With less than three months remaining until Election Day,
and with voting beginning next month in several states, the 2024
presidential race has been transformed by President Joe Biden’s
withdrawal from the race..

Many things about the 2024 election have been highly unusual,
including the withdrawal of the incumbent president under pressure
from his own party’s leaders, his replacement by a woman of mixed
Black and Indian ancestry, the Republican Party’s nomination of a
former president who has been convicted on felony charges, and an
attempted assassination attempt against that Republican
candidate. Despite these remarkable developments, however, the
*Time for Change* forecasting model should allow us to predict both the
popular and the electoral vote with a high degree of accuracy because
this election, like all presidential elections, is likely to be
decided by a few fundamental forces.

The assumption underlying the *Time for Change* model, which has an
excellent track record in predicting the outcomes of presidential
elections since 1992, is that the results of these contests are
largely determined by three factors: the popularity of the incumbent
president, the state of the economy, and the number of terms that the
president’s party has controlled the White House.

Plugging in President Biden’s net approval rating of -18% in late June
and the estimated second quarter growth rate of 2.8% in real GDP along
with the fact that Kamala Harris will be defending the White House
after a single Democratic term in office, the *Time for Change* model
predicts narrow Democratic victories"

[[-]](https://centerforpolitics.org/crystalball/time-for-change-model-predicts-close-election-with-slight-edge-for-kamala-harris/)

---

Euronews: "EU electric car sales stall as Germany lifts its foot off
the pedal"

---

Forbes: "Former President Donald Trump proposed the creation of a
sovereign wealth fund for the U.S. on Thursday, suggesting the
government-owned investment fund used by countries such as Norway,
China and South Korea would be created and partially funded by tariffs
if he wins the presidential election."

---

Steve Bannon: "America is not an idea. America is a country, with
borders and citizens"

---

Gun violence too has to do with US' "business-first" mentality, not
attacks on "freedom". Rampant capitalism is killing those people, gun
manufacturers hide behind sacred words such as liberty, they don't
give a damn what happens to anyone as long as they make money. I don't
think the founders had the kind of hardware in mind that could take
out an entire British regiment within seconds when they wrote what
they wrote back in the day. Some perspective is needed here, but
muckers already know that. The only founder they care about is Benjamin.

---

The French left has some bizarre ideas on Ukraine.. They are pro-war
pro-corporation funded US politics fanning the flames in the middle of
Europe causing chaos. Why would you be for that?

---

So despite forming a block to freeze out the National Rally, the left
got nothing, NR is getting a policy concession on immigration via
Barnier. Appropriate electorally? Bcz the mechanism used to boot out
NR were un-democratic, they would have won more votes in a regular
election so deserved more concessions.

---

Politico: "Macron attempted to break an almost two-month political
deadlock on Thursday by appointing Michel Barnier as prime
minister.. Barnier, a conservative heavyweight in the right-wing
Republicans party, is a well-known figure in Brussels, having served
as the European Union’s former chief Brexit negotiator and twice as a
European commissioner... In a conversation [in July], Barnier said
France’s most pressing issues were immigration, the state of its
public finances and rebuilding its industrial and agricultural
capacities"

---

AA: "Netanyahu's stance on Philadelphi corridor driven by fear of
government collapse, says former Shin Bet chief.. ‘Philadelphi
corridor is only required for the Netanyahu-Smotrich axis to preserve
this messianic and dangerous government,’ argues Nadav Argaman"

---

Anatolian Agency: "Netanyahu's insistence on military presence in
Philadelphi Corridor undermining cease-fire deal"

---

