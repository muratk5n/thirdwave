# Week 41

F24: "How Donald Trump engineered the Gaza deal.. [M]ost of Trump's
efforts had been behind the scenes, as he sought to pressure a
reluctant Benjamin Netanyahu and win Arab support...

Trump has shifted from giving Israel a "blank check" to a conditional
stance...Trump was also privately incensed by Israel's attack on Hamas
members in fellow US ally Qatar while negotiations were at a sensitive
stage. He used Arab unity against the attack to get them all to agree
to the plan.

He then ambushed Netanyahu, making him call Qatar's leader from the
Oval Office to apologize. Trump even sat holding the phone for
Netanyahu while the Israeli leader read from a piece of paper, a photo
released by the White House showed...

Firstly, the plan he laid before Netanyahu and Israeli officials had
already been drafted following extensive consultations with Arab and
Muslim leaders at the United Nations the previous week.

When Netanyahu was confronted with it, he found there were key areas
in it that he had sworn not to accept, especially on his refusal to
allow a Palestinian state.

Hamas responded [partial acceptance].. There was no mention of the
fact that Hamas had not fully agreed to most of the other points in
his plan. But instead of quibbling over the details, Trump pushed
Israel, Hamas and their mediators to quickly thrash out a deal.

Trump told the Axios news outlet that he had said to Netanyahu: '"Bibi,
this is your chance for victory.' He was fine with it. He's got to be
fine with it. He has no choice. With me, you got to be fine""

---

The American Conservative: "Israel and Hamas Sign Off on First Phase
of Ceasefire Deal"

---

F24: "Argentina's Congress curbs Milei’s decree powers in major blow
to libertarian leader"

---

"@jbz@indieweb.social

⚠️ Qualcomm just bought Arduino, holy f*ck.

Huge loss for everyone, including Qualcomm, there's no way they'll
recover their money once we ran away."

---

[Link](https://youtu.be/86URGgqONvA?list=RD86URGgqONvA&t=67)

---

Sornette's bubble detection formula,

$$
\ln(p(t)) = A + B(t_c - t)^\beta  \big[ 1 + C \cos (\omega \ln(t_c-t) + \phi )  \big]
$$

We can fit that to data.. Let's try SP 500.

```python
df = u.get_yahoo_ticker2(2024, "SPY")
df = df[df.index > '2025-04-01']
u.sornette_lppl(df, "SPY")
```

```text
tc: 190.115448
m: 0.990000
w: 12.460486
A: 6.524082
B: -0.001276
C1: 0.000001
C2: -0.000183
C_amplitude: 0.143820
phi_phase: -1.567148
```

The characteristic parameters of a bubble occurs at $B<0$, $0<m<1$,
$6<\omega<13$, the values above fit that pattern. There is a bubble.

---

The Internet is abuzz with that share

[[-]](https://cdn.fosstodon.org/media_attachments/files/115/341/942/328/006/737/original/82e68bc5b1d4cdbe.jpg)

---

Daily Mail: "Charlie Kirk furiously criticized 'bullying' Jewish
donors and said he was considering 'leaving the pro-Israel cause'
before his death, it was confirmed today.

The bombshell revelation comes after Candace Owens released a
screenshot of Kirk fuming in a group chat that Jewish donors were
pulling funding over his links to Tucker Carlson.

Turning Point spokesman Andrew Kolvet confirmed the authenticity of
the screenshots on Tuesday during the latest episode of The Charlie
Kirk Show.

In the text messages, Kirk privately complained that a Jewish donor
had withdrawn a $2 million investment into the organization because he
refused to disinvite Carlson from the upcoming AmericaFest event.

'Just lost another huge Jewish donor,' Kirk wrote. '$2 million a year
because we won't cancel Tucker. I'm thinking of inviting Candace.'

'Jewish donors play into all the stereotypes. I cannot and will not be
bullied like this.'

Kirk concludes: 'Leaving me no choice but to leave the pro Israel
cause.'"

---

Sornette: "[8/4] Since the 2008 Global Financial Crisis, the
U.S. equity market has been buoyed by one unprecedented monetary
intervention after another: QE1, QE2, QE3, Operation Twist, and what
was essentially QE-infinity. Even major shocks—2018’s rate-driven
selloff, the COVID-19 crash of 2020, and the losses of 2022—were
rather brief and followed by aggressive recoveries, aided by dovish
central banks and unprecedented fiscal expansion. In recent years, the
U.S. federal government has run deficits around 7% of GDP—levels
historically associated with wartime or deep recessions—despite
operating in a context of peace and nominal full employment. The
source of U.S. market exceptionalism is no mystery: it has been driven
by this relentless policy support, a potent mix of ultra-loose
monetary conditions and fiscal largesse, rather than by organic or
sustainable economic fundamentals. This cocktail of interventions has
inflated asset prices, masked structural fragilities, and fostered a
dangerous illusion of resilience.

The U.S. market has come to represent nearly 70% of global market
capitalization, despite the U.S. economy accounting for only ~24% of
global GDP. This imbalance is amplified by record-breaking
concentration: over 33% of U.S. equity value is now housed in just the
20 largest firms—a degree of dependence that has no historical
precedent.

All this converges to a troubling picture: a market propped up not by
resilient fundamentals, but by layers of leverage, fiscal deficits,
speculative AI and tech euphoria, and massive defense spending...

Trump’s return and his tariff escalation are not historical
aberrations. They are symptoms of a long unaddressed social and
economic decay. The last two decades have seen exploding inequality
growth, real wage stagnation, and the erosion of the middle class—the
backbone of functional democracies. Much like the French
Revolution—where poorly managed famines following successive crop
failures ignited long-simmering social tensions—the rise of today’s
populist movements is a direct consequence of persistent elite
mismanagement and failure to address deepening inequality...

Expect high volatility, deeper corrections, and a breakdown of the
AI-tech-shale-military bubble that has dominated capital
flows. Mega-cap concentration will unwind painfully. Value stocks may
perform better, but broad indices like the S&P 500 are likely to
struggle for years."

---

Didier Sornette is a physicist who applied the mechanics of material
breakdown to financial markets, predicting bubbles and crashes. His
latest newsletter above.

---

MIT Economics: "Some predictions have claimed AI will double growth or
at least create a higher growth trajectory than usual. By contrast, in
one paper, *The Simple Macroeconomics of AI* published in the August
issue of Economic Policy, [economist] Acemoglu estimates that over the
next decade, AI will produce a 'modest increase' in GDP between 1.1 to
1.6 percent over the next 10 years, with a roughly 0.05 percent annual
gain in productivity"

---

Financial Times: "Lately, [AI] optimism has become a self-fulfilling
prophecy. The hundreds of billions of dollars companies are investing
in AI now account for an astonishing 40 per cent share of U.S. GDP
growth this year... Since the wealthiest 10 per cent of the population
own 85 per cent of U.S. stocks, they enjoy the largest wealth effect
when they go up...

In a way, then, America has become one big bet on AI. Outside of the
AI plays, even European stock markets have been outperforming the
U.S. this decade, and now that gap is starting to spread... What that
suggests is that AI better deliver for the U.S., or its economy and
markets will lose the one leg they are now standing on."

---

Chollet: "You can teach a Transformer to execute a simple algorithm if
you provide the exact step by step algorithm during training via CoT
tokens.

This is interesting, but the point of machine learning should be to
*find* the algorithm during training, from input/output pairs only --
not just memorize an externally provided algorithm. Pretty trivial
program synthesis techniques can achieve just that in the case of
multiplication.

Because if you already have the algorithm, you can just write it down
and execute it instead of training a Transformer to inefficiently
encode it."

---

Paul: "A beautiful paper from MIT+Harvard+ @googledeepmind
👏.. Explains why Transformers [used in LLM neural nets] miss multi
digit multiplication and shows a simple bias that fixes it. The
researchers trained two small Transformer models on 4-digit-by-4-digit
multiplication. One used a special training method called implicit
chain-of-thought (ICoT), where the model first sees every intermediate
reasoning step, and then those steps are slowly removed as training
continues."

---

Chollet: "The point of our work isn't to build an artificial
human. The universe is full of questions far more interesting than our
own reflection. The point is to create a new kind of mind to help us
explore & understand the universe better than we can ourselves. The
way to think about AGI is as a scalable, efficient formalization &
implementation of the scientific method. Not a brain in a jar."

---

"Vietnam reports that some 400,000 people have suffered death or
permanent injury from exposure to Agent Orange. Furthermore, it is
estimated that 2,000,000 people have suffered from illnesses caused by
exposure and that half a million babies were born with birth defects
due to the effects of Agent Orange"

---

JFK gave the order for the use of the weapon. An overrated president,
and a war criminal.

---

'Aw man, we can't see Charlie among those trees.'

'Why don't we destroy all trees!'

This is literally how they thought

---

"USVA Agent Orange is a blend of tactical herbicides the U.S. military
sprayed from 1962 to 1971 during Operation Ranch Hand in the Vietnam
War to remove trees and dense tropical foliage that provided enemy
cover."

---

If quantum computation does not provide much improvement over
classical, it will reinforce the view that there is no inherent
parallelism in nature to be exploited at quantum level, the Copenhagen
interpretation is a farce, as Masse stated below.

[[-]](../../2025/04/masse-collected-comments.html#qm)

---

My first software project as programmer used Oracle in its solution
stack, I am very familiar in what it can and cannot do. It was okay
when there were no alternatives... I remember their pricing was at eye
watering levels.. That is how ZioJew Ellison made his mint.

---

There is no need to use Oracle in any organization. Free and open
source software Postgresql can help on almost all needs. It is fast,
can scale, it is actually seen as a drop-in replacement for Oracle
database.

---

Here is a joke for you: **British Cuisine**.

That's funny right?

Fish and chips and mad-cow disease, that's basically the menu

---

Learning how to cook from Jamie Oliver.. Why would anyone learn
cooking from a Brit?

[[-]](https://youtu.be/-cljlH9QmTo?t=493)

---

Jacobin: "Among Democrats, democratic socialists enjoy significant
popularity. The poll’s findings include:

- Democrats prefer democratic socialism to capitalism by a 58 point
margin. Socialism wins overall with likely voters under forty-five
years old.

- Democrats prefer left-wing political figures.. This was also true
across party lines in critical voting blocs: noncollege (+9), Latinos
(+30).

- Candidates who identify as democratic socialists are viewed just as
favorably (+69) among registered Democrats as candidates who identify
only as Democrats (+67).

'These results tell a clear story: democratic socialism is now
mainstream,' said DSA Fund executive director Gabe Tobias."

---

"@GossiTheDog@cyberplace.social

A few days ago Oracle, via the media, blamed their own customers for
not installing a July security update.. then when the media coverage
stopped, quietly released a new security update for the actual
exploited vulnerability. 🥴"

---

The Telegraph: "Merkel: Poland and Baltics partly responsible for
Ukraine invasion.. Former German chancellor claims the countries’
opposition to negotiations with Moscow fuelled Russian ‘aggression’"

---

Politico: "Judges appointed by Trump keep ruling against him. He’s not
happy about it."

---

For democratic politicking to work, the views of the new actors who
saw vote increases in the last election must be included in
governance. The centrists could adapt one hot button issue from each,
NR and the leftist coalition."

---

CNBC: "Déjà vu in France as political chaos returns. But this time,
it’s different.. the Lecornu government was not toppled by the
opposition, like those of predecessors Michel Barnier or Francois
Bayrou — it was its own allies that caused its downfall."

---

Of course.. time is ripe for such attempts.. 

F24: "Maduro says Venezuela thwarted 'false flag' plot to bomb US
embassy"

---

Firstpost: "With Gaza plan, Trump throws Netanyahu toughest dare:
making peace with Palestinians.. Two years after Hamas triggered the
ongoing war in the Gaza Strip with its all-out invasion of Israel,
Prime Minister Benjamin Netanyahu appears to be facing the toughest
moment of his decades-long career. His principal supporter, US
President Donald Trump, has told him to make peace with Palestinians —
and he would not take no for an answer.

But Netanyahu cannot afford peace.

Domestically, continuing the war favours Netanyahu, and, indeed,
prolonging the conflict with the Palestinians has always worked to his
advantage, and now Trump’s push for peace has cornered him, says
Muddassir Quamar, a scholar of the Israeli-Palestinian conflict at the
Centre for West Asian Studies at Jawaharlal Nehru University (JNU),
Delhi."

---

This is good analysis.. Says Lady Gaga is talented but actually
interested in something else, Drake is a Nepo Baby, and Britney Spears
was a total robot, her music, dance careography all managed by others.
Then the drama around her conservatorship, the father was not a
one-time event, that was basically her whole life.

[[-]](https://www.youtube.com/watch?v=dSfkdNSEuXo)

---

We should not try to mimic exactly how nature does things. We can
learn, get inspiration from it, but humans solve things differently. A
plane does not fly like a bird. Our math, our formulations
generalize. You can't compete with nature at micro level, you would
need a computer as big as the nature for that, and it still wouldn't
be fast enough.

---

HRMs introduce more structure into black-box neural-net artificial
intelligence systems. An analogy is we don't try to simulate fluid
dynamics starting with tiny water molecules, we use math to
generalize, there is always top-down structure imposition. HRMs raise
the level of abstraction, they attempt to mimic the outward effects,
abstract steps of thought via guidance rather than bottom up
micro-monkey interactions hoping it will reach intelligence. It's like
hoping unfettered markets with micro-monkey interactions of people,
bihnesses can lead to walhalla, vs controlled capitalism. LLM neurons
relied on tiny components whose magical, chaotic interrelations would
supposedly bring about Artificial Superintelligence. They failed. HRM
is pointing towards the new way.

---

\#HRM

[Code](https://github.com/sapientinc/HRM)

---

Paper: "Current large language models (LLMs) primarily employ
Chain-of-Thought (CoT) techniques, which suffer from brittle task
decomposition, extensive data requirements, and high latency. Inspired
by the hierarchical and multi-timescale processing in the human brain,
we propose the Hierarchical Reasoning Model (HRM), a novel recurrent
architecture that attains significant computational depth while
maintaining both training stability and efficiency. HRM executes
sequential reasoning tasks in a single forward pass without explicit
supervision of the intermediate process, through two interdependent
recurrent modules: a high-level module responsible for slow, abstract
planning, and a low-level module handling rapid, detailed
computations. With only 27 million parameters, HRM achieves
exceptional performance on complex reasoning tasks using only 1000
training samples. The model operates without pre-training or CoT data,
yet achieves nearly perfect performance on challenging tasks including
complex Sudoku puzzles and optimal path finding in large mazes."

[[-]](https://arxiv.org/pdf/2506.21734)

---

"Hierarchical Reasoning Model (HRM): a tiny brain that embarrasses
giant LLMs.. Sudoku-Extreme, the puzzles that leave most models
hopeless, HRM solved 55% of them, Claude and o3-mini, Zero. Same for
large 30×30 mazes. HRM found the optimal path 74.5% of the time, while
the others sat at zero!.. The model that’s smaller than GPT-1, the
original GPT with 117M parameters, suddenly outperforming models
thousands of times its size on reasoning-heavy tasks."

---

France is the new Italy

CNBC: "France's new PM resigns sparking fresh political chaos"

---

ADL = ZJL, Zionist-Jew League.. 

---

The Guardian: "FBI cuts ties with two advocacy groups that track US
extremism after rightwing backlash... FBI director Kash Patel said
agency would sever ties with Southern Poverty Law Center and
Anti-Defamation League"

---

Moyers: "[2016] Bill Clinton's legacy in empowering the consolidation
of corporate media is right up there with the North American Free
Trade Agreement (NAFTA).. [T]he Telecommunications Act of
1996.. signed into law on February 8, 1996, was 'essentially bought
and paid for by corporate media lobbies,' as Fairness and Accuracy in
Reporting (FAIR) described it, and radically 'opened the floodgates on
mergers.'"

---

BHJ: "In 1983, the US media was controlled by 50 companies.. by 2020
the number shrank to six... Not only are there six conglomerates alone
that mainly own the media, but these six are so interconnected that
they are practically one."

---

Robert Reich: "[9/24] The richest man on earth owns X.

The second richest man on earth is about to be a major owner of TikTok.

The third richest man owns Facebook, Instagram, and WhatsApp.

The fourth richest man owns The Washington Post. 

See the problem here?"

---

Mortgage demand, their use can cause house price increases, which in
turn raise demand for mortgages more, raising house prices again, and
on and on.. A snowball effect.  But if you rewind it all back, why did
people *start* to need bigger mortgages to begin with? The culprit:
rising inequality. The snowball naturally will make that worse too,
only the top 1% will have the money to lend to struggling home owners,
and middle class' monthly payments will generate a massive passive
income for the rich which they can use to buy even more assets.

---

Why isn't Canadian healthcare financing become problematic when their
conservatives are in power? Well because they haven't done a half
assed job like the US, their system has proper funding from get-go.

---

Trust the corporatist guy (former chairman of Blackrock DE) to do the
right thing

"@signalapp@mastodon.world

We are alarmed by reports that Germany is on the verge of a
catastrophic about-face, reversing its longstanding and principled
opposition to the EU’s Chat Control proposal which, if passed, could
spell the end of the right to privacy in Europe."

---

\#Ukraine 09/27 - 10/05

[[-]](ukrdata/map38.html)

---

"Bush was pivoting to a War on Drugs as a new frontier for defense
contracts".. Them defense contracts

Katz, *Gangsters of Capitalism*: "Noriega rose through the ranks of
the National Guard of Panama, a force created during the Cold War
along the lines of the Somozas’ militia in Nicaragua.  While being
paid by the U.S. government to spy on leftist movements in Panama in
the early 1960s, he enrolled at the U.S. Army’s School of the Americas
training center, then based in the Canal Zone. (Noriega’s fellow
alumni included the future heads of death squads and secret police
across Latin America.) In 1970, Noriega was made Panama’s chief of
military intelligence. A year after, he was formally put on the
payroll of the CIA..

In January 1989, a former director of the CIA, George Herbert Walker
Bush, became president of the United States. Noriega, who had started
working with Bush in 1976, must have thought he had won the
lottery. But with the Cold War coming to an end, Bush was pivoting to
a War on Drugs as a new frontier for defense contracts, surveillance,
and a pretext for military control. Once in office, Bush turned on his
erstwhile employee, calling for Noriega to step down and imposing
crippling sanctions on Panama. On December 15, 1989, the Panamanian
national assembly named Noriega the country’s 'maximum leader of
national liberation' and symbolically declared war on the United
States. The next day, a group of U.S. troops got into an argument with
PDF soldiers at a roadblock in El Chorrillo. A Marine lieutenant named
Robert Paz was shot.  He died soon after at Gorgas Hospital in the
former Canal Zone. On December 20, citing the Colombian-born
U.S. Marine’s death as a justification, the United States invaded
Panama for the second time."

---

The National Interest: "Why Did America Just Send a Dozen Aerial Tankers to Qatar?"

---

Calm down, the word just means "the leader" in Italian.

---

\#USNavy There is still some concentration around Iran, less than last
time I checked, and of course, there is massive focus around
Venezuella. What is Il Duce up to?

[[-]](map15.html)

---
