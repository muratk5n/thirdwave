# Satoshi Identification

Used email communication data between BTC team, data taken from [1,2],
and its raw data [3]. Merely tokenized the messages, create a word
frequency vector for each person, and computed its cosine similarity
to "Satoshi".

```python
import satoshi
satoshi.compare()
```

```text
sato dict 6364
gavin-andresen 0.009 23821
hal-finney 0.058 19868
jed-mccaleb 0.028 7506
nick-szabo 0.133 33000
roger-ver 0.016 11586
craig-steven-wright 0.246 10055
wei-dai 0.19 25717
```

Gavin Andresen's writing, word usage seems closest.

Using another measure, Kullback-Leibler divergence,

```python
import satoshi
satoshi.compare_kl()
```

```text
sato dict 6364
gavin-andresen 0.362
hal-finney 0.561
jed-mccaleb 0.213
nick-szabo 0.893
roger-ver 0.422
craig-steven-wright 0.504
wei-dai 0.751
```

[Code](satoshi.py)

References

[1] [Data on GH](https://github.com/jlwatson/cs224n-project)

[2] [Paper](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports/6858026.pdf)

[3] [Data](https://drive.google.com/uc?export=view&id=1ZmJyQr1QTg6XyNjdfOZVOZOMEt90z3v-)

[4] [KL Div](https://machinelearningmastery.com/divergence-between-probability-distributions/)