
They could've performed tests.. possible. Politically time is right for it.
I'm just saying it's not clear in the data.

---

Quakes together with NPP and other facilities.. Not sure if there is a pattern.

```python
import json
irn = json.loads(open("iran-nuke.json").read())
irn.update(res)
u.map_coords(irn, zoom=7, outfile="map7.html")	    
```

[[-]](mbl/2024/map7.html)

---

Locations of quakes, one in the North one in the South

```python
res = dict((k + " magnitude:" + str(v['mag']),
            [v['lat'],v['lon']]) for k,v in df.iterrows())
u.map_coords(res, zoom=4, outfile="map6.html")	    
```

[[-]](mbl/2024/map6.html)

---

Data is from USGS.

---

There were not one, but two quakes

```python
df = u.eq_at(35.59431085, 53.395109027, 800, 8)
df
```

```text
Out[1]: 
                     mag      lat      lon  ago
date                                           
2024-10-05 06:29:26  4.1  32.3247  56.4756    8
2024-10-05 22:15:34  4.5  35.3597  52.8989    7
```

---

Earthquakes in Iran.. were they nuclear weapon tests?

---

Al-Monitor: "'Very challenging': Israel faces Hezbollah in tricky
terrain..As Israel undertakes its fourth ground offensive in southern
Lebanon in 50 years, its troops again face rocky terrain mined with
explosives and full of hiding places that previous generations of
soldiers have battled over"

---

F24: "Israel's decision to begin ground attacks against Hezbollah in
Lebanon has sparked a debate about the wisdom of opening up a second
front and presents Israeli soldiers with a different challenge from
the dense urban environment of Gaza. Analysts believe Hezbollah has
built an intricate network of tunnels cut deep into the hills of
southern Lebanon, a tall order for the Israeli military."

---

F24: "Forty nations that contribute to the UN peacekeeping force in
Lebanon said in a statement on Saturday that they 'strongly condemn
recent attacks' on the peacekeepers."

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

[Games](2024/06/games.html)

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
