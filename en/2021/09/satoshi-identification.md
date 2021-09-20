# Satoshi Identification

Used email communication data between BTC programmers, data taken from
this [1,2] project, raw data here [3], I merely tokenize the messages,
create a word frequency vector from each message, and compute cosine similarity
between everyone and "Satoshi".

```python
import satoshi
satoshi.compare()
```

```text
sato dict 6364
gavin-andresen 0.009133992141456493 23821
hal-finney 0.057810343236745165 19868
jed-mccaleb 0.02754040560622284 7506
nick-szabo 0.1325405137299811 33000
roger-ver 0.01580186622239743 11586
craig-steven-wright 0.24631775402352696 10055
wei-dai 0.19017061765423027 25717
```

According to this, Gavin Andresen's writing, word usage is closest to
Satoshi.

Code

[satoshi.py](satoshi.py), [util.py](util.py)

References

[1] https://github.com/jlwatson/cs224n-project

[2] [Paper](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports/6858026.pdf)

[3] [Data](https://drive.google.com/uc?export=view&id=1ZmJyQr1QTg6XyNjdfOZVOZOMEt90z3v-)

