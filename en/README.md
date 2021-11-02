<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

Rodney Crowell - Fate's Right Hand \#music

[[-]](https://youtu.be/A2CdF5U1ZY8)

---

It's interesting how open to violence this region is, even after all
these years; things get a little funky, troublemakers come out of the
woodwork, as if on cue.

"Fears of Brexit violence as armed men hijack and torch bus in Northern Ireland"

---

With the "emotional brain" concept I dont mean a person "getting
excited" sometimes, and "in the heat of the moment" fail to make
rational decisions. No... even when a person is silently sitting, with
no external stimuli or visible disturbances, they are mostly deciding
emotionally (culturally). Unless one is concious of it, it is
extremely hard to cancel out that stuff, the emotional will almost
always override the rational.

---

Plus it is extremely hard to recycle this stuff, so we'd literally be
using it up, finishing it at a certain point.

---

For the lazy or busy readers, here is the lithium calculation. Energy
stored per kilogram of lithium,

```python
kgkwh = 60/70 #kg/kWh
"%0.2f kg/kwh" % kgkwh
```

```text
Out[1]: '0.86 kg/kwh'
```

Divide the weight of all lithium in the world (dug up or otherwise),
17 million tons, by the number above,

```python
reserves = 17*1e6*1e3 # tonnes
batcap = reserves / kgkwh
"all battery capacity using all lithium: %0.2f kwh" % batcap
```

```text
Out[1]: 'all battery capacity using all lithium: 19833333333.33 kwh'
```

This is the maximum energy storage capacity we can have.

World consumption in one year (2013) was 157,481 Terrawatt
Hours. Divide by 365 per day, and compare,

```python
energy_daily = (157481. / (365)) * 1e9 # Kwh
"%0.2f percent" % (batcap / energy_daily * 100.0)
```

```text
Out[1]: '4.60 percent'
```

Only 5% of the energy need can be stored in batteries. This tech wont
make a dent in fight against climate change.

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


