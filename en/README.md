<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>


Kava Kava - Beats For Cheats \#music

[[-]](https://youtu.be/2diGntB1Ee4)

---

China: Tibet, Qinghai, Sichuan, Shaanxi. All have a lot of potential. 

<img width="150" src="https://pbs.twimg.com/media/FD5unTVXsAUe4PI?format=png&name=small"/>

---

Here the US regions ripe for installations: CA, NV, UT, AZ, NM, even CO. 

<img width="150" src="https://pbs.twimg.com/media/FD5oGr5XsAEuaFz?format=png&name=small"/>

---

Reuters Events: "US may require 39 GW of CSP to decarbonise" 

---

"Spain alone accounts for over 42% of CSP installations in the world"

 ---

Spain too of course.. 

"Spain is one of the European countries with the most hours of sunshine"

---

When I see "sweltering", I read more direct sun rays baby!  Bring'em
on!

NYT: "[A Sicilian town Floridia] is perhaps the most blisteringly hot
town in the recorded history of Europe, offering Italy and the entire
Mediterranean a preview of a sweltering.. future"

---

The EU countries could buy solar produced clean gas from Africa, but
also from a country of their own, Italy. Remember that [news](https://www.nytimes.com/2021/08/13/world/europe/sicily-heat-wave-record-temperature-floridia-italy.html)
abt that Sicilian town, when it got really hot during the summer.
Hell put an SBD, or CSP installation there, ship H2.

---

An electric grid cannot store power like an H2 grid can. Electrons are
too fickle, the moment voltage at the endpoints go away (generation
stops), there is no current. But if new gas stopped flowing into a gas
network, there would still be gas remaining in the pipes. Gas
molecules have substance, they have a physical existence without the
presence of potential difference on either end. For the gas, if
generation stopped, one can still push the remaining gas out through
midpoint stations.

---

"@ACatInParis

Berlin to exclude unvaccinated from restaurants, bars and gyms"

---

Military Deployment [stats](2019/05/confstats.md#gdtroop)

---

Addition, TR Syria events: 2019.

[[-]](2017/12/timeline-syria-tr.md)

---

Dude.. Beijing China,

```python
pollution(39.9042, 116.4074)
```

```text
{'aqi': 5}
co 1201.63
no 44.7
no2 65.8
o3 0
so2 67.71
pm2_5 78.32
pm10 100.23
nh3 17.99
```

AQI (Air Quality Index) at 5 is the worst it can be.. Nov 11, 14:00
EST.

---

OWM API is free BTW (under a certain usage frequency), it has
historical pollution data, starting from late 2020. It uses a
so-called SILAM model to track / interpolate pollution. If emission
monitoring is needed, OWM could be a cheap way of getting those
tracking data points.

---

Stanpoli air quality, for one area, it was ok.. Checked it through Open
Weather Map API. See [doc](https://openweathermap.org/api/air-pollution)
for the range of those numbers. AQI 1 is good, 5 bad.

```python
import requests, urllib.parse, json

def pollution(lat,lon):
    url = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    weatherapi = open(".key/.owm").read() # your api key goes in that file    
    payload = { 'lat': str(lat), 'lon': str(lon), 'appid': weatherapi }
    r = requests.get(url, params=payload)
    res = [json.loads(x.decode()) for x in r.iter_lines()]
    print (res[0]['list'][0]['main'])
    comp = res[0]['list'][0]['components']
    for xx in comp: print (xx, comp[xx])

pollution(41.03071019894891, 29.051911282099258)
```

```text
{'aqi': 2}
co 273.71
no 0
no2 4.41
o3 84.4
so2 7.27
pm2_5 3.06
pm10 5.89
nh3 0.56
```

---

## For Members

[Link](https://thirdwave-members.herokuapp.com)

## Reference

[Nations and Nationalism, Culture, Narratives](/2013/02/nations-and-nationalism.md)

[The Fundamentals of Industrial Ideologies](/2011/04/fundamentals-of-industrial-ideologies.md)

[Education, Workplace](2017/09/education-workplace.md)

[Patents](/2018/09/patents.md)

[Democracy, Parties](/2016/11/democracy.md)

[Economy](/2018/05/economy.md)

[Globalization](/2018/09/globalization.md)

[Rome, The First Wave, Religion](/2017/12/rome.md)

[Human Nature & Health](/2020/07/human-nature.md)

[Climate Change](/2018/12/climate.md)

[Reports](/2019/05/reports.md)

[The Middle East](/2019/07/middleeast.md)

[TR](../tr)

## Browse

[By Year](years.md)

[Search](search.html)

[Tweet Archive](/tweets/README.md)


