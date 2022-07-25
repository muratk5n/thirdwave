# Enerji İstatistikleri


def get_bp_country(country):
    fin = '../../2019/05/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
    df = pd.read_csv(fin)
    df = df[df.Country == country]
    df = df.set_index('Year')
    df = df[df.index > 1980]
    
    df = df[['wind_twh','solar_twh','oilprod_kbd','nuclear_twh','hydro_twh',\
             'gasprod_ej','coalprod_ej','coalcons_ej','gascons_ej','oilcons_ej']]

    df['oil_twh'] = df.oilprod_kbd * 365 * 1700 * 1000 / 1e9
    df['coal_twh'] = df.coalprod_ej * 277.778
    df['gasprod_twh'] = df.gasprod_ej * 277.778
    df['oil_imp_twh'] = (df.oilcons_ej * 277.778) - df.oil_twh.fillna(0)
    df['gas_imp_twh'] = (df.gascons_ej * 277.778) - df.gasprod_twh.fillna(0)
    df['coal_imp_twh'] = (df.coalcons_ej * 277.778) - df.coal_twh.fillna(0)
    cols = [x for x in df.columns if '_twh' in x]
    df = df[cols].fillna(0)
    df2 = df[cols].tail(1).unstack()
    df2 = (df2 / df2.sum())*100.0
    df2 = df2.dropna()
    return df2



```python
import pandas as pd
pd.set_option('display.max_columns', None)
fin = '../../../en/2019/05/bp-stats-review-2022-consolidated-dataset-panel-format.csv'
df = pd.read_csv(fin)
df = df[df.Country == 'Turkey']
df = df.set_index('Year')
df = df[df.index > 1980]
df = df[['wind_twh','solar_twh','oilprod_kbd','nuclear_twh','hydro_twh',\
         'gasprod_ej','coalprod_ej','coalcons_ej','gascons_ej','oilcons_ej']]

df['oil_twh'] = df.oilprod_kbd * 365 * 1700 * 1000 / 1e9
df['coal_twh'] = df.coalprod_ej * 277.778
df['gasprod_twh'] = df.gasprod_ej * 277.778
df['oil_imp_twh'] = (df.oilcons_ej * 277.778) - df.oil_twh.fillna(0)
df['gas_imp_twh'] = (df.gascons_ej * 277.778) - df.gasprod_twh.fillna(0)
df['coal_imp_twh'] = (df.coalcons_ej * 277.778) - df.coal_twh.fillna(0)
cols = [x for x in df.columns if '_twh' in x]
df = df[cols].fillna(0)
df[cols].plot()
plt.savefig('energy-sources.png')
print (df[cols].tail(3))
```

```text
       wind_twh  solar_twh  nuclear_twh  hydro_twh  oil_twh    coal_twh  \
Year                                                                      
2019  21.730700   9.249800          0.0  88.822800      0.0  201.773096   
2020  24.828200  10.950200          0.0  78.094300      0.0  182.830358   
2021  31.137427  12.833868          0.0  55.695232      0.0  208.643868   

      gasprod_twh  oil_imp_twh  gas_imp_twh  coal_imp_twh  
Year                                                       
2019          0.0   558.265075   433.613797    285.753747  
2020          0.0   511.008829   462.099445    289.536787  
2021          0.0   524.657636   573.235049    275.431126  
```

![](energy-sources.png)


Çeşitlere göre önceki senenin enerji verileri. `_cons` değişkenleri
sadece tüketimi gösterir, o birimler ülkede üretilmemekte,`gas_prod`,
`oil_prod` sıfır seviyesinde.

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
wind_twh      2021     1.851617
solar_twh     2021     0.763178
nuclear_twh   2021     0.000000
hydro_twh     2021     3.311971
oil_twh       2021     0.000000
coal_twh      2021    12.407209
gasprod_twh   2021     0.000000
oil_imp_twh   2021    31.199272
gas_imp_twh   2021    34.087975
coal_imp_twh  2021    16.378778
dtype: float64
```

![](source-pie.png)



