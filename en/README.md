<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

H2 View: "Siemens Energy to begin industrial-scale electrolyser
manufacturing in Berlin, Germany"

---

H2 View: "Teco 2030, Narvik Hydrogen sign agreement to develop the
Norwegian hydrogen value chain"

---

H2 View: "Baker Hughes has revealed plans to provide hydrogen-ready
turbo-compression technology for a pipeline in Greece... This could be
a vital development not only for the Greek hydrogen value chain but
also the wider European market with a hydrogen pipeline backbone vital
in accelerating the adoption of hydrogen"

---

Strategic Petroleum Reserve is 714 million barrels.. US consumes 19.78
mil barrels per day on avg; Month and a half worth of storage.

---

H2 Fuel News: "[USG] has announced that the infrastructure necessary
to support natural gas shipments to Europe, and eventually hydrogen
fuel instead, is already being built"

---

Water shortage worries? Clean water will be all about
energy. Desalination is getting cheaper.. Energy consumption of
seawater desalination reached as low as 4 kWh/m3. If we can increase
energy output, especially green energy output, we can heat, cool,
desalinate to our heart's content.

[[-]](https://en.wikipedia.org/wiki/Desalination#Energy_consumption)

---

TDB: "Putin to Europe: Pay for Your Gas in Rubles or We’ll Cut You Off"

---

Al Jazeera: "India-Russia explore a rupee-rouble payment scheme to bypass war"

---

House prices were (are) up because FED rates were low (2 yrs ago was
start of covid). In low rate environments too much speculative money
chases housing, raising the price.. If two years ago the rates were
higher, US would not be in this situation today.

---

Time shift housing (2 yrs back) and check against rent, to see if
house price changes in the past caused rent increases,

```python
df.incrent.corr(df.inchouse.shift(24))
```

```text
Out[1]: 0.612
```

Not a small effect there.. since we time shifted, hint at causation

That means it takes ~2 years for house price changes to effect rent changes.

If there is mega rent increase now there was mega house price increase
2 years ago

---

YoY rent and house price % increases below,

```python
import urllib.request as urllib2, time as timelib
import pandas as pd, datetime
from pandas_datareader import data

today = datetime.datetime.now()
start=datetime.datetime(1970, 1, 1)
end=datetime.datetime(today.year, today.month, today.day)
cols = ['CUUR0000SEHA','MSPUS']
df = data.DataReader(cols, 'fred', start, end)
df = df.interpolate()

df['incrent'] = (df.CUUR0000SEHA-df.CUUR0000SEHA.shift(12))/df.CUUR0000SEHA.shift(12)*100
df['inchouse'] = (df.MSPUS-df.MSPUS.shift(12))/df.MSPUS.shift(12)*100

plt.figure()
ax1 = df.incrent.plot(color='blue', grid=True, label='rent inc %')
ax2 = df.inchouse.plot(color='red', grid=True, label='house price inc %',secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
plt.savefig('out.png')
```

<img width="340" src="https://pbs.twimg.com/media/FPO1uM_XsAgAA2x?format=png&name=small"/>

---

Paper on long-run relation between housing prices and rent. Says there
is causality with a delay. Let's check.

[PDF](https://www.federalreserve.gov/pubs/feds/2004/200450/200450pap.pdf)

---

"@FatherlyHQ

Rent, one of the most basic payments that many millions of Americans
have to pay monthly, is just one of the things that has exploded in
cost lately"

---

Oz deputy PM too said some mild things about Assange, that he is an
Australian citizen -which is true- and should not be tried abroad, and
some odd stuff (!) happened afterwards.. His SMS some time ago talking
shit on the sitting PM, his coalition partner, were leaked. Weird.

---

Pak PM Imran Khan is in trouble? IK isn't exactly pro-establishment,
world-order kind a guy.. I heard him defend Julian Assange once.

---

GCHQ says so.. really? It must be true then 😶

FT: "China’s interests ‘not well served’ by aligning with Russia, GCHQ says"

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


