# Enerji İstatistikleri

```python
import pandas as pd
pd.set_option('display.max_columns', None)
fin = '../../../en/2019/05/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
df = pd.read_csv(fin)
df = df[df.Country == 'Turkey']
df = df.set_index('Year')
df = df[df.index > 1980]
df = df[['wind_twh','solar_twh','oilprod_kbd','nuclear_twh','hydro_twh','gasprod_ej','coalprod_ej']]
df['oil_twh'] = df.oilprod_kbd * 365 * 1700 * 1000 / 1e9
df['coal_twh'] = df.coalprod_ej * 277.778 
df['gas_twh'] = df.gasprod_ej * 277.778
cols = [x for x in df.columns if '_twh' in x]
df = df[cols]
df[cols].plot()
plt.savefig('energy-sources.png')
print (df[cols].tail(3))
```

```text
       wind_twh  solar_twh  nuclear_twh  hydro_twh  oil_twh    coal_twh  \
Year                                                                      
2019  21.730700   9.249800          NaN  88.822800      NaN  201.773096   
2020  24.828200  10.950200          NaN  78.094300      NaN  182.830358   
2021  31.137427  12.833868          NaN  55.695232      NaN  208.643868   

      gas_twh  
Year           
2019      NaN  
2020      NaN  
2021      NaN  
```

![](energy-sources.png)

```python
df2 = df[cols].tail(1).unstack()
df2 = (df2 / df2.sum())*100.0
df2 = df2.dropna()
df2.plot(kind="pie")
plt.savefig('source-pie.png')
df2
```

```text
Out[1]: 
           Year
wind_twh   2021    10.099376
solar_twh  2021     4.162645
hydro_twh  2021    18.064662
coal_twh   2021    67.673316
dtype: float64
```

![](source-pie.png)



