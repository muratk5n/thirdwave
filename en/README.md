<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

<iframe width="340" src="https://www.youtube.com/embed/B3knAZxXMzo?start=195" title="How Hydrogen Could Solve the Energy Crisis: Bloomberg Green" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Fast Company: "Of course, the sun—and wind, for that matter—aren’t
always available, and certainly not everywhere. 'Heavy industry runs
24-7. You don’t find any factories that shut down and only run one
shift,' says Bill Gross, founder and CEO of Heliogen, a company that
stores as much thermal energy as possible to then convert to green
hydrogen, an alternative fuel..

'I feel it’s all about using science and technology to find a way to
beat that price of fossil fuel,' Gross says. Heliogen has built a
“sunlight refinery”: a setup whereby thousands of mirrors.. reflect
beams of sunlight.. onto a single spot at the top of a tower, the size
of a basketball hoop. That concentration allows the collected sunlight
to reach temperatures of more than 1,000 degrees Celsius.. 

It then stores that thermal energy in tanks of gravel. 'Imagine a
thousand pizza stones in an oven where you close the door after you’ve
heated them up,' Gross says. 'Those are going to stay hot for a very
long time.' The energy can then be easily transported to less sunny
climes, wherever it’s needed. 'It allows us to run on cloudy days. It
allows us to run through any other kind of interruption. That’s what’s
crucial for the world because we all want to have uninterruptible
power.

They then convert that energy into green hydrogen via electrolysis,
which essentially splits the hydrogen from water (and an important
distinction from dirty hydrogen, which is traditionally produced from
methane). “When you burn hydrogen, it releases nothing,' Gross
says. 'It releases just water vapor to the atmosphere. That’s the
beauty of hydrogen.'"

[[-]](https://www.fastcompany.com/90756680/how-much-could-renewable-sources-like-solar-and-thermal-shape-our-future-energy-needs)

---

H2 Central: "Engines equipped with H2-HPDI (High Pressure Direct
Injection) fuel systems run on hydrogen and offer a spectrum of
advantages over other technologies, making it possible to accelerate
H2 adoption as a component of sustainably operating heavy-duty
vehicles. Among the advantages of using H2-HPDI systems from Westport
Fuel Systems include its practicality for fleet managers that require
straightforward operations and maintenance in the transition toward
improved sustainability. Furthermore, engines equipped with these
systems can exceed the performance of current heavy-duty diesel
vehicles while simultaneously minimizing greenhouse gas emissions to
the point that they are nearly eliminated"

---

H2 Fuel News: "Pilot Company expands into compressed natural gas and
hydrogen: partners with VoltaGrid. Pilot Company, one of the leading
suppliers of fuel and the largest operator of travel centers in North
America, announced that the company is building upon its current
initiatives in the alternative fuels space with a new compressed
natural gas (CNG) and hydrogen delivery platform. This expansion
includes a partnership with VoltaGrid LLC (“VoltaGrid”) to develop a
low-carbon fuels network that contributes to reduced emissions and
decarbonization for third-party customers in industries like water
disposal, dual-fuel applications, water heating operations, and
natural disaster response"

---

H2 View: 'Nuvera Fuel Cells, LLC, a provider of heavy-duty hydrogen
fuel cell engines for on- and off-road mobility and other
applications, announces an order for an E-Series Fuel Cell Engine from
CMT, a propulsion technology research institute at the Universitat
Politècnica de València, Spain. Focusing on accelerating the
widespread adoption of zero-emission vehicle power sources, CMT is
building a 200 kW fuel cell test bench facility in collaboration with
AVL, a worldwide engineering leader"

---

H2 View: "GRTgaz and Fluxys are Willing to Develop The First
Open-Access, Cross-Border Hydrogen Transmission Network Between France
and Belgium"

---

Al Monitor: "Saudi Arabia's futuristic planned city NEOM plans to
build a water desalination plant powered by renewable energy"

---

The increase in renewables is great, but we are still inching forward
megawatt by megawatt and 1 GW plant is considered a big deal. Still
tough to keep up with oil / natgas resources of eg US, Iran, Qatar or
Russia. Guy digs one hole in the ground and boom: 60 Gigawatts. Need
more? Another hole, boom. Another 60. Saudi Arabia's total energy
output is about 1 Terrawatt.

---

CNBC: "Look for more selling pressure next week as investors learn the
hard way not to fight the Fed"

---

Al Jazeera: "Apple Inc workers in Maryland, US vote to join a union"

---

All previous reports, graphs, maps shared are accessible from the
[reports](2019/05/reports.html) page.

---

McDonalds switched to veg oil from tallow for cooking its fries?
Likely due to the "war against fat" wave.. 

---

The article doesn't mention it but animal fat is healthier too

---

Aaand here it is - [lab-grown fat](2022/06/lab-grown-meat.md#fat)

---

"@MoonmanND

The only vending machine has to connect to the internet apparently, so
today I just don't get to eat breakfast I guess"

[[-]](https://twitter.com/MoonmanND/status/1537366091441356800)

---

When dollar is strong, other countries have trouble securing the
dollars to buy the oil with, ergo oil demand (and global price)
decreases. Non-US demand would effect oil price more, there are more
people outside US.

The Balance: "When it comes to international trade for raw materials,
the dollar is the exchange mechanism... When the value of the dollar
drops, it costs more dollars to buy commodities. At the same time, it
costs a lesser amount of other currencies when the dollar is moving
lower"

---

Historically there was a reverse correlation between dollar and oil.
Strong dollar, weak oil, and vica versa. The relation broke recently
we'll see if it sticks. Is the petrodollar system broken already?

---

Dollar and Oil

```python
import util
df = pd.merge(util.get_yahoofin(1990,"CL=F"),
              util.get_fred(1990,['DTWEXBGS']),
              left_index=True,right_index=True)
df.columns = ['oil','dollar']
ax1 = df.dollar.plot(color='blue', grid=True, label='dollar')
ax2 = df.oil.plot(color='red', grid=True, label='oil',secondary_y=True)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
plt.legend(h1+h2, l1+l2, loc=2)
```

<img width="200" src="https://pbs.twimg.com/media/FVgvWwKUcAIfD3k?format=png&name=small"/>

---

Investopedia: "With the Federal Reserve raising rates and expected to
continue to do so, the U.S. Dollar has been growing stronger"

---

"The FED giveth, and the FED taketh away" Hah

---

"Flat is the new up". Heard on fin channel

---

Bloomberg: "'Not Buying This Dip,' Says BlackRock's Brazier"

---

Italy's Rome went gone long time ago - that helped Italy 

---

The coup culture is usually connected to a previous feudal culture;
Greece and Asia Minor suffered various coups because of their earlier
Roman / Byzantium / Ottoman past. Remember the Praetorian Guard? In
sum, if agrarian-taxer-plunderer parasitic-government culture becomes
entrenched, it creates the types of people in society who think anyone
with military power can and should take the reins by force. This is
the feudal way (other side effects are paternalism, hierarchy,
inequality and more). Coups are, therefore, pre-modern creations
experienced in countries on the road towards modernity.

---

Quora: "Why there have been frequent military coups in Pakistan as
compared to it's neighbour India?..

The British always divided Hindus and Muslims by treating Muslims
preferentially by recruiting Muslims/Sikhs in army under the concept
of Martial races. Indian army had excessive percentage of Pujabi
Muslim Army units. The units were organised with people from single
regions or castes. They were led by British officers and this resulted
excessive allegiance by minority units like punjabi Muslims who
imitated British officers and this perceived superiority complex
exists even today in Pakistan society.  This was broken by India once
India became free and the rule of Martial races in recruitment was
buried. Chaudhries and sardars were thrown out of the window giving a
body blow to Feudals. Feudalism was weakened by land reforms.
Pakistan continued in the old ways.and new Feudals are the Army,
Sardars in NWFP, KPK, POK, Baluchstan, Bueraucrats, and now a small
bands of industrialists.

---

Janes Defense: "Reacting to pressure from NATO's former Warsaw Pact
members and Russia's brutal war tactics in Ukraine, the alliance is
ditching its thin, so-called tripwire line of defence along its
eastern flank for a military posture more redolent of decades past:
more troop deployments, more pre-positioned weapons and supplies
across the region, and a return to Cold War-like pre-designated areas
for particular allies to defend on short notice"

---

"A recent Bloomberg report called attention to the unwelcome but
predictable consequences of broad Russia sanctions: “But some Biden
administration officials are now privately expressing concern that
rather than dissuading the Kremlin as intended, the penalties are
instead exacerbating inflation, worsening food insecurity and
punishing ordinary Russians more than Putin or his allies.”.. These
harmful effects of broad sanctions should not come as a surprise to
anyone that has followed these issues closely, since this is what
almost always happens when a country’s entire economy is targeted for
punishment. The inability to change the behavior of a targeted
government is even less surprising, since it is extremely rare for
unfriendly authoritarian states to knuckle under in the face of
U.S.-led pressure campaigns"

[[-]](https://responsiblestatecraft.org/2022/06/17/we-shouldve-known-sanctions-on-russia-wouldnt-work-as-intended/)

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
