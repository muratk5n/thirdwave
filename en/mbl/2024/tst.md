# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
cols = ['SIPOVGINIAUS','SIPOVGINIARG','SIPOVGINIGBR','SIPOVGINIUSA',\
        'SIPOVGINITUR','SIPOVGINIDEU','SIPOVGINIRUS','SIPOVGINIFIN']
df = u.get_fred(1980,cols)
df = df.interpolate(method='bfill')
df.columns = ['AU','ARG','GBR','USA','TR','DE','RU','FIN']
df.plot(title='GINI Index')
plt.savefig('/tmp/out.jpg')
```














```python
u.biden_approval()['net'].tail(4)
```

```text
Out[1]: 
end_date
2024-01-31   -14.840239
2024-02-01   -15.629743
2024-02-02   -16.002866
2024-02-03   -15.993473
Name: net, dtype: float64
```

```python
app = u.biden_approval()
app = app[app.index > '2023-01-01']
app['net'].plot()
plt.title("Biden Net Approval")
plt.savefig('/tmp/out.jpg')
```



