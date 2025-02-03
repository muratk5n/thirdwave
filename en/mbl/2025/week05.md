# Week 5

NYT: "[Gates] recently brought out his second Netflix series, 'What’s
Next? The Future With Bill Gates.' The fourth of the five episodes,
'Can You Be Too Rich?' had people, including Senator Bernie Sanders,
the democratic socialist from Vermont, saying definitively yes. It was
a mild but real form of self-criticism that few other billionaires
would subject themselves to... he supports a tax system that is more
progressive. Every year, he adds up the taxes he has paid over his
lifetime. He figures he has paid $14 billion.. Under a better system,
he calculates, he would have paid 40 billion"

---

Gretchen Whitmer is great on clean energy. I remember the post below.

[[-]](https://www.mlive.com/environment/2024/11/clean-hydrogen-hub-in-michigan-gets-22m-in-federal-backing.html)

---

Good for you, Shapiro. It looks like he has some positive attributes

AP: "Gov. Josh Shapiro said Thursday that he wants to fast-track the
construction of big power plants in Pennsylvania and offer hundreds of
millions of dollars in tax breaks for projects that provide
electricity to the grid and use hydrogen.. Shapiro, a Democrat, said
he wants to start the 'next chapter in Pennsylvania’s long story of
energy leadership'.. 'Pennsylvania, it’s time for us to be more
competitive. It’s time for us to act. We need to take some big and
decisive steps right now, build new sources of power so Pennsylvania
doesn’t miss out,' Shapiro said at a news conference at Pittsburgh
International Airport"

---

MarineLink: "Yanmar to Accelerate Hydrogen Engine Production.. Yanmar
Power Technology has received Japanese government approval for its
production plans for hydrogen-fueled engines and fuel cells."

---

Offshore Energy: "German specialty chemicals company Evonik has signed
a term sheet with Dutch energy company VoltH2 to advance green
hydrogen production at the Delfzijl chemical park in the Netherlands"

---

Marche, *The Next Civil War*: "The Patriotic Millionaires formed in
2010 with two extraordinary goals: to lobby politicians to increase
their taxes.. [Some..] rich know what historians know: every society
in human history with levels of inequality like those in the United
States today has descended into war, revolution, or plague. No
exceptions. There are precisely zero historical precedents that don’t
end in destruction"

---

Higher inequality causes lower growth, see below. There is a reverse
correlation between GINI and GDP increase, and, since we shift one
series back in time, the correlation suggests causation.

```python
# Get GINI, GDP
df = u.get_fred(1980,['SIPOVGINIUSA','GDP']).interpolate()
df['Growth'] = df.GDP.pct_change().shift(-3)
df[['SIPOVGINIUSA','Growth']].corr()
```

```text
Out[1]: 
              SIPOVGINIUSA   Growth
SIPOVGINIUSA     1.000000 -0.283214
Growth          -0.283214  1.000000
```

---

Whose fault is it... Can we also ask why is the military running
training flights over heavily populated areas, near known flight
routes, close to both the White House and the Pentagon? The
military-industrial complex is a sprawling enterprise.. it intrudes
into everyone's space. The public does not need more helicopters, more
training flights, more weapons, more bombs. 

---

RSF is getting its ass kicked.. They lost most of Sennar and its
connection to their main area. They are losing in Al Jazirah,
Khartoum, South Kurdufan...

\#Sudan \#RSF \#SAF - 11/24 - 01/31

[[-]](sdndata/map01.html)

---

MV Times: "Amid rumors and speculation that federal immigration
enforcement agents would conduct raids [in Martha's Vineyard] on
Thursday, schools and local businesses reported widespread absenteeism
because undocumented immigrants were staying at home.

Lumberyards have been eerily empty. Some Martha’s Vineyard schools
have reported nearly double their normal absentee rate, which
officials say is likely because parents — and their children — are
staying home over fears of being deported. A proprietor of a large
Island business reported that 20 percent of their staff have not shown
up to work, what they believe is over fear of deportation"

---

HotCars: "AVL RACETECH, the motorsport arm of AVL, took a massive leap
forward in 2022 by unveiling [a 2.0-liter hydrogen-powered internal
combustion engine (H₂-ICE) prototype. With water injection technology
and a turbocharged design, the engine delivers performance figures
that rival modern gasoline racing engines while offering the promise
of zero tailpipe..

AVL RACETECH Hydrogen Engine Highlights

- 150 kW per liter
- Up to 369 lb-ft between 3,000 and 4,000 RPM
- Up to 410 horsepower at 6,500 RPM

Key to this achievement is AVL’s innovative water injection system. By
injecting water into the intake air, the system increases boost
pressure.. This allows the engine to generate up to 369 lb-ft between
3,000 and 4,000 RPM. The design is backed by AVL’s expertise in
advanced simulation modeling and 3D flow calculations, ensuring
maximum efficiency without compromising safety or reliability"

---

Just like you cannot formulate physics by running regression on
physics datasets, language, human thought can not be formulated via
language data alone. Larger scale produces interesting answers, but no
real-world deployable solutions that include
[planning](https://www.theatlantic.com/technology/archive/2024/02/chatbots-marketing-plan-your-next-trip/677481/).

---

Chomsky is uniquely qualified to comment on LLMs, as he was the
creator of formal language theory, worked at MIT, aware of
computational issues, approaches in the field.

---

Paper: "How should the advancement of large language models affect the
practice of science?.. Downstream, LLMs threaten the notion of
scientific expertise, shift incentive structures, and undermine trust
in the literature. Notions of systematic review are undercut by the
randomness inherent in LLM output. And most importantly, when someone
uses an LLM to generate a literature review, the claims generated are
not directly derived from the manuscripts cited. Rather, the machine
creates textual claims, and then predicts the citations that might be
associated with similar text. Obviously, this practice violates all
norms of scholarly citation. At best, LLMs gesticulate toward the
shoulders of giants"

[[-]](https://www.pnas.org/doi/10.1073/pnas.2401227121)

---

Status Coup: "Liza Star, a pregnant fisherwoman.. lives with her
family about 1,000 feet away from the Moss Landing lithium plant fire
that has sickened residents near and far. Black particles--that seem
to be ash—have blanketed the boat that she and her family live in and
she and her daughters have been suffering with various health symptoms
since the fire nearly two weeks ago"

---

"@mosseri@threads.net

Threads has reached 320M monthly actives and is going strong with more
than 100M daily actives. There’s still so much more to do, but we’re
excited about the progress"

---

People who are paying mortgages (mortgagors?) should not be counted as
"home owners". If you paid 1 year of a 10 year mortgage you still
don't *own* a home, you own 10% of a home. 90% of that house is owned
by someone else, the bank or someone wealthy who can hold that debt
and collects interest on it. The statistics should capture this, eg 10
people owning 10% of a house adding up to home ownership of 1.

---

```python
u.rottentomatoes("Star Trek Section 31")
```

```text
Out[1]: {'critics': '20', 'audience': '17'}
```

---

\#Frontline \#UA \#RU - 01/26 - 01/31

[[-]](ukrdata/map05.html)

---

Marche, *The Next Civil War*: "You know the problem of inequality is
serious when rich people have started to worry that they’re too
rich. In the United States, the wealthiest of the ultrawealthy, the
kind who wouldn’t notice $10 million one way or another, are forming
political action committees opposed to the concentration of wealth in
their own hands. The Patriotic Millionaires formed in 2010 with two
extraordinary goals: to lobby politicians to increase their taxes, and
to explain to ordinary Americans how unjust the economic order is. Two
of the richest men in the world, Bill Gates and Warren Buffett, have
publicly called on the government to raise their tax rates. 'I have a
message for my fellow filthy rich, for all of us who live in our gated
bubble worlds,' warned early Amazon investor Nick Hanauer in
2014. 'Wake up, people. It won’t last.' He couldn’t be more right. The
Koch brothers have recently shifted their charitable endeavors from
libertarian politics to the problem that the new generation will be
worse off than the old.

The rich know what historians know: every society in human history
with levels of inequality like those in the United States today has
descended into war, revolution, or plague. No exceptions. There are
precisely zero historical precedents that don’t end in
destruction. Since 1980, inequality has been growing globally, but in
the United States the growth is most dramatic. In 2015, the top 1
percent of American families made 26.3 times what the 99 percent did,
garnering 22 percent of all income—the highest share since the peak of
23.9 percent before the Great Depression. In 1965, a CEO made roughly
twenty times the typical worker’s pay.  Now it’s 271 times. From 1980
on, the poorest 50 percent of the population has consistently seen a
decline in their share of income. American inequality is now worse
than it was in 1774"

---

Europe to the rescue..  They could be the antidote to crass Anglo
capitalism.

"@rra@post.lurk.org

In light of US tech oligarchy setting its sights on Wikimedia
Foundation, a historical detail I did not know before: #Wikipedia
became the non-profit it is today partly as the result of a labour
strike of Spanish Wikipedia editors who disagreed with the proposed
inclusion of advertisements. Initially, it was not clear what revenue
model Wikipedia would get, and Wales moved towards a for-profit model
already a year after launch. However, rather than working for free, so
Jimmy Wales could profit from their labour via advertising, Spanish
contributors forked Spanish Wikipedia as the Encyclopedia Libre
Universal. Under the threat of losing the editorial community of such
a large language, Wales conceded and set up the non-profit"

---

Based on all the previous info, everything needed for the law of
centripetal force is there, $m,r,v$, plug those reverse engineer Sun's
mass, and density. That result ain't the mass of plasma. 

---

But then how far is Earth from the Moon in kilometers? Again DIY old
school, time the lunar eclipse, and form a relation with the variables
seen [here](https://physicsteacher.blog/wp-content/uploads/2021/05/screenshot-2021-05-31-at-11.51.45.png?w=640).
Aristrarchus did that 270 BC and got a pretty close answer.

---

The article on Sun's density required prev knowledge of Sun-Earth
distance, how to DIY know that from first principles based on basic
measurements? This was doable even in ancient times, when it's half-moon
we know the 2D [placement](https://upload.wikimedia.org/wikipedia/commons/f/f3/AristarchusHalfLitMoon2.png).
There is a right triangle, measure $\varphi$ w/ basic instruments,
it's like 87 degrees, cosine is $L/S$, reverse that,

```python
np.round(1./np.cos(np.deg2rad(87)),2)
```

```text
Out[1]: 19.11
```

The Sun is roughly 19 times further to Earth than Earth is to the Moon.

---

Note "the reduction in the velocity of light" statement - with the
scheme below the speed of light is variable.

---

Puthoff: "Textbook presentations treat General Relativity (GR) in
terms of tensor formulations in curved space-time.. One [different]
approach that has a long history in GR studies.. is what can be called
the polarizable-vacuum (PV) representation of GR. Introduced by Wilson
and developed further by Dicke, the PV approach treats metric changes
in terms of equivalent changes in the permittivity and permeability
constants of the vacuum, $\epsilon_o$ and $\mu_o$..

In brief, Maxwell's equations in curved space are treated in the
isomorphism of a polarizable medium of variable refractive index in
flat space; the bending of a light ray near a massive body is modeled
as due to an induced spatial variation in the refractive index of the
vacuum near the body; the GR reduction in the velocity of light in a
gravitational potential as compared to a flat-space reference frame at
infinity is represented by an effective increase in the refractive
index of the vacuum, and so forth"

[[-]](https://arxiv.org/pdf/gr-qc/9909037)

---

Puthoff: "Gravitational theory.. is recognized to be essentially
phenomenological in nature. As such, it invites attempts at derivation
from a more fundamental set of underlying assumptions, and six such
attempts are outlined in the standard reference book *Gravitation*, by
Misner, Thorne, and Wheeler. Of the six approaches presented..
perhaps the most far-reaching in its implications for an underlying
model is one due to Sakharov; namely, that gravitation is not a
fundamental interaction at all, but rather an induced effect brought
about by changes in the quantum-fluctuation energy of the vacuum when
matter is present. In this view the attractive gravitational force is
more akin to the induced van der Waals and Casimir forces.. In this
paper we explore the Saharov viewpoint on the basis of a conceptually
simple, classical model"

[[-]](http://www.earthtech.org/publications/PRAv39_2333.pdf)

---

Louis de Brogli was JPV's mentor we mentioned earlier. Big shot. 

---

Jean-Pierre Vigier: "The evidence from.. six experiments that bear on
the question of the speed of gravity is unambiguous in excluding
answers as slow as lightspeed...  no serious claim of experimental
support for gravity propagating at lightspeed has been advanced in
modern times. Attempts to do so have seriously confused changes in
gravitational force fields with gravitational radiation (an effect of
changes in potential fields), the latter of which unquestionably would
propagate at speed c..

When a source mass accelerates, that induces changes in its
gravitational force field. The lack of detectable aberration
(propagation delay) for those changes means that the distant
gravitational field accelerates when the source mass accelerates, in
lockstep. To avoid direct violation of the causality principle, the
propagation delay must be finite, even though much smaller than the
corresponding propagation delay for photons. Because special
relativity (SR) forbids propagation speeds faster than lightspeed in
forward time, the customary interpretation of that theory is in
conflict with, and is potentially falsified by, this result. GR has
always implicitly recognized these facts through its equations of
motion, which use instantaneous coordinates and momenta rather than
retarded ones. That and its reliance on a single frame to define
‘‘coordinate time’’ mean that GR is based as much on Lorentz’s
interpretation of relativity (LR) as on SR. These two theories, LR and
SR, both employ the relativity principle and the same math (Lorentz
transformations), but LR adopts a preferred frame and lacks the
reciprocity between frames postulated by SR. Interestingly, no
experiment testing SR or LR confirms frame reciprocity. Therefore,
because LR is consistent with all experiments, it remains just as
viable as SR as a model for the relativity of motion. It follows that
the falsification of the SR interpretation in favor of the LR
interpretation has no immediate mathematical consequences for GR. The
main physical consequence is negation of the proof that
faster-than-light propagation is impossible"

[[-]](https://www.researchgate.net/publication/225711498_Experimental_Repeal_of_the_Speed_Limit_for_Gravitational_Electrodynamic_and_Quantum_Field_Interactions)

---

As Chomsky [said](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html)
these things are "lumbering statistical engine[s]" for pattern
matching which "gorg[e] on hundreds of terabytes of data and
extrapolating the most likely conversational response or most probable
answer to a scientific question". They are not efficient. So it should
be no surprise some found ways of optimizing it. But the optimization
is like optimizing an hammer that constantly, wrogly seeks nails to
hit, in other words a better wrong tool for a misanalyzed problem.

---

Chollet: "o1 does represent a paradigm shift from 'memorize the
answers' to 'memorize the reasoning', but is not a departure from the
broader paradigm of improving model accuracy by putting more things
into the pre-training distribution"

---

Same as o1..? o1 itself was not good enough.. And even o3 will likely
fall short of the new ARC 2 test. 

---

Nature: "DeepSeek-R1 performs reasoning tasks at the same level as
OpenAI’s o1..  DeepSeek emerged from relative obscurity last month
when it released a chatbot called V3, which outperformed major rivals,
despite being built on a shoestring budget. Experts estimate that it
cost around $6 million to rent the hardware needed to train the model,
compared with upwards of 60 million dollar for Meta’s Llama 3.1 405B,
which used 11 times the computing resources"

---

Politico: "Secretary of State Marco Rubio halted spending Friday on
most existing foreign aid grants for 90 days. The order, which shocked
State Department officials, appears to apply to funding for military
assistance to Ukraine"

---

Here's a simple rule - do not use lithium-ion tech.

This plant was seperate from the wildfires BTW, the shit just ignited,
and turned into hellfire. 

LA Times: "‘Horrifying’ fire at California lithium battery plant
sparks calls for new clean energy rules"

---

Carbon Credits: "Vistra Fire and Teslas Burning in California: Is it a
Wake-Up Call for Battery Storage Safety?"

---

Lithium-ion batteries likely contributed to the spread of LA
wildfires..  if they burn longer and almost impossible to put out,
they would contribute to the spread more than any other material.

---

VICE: "Burning EV Batteries Are Delaying LA Wildfire Clean-Up...
lithium-ion batteries.. have complicated the fight against LA
wildfires. When those batteries catch fire, they become a raging
inferno nearly impossible to put out. A Tesla-related car accident
back in 2018 is a tragic example of this. The car crashed, bursting
into flames and killing everyone inside. It took emergency responders
almost 300 gallons of water and foam to extinguish the fire. After
everyone thought the blaze was subdued, responders were loading the
Tesla for removal when the battery ignited again, entirely on its
own. The fires are so intense and difficult to combat that a common
tactic for battling them is to not battle them at all — just let them
burn until there’s nothing left.

---

Bloomberg: "Burning Teslas in LA Add to Toxic Mix Hindering Wildfire
Cleanup.. As the smoke clears from devastating Los Angeles wildfires,
efforts to clean up the affected areas are being complicated by
burnt-out electric and hybrid vehicles and home-battery storage
systems.

Lithium batteries from Tesla Inc., along with those from other
carmakers, have added to the mix of toxic materials requiring
specialized removal in the wake of the fires, delaying the fire
victims’ return to their properties.

'A lot of the cars in the evacuation area were lithium batteries,'
said Jacqui Irwin, a state assembly member representing the Pacific
Palisades, one of the neighborhoods hardest hit by the fires. 'We’ve
heard from firefighters that those lithium batteries burned fires near
homes – like those with power walls – for much longer.'.. Fires in
lithium batteries can require large amounts of water to put out"

---

Wendell Pierce is the new Perry White. I have to see this.

---

The National: "In a statement marking the one-year anniversary of the
ICJ saying that Palestinians’ right to be protected from genocide
faced a 'plausible' risk from Israel, Amnesty International said the
UK Government had 'contributed to Israel’s impunity and risked British
complicity in serious crimes against international law'"

---

Section 31 was not part of Roddenberry canon, it was added later,
during the Deep Space Nine era where the storylines also displayed
frequent usage of munee, capitalist Ferrengi were normalized, and
other weirdo shit was there... DS9 is the worst of the bunch IMO until
its record was beaten by ST Discovery.

---

\#Burr \#Kimmel

[[-]](https://www.youtube.com/embed/r7wcU4W4tDE?start=160&end=177)

---

There is no deep state in US today

---

\#FreeLuigi

---

The movie is about "Section 31" the deep state of the
Federation. Today's corporate power via their movies would rather have
you think about a futuristic deep state which evokes images of
bureucratic opression, this way you fear government structures
*today*, with that fear tell the gov not to tax the rich (anything gov
does is bad), and the current privatized dystopia, a fascistic
corporate control mechanisms continue. Thankfully the movie sucks so
it will likely create the opposite effect.

---

Critic: "The only thing Star Trek about this [movie] is some of the
names of the alien races, a few references here and there, and some
familiar sound effects. There's no boldly going anywhere here, there's
no interesting sci-fi concept, no highbrow ideas, no moral or ethical
dilemma, no intelligent plot, no exploration, no optimism, and no
hope. It's bland, bleak, dark, joyless, and dreadful"


---

One of those degenerate ones... Jar Jar Ibrahim / Kurtzman
type.  The reviews aren't good.

---

There is a new Trek movie?

---

No Shit

Paper: "In this paper our aim is to show that an increase in wealth
inequality is associated with a slowdown in economic growth"

[[-]](https://www.sciencedirect.com/science/article/pii/S003801212400003X)

---

Sriskandarajah, LSE: "The rest is not just politics: how inequality is
trumping democracy.. In essence, the exponential accumulation of
wealth and power by the 'private few' reduces the capacity of the
'public many' to exercise the freedom to make the choices that shape
our lives. The promise that each of us in a democracy has an equal
vote and equal say in how our society functions then begins to ring
hollow.

Those earning less than a minimum wage are the least likely to be
civically engaged... inequality lowers an individual’s sense of trust
in others: not in family or friends but in unspecified persons. Again,
this kind of generalised trust is a core component of social
capital. We tend to have less trust in people who are dissimilar to
us, which might explain the striking correlation observed in countries
like the US between an increase in income inequality and a sharp
decline in trust.

Central to neoliberalism is the push to shrink the size of the state –
to see little or no need for social security provisions or any other
transfers of resources from richer to poorer groups of
society. Neoliberals are steadfastly against such
'redistribution'. But a study by the non-partisan RAND Corporation
found an eye-watering level of redistribution in the US in the period
between 1975 and 2018 – just not in the direction that progressives
were calling for. During this era in which Reagonomics and neoliberal
policies were let loose, the bottom 90 per cent of America’s income
earners saw a hit to their combined incomes of $2.5 trillion each year
relative to the case where their incomes had grown in line with the
average(per capita) income trend for the country as a whole over this
period"

---

\#Davis \#Baud \#Ukraine

[[-]](https://www.youtube.com/embed/TnSD3l5Bbfc?start=1063&end=1324)

---

Doom CAPTCHA

[[-]](https://doom-captcha.vercel.app/)

---

RR's acting took a dive after he became a bidnessman.. it's a
long-running sarcastic shtick now rather than anything of substance.

[[-]](https://youtu.be/j_6bscCG7OA?t=813)

---

The wife is one of those "entrepreneurial" stars too apparently. When
these people are on screen you are not sure whether they are selling
products to make a movie, or making a movie to sell a product.

---

Guy felt up Ryan Reynold's wife, RR is jealous trying to cancel him? 🤣

---

It is supposed to be 1 person 1 vote. Thanks to inequality now it is
"1 dollar 1 vote".

---

\#Frontline \#UA \#RU - 01/19 - 01/26

[[-]](ukrdata/map04.html)

---
