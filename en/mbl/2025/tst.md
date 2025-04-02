# Test

```python
import util as u
import pandas as pd
pd.set_option('display.max_columns', None)
```

```python
import json
jres = json.loads(open("mh370_areas.json").read())
print (jres["areas"].keys())
print (jres["colors"].keys())
print (jres["colors"].values())
```












