<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

CSP, Heliogen, H2 

<iframe width="340" src="https://www.youtube.com/embed/ZvdENQ5KMjo?start=192" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

H2 View: "[South Korean] Scientists create new non-metallic
photocatalyst for green hydrogen production.. Inha University
researchers had developed a high-performance non-metallic carbon
nitride photocatalyst with a newly designed structural shape. It can
be employed to use sunlight for breaking down the molecules of water
into oxygen and H2"

---

H2 Fuel News: "H2-Industries to develop US $1.4 billion
waste-to-hydrogen plant in Oman"

---

H2 View: "€1bn investment in Sines, Portugal, will see the
construction of a 500MW green hydrogen project"

---

H2 Fuel News: "Plug Power to supply Walmart with up to 20 daily tons
of green liquid hydrogen"

---

H2 View: "Large-scale hydrogen salt cavern storage to be explored by
Atura Power and Plains All American"

---

Oil and Gas: "The remarkable fall in the cost of renewable power has
surely enabled commercial green hydrogen ventures such as NEOM... To
really launch a MENA hydrogen economy, Matthes points to a key piece
of infrastructure that could come about through international
collaboration. A pipeline connecting the eastern Mediterranean with
Europe would be the kind of ‘Marshall Plan’ project [Cornelius
Matthes, CEO of Dii Desert Energy] has in mind.

While natural gas pipelines in the western Mediterranean currently
link Algeria, Tunisia, and Morocco to Spain, Portugal and Italy, there
is no pipeline in the east. But a hydrogen-capable pipeline there
could be a breakthrough for NEOM and others. Matthes says that within
a 300-kilometre radius of Sharm el-Sheikh (where the COP 27 conference
will occur this fall) are places with potential 100+ GW production
potential in Saudi Arabia, Egypt, and Jordan"

---

Pipeline Journal: "Osaka Gas and Pipeline Company Delves Into Green Hydogen"

---

"Dr. Terry Galloway [led] the team of astronomers at Chabot Observatory
who calculated the position of, and therefore helped save, the Apollo
13 spacecraft and crew"

---

"At Raven [SR Inc], we are revolutionizing the way the world uses
waste. We take any organic waste and convert it to clean hydrogen and
synthetic Fischer-Tropsch fuels through our patented Steam/CO2
Reforming process. We use steam and a chemical process, not
combustion, to process mixed feedstock (biogenics, plastics and/or
methane) into saleable products in an environmentally friendly,
efficient and profitable way. Our story begins in 1885 with Daniel
Best – great-grandfather of Dr. Terry Galloway (technology creator)
and great-great grandfather of Matt Murdock (Raven founder)"

[[-]](https://ravensr.com/about/#about-history)

---















Latest Israeli violence.. ? I'm watching Raam; how will they react?
Raam is the Arab-Israeli party in the coalition. They claim suspension
of their membership, wonder what's next.

---

"US urges Iraqi government formation as stalemate drags on"

---

Chris Joss - Surrounded \#music

[[-]](https://youtu.be/nxm2qD7_Bjc)

---

WION: "New Zealanders are ordering grocery from Australia, even saving money"

---

Emancipator - Land & Sea (Feat. Molly Parti) \#music

[[-]](https://youtu.be/zEOH_BAQWhg)

---

Wanted: data journalism. Instead of just pretty maps, also supply the
data as below.. The ISW war map could be shared as JSON data - regions
are just a collection of lat,lon points of a "polygon" after all,
offer download and let users plot, process DIY.

---

And of course - the usual troublemaker country [appears](https://english.alaraby.co.uk/news/krg-pm-barzani-hit-eggs-during-visit-london).

---

Current news: there are TR attacks toward all PKK areas, in Syria and
Iraq, even the Iraqi gov joined in for attack on Sinjar. Trouble
around Idlib too..

Asia Minor incursion required KDP (Barzani family) help, and they are
helping, with cries of backstabbing, "Kurd against Kurd violence"
blame thrown at them.

---

From TR standpoint, the more PKK was attacked the more it spread.
So policy has been a fail so far.

---

The fascist coup of 80s fueled PKKs rise

[[-]](2009/09/modern-history-of-kurds-mcdowall.md#pkk80s)

---

Fields connected by pipeline, did not help patch things up between all
stakeholders?

[[-]](https://pbs.twimg.com/media/FQ28zalWQAA0C7w?format=png&name=small)

---

Post Arab Spring PKK spread to Sinjar, near Syria (red cross in map),
helping anti-ISIS fight there, after the fight they stayed. Then they
linked with Syrian NE. Then the sister org there declared autonomy, 2017.
Territory where PKK / sister YPG is active is in [yellow](https://pbs.twimg.com/media/FQ28SJdXoAEcSjR?format=jpg&name=small).
Lots of oil/gas.

[[-]](https://www.crisisgroup.org/europe-central-asia/western-europemediterranean/turkey/turkeys-pkk-conflict-regional-battleground-flux)

---

Various paths from that Qandil mountain to TR; one from Iraq but they
cld easily enter through Iran, immediately cross the Iranian border,
go north and enter from there.. I'm sure they received a lot of help
from Iran over the years.

---

[Data](tweets/2022/kurd1.json)

---

```python
import json, simplegeomap

clat,clon=37.377413, 42.78591;zoom=0.6
simplegeomap.plot_countries(clat,clon,zoom)
simplegeomap.plot_elevation(clat,clon,zoom)
d = json.loads(open("kurd1.json").read())
simplegeomap.plot_region(np.array(d['duhok']),color='seagreen')
simplegeomap.plot_region(np.array(d['erbil']),color='seagreen')
simplegeomap.plot_region(np.array(d['suleymaniah'],),color='mediumseagreen')
pars = [(40,38,'TR'),(46,37,'Iran'),(43,35,'Iraq'),(40,36,'Syria')]
for x in pars: plt.text(*x)
lon,lat = d['qandil']; plt.plot(lat,lon,'rd')
lon,lat = d['sinjar']; plt.plot(lat,lon,'rx')
```

<img width="340" src="https://pbs.twimg.com/media/FQ5hHcJXEAYefG6?format=png&name=small"/>

The darker green areas are Kurdish regions of Iraq, recognized by
central gov, with three governates, associated with two seperate
Kurdish Regional Gov families (north vs south), KDP and PUK. PKK
nestled itself at the intersection of three of these actors, KDP, PUK,
Iran, and on top of the hightest mountain of Iraq (the red dot).
KDP/PUK fought before, while in alliance now, doesn't hurt to
stay right between them for max leverage.

---

Why has the Kurdish terrorist group PKK active in TR been so difficult
to beat? Map above,

---

Secret RU oil shipments to the West? Destination Unknown.. The Latvian
Blend.. \#WION

Whoever needs oil, should get the oil. This is an unnecessary proxy
war, people should not pay the price.

[[-]](https://youtu.be/9tbgMKk0bEM?t=220)

---

Al Jazeera: "Russian media report alleges that the SAS has deployed to
the Lviv region in western Ukraine"

---

Arab News: "Unlikely change in Delhi-Moscow ties as UK PM visits India"

---

\#UKR \#FoxNews \#Carlson

[[-]](https://youtu.be/4IEuCJI6coA?t=152)

---

WSJ: "World Governments Confront Grim Ukraine Toll"

---

Jane's Defense: "Russia begins Donbas offensive"

---

AFP: "The Russian army will aim to take full control over eastern and
southern Ukraine, Russian news agencies quotes a top general as
saying, a day after Moscow announced the 'liberation' of Mariupol"

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


