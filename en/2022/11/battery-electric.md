# Battery Electric Tech

### Low Energy Density

### Insufficient Lithium Reserves

Even for transportation, widespread use use of lion batteries is
impossible. In 2020, 48.6 percent of all oil consumed in the OECD was
related to motor vehicle usage [1].

2019 crude oil consumption 100.37 million b/d. 

Crude oil 10.215 kwh / kg.

For total energy use the picture is more grim.  According to
[EIA](https://en.wikipedia.org/wiki/World_energy_consumption),
estimated world energy consumption was 157,481 Terrawatt Hours in
2013, meaning 431 TWh/day. If we were to store today's energy
consumption one day in batteries,

```python
consumed_one_day = 431 * 1e9 # Kwh
reserves = 17.0 # mtones
req = ((consumed_one_day / 70.0) * 60.0) / 1e9
print ("%d mil. tons" % req)
print ("Can hold %0.2f percent of required energy" % ((reserves / req)*100.0) )
```

```text
369 mil. tons
Can hold 4.60 percent of required energy
```

.. it would require over 20 times the amount of available lithium in
the world.


### Degradation

Lion tech has a huge degredation problem, ie with every use the
performance of the battery degrades. Most know this fact probably from
our notebook batteries; well, since some idiot decided to migrate the
same tech to a car, now the same problems have migrated to this domain
as well, except in a larger scale.

From the owner of a home storage system: "[If I am] cycling through my
battery Powerwall every single day, I'm actually degrading the
battery, and the sooner that it's going to basically be dead and
unusable and you need to go buy another one. My battery pack is only
there for an emergency, like if something crazy happens like the power
goes out.. And when I say it's not worth the money.. I could have
taken that $20,000 that it cost to put these on the wall, and I could
have put a bunch more, maybe 20, maybe 30 more solar panels on the
house.  Every single day that would be generating money for me and
money for our house, decreasing the cost"

[[-]](https://youtu.be/Qgv6Lgvy8Lc?t=495)

### Safety

<iframe width="340" src="https://www.youtube.com/embed/46y3FN4fKlE" title="E-Bikes, E-Scooters Injuries Multiplying" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>




















References

[1] [Statista](https://www.statista.com/statistics/307194/top-oil-consuming-sectors-worldwide/)


