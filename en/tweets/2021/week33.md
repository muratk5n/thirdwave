# Week 33

NYT: "[A Sicilian town Floridia] is perhaps the most blisteringly hot
town in the recorded history of Europe, offering Italy and the entire
Mediterranean a preview of a sweltering and potentially uninhabitable
future brought on by the globe’s changing climate... [A] nearby
monitoring station registered a temperature of ... nearly 49 degrees
Celsius....  the unprecedented heat rendered Floridia a blindingly
bright ghost town, with its bars deserted, its baroque and
sand-colored churches darkened, its piazzas emptied.In the surrounding
fields, the area’s famed snails burned in their shells. The relentless
sun branded the verdello green lemons with yellow blots and stewed
their flesh within. Everyone holed up in their houses. The
air-conditioning they blasted prompted blackouts"

---


The "balanced plate" idea for prediction is looking better.. Bunch of
eqs on one side (bottom left), had to be balanced by a big eq on the
other side.

---

<img width="340" src="https://pbs.twimg.com/media/E8weTFtXEAA11rZ?format=jpg&name=small"/>

---

7.2 in Haiti

---

NYT: "Why the Afghan Military Collapsed So Quickly.. The Taliban’s
rapid advance has made clear that U.S. efforts to turn Afghanistan’s
military into a robust, independent fighting force have failed, with
its soldiers feeling abandoned by inept leaders"

---

BBC: "Climate change: July world's hottest month ever [says] US agency"

---

WSJ: "Greece Clamps Down on Aid Groups That Help Migrants.. The
country has accused nongovernmental organizations of involvement in
trafficking as part of its efforts to stem the flow of migrants and
refugees who continue to make dangerous journeys to Europe"

---

Amazon?

```python
q = yf.get_financials("AMZN")
print ('AMZN', [(d[:20] + ': ' + q[d]) for d in ds])
```

```text
AMZN ['Revenue  (ttm): 443.3B', 'Quarterly Revenue Gr: 27.20%', 'Quarterly Earnings G: 48.40%']
```

Earnings growth 48.40%? Is that right?

Now we know where all that pandemic spnding went.

---

The company certainly helped itself by pushing for content like *The
Mandalorian*, becoming less cuck

---

Disney raked it in..? Let's check


```python
import yf

ds = ["Revenue  (ttm)", "Quarterly Revenue Growth  (yoy)",\
      "Quarterly Earnings Growth  (yoy)"]
      
q = yf.get_financials("NFLX")
print ('NFLX', [(d[:20] + ': ' + q[d]) for d in ds])
q = yf.get_financials("DIS")
print ('DIS', [(d[:20] + ': ' + q[d]) for d in ds])
```

```text
NFLX ['Revenue  (ttm): 27.59B', 'Quarterly Revenue Gr: 19.40%', 'Quarterly Earnings G: 87.90%']
DIS ['Revenue  (ttm): 63.59B', 'Quarterly Revenue Gr: 44.50%', 'Quarterly Earnings G: N/A']
```

DIS rev growth looks good

---

CNBC: "Disney won this earnings season by adding 12 million Disney+
subscribers while Netflix's growth stalled"

---


