# Energy Needed for Heating

We can use the heat conduction formula due to Fourier,

$$
P = \frac{dQ}{dT} = \frac{k A (T_2 - T_1)}{d}
$$

Formula will calculate the power of the heat transfer between two
temperatures, for our needs from an ideal inside to a known
outside. Therefore to keep the inside at that temp level, we'll know
how much power we have to add in the inside (with a heating unit).

Formula needs surface size $A$, the surface through which heat flows
(or leaks), which will be all four walls roof and floors. Material
heat conductivity $k$, wall thickness $d$, a target temperature $T_2$,
and outside temperature $T_1$.

Target temperature is room temperature 22 degrees C.

Outside temperature can be annual world average temperature (the one
that keeps rising, and everyone is freaked out about), 13.7 deg C. We
can assume it's always at that level outside for everyone all the
time, and people want room temperature on the inside. What was that
movie line? "It's chilly outside, and it's Chilly inside". We just
want chilly outside.

Home sizes differ from country to country, as average we'll take
Denmark, 150 m2. Multiply by 4 meter height, get home volume. Assume a
cube for volume, so we w/ cube root calc one side, then using sides
side^2 x 6 gives a complete outside surface area.

Material heat conductivity? Units $W/m \cdot C$, or $J/s \cdot m \cdot C$.
We have concrete brick 0.84, plasterboard 0.16, wood 0.10. I dont know..
what would average material be? Better than mere bricks, but little worse
than wood? Let's take 0.15.

We'll further assume 4.2 people per home (I looked this up), a 2013
world population of 7.17 billion (I am trying to reach an annual
energy needed for heating, worldwide), so


```python
ppl_per_home = 4.2
pop = 7.17*1e9 # world 2013
world_t =  13.7 # C
room_temp = 22
home_vol = 150*4 # m3
d = 11 # cm, wall width
k = 0.15 # W/m*C = J/s*m*C

side = np.power(home_vol,1/3.)
A = (side**2)*6

P = k*(room_temp-world_t)*A / (d*0.01)

total = (pop/ppl_per_home)*P*24*365
print ('home heating %d twh' % (total / 1e12))
```

```text
home heating 72244 twh
```

The entire world energy consumption for that year was 157,481
Terrawatt Hours. The number above is a good chunk of that.

