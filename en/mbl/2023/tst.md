# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```






Next up:
--
Main
Makarivka
Novomaiorske
Marinka
Lobkove
Orikhiv, Robotyne, Malaya Tokmachka
Krasnohorivka
Kreminna






```python
geo = [["Main"],["Makarivka"],
       ["Novomaiorske"],["Marinka"]]

u.sm_plot_ukr4('ukrdata/fl-0613.csv','ukrdata/fl-0521.csv',geo,2,2,zoom=0.03)
plt.savefig('/tmp/out.jpg',quality=40)
```












```python
geo = [['Main'],['Orikhiv','Malaya Tokmachka','Robotyne'],['Zaporizhzhya NPP'],
       ['Avdiivka'],['Vuhledar','Velyka Novosilka'],['Khromove','Bakhmut'],
       ['Kherson'],['Blahodatne'],['Lobkove']]
u.sm_plot_ukr4('ukrdata/fl-0613.csv','ukrdata/fl-0521.csv',geo,3,3,zoom=0.03)
plt.savefig('/tmp/out.jpg',quality=40)
```



















```python
clat=48.59;clon=37.96
u.sm_plot_ukr1('ukrdata/fl-0521.csv','ukrdata/fl-0516.csv',["West Bakhmut Sports Complex","Bakhmut Children's Hospital","West Bakhmut Residential Area","Bakhmut"],clat,clon,zoom=0.005)
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




