# Drugs

### Routes

Data comes from UNODC, apparently based on law enforcement data on
individual arrests between 2011-2016. If they caught the smuggling en
route from and to country are usually recorded, or the intented
destination had the transport went ahead. Sometimes source, target is
missing, but if they recorded the production country I take that as
source. If destination is missing, I take country of arrest as final
destination.

Report treats the weights of all drugs as equivalent, they are summed
per from-to route, to give a general idea of the importance of each
route. I multiply tablet quantities with 100 mg per tablet to turn
them into weights as well. I filter out all cannabis related transport
as this drug is becoming accepted at the same level of alcohol these
days, report's focus is harder drugs.

Routes are drawn from country's center coordinate to another's center
coordinate, the places per country are nothing special (they are not
cities, ports).

Arrest location counts below;

```python
import zipfile, pandas as pd

with zipfile.ZipFile('drug-trafficking-unodc.zip', 'r') as z:
    df = pd.read_csv(z.open('drug-trafficking-unodc.csv'),sep=';')
    print (df.groupby('TRANSPORT').size().sort_values(ascending=False))
```

```text
TRANSPORT
Commercial air     19137
Land                8933
Private road        6933
Other               5942
Commercial road     3471
Unknown             2833
Commercial sea      1021
Mail                 924
None                 534
Rail                 368
Private air           57
River                 30
Private sea           24
Pedestrian            16
Air                    6
dtype: int64
```

[Data Source](https://dataunodc.un.org/ids)

[Data (ZIP)](drug-trafficking-unodc.zip)

[Code](drugs.py)

[Output](drugs-out.html)

