# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```






['Makarivka']
['Orikhiv']
['Marinka']
['Yahidne']
['Orikhovo-Vasylivka']
['Kreminna']





```python
geo = [['Main'],['Spirne', 'Berestove'], ['Orikhiv'],
       ['Lobkove'],['Makarivka'], ['Vuhledar', 'Velyka Novosilka'],
       ['Marinka'],['Avdiivka', 'Opytne'],['Bakhmut', 'Chasiv Yar']]
u.sm_plot_ukr4('ukrdata/fl-0703.csv','ukrdata/fl-0621.csv',geo,3,3,zoom=0.03,fsize=(12,12),)
plt.savefig('/tmp/out.jpg',quality=40)
```
































































```python
df = u.biden_approval()['net']
print (df.tail(4))
df.plot()
plt.savefig('/tmp/out.jpg')
```

```text
modeldate
2023-06-06   -13.580007
2023-06-07   -13.815057
2023-06-08   -13.862946
2023-06-09   -13.822625
Name: net, dtype: float64
```




