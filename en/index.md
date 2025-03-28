
Wiki: "The Guatemalan Revolution began in 1944, after a popular
uprising toppled the military dictatorship of Jorge Ubico. Juan José
Arévalo was elected president in Guatemala's first democratic
election. He introduced a minimum wage and near-universal
suffrage. Arévalo was succeeded in 1951 by Árbenz, who instituted land
reforms which granted property to landless peasants...

The U.S. government feared that Guatemala's example could inspire
nationalists wanting social reform throughout Latin America. The
United Fruit Company (UFC), whose highly profitable business had been
affected by the softening of exploitative labor practices in
Guatemala, engaged in an influential lobbying campaign to persuade the
U.S. to overthrow the Guatemalan government. U.S. President Harry
Truman authorized Operation PBFortune to topple Árbenz in 1952"

----

Let's see whose estimate wins out in the end. 

---

My estimate looks close to the Bayesian guy's number. Interesting. 

---

We now have Richard Godfrey estimate, and I came across a book using
Bayesian (a stat technique) analysis (by Davey, Gordon), I'll throw
that in there, and there is mine, all of the estimates shown on map below.

```python
cs = {"Godfrey": [-33.176793409, 95.300021451],
      "Kuala Lumpur Intl Airport": [2.8181270526, 102.18700262],
      "Last Military Radar Contact": [6.65,96.34],
      "Bayesian": [-38,88.2],
      "TW": [-38.74608593396341,84.44331631045696]
     }
u.map_coords(cs, zoom=3, outfile="map05.html")
```

[[-]](mbl/2025/map05.html)

---

The path along with the satellite handshake range rings, along with
the best final estimate (printed below before map link),

```python
u.plot_mh370(bearings_list=res['x'],outfile="map04.html")
```

```text
-38.74608593410704 84.44331631070675
```

[[-]](mbl/2025/map04.html)

---

Oh yeaaaaah


```python
from pygeodesy.sphericalNvector import LatLon
import pandas as pd, numpy as np
from scipy.optimize import minimize

pd.set_option('display.max_columns', None)

df = pd.read_csv('mh370b.csv')

#Last Military Radar Contact
#18:22:12 6.65,96.34
d1 = (pd.to_datetime("2014-03-07 18:25:27.421") - \
      pd.to_datetime("2014-03-07 18:22:12.000")).total_seconds()/3600
R = 6378
vavg = 881.552 # km/h

def cost(pars):
    b1,bearings = pars[0],pars[1:]
    lat,lon = 6.65,96.34
    p1 = LatLon(lat,lon)
    curr = p1.destination (d1 * vavg, bearing=b1, radius=R)    
    deltas = []
    for i,row in df.head(len(df) - 1).iterrows(): # skip last row
        p1 = LatLon(row['Lat'],row['Lon'])
        deltacurr = p1.distanceTo(curr) / 1000
        # add diff between ring and distance to sat
        deltas.append(np.abs(deltacurr-row['BTOr']))
        travel = row['Duration']*vavg
        curr = curr.destination (travel, bearing=bearings[i], radius=R)

    return np.sum(deltas)
    
bearings = np.ones(len(df))*180
opts = {'maxiter': 100, 'verbose': 3}
res = minimize (fun=cost,x0=([220] + list(bearings)),
                method='Nelder-Mead',
                options=opts)
print (res['x'],res['fun'])
```

```text
[198.85552101 206.23787955 192.41281668 188.38700846 189.66879695
 192.3739793  170.24571194 157.94930991] 239.47309090193585
```

---

Optimization could be quicker though, speed, duration btw handshakes
known, bearing unknown. Cost function tries to stick to "BTO rings" as
close as possible, and find optimal bearing list.

---

This problem sounds a lot like ultrasonic sensors processing for robot
localization, those sensors also report range no bearing.. You would
compute distance to sensor from estimated location via simple
Euclidian distance add Gaussian noise on top, and run that through a
particle filter to estimate next best location after movement.

---

Particle filters, or optimization.. 🤔 ... 

---

Found data for the handshakes oh yeaaa

---

There were seven sat handshakes w/ the plane at various times. The sat
provided range-only data, no bearing, meaning draw a circle around the
sat location with radius being range, and MH 370 could be anywhere on
that circle. But plane moves (w/ known speed), you get more circles
(at known times), if you combine all the uncertain measurements you
could arrive at an estimate.

---

I never did my own estimate for this location.. Should we do some scicomp?

---

Great.

NPR: "Malaysia approves a new search for MH370 wreckage in the Indian Ocean"

---

## Reference

[Nations and Nationalism, Culture, Narratives](0119/2013/02/nations-and-nationalism.html)

[The Fundamentals of Industrial Ideologies](0119/2011/04/fundamentals-of-industrial-ideologies.html)

[Education, Workplace](0119/2017/09/education-workplace.html)

[Science and Technology](0119/2018/09/science-technology.html)

[Democracy, Parties](0119/2016/11/democracy.html)

[Economy](2021/01/economy.html)

[Globalization](0119/2018/09/globalization.html)

[Rome, The First Wave, Religion](0119/2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2022/01/climate.html)

[Reports](2021/01/reports.html)

[The Middle East](0119/2019/07/middleeast.html)

[TR](../tr/index.html)

## Browse

[Members, Donations](2022/08/members.html)

[By Year](years.html)

[Search](https://muratk5n.github.io/thirdwave/en/search.html)

[Microblog Archive](mbl/index.html)

[PDF](https://www.dropbox.com/scl/fi/8kl0sla1booo83zeb28dn/tw-all.pdf?rlkey=p9r319p8jbzak5du3dasju05y&st=28wknfsp&raw=1)

Also on 
[Mastodon](https://fosstodon.org/@muratk5n),
[Codeberg](https://muratk5n.codeberg.page/en/),
[Github Pages](https://muratk5n.github.io/thirdwave/en/)

