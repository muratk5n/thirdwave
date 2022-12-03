# The Gaseous Sun

The claim is the Sun is gasous plasma. There are many signs that this
claim is false.

If the Sun is not gaseous, it cannot collapse itself and black holes
cannot form. James Jeans, who along with Arthur Eddington is a founder
of British cosmology said: "Mathematical analysis shows that if the
centre of a star is either liquid, or partially so, there is no danger
of collapse; the liquid center provides so firm a basis for the star,
as to render the collapse impossible".

### Planck Spectrum

When we plot white light intensity against each frequency we get a
Planck spectrum. But gaseous plasmas are known to never be able to
produce a Planck spectrum. As stated by this [2] paper, "the gaseous
models fail to properly account for the occurrence of the solar
spectrum.  Gases are unable to emit a continuous spectrum. Rather,
they emit in bands (see [21,70] and references therein). Even when
pressure broadened, these bands cannot produce the black- body
lineshape. Moreover, when gases are heated, their emis- sivity can
actually drop [21,70], in direct contradiction of Ste- fan’s law
[18]. Under these circumstances, the answer cannot be found in the
gaseous state. One must turn to condensed matter"

### Sun Mass and Density

We can attempt to calculate Sun's mass using few assumptions, ie only
orbital information - the mass that can cause the orbit we observe
today. Using the Earth’s orbit [1] and the law of centripetal force,
we get that the Sun must be gravitationally pulling on the Earth with
a force of $F=mr(\frac{2\pi}{T})^2$ where m is the mass of the Earth,
$r$ the radius of the Earth’s orbit and T the time it takes the Earth
to go around the Sun.

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

[2] Robitaille, Fourty Lines of EVidence for Condensed Matter

[[Up](../../2018/09/junk-science.html)]

