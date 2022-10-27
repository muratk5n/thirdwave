
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
u.gov_fa_538()
```

```text
Out[1]: 
(['Ron DeSantis', '10/24/22', 'U. North Florida', 55.0],
 ['Charlie Crist', '10/24/22', 'U. North Florida', 41.0])
```















```python
import pandas as pd
f = '/home/burak/Downloads/fatal-police-shootings-data.csv'
df = pd.read_csv(f)
df['year'] = pd.to_datetime(df['date']).dt.year
```

```python
pd.set_option('display.max_columns', None)
#g = df.groupby('year').size().plot(kind='bar')
#g = df.groupby(['year','race']).size().plot.bar(stacked=True)
g = df.groupby(['year','race']).size().reset_index()
g1 = g.pivot_table('race')
print (g)
#plt.savefig('/tmp/out.png')
```

```text
    year race    0
0   2015    A   15
1   2015    B  258
2   2015    H  173
3   2015    N    9
4   2015    O   14
5   2015    W  502
6   2016    A   15
7   2016    B  236
8   2016    H  161
9   2016    N   17
10  2016    O   11
11  2016    W  465
12  2017    A   16
13  2017    B  223
14  2017    H  180
15  2017    N   22
16  2017    O    5
17  2017    W  458
18  2018    A   21
19  2018    B  228
20  2018    H  169
21  2018    N   16
22  2018    O    4
23  2018    W  460
24  2019    A   20
25  2019    B  251
26  2019    H  168
27  2019    N   13
28  2019    O    9
29  2019    W  424
30  2020    A   15
31  2020    B  243
32  2020    H  171
33  2020    N    9
34  2020    O    3
35  2020    W  459
36  2021    A    4
37  2021    B  182
38  2021    H   83
39  2021    N    8
40  2021    W  305
41  2022    A    7
42  2022    B   74
43  2022    H   30
44  2022    N    6
45  2022    W  131
```


```python
df1 = df[(df.race != 'W') & (df.armed == 'unarmed')]
df1.groupby('year').size().plot()
df2 = df[(df.race == 'W') & (df.armed == 'unarmed')]
df2.groupby('year').size().plot()
plt.legend(['Non-white','White'])
plt.savefig('unarmed.png')
```

