# Conflict Statistics

### UCDP/PRIO Armed Conflict Dataset

[Data](https://ucdp.uu.se/downloads/)

Deaths, Incidences, Globally

```python
import pandas as pd

def overall_deaths(mon):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   g = df[['country','deaths_b']].\
       groupby(['country']).\
       agg({'country':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g.sort_values('deaths',ascending=False)

print (overall_deaths(mon=6).head(20))
```

```text
                     incidents  deaths
country                               
Afghanistan                855    6626
Somalia                     42     435
Nigeria                    101     301
Yemen (North Yemen)         45     100
DR Congo (Zaire)            49      57
Burkina Faso                15      44
Syria                       63      35
India                       28      29
Mali                        10      21
Iraq                        20      20
Niger                       12      18
Myanmar (Burma)             41      15
Philippines                 14      13
Pakistan                    19      11
Ukraine                     10      11
Mozambique                  12      10
Mexico                     318      10
South Sudan                  5      10
Iran                         4       9
Burundi                      9       8
```

Details for Specific Country

```python
def country_attacked(mon, country):
   url = 'https://ucdp.uu.se/downloads/candidateged/GEDEvent_v21_0_%d.csv' % mon
   df = pd.read_csv(url)
   df1 = df[df.country == country]
   g = df1[['country','deaths_b','side_b']].\
       groupby(['side_b','country']).\
       agg({'side_b':'count', 'deaths_b': 'sum'})
   g.columns = ['incidents','deaths']
   return g.sort_values('deaths',ascending=False)

print (country_attacked(6, 'Syria'))
```

```text
                              incidents  deaths
side_b               country                   
Syrian insurgents    Syria           22      27
SDF                  Syria           16       8
Civilians            Syria            8       0
Government of Israel Syria            1       0
Government of Syria  Syria            1       0
IS                   Syria           15       0
```

<a name='gdeltme'/>

### GDELT

Iraq and Syria based conflict stats. GDELT uses natural language
processing ("AI") to extract Actor - Action - Actor triplets. The
result is not curated, there can be mistakes, but as an overall
outlook, it can be useful.

US military bases, Syria, reverse-engineered from [source](https://bit.ly/3gOBQHx),
are also added.

[Codes](http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf)

[Data](http://data.gdeltproject.org/events)

[Script](confstat-me.py)

The output of the code is below

[Output](conflict-out.html)

<a name='gdtroop'/>

### GDELT, Troop Deployments

Filtering on CAMEO code 154 (military deployment), attempting to
extract geoloc from the text itself, and filtering for the word
'troop' in the URL.  No regional filtering, we attempt to find
worldwide deployments, by all countries.

[Script](confstat-milmob.py)

[Output](conflict-milmob.html)

<a name='gdeltblm'/>

### GDELT, BLM

Scanning events of the the last month looking for black deaths due to 
police shootings.

[Script](2019/05/blm.py)

[Output](blm-out.html)

<a name='usgun'/>

### US Gun Violence

Data came from the [Gun Violence Archive](https://www.gunviolencearchive.org/reports),
see data for "mass shootings - all years". Plot is monthly incidents and deaths.


```python
import pandas as pd, zipfile
with zipfile.ZipFile('mass-shooting-us.zip', 'r') as z:
      df =  pd.read_csv(z.open('USmassshooting.csv'))

df['Date'] = df.apply(lambda x: pd.to_datetime(x['Incident Date']), axis=1)
df['DateYM'] = df.apply(lambda x: "%d%02d" % (x['Date'].year, x['Date'].month), axis=1)
g = df.groupby('DateYM').agg({'Incident ID':'count', '# Killed': 'sum'})
g['# Killed (Avg)'] = g['# Killed'].rolling(10).mean()
print (g[['# Killed','# Killed (Avg)']].tail(5))
g.plot()
plt.savefig('gunvio.png')
```

```text
        # Killed  # Killed (Avg)
DateYM                          
202102        44            48.2
202103        67            51.0
202104        55            49.6
202105        79            50.1
202106        58            50.7
```

![](gunvio.png)

