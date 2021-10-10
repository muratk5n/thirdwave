# Codebook 2

Polity

http://www.systemicpeace.org/inscrdata.html

http://www.ub.umu.se/sok/tidskrifter/cnts

```python
import pandas as pd
#name = 'SGP'
#name = 'SIN'
#name = 'CHN'
#name = 'VEN'
#name = 'TUR'
#name = 'RUS'
df = pd.read_csv('bdm2s2_nation_year_data_may2002.csv')
df2 = df[(df['worldbankcode']==name) & (df['year'] > 1980)]
def W(df_in):
    df_in['W2'] = 0.
    df_in['W2'] += ((pd.isnull(df_in['RegimeType'])==False) & (df_in['RegimeType'] !=2) & (df_in['RegimeType'] != 3)).astype(int)
    df_in['W2'] += (df_in['xrcomp'] >= 2).astype(int)
    df_in['W2'] += (df_in['xropen'] > 2).astype(int)
    df_in['W2'] += (df_in['parcomp'] == 5).astype(int) # none for TR
    df_in['W2'] = df_in['W2'] / 4.
```

```python
W(df2)
print df2[['worldbankcode','RegimeType','xrcomp','xropen','parcomp','year','W','W2','S']]
```

```
      worldbankcode  RegimeType  xrcomp  xropen  parcomp  year     W    W2  S
10228           RUS           1     NaN     NaN      NaN  1981  0.75  0.25  1
10229           RUS           1     NaN     NaN      NaN  1982  0.75  0.25  1
10230           RUS           1     NaN     NaN      NaN  1983  0.75  0.25  1
10231           RUS           1     NaN     NaN      NaN  1984  0.75  0.25  1
10232           RUS           1     NaN     NaN      NaN  1985  0.75  0.25  1
10233           RUS           1     NaN     NaN      NaN  1986  0.75  0.25  1
10234           RUS           1     NaN     NaN      NaN  1987  0.75  0.25  1
10235           RUS           1     NaN     NaN      NaN  1988  0.75  0.25  1
10236           RUS           1     NaN     NaN      NaN  1989  0.75  0.25  1
10237           RUS           1     NaN     NaN      NaN  1990  0.75  0.25  1
10238           RUS           1     NaN     NaN      NaN  1991  0.75  0.25  1
10239           RUS           1       3       4        3  1992  0.75  0.75  1
10240           RUS           1       3       4        4  1993  0.75  0.75  1
10241           RUS           1       3       4        4  1994  0.75  0.75  1
10242           RUS           1       3       4        4  1995  0.75  0.75  1
10243           RUS           1       3       4        4  1996  0.75  0.75  1
10244           RUS           1       3       4        4  1997  0.75  0.75  1
10245           RUS           1       3       4        4  1998  0.75  0.75  1
10246           RUS           1       3       4        4  1999  0.75  0.75  1
```

```python
df['WS'] = df['W']/(np.log((df['S']+1)*10)/3)
```


```python
df2['S2'] = df2['Legselec'] / 2.
print df2[['year','legselec','S','S2']]
```

```
       year  legselec   S  S2
15018  1981         0   0   0
15019  1982         0   0   0
15020  1983       NaN   1   1
15021  1984       NaN   1   1
15022  1985       NaN   1   1
15023  1986       NaN   1   1
15024  1987       NaN   1   1
15025  1988       NaN   1   1
15026  1989       NaN   1   1
15027  1990       NaN   1   1
15028  1991       NaN   1   1
15029  1992       NaN   1   1
15030  1993       NaN   1   1
15031  1994       NaN   1   1
15032  1995       NaN   1   1
15033  1996       NaN   1   1
15034  1997       NaN   1   1
15035  1998       NaN   1   1
15036  1999       NaN   1   1
15037  2000       NaN NaN NaN
```

```python
pol = pd.read_csv('polity4v2013.csv')
pol['RegimeType'] = 1.
pol2 = pol[(pol['scode']==name) & (pol['year'] > 2000)]
W(pol2)
print pol2[['scode','year','xrcomp','xropen','parcomp','W2']]
```

```
      scode  year  xrcomp  xropen  parcomp    W2
12558   RUS  2001       2       4        4  0.75
12559   RUS  2002       2       4        4  0.75
12560   RUS  2003       2       4        4  0.75
12561   RUS  2004       2       4        4  0.75
12562   RUS  2005       2       4        4  0.75
12563   RUS  2006       2       4        4  0.75
12564   RUS  2007       2       4        4  0.75
12565   RUS  2008       2       4        4  0.75
12566   RUS  2009       2       4        4  0.75
12567   RUS  2010       2       4        4  0.75
12568   RUS  2011       2       4        4  0.75
12569   RUS  2012       2       4        4  0.75
12570   RUS  2013       2       4        4  0.75
```

```python
a = 0.029
print 10*1000 * ((1+a)**10.)
```

```
13309.2550483
```

```python
df = pd.read_csv('bdm2s2_nation_year_data_may2002.csv')
df = df[(df['S'] == 0.5) & (df['year'] > 1950)]
print df[['country','year','xrcomp','xropen','parcomp','W','S']]
```

```
           country  year  xrcomp  xropen  parcomp     W    S
2439     NICARAGUA  1980     -77     -77      -77  0.00  0.5
2440     NICARAGUA  1981       0       0        2  0.00  0.5
2441     NICARAGUA  1982       0       0        2  0.00  0.5
2442     NICARAGUA  1983       0       0        2  0.00  0.5
2884      COLOMBIA  1954       1       4        3  0.25  0.5
2885      COLOMBIA  1955       1       4        3  0.25  0.5
2886      COLOMBIA  1956       1       4        3  0.25  0.5
2887      COLOMBIA  1957       2       4        4  0.50  0.5
3303      SURINAME  1985     NaN     NaN      NaN  0.50  0.5
3304      SURINAME  1986     NaN     NaN      NaN  0.50  0.5
4729       URUGUAY  1973       1       4        1  0.25  0.5
4730       URUGUAY  1974       1       4        1  0.25  0.5
4731       URUGUAY  1975       1       4        1  0.25  0.5
4732       URUGUAY  1976       1       4        1  0.25  0.5
4733       URUGUAY  1977       1       4        1  0.25  0.5
4734       URUGUAY  1978       1       4        1  0.25  0.5
4735       URUGUAY  1979       1       4        1  0.25  0.5
4736       URUGUAY  1980       1       4        1  0.25  0.5
4737       URUGUAY  1981       1       4        1  0.25  0.5
4738       URUGUAY  1982       1       4        1  0.25  0.5
4739       URUGUAY  1983       1       4        1  0.25  0.5
6269         SPAIN  1951       0       0        1  0.25  0.5
6270         SPAIN  1952       0       0        1  0.25  0.5
6271         SPAIN  1953       0       0        1  0.25  0.5
6272         SPAIN  1954       0       0        1  0.25  0.5
6273         SPAIN  1955       0       0        1  0.25  0.5
6274         SPAIN  1956       0       0        1  0.25  0.5
6275         SPAIN  1957       0       0        1  0.25  0.5
6276         SPAIN  1958       0       0        1  0.25  0.5
6277         SPAIN  1959       0       0        1  0.25  0.5
...            ...   ...     ...     ...      ...   ...  ...
18601       BRUNEI  1992     NaN     NaN      NaN  0.75  0.5
18602       BRUNEI  1993     NaN     NaN      NaN  0.75  0.5
18603       BRUNEI  1994     NaN     NaN      NaN  0.75  0.5
18604       BRUNEI  1995     NaN     NaN      NaN  0.75  0.5
18605       BRUNEI  1996     NaN     NaN      NaN  0.75  0.5
18606       BRUNEI  1997     NaN     NaN      NaN  0.75  0.5
18607       BRUNEI  1998     NaN     NaN      NaN  0.75  0.5
18608       BRUNEI  1999     NaN     NaN      NaN  0.75  0.5
18681    INDONESIA  1951       1       4        3  0.50  0.5
18682    INDONESIA  1952       1       4        3  0.50  0.5
18683    INDONESIA  1953       1       4        3  0.50  0.5
18684    INDONESIA  1954       1       4        3  0.50  0.5
18690    INDONESIA  1960       1       4        2  0.50  0.5
18691    INDONESIA  1961       1       4        2  0.50  0.5
18692    INDONESIA  1962       1       4        2  0.50  0.5
18693    INDONESIA  1963       1       4        2  0.50  0.5
18694    INDONESIA  1964       1       4        2  0.50  0.5
18695    INDONESIA  1965       1       4        2  0.50  0.5
18698    INDONESIA  1968       1       4        2  0.25  0.5
18699    INDONESIA  1969       1       4        2  0.25  0.5
18700    INDONESIA  1970       1       4        2  0.25  0.5
19649        TONGA  1970     NaN     NaN      NaN  0.75  0.5
19651  UA EMIRATES  1972     NaN     NaN      NaN  0.75  0.5
19652  UA EMIRATES  1973     NaN     NaN      NaN  0.75  0.5
19653  UA EMIRATES  1974     NaN     NaN      NaN  0.75  0.5
19658  UA EMIRATES  1979     NaN     NaN      NaN  0.75  0.5
19666        TONGA  1987     NaN     NaN      NaN  0.75  0.5
19673  UA EMIRATES  1994     NaN     NaN      NaN  0.75  0.5
19675  UA EMIRATES  1996     NaN     NaN      NaN  0.75  0.5
19678        TONGA  1999     NaN     NaN      NaN  0.75  0.5

[270 rows x 7 columns]
```










