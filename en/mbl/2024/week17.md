# Week 17

H2 Central: "Aurora Hydrogen, an Edmonton-based hydrogen technology
company, is producing the world’s first high-efficiency clean hydrogen
through methane pyrolysis and collaborating across the industry to
develop the low-carbon hydrogen market in Canada"

---

H2 Central: "Green hydrogen company Hiringa Energy has launched what
it says is Australasia’s first zero-emission green hydrogen refuelling
network – Hiringa Refuelling New Zealand (HRNZ). The initiative was
officially opened by energy and transport minister Simeon Brown. With
25% of New Zealand’s transport emissions coming from the heavy
transport sector in spite of only making up 4% of the vehicles on the
roads, this marks a groundbreaking step towards decarbonising the
country’s heavy transportation sector, says Hiringa"

---

"@ben@werd.social

'The FTC’s final rule to ban noncompetes will ensure Americans have
the freedom to pursue a new job, start a new business, or bring a new
idea to market.' This is genuinely wonderful"

---

"@GeofCox@climatejustice.social

Who killed Britain? [This](https://www.information.dk/udland/2024/04/hvem-slog-storbritannien-ihjel)
Danish article has the correct answer: Thatcher"

---

The Verge: "Amazon is shutting down its drone delivery service in
California"

---

Productivity growth (workers producing more with less) does not
guarantee income growth. See [the case of US](https://files.mastodon.social/media_attachments/files/112/313/564/334/769/633/original/ebbf8c2067795d43.png).
Factory installs better machines, workers produce more with it, but
will they have barganing power to increase their wages because of
those machines? No. To the contrary during globalisation, in the
absence of unionization, they could lose barganing power.

BOE Gov Mark Carney: "[2015] In the medium term, productivity growth –
doing more with less – is the key determinant of income growth"

---

US will likely end up like other democratic countries who have deep
structural issues - prez gets elected, in a few months, wham! Net
popularity sinks sub -20,-30 (we see such numbers globally), in that
case even incumbency advantage won't help for a second term, every
president is a one-term president. Gets elected falls to -30, and
booted out in four years. 

"If US prez net popularity keeps decreasing for each prez, where does
that lead?"

---

"@jasongorman@mastodon.cloud

So where are all these A.I.-assisted dev shops out-bidding their
competitors with their increased productivity, then? We should be
seeing them by now, surely?"

---

Sounds crazy but can work \#Terraform \#Sequester

[[-]](https://youtu.be/G-WO-z-QuWI?t=217)

---

"@frameworkcomputer@fosstodon.org

Wild test results from Phoronix.  Great work @AMDRyzen and @ubuntu teams!"

<img width='300' src='https://cdn.fosstodon.org/media_attachments/files/112/300/530/876/348/377/small/bd681e938eecb189.jpeg'/> 

---

While Planck was formulating the black-body radiation he reached a
point when he said "I was ready to sacrifice any of my previous
convictions about physics" (well, except thermodynamics anyway). The
man was ready to throw it all out. That is courageous - the hallmark
of a great scientist.

---

Does he need their money? All of a sudden not the gungho 80s style
cold warrior anymore.

Bloomberg: "Milei backed off on China"

---

\#Sudan WTF? Who are these guys called "SLM" in Sudan? They just took
a bite out of RSF territory (around Thabit).

[[-]](https://cdn.fosstodon.org/media_attachments/files/112/325/923/128/930/606/original/627b57111fa281a0.png)

---

"In an astonishing [!] turn of events, Israel has failed to provide
evidence to back up its allegations against Unrwa for the UN’s final
report... because that evidence doesn't exist. I know, my jaw dropped
too! Israel had made the totally plausible claim that 1 in 10 Unrwa
workers are members of Hamas, but it provided no evidence to the
independent investigation led by French foreign minister Catherine
Colonna"

[[-]](https://www.normalisland.co.uk/p/world-stunned-as-israel-fails-to)

---

The war was worth it for the MIC on this alone.

NYT: "Ukraine War Helped Push World Military Spending to 35-Year High,
Study Says"

---

Firstpost: "After Columbia, other top US universities rocked by
pro-Palestine protests.. Prestigious universities like Yale,.. MIT,
and [NYU] have been attempting, but failing, to put an end to these
demonstrations amid mounting calls for divesting from Israel and a
ceasefire in Gaza"

---

The Japan Times: "The oil-rich Malaysian state of Sarawak in Borneo is
aiming to transform itself into a center for clean hydrogen energy"

---

Regression is like multidimensional line fitting (to noisy data)

---

Yep, `bop`, `domcred` are statistically significant, so are the
exchange rate `xch`, and `govdebt`. Gov debt can matter if one is
distributing unfunded money that circulates among the population. The
classic inflation culprit overheated econ (low unemployment) did not
work independently but in correlation with balance of payment.
Argentina's job creation might be tied to foreign currency dependent
sectors.. ARG case is a clear case of econ mismanagement rather than
the result of an econ cycle. 

---

Let's look at the data, run a little regression


```python
import statsmodels.formula.api as smf

cols = ["ARGBCAGDPBP6","ARGCPALTT01GPM","CRDQARBPUBIS","MKTGDPARA646NWDB","RBARBIS","GGNLBAARA188N","MYAGM2ARM189N","SLUEM1524ZSARG"]
df = u.get_fred(1990,cols)
df.columns = ["bop","cpi","domcred","gdp","xch","govdebt","m2","unemploy"]
df['inflation'] = (df.cpi - df.cpi.shift(12)) / df.cpi.shift(12) * 100.0
df['growth'] = (df.gdp - df.gdp.shift(12)) / df.gdp.shift(12) * 100.0
df = df.interpolate()
smf.ols('inflation ~  unemploy:bop + domcred + xch + govdebt', data=df).fit().summary()
```

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              inflation   R-squared:                       0.407
Model:                            OLS   Adj. R-squared:                  0.374
Method:                 Least Squares   F-statistic:                     12.03
Date:                Sun, 21 Apr 2024   Prob (F-statistic):           1.69e-07
Time:                        10:50:21   Log-Likelihood:                -417.30
No. Observations:                  75   AIC:                             844.6
Df Residuals:                      70   BIC:                             856.2
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept      593.4201    103.217      5.749      0.000     387.560     799.280
unemploy:bop    -1.1730      0.290     -4.047      0.000      -1.751      -0.595
domcred          0.0106      0.003      3.914      0.000       0.005       0.016
xch             -4.6241      0.931     -4.967      0.000      -6.481      -2.767
govdebt         21.8747      7.291      3.000      0.004       7.334      36.415
==============================================================================
Omnibus:                       18.622   Durbin-Watson:                   0.972
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               23.387
Skew:                           1.136   Prob(JB):                     8.35e-06
Kurtosis:                       4.523   Cond. No.                     9.63e+04
==============================================================================
```

---

Argentina: Inflation is effected by balance of payments, domestic
credit.. Of course..  You buy more than you can sell, foreign products
rise in price.. If such products have no local subtitute and are
essential, there is inflation. You print money for credit, money value
decreases, inflation..

---

"@fuck_cars_bot@botsin.space

'Use those rights-of-way for a better purpose: trains, housing, and
linear parks'"

[[-]](https://cdn.fosstodon.org/cache/media_attachments/files/112/301/401/247/278/043/original/6be4efd735fa98b0.jpeg)

---

Dam, they have *Top Gun*, *Mission Impossible*, *Transformers*.. Could
be a gold mine for Sony.

---

Would the purchase mean Halo on Sony Playstation? Probably.

---

Paramount has IP for *Terminator*, and *Halo*? Yeah plz fix those too.

---

I have only one request, please fix Trek.

NYT: "Sony in Talks to Join a Bid to Buy Paramount"

---

Frontline \#UA \#RU 04/13 - 04/23

[[-]](ukrdata/map14.html)

---

Creative Good: "Vision Pro, unscrambled, is 'I Poison VR'.. Apple’s
new face jail goes on sale today.. In Apple’s promotional video, I
wrote, we can see people sit on a couch, talk to coworkers, play with
their kids – all while blinded by the tentacled grip across their
eyes. There’s nothing liberating, exciting, or hopeful in any of
it. And if it looks futuristic at all, it’s because we’ve lost our
sense of what the future should be. As Alan Jacobs writes, the machine
'doesn’t look like something to use, it looks like something to be
sentenced to – by an especially cruel judge'"

---

A company colonizing the world.. there it is.. plutocratic fascism..
The concept is stil alive today, we are living in it.

Wiki: "The East India Company was a.. British, joint-stock company
founded in 1600.. It was formed to trade in the Indian Ocean region,
initially with the East Indies (the Indian subcontinent and Southeast
Asia), and later with East Asia. The company gained control of large
parts of the Indian subcontinent and colonised parts of Southeast Asia
and Hong Kong. At its peak, the company was the largest corporation in
the world by various measures and had its own armed forces"

---

Some accounts claim they actually succeeded in doing that,
cutting off thumbs that is

The Guardian: "For at least two centuries the handloom weavers of
Bengal produced some of the world's most desirable fabrics, especially
the fine muslins, light as 'woven air', that were in such demand for
dressmaking and so cheap that Britain's own cloth manufacturers
conspired to cut off the fingers of Bengali weavers and break their
looms"

---

UK corporate media is a cesspool of plutocracy, circle jerk among the
members of corporate power. All they care about is protecting their
interests.. 90% people are for Gaza, 90% of corporate press support
Israel's attack on Gaza. They smear, attack, bury the mildest troublemakers
drag them through the mud. Remember [Red Ed](https://cdn.fosstodon.org/media_attachments/files/112/314/561/102/385/064/original/6c7d72ba8a0fc9df.jpeg)?

---

Two cheeks of the same ass.. That's great. It describes corporate Dems
and Reps to a T, ditto for "Third Way" Labor of
[Blair](../2022/tonyblairkeiser.png) and Tories.

Galloway: "In Western democracies, we have two cheeks of the same butt
side, two sides of the same coin. Sure you can go for this party or
that party, but both parties stand for the same thing and have the
same program essentially of neoliberal economics"

---

They attacked Iran, when it responded, most corporate media and the
bought out politicians ignored why the counterattack
happened. Decontextualization at work again. Just like Pal/Isr history
started on October 7, Irn/Isr history started when they sent drones
towards Israel. The sights in the UK parliament were especially sad,
both parties acted like Iran just woke up one day and decided to lob
bunch of missiles.. George Galloway helpfully reminded everyone what
the hell was going on, so at least now that statement is on
record. What a shit show.

---

Israel's attack on Iran was likely to shift focus from recent events
that made them look bad, eg the killing of World Central Kitchen
workers, among others... They knew the attack would not cause WWIII,
that Iran would respond in a balanced way. The overall attempt was a
success, nobody talks about the WCK event, and other distractions
anymore. Forgotten.

---

The previous "dated metaphor for racism" comment on the X-Men is from
an Marvel action / comic relief character Deadpool who is allowed to
go meta and even break the fourth wall once in a while.

---

"We Need To Rewild The Internet.. The internet has become an
extractive and fragile monoculture. But we can revitalize it using
lessons learned by ecologists.. Rewilding 'aims to restore healthy
ecosystems by creating wild, biodiverse spaces,' according to the
International Union for Conservation of Nature... [it] has much to
offer people who care about the internet"

[[-]](https://www.noemamag.com/we-need-to-rewild-the-internet/)

---

MIT Technology Review: "Hydrogen trains could revolutionize how
Americans get around.. Like a mirage speeding across the dusty desert
outside Pueblo, Colorado, the first hydrogen-fuel-cell passenger train
in the United States is getting warmed up on its test track. Made by
the Swiss manufacturer Stadler and known as the FLIRT (for “Fast Light
Intercity and Regional Train”), it will soon be shipped to Southern
California, where it is slated to carry riders on San Bernardino
County’s Arrow commuter rail service before the end of the year...

<img width='340' src='https://wp.technologyreview.com/wp-content/uploads/2024/04/The-Great-Hydrogen-Train-Debate.png?fit=1616,908'/> 

So far, hydrogen has been the big technological winner in
California. Over the past year, the California Department of
Transportation, known as Caltrans, has ordered 10 hydrogen FLIRT
trains at a cost of $207 million. After the Arrow service, the next
rail line to receive hydrogen trains is scheduled to be the Valley
Rail service in the Central Valley. That line will connect Sacramento
to California High-Speed Rail, the under-construction system that will
eventually link Los Angeles and San Francisco. In its analysis of
different zero-­emissions rail technologies, Caltrans found that
hydrogen trains, powered by onboard fuel cells that convert hydrogen
into electricity, had better range and shorter refueling times than
battery-electric trains"

---

"@jasongorman@mastodon.cloud

Replacing your junior developers with LLMs is a bit like replacing
your tomato plants with pasta sauce"

---

Zitron: "Researching the beginning of this article took me about 30
minutes, because every time I googled something — like what percentage
of web traffic goes to Google — I kept being given 'authoritative'
sources like 'Forbes Advisor' (the affiliate marketing arm of Forbes
with nothing to do with the magazine) with sources ranging from
'Blogging Wizard' to a literal list of website names, with no actual
links...  This is the state of the modern internet — ultra-profitable
platforms outright abdicating any responsibility toward the customer,
offering not a 'service' or a 'portal,' but cramming as many ways to
interrupt the user and push them into doing things that make the
company money..  These platforms are now pathways for the nebulous
concept of 'content discovery,' a barely-personalized entertainment
network that occasionally drizzles people or things you choose to see
on top of sponsored content and groups that a.. database has decided
are 'good for you.'"

[[-]](https://www.wheresyoured.at/the-great-looting-of-the-internet/)

---

Oxford shuts down the institute run by Nick Bostrom. Guy's is a
gasbag, good call. 

---

CNBC: "Defense giant BAE Systems linked to arms deals in countries
accused of human rights abuses, report finds"

---

The Turing test might have been passed by "AI" but I don't think
Turing foresaw the bullshit generator machines of late... modern
computers did not exist in his time, much of the concepts around
intelligence were simply beyond that era's science.

---

Marisa Kabas: "I spoke with a Google worker fired for protesting a
$1.2 billion contract with Israel. 'It was a complete overreaction on
their part to not only fire everyone who was and wasn't involved, but
then also threaten everyone else in the company who would dare think
to stand up against this...it feels like a very fascist environment"

[[-]](https://www.thehandbasket.co/p/google-worker-fired-protest-israel-project-nimbus)

---

"@fuck_cars_bot@botsin.space

Just imagine what could have been in the US"

[[-]](https://files.botsin.space/media_attachments/files/112/296/917/987/576/715/original/0ceafa759523ca56.jpeg)

---

.. which isn't much of a democracy. Plutocratic muckers are
running your lives. After the New Deal people ended up with Raw Deal,
and they sold that via an actor in a cowboy hat promising the return
of good ol' days when things were "rougher". Well congrats, it got
rougher, even when there is plenty of wealth to go around. 

"wb x64@wilbr@glitch.social

'Democracy with American characteristics'"

---

The X-Men, "a dated metaphor for racism in the '60s" is becoming part
of MCU.. That is grand. They can beat that dead horse too now, bring
back that Red Skull guy (with a red cap this time), and have him fight
X-Men, while watching in our minds we can always create parallels
between that and different varities of Woke and its phobes, root for
the X-Men, fear government, cherish "freedom".

---

Disney will serve a MAGA Hulk basically (who in human form will also
be president), and I am guessing he will be fighting "diversity"?
Because, well, along with abortion, gender issues, there are no other
important issues in the country, like millions without health
insurance, poverty, shit jobs and concentration of wealth. No. We will
have a MAGA Hulk fighting non-MAGA heroes (and wink wink fighting the
government at the same time, remember that when they want to tax our
ass). Bidness interests gaslight. Look, squirrel!

---

Red Hulk eh? I smell corporate messaging again.. Will he have
cufflinks, one says "MA" the other "GA"?

---

"*Captain America 4 Brave New World* will feature Red Hulk as the
villain."

---

\#Fallout had a good villain. I see big names, MacLachlan (80s
*Dune*), M. Emerson (*PoI*).

---

Yahoo Finance: "Seattle gave low-income residents $500 a month no
strings attached. Employment rates nearly doubled"

---

Railway Technology: "EU’s FCH2Rail hydrogen train project finishes
testing in Portugal"

<img width='340' src='https://files.mastodon.social/cache/preview_cards/images/094/531/168/original/af34b0c7e075e764.jpg'/> 

---

Palestine Chronicle: "China Leads the Way – Beijing Supports Full UN
Membership for Palestine"

---

Quick! Attack Iran again to shift focus!

---

The New Arab: "Munther Isaac [interviewed by Tucker Carlson..]  is a
Lutheran pastor in Bethlehem, slammed right-wing Evangelical
Christians in the US who have supported Israeli actions in Gaza and
the occupied West Bank which bring huge harm to the Palestinian
Christian community.

He noted how despite the strongly held views by the religious right on
the subject 'their knowledge on the situation here seems to be very
very shallow'..

Isaac further described how Israel's military occupation was causing
many Palestinian Christians to flee the occupied territories and its
assault on Gaza is endangering the Christian community in the enclave"

---

UnHerd: "The capitalists are circling over Ukraine.. Western
multinationals had long had their eyes on Ukraine’s vast agricultural
wealth, but a 2001 moratorium on the sale of land to foreigners had
always represented an obstacle to unrestrained privatisation. As
post-Maidan governments turned again to the IMF for financing, aid was
conditioned on a series of land reforms that would finally allow
foreign corporations to acquire vast tracts of the country’s
farmland. In the 2015 TV series, Servant of the People — which starred
Zelenskyy as the fictional president, Goloborodko — the conditions
required by the IMF for a new loan are rejected and the Western
delegation is expelled. But in reality, things went rather
differently. In 2020, Zelenskyy gave in to the IMF’s demands and
finally repealed the moratorium"

---

Bidnessman.. they make the best terrorists..

Wiki: "The 2003 ricin letters were two ricin-laden letters found on
two occasions between October and November 2003... The letters were
sent by an individual who referred to themselves as 'Fallen
Angel'. The sender, who claimed to own a trucking company, expressed
anger over changes in federal trucking regulations... [which] took
effect which directly affected the over-the-road trucking industry in
the United States. The rules.. aimed at reducing fatigue related
accidents and fatalities. Called the most far-reaching rule changes in
65 years, the regulations reduced daily allowed driving time from 11
hours to 10"

---

"@masek@infosec.exchange

If you do 12 Bitcoin transactions per year, you use a higher amount of
energy than we use for a complete family.. in the same year"

---

"@jk@mastodon.social

The security features of windows basically consist of checking through
the 100 million files on your computer and 35 hours later it announces
that it's found, and helpfully deleted, a keygen for age of empires
II"

---

Andersen: "Rupert Murdoch had started buying U.S. newspapers and
magazines in the 1970s, including the New York Post, which he turned
overnight.. to right-wing. Jack Kemp said in 1981 that 'Rupert Murdoch
used the editorial page, the front page and every other page
necessary' in the Post 'to elect Ronald Reagan President.'  In 1985
Murdoch moved into television, spending the equivalent of $5 billion
to buy TV stations in seven of the ten biggest cities. Reagan helped:
he fast-tracked Murdoch for U.S. citizenship so that his company could
get around the federal law forbidding foreigners from owning stations,
then waived the federal rule forbidding anyone from owning a TV
station and a newspaper in the same city, as Murdoch suddenly did in
New York and Boston"

---

Eric Holder works for these guys too.. Tony Blink 737, Raytheon
Austin.. Dems like their revolving doors.. Reps too of course

NYT: "[2016] Longtime U.S. Prosecutor to Join Covington &
Burling.. Arlo Devlin-Brown, a veteran federal prosecutor in Manhattan
who led a string of prominent Wall Street cases.. is departing for the
private sector. In August, he will join the law firm Covington &
Burling"

---

easyJet: "Leads First Hydrogen Refueling Trials At Bristol Airport"

---

Clean Technica: "Solar Foods.. has developed a system for producing
large quantities of a natural microorganism, fed by carbon dioxide
along with green hydrogen and oxygen"

---

Zucman: "As Roosevelt’s [1942] message to Congress expresses clearly,
the quasi-confiscatory top marginal income tax rates championed by the
United States were designed to reduce inequality, not to collect
revenue. Why would anyone try to earn more than a million dollars if
all of that extra income went to the IRS? No employment contract with
a salary above a million would ever be signed. Nobody would amass
enough wealth to receive more than a million in annual capital
income. The rich would stop saving after they reached that point. They
most likely would give their assets to heirs or charities once they
surpassed the threshold. As such, the goal of Roosevelt’s policy was
obvious: reduce the inequality of pre-tax income. The United States,
for almost half a century, came as close as any democratic country
ever has to imposing a legal maximum income"

---
