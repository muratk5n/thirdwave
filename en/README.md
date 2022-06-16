<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

Pinned Tweet

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Bosch North America announced it will be investing $1.3 billion in hydrogen fuel cell and electrolyzer technology by 2025. <a href="https://t.co/r2Sl5ePqSp">https://t.co/r2Sl5ePqSp</a> <a href="https://t.co/farrACJmR7">pic.twitter.com/farrACJmR7</a></p>&mdash; Jason Curtis (@ski_jason) <a href="https://twitter.com/ski_jason/status/1536758744297644036?ref_src=twsrc%5Etfw">June 14, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

I dont think that supply can match even a single pipeline from RU,
plus the pipeline envisioned (in my natgas map) is a proposal, it
doesn't yet exist, at least 7 yrs away according to reports.

Al Jazeera: "Is the EU deal with Israel and Egypt a way out from
Russian gas?.. Critics argue that the EU will face problems dealing
with Israel and Egypt despite Brussels's enthusiasm"

---

Apparently the voice-over is James-Earl Jones' earlier work resampled,
regenerated.. It was as though JEJ was speaking. Uncanny.

---

*Obi-Wan Kenobi* Episode 5 was good; Vader, OWK were in top form.
Little Leia's character definitely reminds one of the adult Leia. The
story complements the trilogy in a way, now we know how Leia knew
about OWK, she asked for his help bcz he knew him from before. Great
to see McGregor, Christensen again.

---

If yes then the product can do well in rural areas, farms.

---

What are the features of this robot? Can it perform all the tasks a
goat can? 😶

FT: "Japanese goat robot helps ageing society. Engineers at Japan's
Kawasaki Heavy Industries show off their latest invention: a
four-legged rideable robot modelled after an Ibex"

---

Interesting, [this guy](https://youtu.be/MElMJsIP1Y0?t=404) puts in
melted liquid tallow on top of dried beef, the whole thing hardens
together. It's true, melted fat binds together extremely well once
cooled.

---

Draxe: "Tallow is rich in CLA, a fatty acid that studies suggest can
support a healthy metabolism and may lead to fat burning. There's some
evidence demonstrating that CLA also has anti-inflammatory and
immune-supporting properties, possibly even fighting growth of tumors,
as does the fatty acid oleic acid"

---

How to make beef tallow? Axe the butcher, 'need beef fat', they'll
have it on the side. Tallow has CLA, can't do without. No wonder
American Indians mixed fat into pemmican.

---

Is this permanent resettlement status numbers? How about all peoples
who left their country and entered this other one? This API
sucks. Also a simple CSV file per year, from-country, to-country
counts would be fine for a general outlook. Details, demographics etc
can be in a seperate file.

---

[Link](https://drive.google.com/uc?export=view&id=1KdW52Guba1DGZyioXMrc9BU8OMBfFcmh)

---

Says a total 270K people went from Syria into TR? There were more
people than that!

---

🤨 🤨 🤨 


```python
import pandas as pd, datetime, io
import urllib.request as urllib2

url = "http://api.unhcr.org/rsq/v1/export/csv?type=submissions&year="+\
      "2012,2013,2014,2015,2016,2017,2018,2019,2020"+\
      "&origin=SYR&resettlement=TRY"

r = urllib2.urlopen(url).read()
df = pd.read_csv(url,sep=',',skiprows=11)[['Year','Total submissions (persons)']]
df.columns = ['Year','Refugees']
df = df.set_index('Year').dropna()
print (df,'\n\n','Total',np.float(df.sum()))
```

```text
      Refugees
Year          
2012      90.0
2013    5277.0
2014   21154.0
2015   53305.0
2016   77254.0
2017   37332.0
2018   28189.0
2019   29660.0
2020   18220.0 

 Total 270481.0
```

---

UN has a data API `api.unhcr.org`, allows data access to refugee
numbers. Checking

---

FT: "Christopher Geidt resigned as ethics adviser to Boris Johnson
after a potential breach of World Trade Organization rules proved the
final straw following the partygate controversy"

---

CNBC: "Dow falls 700 points, tumbling below 30,000 to the lowest level in more than a year"

---

Oooww burn 🔥 

Al Monitor: "Saudi embassy in Washington now on 'Jamal Khashoggi Way'"

---

Am I for lifting sanctions on Cuba? Sure why not - but the party doing
it would get killed in Florida. They're crazy about that stuff over
there. Emotional subject; very hard to work around. 

---

It was Eisenhower's plan with lots of odd restrictions added on
top. JFK had mil experience but for some reason had bizarre ideas
about mil operations and did not utilize his own military efficiently.

---

Bay of Pigs failure resp lies with Kennedy, [bungled](2021/08/nuclear-folly-plokhy.html#bayofpigs)
the whole thing. The plan followed by the military was the one approved by WH.

"Bay of Pigs was US military's fault"

---

What would the military-industrial complex have to gain from JFK's
death? He was good to them. Increased their budget many times over the
years (whenever he was bitchslapped by the Soviets he'd go to Congress
and ask for more money, give it to mil).

---

If there was a conspiracy for the assasination of JFK it was a
conspiracy originating from Cuba; Castro might have wanted payback for
USA trying to assasinate him.

---

Captured near the gobble gobble controlled area apparently. That
should be no surprise; US itself helped most of those force to topple
Assad with TR help, those f-kers would roam around for sure in the
same area.

The op was conducted along with fighters from NE Syria, the
Kurdish-controlled territory, it appears US sent a message with the
op.


ABC News: "Senior IS leader captured in US-led military raid in Syria"

---

Al Jazeera: "As Russia advances, is Western support for Ukraine
faltering? Kyiv is appealing for more heavy weapons from its backers,
but Western leaders' rhetoric suggests support may be ebbing"

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
