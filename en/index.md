
QZ: "An antitrust lawsuit against Google goes to trial on Sep. 12"

---

The Conversation: "Ever-larger cars and trucks are causing a safety crisis on US streets"

[[-]](https://theconversation.com/ever-larger-cars-and-trucks-are-causing-a-safety-crisis-on-us-streets-heres-how-communities-can-fight-back-206382)

---

Ars Technica: "The room-temperature superconductor that wasn’t.. The
summer of room-temperature superconductivity was short-lived" \#LK99

---

OnlySky: "Why libertarian cities fail"

[[-]](https://onlysky.media/alee/why-libertarian-cities-fail/)

---

Schools clearly bet on the wrong technology - ed solutions need to be
based on true open source. DoEd can buy commodity hardware (cheap as
they will buying in bulk) and keep Ed software as "images" on a DoEd
server. Images are snapshots of a machine that has everything kids
need, you burn this image on each machine, give that to students. A
few visiting gov IT people for each school occasionally can fix issues
as they arise. Do not depend on some questionable bidness "on the
cloud".

"‘Chromebook Churn’ report highlights problems of short-lived laptops
in schools Chromebooks are not designed to last...Schools have piles
of working Chromebooks that have become e-waste because they’ve
expired...

Chromebooks have a built-in 'death date,' after which software support
ends. We expect milk to expire, but not laptops. Adding to customer
confusion, expiration dates are based on the certification of a given
model, not the purchase date. This means that consumers or schools can
buy a used or refurbished Chromebook thinking they’re getting a great
deal, only to be surprised when their new laptop expires after a year"

[[-]](https://pirg.org/edfund/resources/chromebook-churn-report-highlights-problems-of-short-lived-laptops-in-schools/)

---

[Link](https://drive.google.com/uc?export=view&id=1XHVZ3G6muR29BGSAsV2zBOqtn9TIvJHA)

---

Browser side programs are usually in Javascript. But Imma test a new
tech - Python in the browser \#PyScript.

---

A lot can be done via static files, even big ones. Some do not realize
but client can even read *parts* of a file on the web server, it's part
of the standard,

```python
from requests import get
url = "http://download.thinkbroadband.com/5MB.zip"
get(url, headers={"Range": "bytes=0-100"})
```

That gets only first 100 bytes. In theory one could even read parts of
a whole database if client knew how to seek/jump between the right
parts of the db file.. This is for read-only apps sure, still,
covers a lot of ground.

---

No need for a whole app server to offer search, static files can work
too (this blog's setup). IDEA: Create a search index offline, push the
index files on the the static site, client, with its code, can read
specific parts of the index, combine, sort them, and present results
on its end.

---

The hell with this "cloud".. Another dependency will be removed.. Time
to DIY

---

WTF happened to site search? Place search box on your page, connect to
ext search (Goog) showed search results for that site. Now bust.

---

\#Bitcoin

[[-]](https://media.universeodon.com/media_attachments/files/111/047/126/852/664/674/original/d7e44c1dce405349.png)

---

CBS News: "Texas paid bitcoin miner more than $31 million to cut
energy usage during heat wave"

---

They apparently make the fake one from horseadish and some starch

"It is estimated only 1% of American wasabi and 5% of Japanese wasabi is real"

[[-]](https://youtu.be/K0OtGIPRcAs?t=315)

---

WION: "Following reports that China, one of the company’s major
markets, had prohibited government personnel from using iPhones as
Beijing intensifies its continuing tech war with the US, Apple shares
plummeted during after-hours trading on Thursday, following the
company’s greatest single day loss in a month, according to a report
by Forbes"

---

"[Clean Energy Latin America's] LCoH Brazil Index reveals that it is
currently feasible to manufacture green hydrogen in select strategic
locations within Brazil at a levelized cost ranging from $2.87/kg to
3.56/kg. However, with optimization and incentives, these costs could
potentially decrease to as low as 1.69 dollar/kg, making them highly
competitive when compared to gray hydrogen derived from fossil fuels,
known for its environmental impact"

<img width='340' src='https://www.pv-magazine.com/wp-content/uploads/2023/05/index-1536x1152-1-1024x768-1.jpg'/> 

---

Ars Technica: "Chrome's invasive new ad platform, ridiculously branded
the 'Privacy Sandbox,' is.. getting a widespread rollout in Chrome
today. If you haven't been following this, this feature will track the
web pages you visit and generate a list of advertising topics that it
will share with web pages whenever they ask, and it's built directly
into the Chrome browser.. Google seemingly knows this won't be
popular. Unlike the glitzy front-page Google blog post that the
redesign got, the big ad platform launch announcement is tucked away
on the privacysandbox.com page"

---

Over 200 mil in the red. Why did it bomb so bad? Was it Woke? Because
it looks like film went broke. 😂 😂 

```python
u.mov_profit(budget=294,gross=380)
```

```text
Out[1]: -213.0
```

---

Ugh.. looks bad.. Lost munee

```python
u.boxofficemojo("Indiana Jones and the Dial of Destiny")
```

```text
Out[1]: 
{'Domestic Opening': '$60,368,101',
 'Domestic': '$174,385,511',
 'International': '$207,888,377',
 'Worldwide Total': '$382,273,888',
 'Release Date': 'June 28, 2023'}
```

---

"@croissant@zeroes.ca

Long COVID, which occurs in 10% of infections and which is not fully
prevented by vaccines, is becoming an exclusion criteria for any kind
of insurance — including travel, disability, and life.

The actuaries know."

---

Interesting Eng: "First liquid hydrogen-powered piloted plane soars
into sky.. H2FLY, the Stuttgart-based firm acquired by Joby Aviation
in 2021, completed four such flights in its HY4 demonstrator aircraft
fitted with a cutting-edge hydrogen-electric fuel cell propulsion
system and cryogenically stored liquid hydrogen..

Replacing gaseous hydrogen with liquid hydrogen effectively doubled
the maximum range of the HY4 aircraft from around 466 miles (750 km)
to approximately 932 miles (1,500 km), showing great promise for a
future with cleaner and more sustainable air travel"

<img width='340' src='https://interestingengineering.com/_next/image?url=https%3A%2F%2Fimages.interestingengineering.com%2F1200x675%2Ffilters%3Aformat(webp)%2F2023%2F09%2F09%2Fimage%2Fjpeg%2FRwp0ZKG4ICGIclLzBiN37DcX40r7nCCvz8b6sNeM.jpg&w=1920&q=75'/> 

---

F24: "G20 summit closes with Russia, Brazil and India boasting
success.. Modi formally closed the summit by passing on a ceremonial
gavel to Brazilian President Luiz Inacio Lula da Silva, whose country
will take the bloc's presidency in December. 'We cannot let
geopolitical issues sequester the G20 agenda of discussions,' Lula
said, an implicit reference to wrangling over the Ukraine war"

---

Politico: "West goes easy on Russia to save the G20"

---

AP: "Biden, Modi and G20 allies unveil rail and shipping project
linking India to Middle East and Europe.. President Joe Biden and his
allies on Saturday announced [the] plans.. an ambitious project aimed
at fostering economic growth and political cooperation... The rail and
shipping corridor would help physically tie together a vast stretch of
the globe, improving digital connectivity and enabling more trade
among countries, including with energy products such as hydrogen"

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

[Search](search.html)

[Microblog Archive](mbl/index.html)

[PDF](https://drive.google.com/uc?export=view&id=1FSi-1MnqXVq_PVTEXzzflwN8-7h92N_R)

Also on 
[Mastodon](https://fosstodon.org/@muratk5n),
[Codeberg](https://muratk5n.codeberg.page/en/),
[Github Pages](https://muratk5n.github.io/thirdwave/en/)

<img src='https://drive.google.com/uc?export=view&id=1zsIeciFSvlr-sWB84Tc0mfZ_NYqn9VQx'/> 
