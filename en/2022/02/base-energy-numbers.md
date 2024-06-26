# Base Energy Numbers, Data

Energy Densities

1 Megajoule is 0.227 Kilowatt hours

1 kg has H2 energy of 33.6 kWh (143 MJ).

H2 under ambient conditions 3 KWh / m3

H2 under ambient conditions 11.9 m3 / kg

Density of liquid ammonia 682 kg/m³ 

At 500 bar, 33 kg H2 /m3.

At 350 bars H2 density is 28 kg/m3.

At 300 bars H2 density is 20 kg/m3.

At 100 bars H2 has energy density is 250 kwh/m3, at ambient temp, see [18].

At 200 bars H2 has energy density is 500 kwh/m3, ditto.

At 250 bars H2 has energy density is 700 kwh/m3, ditto.

At 300 bars H2 has energy density is 750 kwh/m3, ditto.

Crude oil 10.215 kwh / kg

Ammonia 6.25 kwh / kg

Ammonia 22.5 MJ / kg

Ammonia 15.6 MJ / L

Petroleum 34.2 MJ/L

LNG 22.2 MJ/L

Density of light crude oil 875.7 kg/m3

Liquid hydrogen has a an energy density of 2216 kwh/m3

Liquid hydrogen has a weight density of 71 kg/m³.

Gasoline has a density of 32 MJ/L.

Natural gas has 10.55 kWh per cubic meters

Natural gas 5800 cubic feet for one BOE.

Natural gas 170 cubic metres for one BOE.

1 barrel of crude oil carries approximately 1700 kwh of energy.

As standard the 1 barrel (119 liter) of crude oil produce approximately
159 liters of gasoline / petrol.

8 kWh of heat can be generated from 1 kg of coal

H2 pipelines can carry 7 GW for 36 inch and 13 GW for 48-inch pipelines.

<a name='lithium'></a>

Lithium

There is >60kg of lithium carbonate in a 70kWh battery. 400 liters of
water is used per kilo of lithium [7]. Water is a problem bcz while
lithium rich water is pumped, potable water resources also shift.

The entire world reserve for lithium is estimated to be ~17 million
tonnes.

According to [EIA](https://en.wikipedia.org/wiki/World_energy_consumption),
estimated world energy consumption was 157,481 Terrawatt Hours in 2013, 
meaning 431 TWh/day. If we were to store today's energy consumption one
day in batteries,

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


Grid and Pipelines

Pipelines can transmit 10 times the energy at one-eighth the costs
associated with electricity transmission lines [8]. 

Gasoline

1 gallon is 2.56 kg. In Europe the gasoline price is about 9 dollar
per gallon, or 3.51 dollar / kg.

H2

Green ammonia production efficiency is over 74% [12]. "Crackers" that
generate H2 from ammonia are about 76% efficient [6].

Personal Consumption

10 KW / person, based on first world standards.

Typical energy requirements of household items

Single burner electric stove: 1500 Watts
TV: 80-400 Watts
Fridge: 100-250 watts

Electric heating / stove is 33% efficient [10]

HFC Cars

A Nexo tank carries 210 kWh of energy. The car can travel 756 km on a
full tank [3], the tank capacity is 6.33 kg. There are actually three
tanks, each at 10,000 psi [4].

For the Toyota Mirai, the energy capacity of the fuel-cell vehicle's 5
kilograms of hydrogen, compressed at 10,000 psi, is more than 150
kilowatt-hours [5]. Max range 500 km, 1848 weight, 

```python
F = 1.848*200
w = (F*500*1000) / 3600.
print ( w / (150*1000) )
```

```text
0.342
```

Solar panels

Sun energy falling on Earth on average (accounting for day/night seasons)
at its highest point 

300 W/m2

Solar panel efficiency is 20%

Electrolysis

Current best processes for water electrolysis (PEM or alkaline
electrolysis) have an effective electrical efficiency of 70–80%,
producing 1 kg of hydrogen requires 50–55 kW⋅h of electricity
[1]. 


Storage in Pipelines

H2 pipelines can transmit energy efficiencly. But even when we are not
pumping in new H2, the pipes themselves would still have gas in them,
so they can be considered a form of storage. The capacity of the
German natural gas network is more than 200,000 GWh, which meets the
requirements for several months. In comparison, the capacity of all
the German pumped storage power plants only amounts to about 40 GWh [13].

Desalination

Energy consumption [2] of seawater desalination has reached as low as 4 kWh/$m^3$,

<a name='arabia'></a>

Dirty Fuels, Oil

How much solar panel space would Saudi Arabia need to produce its
crude output's equiv energy,

Production is 9.01 million barrels / day (Nov 2020).

1 Barrel of oil is 136 kg. 1 barrel is 0.16 m3. Energy density of
crude oil 10.2 Kwh/kg. 1 million barrels of oil can produce half a
million barrels of gasoline. Gasoline energy density is 12.88 kwh/kg.

Largest oil fields (nummbers in thousands)

```
'West Qurna Field, Iraq',465
'Rumaila Field',1500
'Romashkino Field, Russia',1500
'Marun Field Iran',100
'Samotlor Field, Russia',300
'Kashagan Field, Kazakhstan',380
'Aghajari Field, Iran',200
'Safaniya Oil Field, Kuwait / Saudi Arabia',100
'Upper Zakum Oil Field, UAE',1000
'Ahvaz Field, Iran',750
'Burgan Field, Kuwait',1680
```

Sun energy falling on Earth 1 kW/m2, 24 KWh/m2 in a day.

Panel efficiency 20%, sunlight availability 50% (highest for SA)

```python
solar_kwh_day_m2 = 24*0.20*0.50
oil_energy_day = 136 * 9.01 * 1e6 * 158.4
area = (oil_energy_day / solar_kwh_day_m2)
print ("area of %0.2f km^2" % (area / 1e6))
print ("square with one side %0.2f km" % (np.sqrt(area) / 1000.0))
```

```text
area of 80873.76 km^2
square with one side 284.38 km
```

An area 290 km x 290 km. of panels. SA Rub' al Khali desert is 650,000
km^2, 1/7th of that is needed approximately.

Carbon

A tree can absorb 25kg of CO2 per year. When burned that carbon is
released into the air.

1011 g / kwh emitted from coal [21].

400 g / kwh emitted from natgas.


Transport

Europe imported 380 million cubic meters per day of gas by pipeline from Russia in 2021

Largest ammonia ship 87,000 m3 [14]

Largest liquid H2 ship 1,250 m3 capacity carries gas cooled to -253°C 

837 crude oil tankers arrived at Japanese ports during the fiscal year 2010 [15]

In 2010 Japan's imported 3.75 million barrels of crude oil a day

An LR1 [long range] tanker can carry about 400,000 barrels of light
sweet crude oil.

A large LNG tanker can hold 266,000 cubic meters of LNG.

CSP

[Link](https://www.utilitydive.com/news/cheapest-is-not-always-best-concentrated-solar-power-could-beat-lower-pric/574154/)

Initial investment cost cost 5200/kw. Advanced nuclear reactors are
estimated to cost 5,366 ollar for every kilowatt of capacity. They are
same but nuke plants have LCOE 0.096 dollar/kWh.


References

[1] https://en.wikipedia.org/wiki/Electrolysis_of_water

[2] [WP - Desalination](https://en.wikipedia.org/wiki/Desalination#Energy_consumption)

[3] https://h2.live/en/wasserstoffautos/hyundai-nexo

[4] [extremetech](https://www.extremetech.com/extreme/280219-2019-hyundai-nexo-review-380-miles-on-hydrogen-can-your-ev-go-that-far)

[5] [Business Insider](https://www.businessinsider.com/this-toyota-fuel-cell-car-can-power-your-house-2014-11)

[6] [Ammonia Energy Association](https://www.ammoniaenergy.org/articles/round-trip-efficiency-of-ammonia-as-a-renewable-energy-transportation-media)

[7] [Danwatch](https://danwatch.dk/en/undersoegelse/how-much-water-is-used-to-make-the-worlds-batteries/)

[8] [Hydrogen Insights](https://hydrogencouncil.com/wp-content/uploads/2021/02/Hydrogen-Insights-2021-Report.pdf)

[9] [Energy Central](https://energycentral.com/c/ec/grid-efficiency-opportunity-reduce-emissions)

[10] [Howstwuffworks](https://home.howstuffworks.com/gas-vs-electric-stoves.htm)

[11] [2020 _European Hydrogen Backbone Report](https://gasforclimate2050.eu/wp-content/uploads/2020/07/2020_European-Hydrogen-Backbone_Report.pdf)

[12] [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0306261919318227)

[13] [Underground and pipeline hydrogen storage](https://www.researchgate.net/publication/301254520_Underground_and_pipeline_hydrogen_storage)

[14] https://www.maritime-executive.com/article/phoenix-tankers-orders-largest-gas-carrier-for-lpg-and-ammonia

[15] https://iea.blob.core.windows.net/assets/00cf6755-2976-4cd8-be5d-1c27b13d7df3/2013_OSS_Japan.pdf

[16] https://www.eia.gov/todayinenergy/detail.php?id=17991

[17] https://www.h2-view.com/story/worlds-first-liquid-hydrogen-carrier-on-route-to-japan/

[18] [Link](https://www.researchgate.net/publication/228651542_UUV_FCEPS_technology_assessment_and_design_process)

[19] https://stacker.com/stories/3860/largest-oil-fields-world

[20] https://www.eia.gov/todayinenergy/detail.php?id=17991

[21] https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
