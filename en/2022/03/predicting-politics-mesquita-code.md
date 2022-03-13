# Code for Predicting Politics

An attempt to replicate Dr. Mesquita's [book](predicting-politics-mesquita.md) was
made by David Massad in this [repo](https://github.com/dmasad/Agents-In-Conflict).
I took his code collated it to one script. The China simulation mentioned
by Massad and Mesquita in his book are below,

```python
import bdm, pandas as pd
df = pd.read_csv('ch.csv')
bdm.simulate(df)
```

```text
0.1111111111111111
Zeming              	Position: 0.17	Capability: 0.80	Salience: 0.50
Lipeng              	Position: 0.06	Capability: 0.90	Salience: 0.80
Qiaoshi             	Position: 0.06	Capability: 0.85	Salience: 0.80
Shanghai            	Position: 0.28	Capability: 0.30	Salience: 0.50
Ruihuan             	Position: 0.22	Capability: 0.60	Salience: 0.75
Tianjiyun           	Position: 0.11	Capability: 0.50	Salience: 0.40
Zhurongji           	Position: 0.28	Capability: 0.60	Salience: 0.80
Zoujiahua           	Position: 0.06	Capability: 0.80	Salience: 0.75
Shangkun            	Position: 0.11	Capability: 1.00	Salience: 0.85
Baibing             	Position: 0.06	Capability: 0.85	Salience: 0.85
Wangzhen            	Position: 0.06	Capability: 0.85	Salience: 0.80
Wanli               	Position: 0.17	Capability: 0.60	Salience: 0.60
Ziannian            	Position: 0.11	Capability: 0.60	Salience: 0.60
Cheyun              	Position: 0.00	Capability: 1.00	Salience: 0.85
Boyibo              	Position: 0.11	Capability: 0.75	Salience: 0.70
Pengzhen            	Position: 0.06	Capability: 0.90	Salience: 0.80
Challdem            	Position: 1.00	Capability: 0.20	Salience: 0.90
Chspring            	Position: 1.00	Capability: 0.20	Salience: 0.90
STU/INTEL           	Position: 1.00	Capability: 0.40	Salience: 0.90
USA                 	Position: 1.00	Capability: 0.70	Salience: 0.40
Japan               	Position: 0.56	Capability: 0.50	Salience: 0.50
Europe              	Position: 0.89	Capability: 0.55	Salience: 0.30
Hong-Kong           	Position: 1.00	Capability: 0.25	Salience: 0.85
Guandung            	Position: 0.44	Capability: 0.30	Salience: 0.70
```


[Code](bdm.py)

