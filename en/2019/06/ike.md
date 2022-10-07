# Hurricanes, Integrated Kinetic Energy

In the western hemisphere, hurricanes are all rated on the
Saffir-Simpson scale..  To compute a storm's category rating, you have
to measure the highest speed sustained by a gust of wind for an entire
minute.. Based on how large this maximum speed is, a storm is assigned
to one of five different categories [1].

The problem with this number is that it only captures one aspect of a
storm's intensity - the highest speed that it can sustain. Not only is
it tricky to measure this peak speed, but different organizations may
come to different conclusions about it, depending on their coverage of
the wind data. This number doesn't tell you anything about the size of
the storm, nor about how the wind-speeds are distributed overall.

Consider a tale of two storms - the first is fierce but more
contained, whereas the second is larger, and though it has lower peak
wind speed, these wind speeds are spread over a larger area. The SS
scale would give the first storm a higher score, even though the
latter may be more destructive. Based on the rating, people might have
expected Katrina to be about as destructive as Camille...

Integrated Kinetic Energy

We can get a sense of a storms' strength with a little bit of high
school physics. You might remember that every object in motion carries
a certain amount of energy, known as its kinetic energy. The kinetic
energy of an object depends on the square of its speed, and is
directly proportional to the mass of the object..

Well, think of a storm as being built out of moving parcels of
air. Each of these parcels has a certain amount of kinetic energy.

IKE is calculated as

$$
IKE = \int_v \frac{1}{2} \rho U^2 dV
$$

$v$ is volume, $\rho$ is density, $U$ is speed. This is the familiar
kinetic energy calculation, a variation of $1/2 m v^2$ (here $v$ is
speed). Mass is of the pocket of air, a grid cell of 1 meter
high. Since numerically 1m height, and air density of 1 kg/m3 is
assumed, jut the cell area calculation is sufficient since times 1 wld
give volume times 1 wld give weight. Wind speed from NOAA comes in
$u,v$ components, $u^2+v^2$ will give square speed. Multiply by 0.5
and sum all cells, this gives total energy. Wind speed is retrieved
from a NOAA for each grid cell.

[Code](ike.py)

Hurricane Katrina

```python
import ike
lat=25;lon=-90; year = 2005;month = 8;day = 30; hour = 10
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
340.975708798976 TJ
```

Hurricane Sandy

```python
lat=39;lon=-74; year = 2012; month = 10; day = 29; hour = 13
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
213.907591397376 TJ
```

Hurricane Ivan

```python
lat,lon = 30.302, -87.751; year = 2004; month = 9; day = 16; hour = 10
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
175.953368055808 TJ
```

References

[1] [Wired](https://www.wired.com/2012/11/what-is-the-true-measure-of-a-storm/)

[2] [WaPo](https://www.washingtonpost.com/nation/2021/08/31/how-ida-katrina-compare-wind-fingerprints)

[3] Powell, Reinhold [Paper](https://www.researchgate.net/publication/252765649_Tropical_Cyclone_Destructive_Potential_by_Integrated_Kinetic_Energy)

[4] [NOAA Python Code](https://unidata.github.io/python-training/workshop/MetPy_Case_Study/metpy-case-study/)
