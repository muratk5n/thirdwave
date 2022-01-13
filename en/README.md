<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

H2 View: "UAE, UK to explore clean hydrogen opportunities through new
partnership"

---

H2 View: "Aberdeen Investee, AES-100 Inc., Reports Technical Viability
of Hydrogen Extraction From Natural Gas Pipelines"

---

H2 View: "myFC to develop hydrogen fuel cell systems for bicycle"

---

H2 View: "Carbon emissions reduction technologies company Haldor
Topsoe.. inked a €45m loan agreement to research hydrogen
technologies. An agreement signed with the European Investment Bank,
the loan will allow the company to focus on the production of green
chemicals and renewable fuels, such as green hydrogen, green ammonia
and biofuels"

---

H2 View: "Germany to significantly boost renewable energy technologies
with hydrogen set to be central to decarbonisation"

---

"Saudi-based Acwa Power.. has announced plans to begin the first phase
of Noor Energy 1 [CSP] project, located in Dubai with a total capacity
of 217 MW...

The 950 MW Phase Four is the largest investment project in the world
[in its class]"

---

"1.3GW CSP Projects Planned to Start in 2022 [in China]"

[[-]](http://www.cspfocus.cn/en/market/detail_5026.htm)

---

Chemical, as in the kind used by those disposable hand warmers. DHWs
contain iron powder, salt powder, enclosed in a plastic wrap. When the
contents are removed all comes into contact with air / oxygen, iron
oxide is formed which is an heat-emitting "exothermic" reaction. User
gets heat in the process, the perfect hand warmer. No electricity, no
flame, just basic chemistry.

---

If more ppl came up with chemically activated H2 or ammonia based
heater solutions, it would be helpful, potentially game-changer
even. Something like [this](https://www.design-industry.com.au/lavo-hydrogen-bbq)
tech from Lavo.

---

CO2 from fossil stays in the atmo for very long time.. When an uptick
in the graph falls, doesnt mean CO2 produced at the high disappears.

---

Let's zoom in,

```python
df['twh'].tail(40).plot()
```

<img width="340" src="https://pbs.twimg.com/media/FIzqj7lX0AIAS4t?format=png&name=small"/>

Right there.. Peak on July, peak on January, peak on July, peak on
January..  On and on it goes..

Winter spikes are worse. This is US, in the other parts of the world,
fossil burning wld be more extreme. Wood, coal, cow dung..

---

US fossil fuel consumption, in terrawatt hours, 

```python
import pandas as pd, requests
from datetime import date

api_key = open('.eiakey').read()
url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=TOTAL.FFTCBUS.M' 
r = requests.get(url)
json_data = r.json()
df = pd.DataFrame(json_data.get('series')[0].get('data'))
df['Year'] = df[0].astype(str).str[:4]
df['Month'] = df[0].astype(str).str[4:]
df['Day'] = 1
df['Date'] = pd.to_datetime(df[['Year','Month','Day']])
df = df.set_index('Date')
df = df.sort_index()
df['twh'] = df[1] * 0.29307 # 1 trillion btu to twh
df['twh'].plot()
```

<img width="340" src="https://pbs.twimg.com/media/FIzqh85WYAcYPO5?format=png&name=small"/>

---

1KW of heat is required for every 14 cubic meters. 50 m2 for 4 people,
buildings of 4 meters high,

```python
per_person = 10000 # watts
watt_heat_per_m3 = 1/14*1000.
home_vol = 50*4 
heat_w = home_vol*watt_heat_per_m3 / 4
print ('%0.1f watts per person for heating' % heat_w)
print ('%0.1f perc for heating' % (heat_w / per_person * 100.0))
```

```text
3571.4 watts per person for heating
35.7 percent for heating
```

---

EIA: "On average, more than half (51% in 2015) of a [US] household’s
annual energy consumption is for just two energy end uses: space
heating and air conditioning"

[[-]](https://www.eia.gov/energyexplained/use-of-energy/homes.php)

---

"A deep chasm in the ground that’s been burning since the 1970s is due
to finally be extinguished. Known as the ‘Gates of Hell’, the fiery
sinkhole stretches 230-feet wide and is located in the Karakum Desert
in Turkmenistan.. Noone really knows how it was created, but one of
the popular theories is it was created in ’71 when Soviet scientists
ignited it"

[[-]](https://metro.co.uk/2022/01/10/close-the-gates-of-hell-flaming-chasm-to-be-sealed-up-after-51-years-15894082/?ito=socialmetrouktwitter)

---

Nature: "[To scientists] Build a registry of results that students can
replicate.. To speed research, express conclusions as testable
statements, and incorporate testing into training"

[[-]](https://www.nature.com/articles/d41586-021-03707-9)

---

Marm is veg based too but ok, interesting

"Brussel sprouts are the Marmite of the vegetable world, with a
serious love or loathe divide"

---

Sarkozy started that whole wave didn't he? He used to say he wld clean
out 'trouble' neighborhoods "a la Kärcher". Added bonus, Kärcher (with
umlaut!) is a German name / brand which made the whole comment sound
even badder. Boo. Scary German word from Germany. The company must
have had it by now, can't blame them.

"One of the world's leading makers of pressure washers and steam
cleaners [Karcher] has formally asked French politicians not to use
its name to score political points"

---

Jane's Defence: "The United Kingdom has received its ninth and final
Boeing P-8A Poseidon MRA1 maritime multimission aircraft
(MMA)... Delivery of all nine Poseidon MRA1s is a major milestone in
the reconstitution of the UK's airborne maritime patrol capability"

---

Jane's Defence: "Australia will buy more than 100 tanks and armoured
vehicles from the US for $3.5 billion, [says] defence minister."

---

"Jeremy Corbyn considers launching new party to rival Keir Starmer if
he is not reinstated as a Labour MP"

---

Politico: "[A mother from US] I tweeted, 'Does anyone else feel
enraged at the idea that you’ll be homeschooling in the fall
full-time? Cuz my moms group text is in full-blown acceptance mode and
it bugs the shit out of me.' I didn’t know it yet, but this would be
my first foray into school reopening advocacy..

Members of the parent group I helped lead were consistently attacked
on Twitter and Facebook by two Oakland moms with ties to the teachers
union. They labelled advocates’ calls for schools reopening 'white
supremacy' called us 'Karens,' and even bizarrely claimed we had
allied ourselves with Marjorie Taylor Greene’s transphobic agenda"

---

"More than half of Europeans will be infected by Omicron in next two
months, WHO says"

---

Similar to involuntary manslaughter, on a wide scale.. People get
punished for involuntary manslaughter. Driver hits pedestrian while
drunk can get serious punishment.

---

Curious how much trouble an official acceptance of a covid lab-leak
conclusion can cause. US could be liable for some stuff.. It's like
you killed over 5 million people, akin to dropping a tactical nuke on
a city. Is it enough to throw Fauci under the bus as a modern day
Mengele, and be done with it?

---

"The New Fauci Emails Are Even More Damning Than You Think" \#rising \#grim

[[-]](https://youtu.be/sD0i_YxPATc?t=107)

---

China still continues with zero-covid.. Bcz their vax is probably not
too effective against the new strain? But zero-covid is not a
long-term strategy. Trying to gain time while improving the vax?
Enough questions?

---

"Quebec seeks to tax unvaccinated as health system struggles with Omicron"

---

"@Zachary

The IMF says crypto prices are moving more in lockstep with stocks,
raising the risk of contagion across financial markets"

---

Why is Bitcoin price falling when there is inflation? Aren't they
supposed to be a "safe heaven asset", a hedge against "money being
debased"?  Looks like BTC is merely another risky asset just like
those overvalued tech stocks, or, hell, the stock market itself. And
as risky assets go down so does Bitcoin right along with them.

---

*Run and Gun*, not bad.. not bad at all. Rich Kind was hilarious as ever. 

---

*Call of Duty* mission *Behind Enemy Lines* has a scenic
backdrop.. Saw someone else's play, not a big dumb non-stop action,
lots of moving around silently, gives gamer more time to explore the
environment. Decade old game but still good.

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


