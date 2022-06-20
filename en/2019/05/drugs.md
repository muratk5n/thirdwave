# Drugs

### Routes

Data comes from UNODC, apparently based on law enforcement data on
individual arrests between 2011-2016. If they caught the smuggling en
route from-to-country they are usually recorded. Sometimes source,
target is missing, but if they recorded the production country, code
takes that as source, if destination is missing,country of arrest as
destination is used.

Report treats the weights of all drugs as equivalent, they are summed
per route, to give a general idea of the importance of each
route. Code also multiplies tablet based drugs with 100 mg per tablet,
to turn them into a kilo weight. Cannabis arrests are removed to focus
on harder drugs.

Routes are drawn from country's center coordinate to another's center
coordinate, so the places seen at end points of routes are nothing
special (not cities, nor ports).

A quick sum on transport method during arrest;

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

