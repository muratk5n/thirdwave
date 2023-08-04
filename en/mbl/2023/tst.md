# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```








```python
geo = [['Main'],['Staromaiorske','Makarivka'], ['Klischchiivka','Opytne','Bakhmut'],
       [''],['Novovodiane'], ['Robotyne'],
       ['Lobkove'],['Bakhmut'],['Bakhmut']]
       
u.sm_plot_ukr4('ukrdata/fl-0803.csv','ukrdata/fl-0729.csv',geo,3,3,zoom=0.03,fsize=(10,10),)
plt.savefig('/tmp/out.jpg',quality=40)
```














```python
u.ru_areas().plot(ylim=[15,16])
plt.savefig('/tmp/out.jpg',quality=40)
```


```python
u.ru_areas().tail(3)
```

```text
Out[1]: 
                 area
dt                   
2022-07-27  15.450287
2022-07-29  15.447815
2022-08-03  15.445465
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




