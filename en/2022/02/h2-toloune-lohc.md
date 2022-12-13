# LOHC

The LOHC (liquid organic hydrogen carrier) concept is a capable
technology [1] for supplying hydrogen refuelling stations due to its
high hydrogen storage densities (57 $kg_{H2} m_{LOHC}^{-3}$) and easy
handling (liquid, low toxicity, low flammability). ...

The LOHC technology is based on the chemical bonding of hydrogen to
liquid organic carriers, which are mostly aromatic hydrocarbons or
heterocyclic substances. ...

In contrast to some other chemical hydrogen storage processes, these
reactions are reversible. The carrier molecule is cycled between a
loaded and unloaded state.  ... The most technically advanced concept,
which is pursued by Hydrogenious Technologies, is based on the use of
the common heat transfer oil dibenzyltoluene, which is available in
large quantities and is not classified as a dangerous good.

Compared to other technologies that store hydrogen at temperatures of
-253 °C or at pressures up to 500 bar, using LOHC technology greatly
reduces the cost of handling hydrogen. 

The hydrogen-rich or loaded LOHC (LOHC+) can be transported via
standard tank trucks to the hydrogen refueling stations, which are
equipped with a dehydrogenation system. There, the hydrogen can be
produced as needed and then integrated into the existing hydrogen
refueling station technology. The German Climate Action Plan of 2050
acknowledges that LOHC technology has considerable potential for
establishing hydrogen as a fuel.

The question of just how hydrogen will get around the world, and what
it will cost, is key to putting in place global hydrogen
infrastructure [3]. A report.. from Rethink Energy, part of Rethink
Technology Research, shows that the bulk of the effort will be split
between pipelines and liquid organic hydrogen carriers (LOHC), often
transported in ships – and points to the limiting cost factors which
shall define each transport use case.

One VLCC ship [3] can carry up to 350,000 DWT which would be
equivalent to 17,000 tons H2.  One train in Europe can pull up to 35
wagons which would be equivalent to 59 tons of H2. A quick calculation
shows the amount of energy that can be carried across Atlantic by a
fleet of 20 ships using LOHC techology,

```python
one_trip = 17000*1000*33.6 / (365*24*1e3)
print ("One trip, single ship %0.1f MW" % (one_trip))
print ("Fleet %0.1f GW" % (one_trip*12*20 / 1e3))
```

```text
One trip, single ship 65.2 MW
Fleet 15.6 GW
```


Reference

[1] [Hydrogenious Presentation - 1](https://www.energiewende-erlangen.de/wp-content/uploads/2018/02/0_HydrogeniousTechnologies.pdf)

[1] [Hydrogenious Presentation - 2](https://arpa-e.energy.gov/sites/default/files/Schneider_HydrogeniousTechnologies_TransportationFuels_Workshop_FINAL.pdf)

[2] [Rethink Energy](https://www.globalhydrogenreview.com/hydrogen/23092022/rethink-energy-pipelines-and-organic-carrier-ships-to-dominate-hydrogen-distribution/)

[3] [Hydrogenious Presentation - 3](https://www.hydrogen.energy.gov/pdfs/07-Schmidt-Liquid%20Organic%20Hydrogen Carriers.pdf)

[[Up]](h2-storage.html)
