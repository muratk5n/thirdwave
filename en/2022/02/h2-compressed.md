# Compressed H2 

[DOE](https://www.energy.gov/eere/fuelcells/physical-hydrogen-storage)

Physical storage is the most mature hydrogen storage technology. The
current near-term technology for onboard automotive physical hydrogen
storage is 350 and 700 bar (5,000 and 10,000 psi) nominal
working-pressure compressed gas vessels—that is, "tanks."..

[C]ompressed hydrogen typically is stored at near-ambient temperatures.

The utility vehicle Hyundai Nexo has three equal-size carbon tanks
mounted under the boot floor and the rear seat hold a total of 6.33
kilos of hydrogen. The NEXO thus has the largest tank [capacity] of
all available fuel-cell passenger cars and, thanks to an optimised
drivetrain/power train, the longest range as well: 756 km [3] stored
at 700 bars.

[Paper](https://www.sciencedirect.com/science/article/pii/B9780128111970000038)

Compressed hydrogen can be transported by trucks in gas cylinders or
gas tubes with pressures between 200 and 500 bar. Usually several
cylinders or tubes are bundled to modules in a 20′ or 40′ container
that is mounted on a trailer (tube trailer)...

A tube trailer with steel cylinders can store up to 25,000 liters of
hydrogen compressed to 200 bar which amounts to around 420 kg of
hydrogen.

Provaris

This company provides compressed H2 shipping solutions. Their presentation [1]
states their tech

- Stores, transports & delivers hydrogen in high purity gaseous form

- Minimal technical barriers, no boil off

- Their system avoids energy and capital-intensive processes, compression
  tech is simpler.

Recently Provaris obtained world's first design approval for
compressed hydrogen carrier from [American Bureau of Shipping]. Their
maximum planned ship will have 120,000 m3 of H2 capacity. Let's
calculate how much energy we could deliver assuming 40 trips / year
and a fleet of 20 ships, using 250 bar H2 having 700 kwh/m3,

```python
capacity = 120000 #m3
print ("Single ship %0.1f MW" % ((ship * 700) / (365*24*1e3)))
ann_trips = 40
print ("Fleet capacity %0.1f GW" % ((20 * ann_trips * capacity * 700) / (365*24*1e6)))
```

```text
Single ship 9.6 MW
Fleet capacity 7.7 GW
```

References

[1] [Provaris Presentation](https://assets.website-files.com/626b0112d67346fa8eab974d/6280ef3d5ce3f07d709f43a7_Provaris%20-%20Corporate%20Deck%20-%2016%20May%202022%20ASX.pdf)

[2] https://en.wikipedia.org/wiki/Compressed_hydrogen_tube_trailer

[3] https://h2.live/en/fuelcell-cars/hyundai-nexo/

[[Up]](h2-storage.html)
