# World Trade, Import/Exports

BACI dataset [1] provides data on bilateral trade flows for 200
countries at the product level (5000 products). Used the
BACI_HS17_V202201.zip file, processed it for 2019 using code below. As
each country-dyad-product is processed line by line, the code creates
a relation matrix, if there is trade between country `i` and `j` its
value is added in `A[i,j]` for each product. First analysis simply
sums all product trades at bilateral level, to create a trade flow
number between two countries. To keep visualization simple, exports
and imports are added to each other.

With the final relation matrix, first simple counts,

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

Naturally all country pairs do not trade; out of approx 400K relations
we have 16K relations.

```python
mean,std = np.mean(vals),np.std(vals)
print (np.round(mean/1e6,2),np.round(std/1e6,2))
```

```text
1.08 10.79
```

Which trade links are above, below average,

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

Trade is highly skewed; many countries trade below average, few are
above average. Some, a massive 4 sigmas away from average comprise the
trading countries we hear about eveyday, US, China, Germany, etc. An
interactive map of the extraordinary flows is below.

[Output](trade-out.html)

[Code](baci.py)

Reference

[1] [BACI](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37), International Trade Database at the Product-Level.

