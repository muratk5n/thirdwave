

```python
import util as u
u.sm_plot_ukr1('ukrdata/alt1-0913.csv', [[48.590869037477354, 38.00222462226966]] )
plt.savefig('/tmp/out1.png')
```


```python
import util as u
df = u.eq_at2(54.9701674206043, 14.933270115918607, radius=5000, ago=600)
df.to_csv('/tmp/eq-baltic.csv')
```








