# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```


```python
u.ecmwf_wind(30,-60,10,M=100,N=60,show_ike=True)
plt.savefig('/tmp/out.jpg',quality=20)
```












```python
geo = [['Main'],['Andriivka','Klischchiivka'],['Bilohorivka','Verkhnokamianske'],
       [],['Bakhmut','Yahidne','Berkhivka'],['Novomykhailivka','Stepne','Marinka'],
       ['Synkivka','Kupiansk','Lyman Pershyi'],['Urozhaine','Staromaiorske'],['Robotyne']]
       
u.sm_plot_ukr4('ukrdata/fl-0913.csv','ukrdata/fl-0830.csv',geo,3,3,zoom=0.03,fsize=(10,10),)
plt.savefig('/tmp/out.jpg',quality=40)
```








```python
h = u.ru_areas()

a1 = h.loc[(h.index.month == 6) & (h.index.day == 9)]
a2 = h.tail(1)
print ('a1 =',int(a1.area),'km2','a2 =',int(a2.area),'km2')
print (int(a1.area) - int(a2.area), 'km taken')
```

```text
a1 = 154618 km2 a2 = 154342 km2
276 km taken
```












```python
u.ru_areas().plot(ylim=[15,16])
plt.savefig('/tmp/out.jpg',quality=40)
```


```python
h = u.ru_areas().tail(20) * 10000

a1, a2 = int(h.iloc[0]), int(h.iloc[-1])

print ('a1 =',a1,'km2','a2 =',a2,'km2')
print (a1-a2, 'km2 taken')
```

```text
a1 = 154536 km2 a2 = 154401 km2
135 km2 taken
```
























































```python
df = u.biden_approval()['net']
print (df.tail(4))
df.plot()
plt.savefig('/tmp/out.jpg')
```

```text
end_date
2023-08-26   -11.839894
2023-08-27   -11.170984
2023-08-28   -11.273347
2023-08-29   -12.649756
Name: net, dtype: float64
```




