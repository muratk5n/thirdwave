# World Trade, Import/Exports


```python
rows,cols = A.nonzero()
print (len(rows))
print (900*900)
vals = np.array([A[row,col] for row,col in zip(rows,cols)])
```

```text
16752
810000
16752
```

```python
mean,std = np.mean(vals),np.std(vals)
print (np.round(mean/1e6,2),np.round(std/1e6,2))
```

```text
1.08 10.79
```

```python
hv = vals[vals > mean]
print (np.count_nonzero(hv))
hv = vals[vals < mean]
print (np.count_nonzero(hv))
hv = vals[vals > mean+4*std]
print (np.count_nonzero(hv))
```

```text
1413
15339
73
```

