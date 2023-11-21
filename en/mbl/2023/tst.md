# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
df = u.get_fred(1990,['VALIMPARM052N','VALEXPARM052N'])
df.columns = ['import','export']
df = df.interpolate()
df.plot()
print (df)
plt.axvspan('01-01-1990', '01-01-1992', color='y', alpha=0.5, lw=0)
plt.axvspan('01-01-1998', '01-01-2003', color='y', alpha=0.5, lw=0)
plt.axvspan('01-01-2012', '01-01-2014', color='y', alpha=0.5, lw=0)
plt.axvspan('01-01-2020', '01-01-2021', color='y', alpha=0.5, lw=0)
plt.savefig('/tmp/out.jpg',pil_kwargs={'quality':40})
```

```text
                  import        export
DATE                                  
2006-01-01  2.324000e+09  3.188000e+09
2006-02-01  2.326000e+09  3.090000e+09
2006-03-01  2.722000e+09  3.648000e+09
2006-04-01  2.545000e+09  3.925000e+09
2006-05-01  2.826000e+09  4.181000e+09
...                  ...           ...
2022-04-01  6.883000e+09  8.337000e+09
2022-05-01  7.886000e+09  8.254000e+09
2022-06-01  8.664000e+09  8.433000e+09
2022-07-01  8.289000e+09  7.805000e+09
2022-08-01  7.837000e+09  7.537000e+09

[200 rows x 2 columns]
```
```python
print (df)
```

```text
            ARGXTIMVA01GYSAQ  ARGXTEXVA01GYSAM
DATE                                          
1991-01-01         48.634949        -15.477277
1991-02-01               NaN         -0.574938
1991-03-01               NaN        -24.351484
1991-04-01        101.282656         -2.448467
1991-05-01               NaN         10.704736
...                      ...               ...
2023-05-01               NaN        -25.774700
2023-06-01               NaN        -36.194936
2023-07-01        -13.751148        -22.894163
2023-08-01               NaN        -19.236312
2023-09-01               NaN        -23.152920

[393 rows x 2 columns]
```




















































```python
df = u.biden_approval()['net']
print (df.tail(4))
df.plot()
plt.savefig('/tmp/out.jpg')
```

```text
end_date
2023-10-10   -13.947808
2023-10-11   -13.981538
2023-10-12   -14.447912
2023-10-13   -14.352457
Name: net, dtype: float64
```




