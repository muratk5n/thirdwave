<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">It’s <a href="https://twitter.com/hashtag/WorldBookDay?src=hash&amp;ref_src=twsrc%5Etfw">#WorldBookDay</a>, so I’m going to take a moment to highlight my fav <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> book 📖 If you haven’t already, you should check out <a href="https://twitter.com/malvera1?ref_src=twsrc%5Etfw">@malvera1</a>’s “The Hydrogen Revolution.” It’s a fav amongst the <a href="https://twitter.com/HystarH2?ref_src=twsrc%5Etfw">@HystarH2</a> team, too! <a href="https://t.co/zzBwkopctO">pic.twitter.com/zzBwkopctO</a></p>&mdash; Leila A. Danielsen (@lasdal) <a href="https://twitter.com/lasdal/status/1517920683443081218?ref_src=twsrc%5Etfw">April 23, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

Cummins partners with Freightliner on hydrogen fuel-cell truck.. The
Freightliner Cascadia chassis will be equipped with fourth generation
equipment from Cummins... [The companies] have announced that they
will be working together on a new hydrogen fuel-cell truck that is
intended for the North American market.

---

H2 View: "The much anticipated, REPowerEU Plan has been presented by
the European Commission, and has set a target of 10 million tonnes of
domestic renewable hydrogen by 2030"

---

Some base data is maintained [here](2022/02/base-energy-numbers.html)

---

It is great Europe is creating the demand upfront, that can spur
companies to get their tech in order; Provaris CEO attended an H2 conf
and says the demand from them is clear, EU wants tons of this
stuff. Where there is demand, there will be supply.. so they are
building the tech for it. Enter the snowball effect; seeing supply,
products will arrive to use it, which will create more demand. Only
policy could kick that off, bidness could not do it on its own.


---

Suiso ship used low temperature. The GH2 ship uses compression. The AU
company that built it is Provaris Energy. Presentation on the tech and
planned infra below. First ship is 26,000 m3 another planned 120,000
m3, compressed H2 at 250 bar can carry 700 kwh/m3 which means one trip
will carry 84.0 Gigawatt-hours, that is mid-size crude oil tanker
equivalent. Very good.

[PDF](https://assets.website-files.com/626b0112d67346fa8eab974d/6280ef3d5ce3f07d709f43a7_Provaris%20-%20Corporate%20Deck%20-%2016%20May%202022%20ASX.pdf)

---

H2 View: "Offshore green hydrogen production unit unveiled.. Technip
Energies and its affiliates, Kanfa and Inocean announced the launch of
its suite of offshore green hydrogen production solutions, GO.H2 TM by
T.EN"

---

H2 View: "A new ship that will collect ocean plastic and produce
hydrogen to be designed.. H2 Industries and naval architecture
company, TECHNOLOG Services have revealed a partnership to design a
ship that will collect plastic waste and convert it into hydrogen"

---

This means LH2 storage does not require extra energy..? That's smart.

"Suiso Frontier (hydrogen tanker) is a custom-built vessel with
double-shell vacuum insulation that enables liquid hydrogen to be
transported without any coolant"

[[-]](https://www.nature.com/articles/d42473-020-00544-8)

---

Can work backwards from capacity to output. LNG replacement? Get ship
capacity, number of trips, or simply an annual export amount giving a
Gwh, now work backwards from there, divide by 365, then 24 - once we
have calc down to Watt-hour within an hour, we can drop the hour, get
Wattage.

---

Converting energy numbers to a Wattage (kilo,giga) as in power input /
output helps to gauge how much of a power need can be met by existing
sources, and compare sources with eachother, no matter how long that
power would be needed (which takes us into Watt-hour, storage capacity
territory). A TV pulls in 60 Watts, an oven 1500 W. Russian NG export
to Europe is 167 Gigawatts (a lot of TVs can run on that
energy). Typical nuclear plant output is 1 GW, Fukushima (the one that
had the meltdown) was 5 GW. We see it will take 33 Fukushima's to
replace Russian exports to Europe. Now in terms of environment policy
that is probably a non-starter. 

---
















---

"@christo92787346

I can't wait for Raytheon baby formula with laser targeted nutrition"

---

AP: "Biden invokes Defense Production Act to boost baby formula
production, authorizes flights to bring imports from overseas"

---

How to get the code references here? If there is an `import` for a
library, but it is not an official Python lib, its `.py` file will be
under that year's archive.  For example `yf.py` is under
`en/tweets/2022` folder.

---

If people's buying patterns truly changed, and -per that great WSJ
supply chain docu- there is about a year's worth of journey behind
every product even though the last-mile delivery of the product looks
instantenous, then changes on demand could manifest itself as supply
chain problems. Then there was covid itself effecting the production.

---

Saw Target CEO on CNBC, his main complaint was 'supply chain supply
chain supply chain'

---

Their stocks were hammered. 

```python
import yf
fig, axes = plt.subplots(2, 1, figsize=(6, 4), sharey=True)
df = yf.get_stock_price('WMT')
df.plot(ax=axes[0],legend=False,sharex = True,title='WMT')
df = yf.get_stock_price('TGT')
df.plot(ax=axes[1],legend=False,title='TGT')
```

<img width="340" src="https://pbs.twimg.com/media/FTGwlY6XEAIbG03?format=png&name=small"/>

---

Doh!

```python
import yf;yf.get_earnings("WMT").head(4)[['startdatetime','epsestimate','epsactual']]
```

```text
Out[1]: 
              startdatetime  epsestimate  epsactual
0  2023-02-21T07:00:00.000Z          NaN        NaN
1  2022-11-15T07:00:00.000Z          NaN        NaN
2  2022-08-16T07:00:00.000Z         1.88        NaN
3  2022-05-17T07:02:00.000Z         1.48        1.3
```

1.3 vs 1.48 for Walmart.

---

Both Target and Walmart had a miss on earnings estimates. 

---

He admitted it \#Iraq \#W \#empire

[[-]](https://twitter.com/sahilkapur/status/1527092111195226114)

---

There will be more shrinkage I bet. Still meddly meddly, messing stuff
up all over the place. Leave Asia Minor alone

"The incredible shrinking Global Britain.. Funding cuts and staffing
turmoil at the Foreign Office are scaling back the UK’s international
ambition"

---

CNBC: "India is not alone. In addition to Russia and Ukraine, Egypt,
Kazakhstan, Kosovo and Serbia have also banned wheat exports"

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


