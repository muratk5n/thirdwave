# Satoshi Identification


```python
from collections import OrderedDict, defaultdict
import pickle, os, glob, re

word_dict = defaultdict(int)
CANDIDATES = ["gavin-andresen", "hal-finney", "jed-mccaleb", "nick-szabo", "roger-ver", "craig-steven-wright", "wei-dai"]

c = 'gavin-andresen'
for path in glob.iglob(os.environ['HOME'] + "/Documents/repos/cs224n-project-master/data/satoshi/%s/*.txt" % c, recursive=True):        
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        print (text)
        text = text.replace("("," ").replace(")"," ")
        text = text.replace(","," KOMMA")
        text = text.replace("."," DOT")
        text = text.lower()
        tokens = re.split('\s',text)
        for token in tokens: word_dict[token] += 1
        print (tokens)
        break
    
print (word_dict)
```








References

[1] https://github.com/jlwatson/cs224n-project

[2] https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports/6858026.pdf

