<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/PowertrainMag?src=hash&amp;ref_src=twsrc%5Etfw">#PowertrainMag</a> 🗞️: China Yuchai, through its main operating subsidiary, Guangxi Yuchai Machinery Company, says that its YCK05 hydrogen-powered engine has achieved stable operation during a recent demo at the Beijing Institute of Technology. Details here: <a href="https://t.co/iJJYU2d4B0">https://t.co/iJJYU2d4B0</a> <a href="https://t.co/HbB9VBpJOr">pic.twitter.com/HbB9VBpJOr</a></p>&mdash; Sustainable Internal Combustion Engine Symposium (@SustainableICES) <a href="https://twitter.com/SustainableICES/status/1481553908480847877?ref_src=twsrc%5Etfw">January 13, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"TECO 2030 has revealed it is set to lead a Norwegian consortium to
develop the world’s first hydrogen-powered high-speed vessel"

---

PV Magazine: "Netherlands to build 10 GW national network for green
hydrogen.. [NL] is planning a €1.5 billion ($1.6 billion) green
hydrogen network that will consist of 85% recycled natural gas
pipes. It is expected to go online in 2027"

---

Energate: "The Bavarian Minister of Economic Affairs.. has now signed
a declaration of intent to this effect with his counterpart.. in
Glasgow. Together they now want to examine possible hydrogen
routes.. "Scotland is a politically stable European partner with a
potential of 25 percent of Europe's offshore wind energy production,"
Aiwanger explained. This means that large quantities of hydrogen can
be produced. Bavaria will have to rely on imports despite the
expansion of renewable energies, he said. The agreement reached also
provides for cooperation in technology development for storage and
transport'

---

Namibia is on the Atlantic, so if they ship or pipeline the product
it would be toward Portugal or Spain instead of going through
Eastern Africa / Suez I'm guessing.

H2 Central: "The European Union is planning to sign a deal with
Namibia to support the country’s ‘green’ hydrogen sector and boost
European imports of the fuel as the bloc works to reduce its
dependence on Russian energy...

In May, the EU’s energy strategy set a goal of importing at least 10
million tonnes of ‘green’ hydrogen by 2030, with another 10 million
tonnes to be produced within the bloc.

EU, Namibia tight-lipped on details of the deal. Under the plan, the
European Union will sign a memorandum of understanding with Namibia on
hydrogen and minerals at the UN Climate Conference due to take place
in Egypt in November"

---

DTT-NET: "The Trans-Adriatic-Pipeline (TAP), which brings
Azerbaijani’s natural gas to EU member countries in Balkan region and
Italy, will be upgraded for hydrogen transport, according to companies
representatives"

[[-]](https://pbs.twimg.com/media/FW2JUprXEAMyKQg?format=png&name=small)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">First Hydrogen powered Russian Limousine <a href="https://twitter.com/AurusRussiaEN?ref_src=twsrc%5Etfw">@AurusRussiaEN</a> The team from NAMI, the Russian National Automotive and Research Unit just unveiled the prototype of an hydrogen powered luxury limousine Aurus Senat! <a href="https://twitter.com/hashtag/meethydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#meethydrogen</a> <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/limo?src=hash&amp;ref_src=twsrc%5Etfw">#limo</a> <a href="https://t.co/g68697OHpC">pic.twitter.com/g68697OHpC</a></p>&mdash; Meet Hydrogen (@meet_hydrogen) <a href="https://twitter.com/meet_hydrogen/status/1402354199585865729?ref_src=twsrc%5Etfw">June 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Just fold'em out they are ready to go

"Australian solar tech company 5B’s rapidly deployable Maverick platform"

[[-]](https://youtu.be/xBRBZ6j8im4?t=20)

---

SCOTUS struck down carbon regulation? There can be a
work-around.. Power stations can be charged a high blanket tax for
energy transmission across state lines, and if they want a rebate on
that tax, station has to prove their carbon emission is low. So gov is
not 'regulating' but simply 'checking' if company would be elligeble
for a rebate. 

---

NYT: "Japan Swelters Through a Punishing Heat Wave.. Temperatures in
Tokyo surpassed [35 C] for the eighth straight day on Saturday, a
streak seen only once before since 1875"

---

Retired too? Had a great run no doubt. Respect

---

I see B Willis went spaz, has some condition that's why he was in so
many bad movies lately.. I was thinking 'BW doesn't choose this
bad'.

---

There was a single super-continent before the last split; fascinating.

"@ErikSolheim

One billion years of tectonic plate movements"

[[-]](https://twitter.com/ErikSolheim/status/1543494751693029376)

---

"@dancow

anyway I was thinking of Jack’s first tweet cratering in value b/c
it’s now July 2022, and brain geniuses are still horny posting on
LinkedIn about how we’ll get rich by selling our airline ticket
stubs. Please if you must do grifts I just want new believable ones"

---

"@dancow

This is the greatest headline of our times (via @guardian)

'Man who paid $2.9m for NFT of Jack Dorsey's first tweet set to lose
almost 2.9 million'"

---

Ljung-Box Q-statistic 

```python
acf,confint,qstat,pvalues = sm.tsa.acf(results.resid, nlags=4, alpha=95,qstat=True, unbiased=True)
print (acf)
print (pvalues)
```

```text
[1.         0.99585547 0.99164499 0.98737151 0.98305291]
[1.02286496e-121 5.63735022e-239 0.00000000e+000 0.00000000e+000]
```

Same here

---

```python
from pandas_datareader.data import DataReader # get data from FRED
cpi = DataReader('CPIAUCNS', 'fred', start='1971-01', end='2016-12')

import statsmodels.formula.api as smf
from statsmodels.stats.stattools import durbin_watson
inf = np.log(cpi)
results = smf.ols('CPIAUCNS ~ 1', data=inf).fit()
print (durbin_watson(results.resid))
```

```text
9.222098132626528e-05
```

Hints at autocorrelation

---

Investopedia: "The Durbin-Watson statistic will always have a value
ranging between 0 and 4.. [v]alues from 0 to less than 2 point to
positive autocorrelation"

---

How to check autocorr statistically? The Durbin-Watson test.. Ljung-Box Q-statistic

---

Sure; high inflation can beget higher inflation so time series would
be correlated with itself, ie autocorrelation. That is partly why CB
raises to quash that self-reinforcing effect.

"Inflation is highly autocorrelated"

---

They are likely paid from taxes, which means existing money, do not
expand the money base. No new inflation.

---

If new money isn't printed for payments, they won't be
inflationary.

---

"@sfchronicle

It’s official: Most Californians will get one-time 'inflation relief' payments"

---

TDB: "‘Active Shooter’ Attacks July 4 Parade in Chicago Suburb"

---

F-ing cops.. They shoot 90 times at the unarmed guy \#Akron, but won't
go in to fight against the actually armed guy killing people
\#Uwalde.. \#defundThePolice

---

Politico: "Acting in concert, the president and Congress may shape
both the size and purview of the court. They can declare individual
legislative measures or entire topics beyond their scope of
review. It’s happened before, notably in 1868, when Congress passed
legislation stripping the Supreme Court of its jurisdiction over cases
related to federal writs of habeas corpus"

---

"Suez Canal Expansion Accelerated as April Traffic Breaks Historic
Records.. Tanker transit statistics via the Suez Canal broke historic
records in April as Europe sought to import more crude oil and LNG
from the Arab Gulf"

[[-]](https://jpt.spe.org/suez-canal-expansion-accelerated-as-april-traffic-breaks-historic-records)

---

The Telegraph: "Suez Canal records highest ever annual revenue of $7
bn"

---

Sadat played for a post-conflict settlement to get Sinai back rather
than through military action itself.. New friends in US would be
necessary for that to work, so he sent the Soviets packing.. Smart
move. See, don't have to win militarily all the time to win something
valueable in military terms. 

History Channel: "Israel’s stunning victory in the Six-Day War of 1967
left the Jewish nation in control of territory four times its previous
size. Egypt lost the 23,500-square-mile Sinai Peninsula and the Gaza
Strip, Jordan lost the West Bank and East Jerusalem, and Syria lost
the strategic Golan Heights. When Anwar el-Sadat (1918-81) became
president of Egypt in 1970, he found himself leader of an economically
troubled nation that could ill afford to continue its endless crusade
against Israel. He wanted to make peace and thereby achieve stability
and recovery of the Sinai, but after Israel’s 1967 victory it was
unlikely that Israel’s peace terms would be favorable to Egypt. So
Sadat conceived of a daring plan to attack Israel again, which, even
if unsuccessful, might convince the Israelis that peace with Egypt was
necessary.

In 1972, Sadat expelled 20,000 Soviet advisers from Egypt and opened
new diplomatic channels with Washington, D.C., which, as Israel’s key
ally, would be an essential mediator in any future peace talks. He
formed a new alliance with Syria, and a concerted attack on Israel was
planned"

---

BTW much of Luxembourg is 'indefensible', Belgium, France, Germany can
reach anywhere in that country with artillery fire. But they don't.
They don't have that kind of animosity over there, can't Israel achive
the same?

---

Israel: The pre-1967 borders talk came up during 2010s, Netanya said
'those borders were indefensible'. Of course the argument was
[bullshit](https://www.972mag.com/netanyahus-lie-regrading-indefensible-1967-borders/).

---

"@williamnhutton

On Thursday the European Research Council terminated 115 grants
offered to UK based researchers as UK breaks international law over
NI"

---

"@MaxAbrahms

America has sponsored more terrorists than Russia from Afghanistan to
Syria.

'SpencerGuard It is past time for the U.S., U.K, and others to
designate Russia a state sponsor of terrorism. It is a fact'"

---

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](2013/02/nations-and-nationalism.html)

[The Fundamentals of Industrial Ideologies](2011/04/fundamentals-of-industrial-ideologies.html)

[Education, Workplace](2017/09/education-workplace.html)

[Patents](2018/09/patents.html)

[Democracy, Parties](2016/11/democracy.html)

[Economy](2018/05/economy.html)

[Globalization](2018/09/globalization.html)

[Rome, The First Wave, Religion](2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2018/12/climate.html)

[Reports](2019/05/reports.html)

[The Middle East](2019/07/middleeast.html)

[TR](../tr)

## Browse

[By Year](years.html)

[Search](search.html)

[Tweet Archive](tweets/index.html)
