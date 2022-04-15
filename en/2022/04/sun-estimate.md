# Sun's Mass and Density 

We are attempting to calculate Sun's mass using few assumptions, ie
only orbital information - the mass that can cause the orbit we
observe today. Using the Earth’s orbit [1] and the law of centripetal
force, we get that the Sun must be gravitationally pulling on the
Earth with a force of $F=mr(\frac{2\pi}{T})^2$ where m is the mass of
the Earth, $r$ the radius of the Earth’s orbit and T the time it takes
the Earth to go around the Sun.

On the other hand, Newton’s law of gravitation states that

$$
F = G \frac{m M}{r^2}
$$

$G$ is the gravitational constant [experimentaly calculated by
Cavendish], $M$ is the Sun’s mass. Equate both,

$$
mr ( \frac{2\pi}{T} )^2 = G \frac{m M}{r^2}
$$

Simplify,

$$
M = \frac{r^3}{G} ( \frac{2\pi}{T} )^2
$$

It turns out we won't have to know Earth's mass it just got canceled
out of the equation.

Filling in the right side $r=1.496 \cdot 10^{11} m$,
$G=6.674⋅10^{−11} m^3 kg^{−1}s^{−2}$, $T=365.2425×24×3600=3.156 \cdot 10^7 s$
gives

$1.988 \cdot 10^{30} kg$ for the mass of the Sun. Verify,

```python
r = 1.496*1e11
G = 6.674*1e-11
T = 365.2425*24*3600 # seconds
M = (r**3 / G)*(2*np.pi / T)**2
print (M)
```

```text
1.9887409506724918e+30
```

Get Sun's volume, divide the mass with it,


```python
sm = 1.988*1e30*1e3 # gram
svol = 1409272569059860000 * 1e15 # cm3
print ("Sun's density is", sm/svol, 'g/cm3')
```

```text
Sun's density is 1.410656847827681 g/cm3
```

References

[1] https://www.quora.com/How-can-I-calculate-the-mass-of-the-sun



