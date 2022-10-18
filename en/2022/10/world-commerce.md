# World Trade, Import/Exports

BACI provides data on bilateral trade flows for 200 countries at the
product level (5000 products) [1]. I took the BACI_HS17_V202201.zip file,
processed it using code below.

[Code](baci.py)

The code creates a relation matrix, if there is trade between country
`i` and `j` its value is in `A[i,j]`.

The first analysis was summing all product trades at bilateral level,
to create a trade flow number between two countries. To keep
visualization simple export/import are added.

```python
import scipy.io as io
A = io.mmread("/tmp/A-final").tolil()
rows,cols = A.nonzero()
print (len(rows))
print (900*900)
vals = np.array([A[row,col] for row,col in zip(rows,cols)])
```

```text
16752
810000
```

Clearly most countries do not trade; out of approx 400K relations we
only have 16K. That number is indicative most countries perhaps
trading with two neighbors, not engaging in air, rail, sea freight
commerce.

```python
mean,std = np.mean(vals),np.std(vals)
print (np.round(mean/1e6,2),np.round(std/1e6,2))
```

```text
1.08 10.79
```

```python
hv = vals[vals < mean]
print (np.count_nonzero(hv))
hv = vals[vals > mean]
print (np.count_nonzero(hv))
hv = vals[vals > mean+4*std]
print (np.count_nonzero(hv))
```

```text
15339
1413
73
```

The numbers above show trade is highly skewed; many countries trade
below average, few are above average. Some, a massive 4 sigmas away
from average comprise the trading countries we hear about eveyday,
US, China, Germany, etc.

The map of these extraordinary flows can be seen below.

[Output]

Reference

[1] [Data](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37)

