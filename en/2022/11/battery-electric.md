# Problems of Battery Electric 

Lion battery tech suffers from multidude of problems that makes it
unfit as a basis of a green transition, and as a general storage
mechanism.

<a name='density'/>

### Low Energy Density

Batteries have low energy density. Plug Power CEO: "Power Density and
Range: fuel cell energy density is four times more than batteries, and
a tank of hydrogen contains more than double the energy of a battery
at the same weight"

Low energy density means heavy-duty transport, or battery based
airplanes are out of the question for an battery-electric
transition. 

easyJet: "When we.. looked back a few years ago, we realised clearly
that the climate emergency is coming our way and that we needed to
address our sustainability issue – and we knew that our passengers
care about that as well.. It was about the time when we started to see
the first electric cars, the Tesla vehicles.. and there was
expectation that everything would go electric. However, once we got
into the detail and the physics and the science behind electric, it
became clear that battery-powered aeroplanes were not going to have
sufficient energy density to power a large commercial aircraft"

Alvera: "A kilogram of gasoline holds 13 kilowatt-hours (kWh) of
energy; a kilogram of lithium-ion battery holds less than 0.3
kWh. This means electricity isn’t going to be the best way of powering
sectors which need to take lots of energy with them. Just think of
long-haul flying: we would need so many heavy batteries that the plane
wouldn’t be able to take off. And batteries won’t compete with
molecules to propel cargo ships across oceans" [3]

<a name='reserves'/>

### Insufficient Lithium Reserves

Even for motor vehicle road transportation, widespread use use of lion
batteries is impossible. In 2020, 48.6 percent of all oil consumed in
the OECD was related to motor vehicle usage [1]. Existing estimated
lithium reserves are at 17.0 millon tons. 2019 crude oil consumption
100.37 million b/d, 1 barrel carries approximately 1700 kwh of energy,

```python
reserves = 17.0 # mtones
kwh_day = 100.37*1e6*1700*0.486
req = ((kwh_day / 70.0) * 60.0) / 1e9
print ("%d mil. tons" % req)
print ("Requirement is %d times of reserves" % (req/reserves))
```

```text
71 mil. tons
Requirement is 4 times of reserves
```

We cannot even transition all driving to a lion based system.

For total energy use the picture is more grim.  According to
[EIA](https://en.wikipedia.org/wiki/World_energy_consumption),
estimated world energy consumption was 157,481 Terrawatt Hours in
2013, meaning 431 TWh/day. If we were to store today's energy
consumption one day in batteries,

```python
consumed_one_day = 431 * 1e9 # Kwh
req = ((consumed_one_day / 70.0) * 60.0) / 1e9
print ("%d mil. tons" % req)
print ("Requirement is %d times of reserves" % (req/reserves))
```

```text
369 mil. tons
Requirement is 21 times of reserves
```

.. it would require over 20 times the amount of available lithium in
the world.

<a name='degradation'/>

### Degradation

Lion batteries have a huge degredation problem, ie with every use the
performance of the battery degrades. Most know this fact probably from
their use of notebook batteries, eventually the battery dies out.
Well, since some retarded genius decided to migrate the same tech to a
car, now the same problem has migrated to this domain as well, except
in a larger scale.

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

<a name='safety'/>

### Charging

[Blowing the Fuse](../../2022/10/grid-fuse.html)

### Safety

Lion batteries routinely blow up. The cause can be from mild collision
between an EV and another car, or salt water during a hurricane as was
witnessed recently in Florida, or in an ebike shop (for no reason)
recently in New York.

<iframe width="340" src="https://www.youtube.com/embed/46y3FN4fKlE" title="E-Bikes, E-Scooters Injuries Multiplying" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

Insurance Journal: "A Florida senator is calling for action from the
Transportation Department and automakers after a series of electric
vehicle fires tied to Hurricane Ian.. Sen. Rick Scott (R-Fla.) raised
concerns.. 'This emerging threat has forced local fire departments to
divert resources away from hurricane recovery to control and contain
these dangerous fires,' Scott said. 'Car fires from electric vehicles
have proven to be extremely dangerous and last for a prolonged period,
taking in many cases up to six hours to burn out.'"

IMPORTANT NOTE: Once the fires start firefighters find it incredibly
hard to put out using traditional methods, this is due to inherent
weaknesses of this particular technology. Lithium salts in the battery
are self-oxidizing, which means that they can't be 'starved out' like
a traditional fire.

### Conclusion

All the problems listed above are enough to doom a technology on their
own. Combined, they are fatal. Considering adaption, TCO issues and
knowing tech migration cycles, even considering a total shift to this
tech would be foolish. The issue goes beyond to being able to
demonstrate a car can move on batteries from point A to point B. There
are larger engineering, economic issues involved here. The industry
will soon realize if all cars, heavy transport, shipping, air flight
cannot be battery electric, it's best not to shift even a portion of
energy use to battery electric. Sadly for its proponents this
technology simply has no future.

References

[1] [Statista](https://www.statista.com/statistics/307194/top-oil-consuming-sectors-worldwide/)

[2] https://thompson-safety.com/company/press/lithium-ion-battery-fire

[3] [The H2 Revolution](../../2022/06/the-h2-revolution-alvera.html)
