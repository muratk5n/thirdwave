# Energy Production Costs, LCOH, LCOE

### Terminology

Levelized Cost of Energy (LCOE)

LCOE measures lifetime costs divided by energy production. Calculates
present value of the total cost of building and operating a power
plant over an assumed lifetime. Allows the comparison of different
technologies (e.g., wind, solar, natural gas) of unequal life spans,
project size, different capital cost, risk, return, and capacities
([DOE](https://www.energy.gov/sites/prod/files/2015/08/f25/LCOE.pdf)).

Levelized Cost of Hydrogen (LCOH)

Similar to LCOE but for pure hydrogen generation. There are multiple
routes to H2 other than electrolysis (using electricity) a cost
calculation of the final product for each source can be useful.

Simple LCOE Concept

![](costs-lcoe-01.png)

Calculating and comparing LCOE can: Measure value across the longer
term, showing projected life-cycle costs.. Highlight opportunities for
investors to develop different scales of projects (facility,
community, or commercial).. Inform decisions to pursue projects on an
economic basis, compared to utility rates.

CAPEX / Overnight cost

Overnight cost is the cost of a construction project if no interest
was incurred during construction, as if the project was completed
"overnight". The overnight cost is a part of the capital cost. It
includes construction, system cost, procurement cost, engineering
cost, cost of equipment, frst fuel load, and other costs. For quick
comparisons, firms will look at what the cost of building a plant
overnight would be or the overnight cost of capital. This is a
hypothetical scenario because a plant cannot be constructed in one
night, but it evaluates the cost of a plant if it were built right
away, with current prices.

Some Data Points

* Avi Shultz (DOE) on CSP: "Our benchmark is based on a plant of
approximately 100 MW with 14 hours of thermal energy storage. We model
that plant would have an LCOE of 9.5 cents/kWh (with no incentives) if
built in the US today"

* Conversion Factors, H2 has 0.143 GJ/kg

### Storage

LCOH

|Source             |LCOH ($/GJ) |Reference| 
|-------------------|------------|----------|
|H2 Undergr. Salt   | 1.46       |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |
|H2 Undergr. LRC    | 2.51       |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |
|H2 Undergr. Pipes  | 15.17      |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |

Capex and LCOE

|Source               | Capex ($/KW)       |LCOE ($/MWh)|Reference| 
|---------------------|--------------------|------------|----------|
|H2 Undergr. Salt     | 35                 |            |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |
|H2 Undergr. LRC      | 51                 |            |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |
|H2 Undergr. Pipes    | 386                |            |[Paper](https://www.hydrogen.energy.gov/pdfs/review19/st001_ahluwalia_2019_o.pdf) |

### Production

LCOH

|Source             |LCOH ($/GJ) |Reference| 
|-------------------|------------|----------|
|Natgas, CCS        | 13.98      |[Paper](https://www.linkedin.com/pulse/what-levelized-cost-clean-hydrogen-production-greg-perkins/)  |
|Nuclear HTGR       | 17.55      |[Book](https://books.google.com.tr/books?id=BpZ7DwAAQBAJ)  |
|Coal IGCC, CCS     | 21.25      |[IEAGHG](https://ieaghg.org/docs/General_Docs/Reports/2014-03.pdf)  |
|PV                 | 26.00      |[Paper](https://www.cell.com/cell-reports-physical-science/pdfExtended/S2666-3864(20)30224-1)  |
|CSP Therm + Ceria  | 42.08      |[Paper](https://www.mdpi.com/1996-1073/12/3/352/pdf-vor)  |


Capex and LCOE

|Source               | Capex ($/KW)       |LCOE ($/MWh)|Reference| 
|---------------------|--------------------|------------|----------|
|Natgas Plant >200MW  | 500                |            |[Paper](https://www.sciencedirect.com/topics/engineering/natural-gas-combined-cycle) |
|Natgas Plant Typical | 1044               |            |[Statista](https://www.statista.com/statistics/243707/capital-costs-of-a-typical-us-combined-cycle-power-plant/#:~:text=The%20capital%20expenditure%20of%20a,dollars%20per%20kilowatt%20by%202050.)  |
|PV Solar             | 1327               | 32.78      |[EIA](https://www.eia.gov/outlooks/aeo/assumptions/pdf/table_8.2.pdf),[IEA](https://www.iea.org/reports/projected-costs-of-generating-electricity-2020)
|Gasoline             |                    | 34.11      |[Link](https://voltaoil.com/what-makes-up-retail-price-for-gasoline)
|LOHC                 | 0.02               | 46.24      |[Paper](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5c551f4c2&appId=PPGMS) |
|Natgas CLC           | 1652               | 55.0       |[Paper](https://www.sciencedirect.com/science/article/pii/S175058361730693X),[Paper](https://www.researchgate.net/publication/326160300_Techno-Economic_Analysis_of_a_Carbon_Capture_Chemical_Looping_Combustion_Power_Plant)  |
|Wind, Onshore        | 1718               | 50.0       |[IEA](https://www.iea.org/reports/projected-costs-of-generating-electricity-2020)
|Nuclear              | 7030               | 53.4       |[Paper](https://link.springer.com/content/pdf/10.1007/s11356-021-18129-3.pdf/)|
|Wind, Offshore       | 4833               | 88.0       |[EIA](https://www.eia.gov/outlooks/aeo/assumptions/pdf/table_8.2.pdf),[IEA](https://www.iea.org/reports/projected-costs-of-generating-electricity-2020)
|Biomass              | 4524               | 89.0       |[EIA](https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf)|
|Coal Wout CCS        | 4074               | 68.64      |[EIA](https://www.eia.gov/outlooks/aeo/assumptions/pdf/table_8.2.pdf)|
|CSP (100 MW)         | 7895               | 95.0       |[EIA](https://www.eia.gov/outlooks/aeo/assumptions/pdf/table_8.2.pdf),DOE (see above)|
|Natgas + CCS         |                    | 112.0      |[EIA](https://www.eia.gov/outlooks/aeo/assumptions/pdf/table_8.2.pdf),[IEA](https://www.iea.org/reports/projected-costs-of-generating-electricity-2020)
|Batteries            |                    | 121.84     | [EIA](https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf)  |
|Coal Comb CCS        |                    | 122.7      |[IEAGHG](https://ieaghg.org/docs/General_Docs/Reports/2014-03.pdf)|
|Coal IGCC CCS        | 3819               | 151.8      |[Doc](https://atb-archive.nrel.gov/electricity/2017/index.html?t=cc&s=cx),[IEAGHG](https://ieaghg.org/docs/General_Docs/Reports/2014-03.pdf)|


