
Sad \#OpenGraph

[[-]](https://mastodon.social/@MikeBlazer/109828086651109401)

---

"@raito@nixos.paris

Presented without comments"

[[-]](https://nixos.paris/system/media_attachments/files/109/807/131/196/194/594/original/b451cc8794dda6cb.png)

---

Electrification mantra was foolish an idea marketed as a new solution
simply bcz it sounded contrarian. Fuels were always the optimal
solution, we merely needed a clean one \#H2 \#NH3

---

Still the total projected cost of F-35 project is at $1.7 trillion.
That's a lot of money... I suspect price-performance ratio of this
project is pretty high.

---

There've been some pushback against this view recently coupled with
better numbers at dogfighting, but, interesting ..  Smoke coming out
of a fire, or just smoke.. as in somebody's blowing it

TDB: "Air Force Admits: Our New Stealth Fighter Can’t Fight.. The F-35
Joint Strike Fighter is supposed to replace almost 90 percent of
America’s tactical aviation fleet. Too bad it ‘wasn’t optimized for
dogfighting,’ according to the Air Force"

---

"@carnage4life@mas.to

180,000 users have paid for blue checks in the past two months which
will generate under $25M/year for Twitter. This is a drop in the
bucket for their revenue goals and less than 0.5% of pre-acquisition
revenue.

Also revenue is down -40% since acquisition"

---

Right now there is a running server at `router.project-osrm.org` with
all of OSM's data. After the apocalypse you'll be running that
locally. It's easy.

---

Driving from Boston to Wyoming..? For f sake

```python
import requests, json, polyline, folium

lat1,lon1 = (42.36880059119,-71.141522762)
lat2,lon2 = (41.125673090,-104.835825219)
url = f'http://router.project-osrm.org/route/v1/driving/' + \
      f'{lon1},{lat1};{lon2},{lat2}?alternatives=false&steps=false'
response = requests.get(url, verify=False)
resp = json.loads(response.text)
decoded = polyline.decode(resp["routes"][0]['geometry'])
map = folium.Map(location=(lat1,lon1),zoom_start=5,control_scale=True)
folium.PolyLine(locations=decoded, color="blue").add_to(map)
```

[Directions](mbl/2023/bos_wyo_dir1.html)

---

For mobile Unix compting A Raspberry Pi will do - power it up with
solar, run micro web server on it access thru local wifi / smartphone
hotspot, view pages served from Pi on the phone's browser.

---

OSM data is produced by volunteer contributors. Freely available,
anyone can contribute.

---

Getting stuck with paper maps after the Zombie Apocalypse? C'mon. To
get ready for that aftermath, need a recent copy of all the files
[here](http://download.geofabrik.de/). There is open source software
that can read those files, it can extract the road network, compute
driving directions, report on POIs from it.. The files aren't too
sizeable, compared to the value they can provide.

---

<iframe width="340" src="https://www.youtube.com/embed/bP5dkR6QQj8?start=169&end=325" title="Jimmy Dore Brings ANTI-WAR Message To Fox News" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

E&E News: "Census: Disasters displaced more than 3M Americans in 2022"

---

FT: "Alphabet shares fall sharply after Google's AI chatbot debut stumbles"

---

## Reference

[Nations and Nationalism, Culture, Narratives](2013/02/nations-and-nationalism.html)

[The Fundamentals of Industrial Ideologies](2011/04/fundamentals-of-industrial-ideologies.html)

[Education, Workplace](2017/09/education-workplace.html)

[Science and Technology](2018/09/science-technology.html)

[Democracy, Parties](2016/11/democracy.html)

[Economy](2018/05/economy.html)

[Globalization](2018/09/globalization.html)

[Rome, The First Wave, Religion](2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2018/12/climate.html)

[Reports](2019/05/reports.html)

[The Middle East](2019/07/middleeast.html)

[TR](../tr)

## Browse

[Members](2022/08/members.html)

[By Year](years.html)

[Search](search.html)

[Microblog Archive](mbl/index.html)

[PDF](https://drive.google.com/uc?export=view&id=1FSi-1MnqXVq_PVTEXzzflwN8-7h92N_R)
