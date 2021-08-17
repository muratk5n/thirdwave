# Week 33

Al Jazeera Eng has some good docu's. The one on NK, and on limits to
econ growth very good..

---

"Russia Approves #Hydrogen Energy Development Concept. 1st stage
involves creation of specialized clusters & pilot projects for
production/export of hydrogen & for domestic market"

[Link](https://bit.ly/3Alk2um)

---

Jeffrey Sachs: G20 shld be G21; African countries shld join as an
African Union (EU joined as a union, why not AU?) 

---


What food was foreign to (most) hunter-gatherers? Tomatoes. For many
in the "Old World", until 16th century there were no tomatoes. The veg
is associated with Italian cooking, but this is a mistake, a recent
development... They, nor or the Greeks, or anyone wld have known it
before 16th.. So if you dont like tomatoes, do not feel
bad. Biologically we did not need it, not part of our evolution, so
can safely be eliminated from diets.

---

There was no god damn [missile gap](2021/08/cuban-missile-crisis.md#gap).
JFK either lied or foolishly believed in it himself, likely the former.
There was a missile gap much earlier, that's why US placed missiles in TR.
Bcz of the 60s missile gap, this time with USSR at a disadvantage, USSR
wanted to place missiles in Cuba.

"How about the missile gap of 1960s? JFK won the election thanks to it"

---

Another Berlin story, [Checkpoint Charlie](2021/08/cuban-missile-crisis.md#berlin). 
One tank moves back five meters, the other too, and another.. Major standoff. 

---

It's true, the North Korean embassy in Berlin is also a hostel. I
passed by it many times.. At first u dont realize it, first see the
hostel, keep walking, while turning around the corner, u notice the NK
stuff. Then it's like 'wait.. it's the same building!'

---

I remember this AFG Prez having bunch of power sharing issues while
back.. now think.. over what? Gov disintegrated like cotton candy!

---

Tali in the palace.. Bleeping hilarious

---

Daam.. AFG Prez got - the - fuck **out**

---

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


