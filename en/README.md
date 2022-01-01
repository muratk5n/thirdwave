<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">📢 <a href="https://twitter.com/heliogeninc?ref_src=twsrc%5Etfw">@heliogeninc</a> to start trading on NYSE on Dec 31<a href="https://t.co/AzAf6mLSFu">https://t.co/AzAf6mLSFu</a><a href="https://twitter.com/hashtag/CSP?src=hash&amp;ref_src=twsrc%5Etfw">#CSP</a> <a href="https://twitter.com/hashtag/solar?src=hash&amp;ref_src=twsrc%5Etfw">#solar</a> <a href="https://twitter.com/hashtag/thermal?src=hash&amp;ref_src=twsrc%5Etfw">#thermal</a> <a href="https://twitter.com/hashtag/concentrated?src=hash&amp;ref_src=twsrc%5Etfw">#concentrated</a></p>&mdash; SolarPACES (@IEA_SolarPACES) <a href="https://twitter.com/IEA_SolarPACES/status/1476811240110448645?ref_src=twsrc%5Etfw">December 31, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Renewables Now: "Spain to hold 500-MW renewables auction for CSP"

---

"Renewable hydrogen is now being produced at a facility in Lloseta,
Mallorca, that could produce at least 300 tonnes of the clean energy
carrier annually"

---

Al-Monitor: "Egypt announces deal for large petrochemical production
complex.. The new integrated complex for the production of methanol,
ammonia and its derivatives in the industrial zone of Ain Sukhna,
Egypt, aims to export its products with a production of one million
tons of methanol and 400 thousand tons of ammonia annually"

---

Floating panels can help FR in their territories. Around Madagascar
there is massive sunshine, floating panels can do the work. From there
ship H2 or ammonia via ships to Europe.

---

Floating solar panels, by French engineer Ludivine Pasquier

<iframe width="340" src="https://www.youtube.com/embed/Yr-WuZxFKxY?start=186" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Ah let's remember [Oct 2021 oil spill](https://www.usatoday.com/story/news/nation/2021/10/05/what-caused-california-oil-spill/6001096001/)
near California.

A ship's anchor broke the pipeline, if H2 was being sent, worst case,
H2 mixing into H2O would be no big deal.

The CA crude oil leak lasted for 3 hours before it was detected. More
than 140,000 gallons of oil leaked into Southern California waters.

---

Reshare

"Sixteen wells off Louisiana have been leaking since September
2004, when a subsea mudslide caused by Hurricane Ivan knocked over a
Taylor production platform"

---

According to data in the link, oil pipelines have 4.9 E-4 per year-km
failure rate, natural gas 7.2 E-5. If Canada has 70,000 kilometers of
pipelines,

```python
print (int(70000 * 4.9*1e-5), 'accidents per year')
```

```text
3 accidents per year
```

Above is the expected \# of accidents (oil).

The best protection is not to have oil pipelines.

[[-]](https://www.icheme.org/media/9672/xxi-paper-044.pdf)

---

Pipelines, coal, natgas.. This is where rubber meets the road;
switching from old to new was never going to be easy.

---

Canada has over 70,000 km of large transmission oil pipelines. Any of
those cld go haywire and the environment disaster would be severe.

Any energy that moves needs to be clean molecules, prefarably H2 gas.
Much cleaner than fossil, more efficient than the electric grid. H2
pipeline can transmit 10 times the energy at 8th the cost.

---

WSJ: "South Africa Says Its Omicron Wave Is in Retreat"

---

Makes sense.. Omicron will overwhelm the system otherwise; less deadly
but spreads faster, T&T is a bad match for that.

"The [AU] New South Wales government’s Covid contact-tracing system
has been all but abandoned, with efforts now focused only on those in
the highest risk categories"

---

US Omicron deaths still less than Delta, no uptrend

[[-]](2020/02/corona.md#usdailydeath)

---

See the SP500 graph; That kind of rise is exponential (right time to
use the word). Rises like that are seen with amoeba, bacteria
population growth when there are no limits in resources; so they eat
everything in their petri dish and multiply.

---

```python
plt.figure()
ax1 = df.FEDFUNDS.plot(color='blue', grid=True, label='fed')
ax2 = df.sp500.plot(color='red', grid=True, label='sp',secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
```

<img width="340" src="https://pbs.twimg.com/media/FH3t_kBWYAQ0ssu?format=png&name=small"/>

---

```python
from io import BytesIO
import urllib.request as urllib2, time as timelib
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1990, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['GDPC1','FEDFUNDS']
df = data.DataReader(cols, 'fred', start, end)

start1 = int(timelib.mktime(start.timetuple()))
end1 = int(timelib.mktime(end.timetuple()))

url = "https://query1.finance.yahoo.com/v7/finance/download/^IXIC?period1=" + str(start1) + "&period2=" + str(end1) + "&interval=1d&events=history&includeAdjustedClose=true"
r = urllib2.urlopen(url).read()
file = BytesIO(r)
df2 = pd.read_csv(file,index_col='Date',parse_dates=True)
df['sp500'] = df2['Close']
df = df.interpolate()
print (df.corr())
```

```text
             GDPC1  FEDFUNDS     sp500
GDPC1     1.000000 -0.728588  0.786939
FEDFUNDS -0.728588  1.000000 -0.470347
sp500     0.786939 -0.470347  1.000000
```

Negative correlation, -0.47, between the stock market and the FED rate.

The asset purchases are do not show up in the base numbers below, but
they can be considered as a form of negative interest rate policy. If
their effect was included somehow, the negative correlation below
would be even more pronounced.

Ergo once the asset purchases stop, that act will be akin to a rate
rise.

---

The stock market is a socialist stock market right now. Government
(the FED) is propping it up with its asset purchases and low
rates. When that stops and rate rises begin let's see that nice "free
market" holds up..

We saw a hint of that in 2018, with a mere 2.40% FEDFUNDS the
"correction" that followed scared the shit out of FOMO
dingbats. "Thanks" to the pandemic FEDFUNDS went near zero now and
voila, the boom of all booms took place. 

---

Not that it hasn't happened [before](2020/03/appelbaum.md#transistor).

---

We should congratulate businesses for being "opportunistic" for
"taking advantage of gov"? Hah :)

Well then maybe gov will opportunistically tax their ass and take
"their IP" 🤨 That would be opportunism too, right?

Yea... now he bitchin..

---

Make money, and aim to make money, fine. My addn is, if DARPA allowed
a company have the base tech, and gov gave them subsidies, they cant
[charge](https://www.theguardian.com/uk-news/2021/dec/05/wall-of-secrecy-in-pfizer-contracts-as-company-accused-of-profiteering)
thirty dolars for one dollar vaccine and still keep their
IP. This is socialism for the corporations, capitalism for the rest.

---

Sony will haul most of those Benjamins home.. not Disney/Marvel.

---

Spiderman told a good story; no doubt. Good movie. It wasn't cuck,
a major factor in its success.

---

Even *Wall E* showed some kind of satisfactory ending; couch potatos
got out of their e-couches, arrived at a planet, something new
began. 

#thematrix

---

One way to look at the Matrix movies is as small, muted, centrist
shitlib protests..  The system is not changed bcz these people are
fine with it as it is, they merely want to be "recognized" in it, to
be its The One (which everyone can beee if you belieeeeve), so they
can fly over it, be "loud and proud" while they enjoy a simplistic
diversity around them, and "represent". Strangely similar ending to
*Jupiter Ascending* (same director), the cleaner girl discovers she is
space royalty, then "saves Earth" with her "diverse" new boyfriend /
soldier, but returns, stays as a cleaner, while once in a while flies
over the city to enjoy her specialness and uniqueness. People are not
being harvested but have no idea what happened, things stay the same

#thematrix

---

The meta stuff was probably due to the original's imagery being an
overbearing presence.. Director must have felt the only way to get out
from under that is to reference it as another version, go a little
meta

#thematrix

---

*The Matrix Resurrections*; good to see the lead actors again, movie
had some good ideas.. but if there are no "reboot sequels", the
situation is no different than at the end of the first movie. Then
it's like what's the point? After the first, most expected the
destruction of the "system". The absence of that ending sapped the
energy of the sequels, wout courage they ended up as neutered, cheap
war movies with a few memorable action scenes

#thematrix

---

Backed the death penalty.. voted for the invasion of Iraq... \#reid

---

I'd just watched the guy on a UFO docu too. he apparently worked on
that.. which is pretty useless for the most pressing needs of
today. These Dem centrists.. I bet they are into UFOs bcz they know
they are of no help and want to get their rocks off on something that
'sounds' substantial.

---

What deal did he showcase those skills on? Obamacare? That's not much of a
skill

"Harry Reid remembered as a fighter, skilled Senate dealmaker"

---

FR seems in love with its nukes and the concept of nuclear.. A
national pride thing I guess in the race to be in the same league
as the big powers.

---

Vid on FR nuke tests, Greenpeace and NZ.

FR operatives *bombed* a Greenpeace ship. 

[[-]](https://youtu.be/kXP8F4TIZ0U?t=543)

---

New schedule, biweekly public TW releases, save emergencies.. let's
see if it works out.

---

Prices can be different for different regions; the supplier is
different (Russia, vs US' local production), transport, demand is
different. Maybe RU also played a blackmail game, to have
Nordstream 2 activated..

---

For European natgas prices, the future contract Dutch TTF can be used.

EU natgas price has been at insane levels.. fell somewhat recently.

[[-]](2019/05/stats.md#eunatgas)

---

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](/2013/02/nations-and-nationalism.md)

[The Fundamentals of Industrial Ideologies](/2011/04/fundamentals-of-industrial-ideologies.md)

[Education, Workplace](2017/09/education-workplace.md)

[Patents](/2018/09/patents.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave, Religion](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[Reports](/2019/05/reports.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


