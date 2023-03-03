
```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
u.global_leader_approval().head(8)
```

```text
Out[1]: 
                                   name   net
0                 Narendra Modi (India)   +60
1  Andrés Manuel López Obrador (Mexico)   +26
2          Anthony Albanese (Australia)   +26
3            Alain Berset (Switzerland)   +21
4    Luiz Inácio Lula da Silva (Brazil)   +17
5                Giorgia Meloni (Italy)   +13
6           Alexander De Croo (Belgium)    -9
7             Joe Biden (United States)    -9
```








```python
#u.rottentomatoes_mov("Ant Man 3")
u.boxofficemojo("Ant Man 3")
```



















```python
u.sm_plot_ukr('ukrdata/fl-0224.csv','ukrdata/fl-221115.csv',[])
plt.savefig('/tmp/out.jpg')
```









