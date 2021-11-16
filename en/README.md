<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>


"@IEA_SolarPACES

Pacific Green shows how #CSP can cut green ammonia costs, [link](https://www.pacificgreen-solar.com/articles/pacific-green-shows-how-cut-green-ammonia-costs-ammonia-energy-conference-2021)"

<img width="340" src="https://pbs.twimg.com/media/FEOBT38XMAECsfL?format=jpg&name=small"/>

[[-]](https://twitter.com/IEA_SolarPACES/status/1460152887716290563)

---

NO SHOW STOPPERS

"No show stoppers for Concentrating Solar Power... A recently published
study confirms that solar thermal power is largely unrestricted by
materials availability"

[[-]](https://www.chalmers.se/en/news/Pages/No-show-stoppers-for-Concentrating-Solar-Power.aspx)

---

Based on paper below, assuming a solar PV panel uses 0.2 g indium per
square meter (a low assumption, paper has it higher, 0.38 g/m2), 300 W
/ m2 solar energy, with 30% panel efficiency, and given world reserves
of indium is 5700 tons,

```python
m2 = 5700*1e6 / 0.2
km2 = m2 / 1e6
print (km2, 'km2')

world = 157481.
eff = 0.30
kw = m2*(300*eff) / 1000.0
twh_year = (kw*24*365) / 1e9
print ('%0.2f percent' % (twh_year / world * 100.0))
```

```text
28500.0 km2
14.27 percent
```

only 14% of world energy requirement can be generated through PV solar
tech, given the indium reserves and its usage. Did not even look at
the other rare earth metals, cadmium, tellerium.. 

[[Paper]](https://www.researchgate.net/publication/281617586_Assessing_Rare_Metal_Availability_Challenges_for_Solar_Energy_Technologies)

---

AZO Cleantech: "[R]ecent research coming out of the Netherlands has
spotted a red flag to relying on solar panels as a panacea for global
emissions problems. Experts have found that the rare metals required
to build solar panels, such as indium and tellurium, are not in
sufficient supply to keep up with demand... Currently, China is
providing the world.. Yet [CH] is no longer abundant with precious
metals"

---

Electrons are fickle.. Must base the new energy system on things with
more of a substance; gas, liquids, molecules, heat, pressure.

"The advantage of the thermal reflector systems is that because they
initially produce heat, this heat can be stored, and it’s an important
consideration if you need to produce electricity after
sunset. Photovoltaic panels, on the other hand, produce electricity
immediately, making storing electricity less efficient. The Negev
Energy project uses a molten salt storage system that enables it to
hold and provide additional 4.5 hours of clean energy each day, at
full capacity, even after sunset or during cloudy days"

[[-]](https://www.timesofisrael.com/israel-marks-start-of-work-at-thermal-solar-sea-of-mirrors-plant-in-negev/)

---

Increasing productivity decreases inflation..? The effect has too long
of a time horizon and it isn't that big, or direct. Don't bet your
econ diploma on it, if you have one 😶

---

Austria is not messing around..

Their vax rates were very low

"Austria lockdown for unvaccinated to start on Monday: chancellor"

---

For AFG pullout, people apparently didn't like its execution.. It
didn't "look good" to them.. WH could've done pre-spin perhaps but
were caught unawares on Tali. 

---

Downtrend on Biden's popularity did not start on Aug; it has been
going on since the beginning of 2021 (Delta?). Without the August
debacle, net pop wld have been at -5, with Aug debacle (AFG pullout)
it went to -10% territory.

```python
import pandas as pd
url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
df['net'] = df['approve_estimate'] - df['disapprove_estimate']
df['net'].plot()
```

[[-]](https://pbs.twimg.com/media/FEQQdehXsAsAo4z?format=png&name=small)

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


