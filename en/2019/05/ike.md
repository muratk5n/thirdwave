# Hurricane, Integrated Kinetic Energy

IKE is calculated as

$$
IKE = \int_v \frac{1}{2} \rho U^2 dV
$$

This is the familiar kinetic energy calculation using a flat rectangle of
air. Since numerically 1m height is assumed area calculation is sufficient.
Wind speed comes as $u,v$ components, $u^2+v^2$ will give square speed
for each cell. Multiply by 0.5 and sum all cells, this gives total energy.

Wind speed is retrieved from a NOAA service for a given area, at grid
points. 

Hurricane Katrina

```python
import ike
lat=25;lon=-90
year = 2005;month = 8;day = 30; hour = 10
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
340.975708798976 TJ
```

Hurricane Sandy

```python
import ike
lat=39;lon=-74
year = 2012; month = 10; day = 29; hour = 13
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
213.907591397376 TJ
```

Hurricane Ivan

```python
lat,lon = 30.302, -87.751
year = 2004; month = 9; day = 16; hour = 10
print (ike.ike(lat,lon,day,month,year,hour), 'TJ')
```

```text
175.953368055808 TJ
```

[Code](ike.py)

References

[1] https://www.wired.com/2012/11/what-is-the-true-measure-of-a-storm/

[2] https://www.washingtonpost.com/nation/2021/08/31/how-ida-katrina-compare-wind-fingerprints

[3] https://www.researchgate.net/publication/252765649_Tropical_Cyclone_Destructive_Potential_by_Integrated_Kinetic_Energy

[4] https://unidata.github.io/python-training/workshop/MetPy_Case_Study/metpy-case-study/
