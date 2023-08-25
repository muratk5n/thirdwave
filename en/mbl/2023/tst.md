# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```





```python
u.boxofficemojo("Blue Beetle")
```

```text
Out[1]: 
{'Domestic Opening': '$25,400,000',
 'Domestic': '$25,400,000',
 'International': '$18,000,000',
 'Worldwide Total': '$43,400,000',
 'Release Date': 'August 16, 2023'}
```
















```python
geo = [['Main'],['Urozhaine','Staromaiorske'], ['Robotyne'],
       ['Orikhovo-Vasylivka','Blahodatne'],['Vuhledar'], ['Lyman Pershyi'],
       ['Kreminna','Lyman'],['Kyslivka','Tabaivka'],['Zolotarivka','Spirne']]
       
u.sm_plot_ukr4('ukrdata/fl-0822.csv','ukrdata/fl-0814.csv',geo,3,3,zoom=0.03,fsize=(10,10),)
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
2022-08-10  15.449787
2022-08-11  15.449593
2022-08-14  15.443127
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




