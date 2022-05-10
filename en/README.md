<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

Pinned Tweet

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Gasgrid Finland participates in the update of <a href="https://twitter.com/ehb_europe?ref_src=twsrc%5Etfw">@ehb_europe</a> development vision – the hydrogen backbone to support the achievement of climate goals, REPowerEU plans, and developing the resilience of the European energy system. <a href="https://twitter.com/hashtag/hydrogen?src=hash&amp;ref_src=twsrc%5Etfw">#hydrogen</a> <a href="https://twitter.com/hashtag/EHB?src=hash&amp;ref_src=twsrc%5Etfw">#EHB</a> <a href="https://t.co/adljzgqa2X">https://t.co/adljzgqa2X</a> <a href="https://t.co/fdAbz5wzwC">pic.twitter.com/fdAbz5wzwC</a></p>&mdash; Gasgrid Finland Oy (@GasgridFinland) <a href="https://twitter.com/GasgridFinland/status/1511248215798161410?ref_src=twsrc%5Etfw">April 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

H2 View: "A cooperation agreement to develop hydrogen refuelling
infrastructure capable of refuelling 100,000 hydrogen-powered vehicles
in the Nordic region has been signed.. Norwegian Hydrogen AS,
FirstElement Fuel Inc. and Mitsui & Co, announced the companies would
be working together to accelerate the expansion of the hydrogen
network across the entire Nordic region"

---

H2 View: "Aviation H2 signs major deal with FalconAir to aid in
developing hydrogen aircraft by 2023. As development of Australia’s
first hydrogen-powered plane ramps up, the company behind the
aircraft, Aviation H2, has unveiled a new major partnership with
FalconAir"

---

H2 Bulletin: "ZeroAvia Kicks Off US 19-seat Aircraft Testing and
Demonstration Program on Path to Worldwide Application of its
Powertrain Technology"

---

H2 View: "Texas, US, continues to ramp up its hydrogen capabilities
with Enbridge and Humble Midstream revealing plans to develop
low-carbon hydrogen and ammonia facilities"

---

H2 Fuel News: "Hydrogen trucks are the most eco-friendly zero-emission
vehicle, says ATRI [American Transportation Research Institute]"

---

H2 View: "Elcogen announced that it has received a €24m ($25.25m)
investment to aid the expansion of its capabilities to produce green
hydrogen, using its reversible solid oxide fuel cell (SOFC)
technology, from HydrogenOne Capital Growth Plc (HydrogenOne)... The
investment is set to allow Elcogen to drive forward its expansion of
facilities in Tallinn, Estonia, to create an automated production line
for SOFCs"

---

H2 View: "Lhyfe has officially launched its initial public offering (IPO) to
support the development of the company’s green hydrogen production
technology and ambitions... The capital increase has soared to over
€145m ($152m)"

---

Thorium on the other hand, can be found in Egypt, Australia, Canada,
US, Brazil, Asia Minor.. Molten-salt reactors show some hope; can
produce H2 easily, added bonus.

---

Wanna do more nuclear? A lot of the fuel for that also comes from
Russia Russia Russia.

---

[Link](https://drive.google.com/uc?export=view&id=1n0aVnSajhY5RR18uEk-tvTD0aRGzQc8D)

---

Saw another asshat claiming 'maybe the Sun just *reflects* GR from
everywhere else' 😂 

---

Of course, dark matter, near black hole, across a time dilation field
seeping into our universe from another. You got it all figured out
champ...

"Dark Matter could be involved here too"

---

Activity would disrupt the activity on that surface, so Gamma rays
would decrease. That's why there is strong anti-correlation. 

---

Nuclear reactions on the surface of the Sun is enough to explain
that. See 'lattice confinement fusion'. Have to accept the Sun does
have a surface, it aint bunch of 'hot gas'.

SciAm: "The Sun Is Spitting Out Strange Patterns of Gamma Rays—and No
One Knows Why.. To their surprise, the researchers found the most
intense gamma rays appear strangely synced with the quietest part of
the solar cycle"

[[-]](https://www.scientificamerican.com/article/the-sun-is-spitting-out-strange-patterns-of-gamma-rays-and-no-one-knows-why/)

---

Many-Worlds Interpretation of QM is made possible by ignoring the
measurement problem, not solving it. 'The collapse' of the
wavefunction is essentially swept under the carpet, but ignoring the
problem doesn't make it go away. 

---

Interesting, though the this tool is overused these days as a literary
clutch. Ditto for 'alternate universes'.

"[Twain novel] *A Connecticut Yankee in King Arthur’s Court*.. is often
said to be the forerunner of all science fiction tales about time
travel"

---

MT depiction in Trek Next Gen was good.

---

It's weird how the image of Twain today is excessively desanitized.
Mark Twain was a vocal anti-war proponent in his day.. He even once
suggested that the stars in the flag be "replaced by skulls and
cross-bones".

"During the Spanish-American War, [Mark] Twain became a fervent
anti-imperialist, even joining the Anti-Imperialist League. His
sentiments about the war and the war in the Phillippines were
published nationwide"

---

Some accents at the UN pronounce piece as 'piss'. Have to work on that
bruh.

---

Social rentals (gov-built rent-controlled homes) as a % of total
housing; France 14%, Denmark 21%, Netherlands 37%. \#ABC \#Oz. That is
a huge number. Taking services completely outside the market structure
can work. This is the way

---

\#Documentary \#WSJ "Trucking used to be one of the very best blue
collar jobs in the US. The the industry was almost fully unionized by
the teamsters union.  Unionized truck drivers were making up to 20%
more than even unionized steel workers or auto workers. It was one of
the best jobs you could get, and when you got one of those good jobs
you were likely to stay in it until you until you retired. [But] the
industry was deregulated 1980, the union was pushed out of the big
segments of the of the industry, and and wages and working conditions
followed [became worse]"

---

He had kicked out the foreigners and nationalized the oil
industry. Then boom - toppled by an 'Anglo' coup.

---

Pity. Iran's democratically elected leader Mossadeg was Time's Man of
the Year for 1952. A terrible fate befell him..

[[-]](https://pbs.twimg.com/media/FSWaDakXMAEnhI5?format=jpg&name=small)

---

Had to guide the processing towards the goal; remove small patches,
tell the segmentation algo to look at coarse objects, put a lower
limit on segment size.. lots of small nudges here and there. There is
no free lunch. Cant do 'Alexa give me the interesting image blocks and
boundaries in this image'.

---

Little image processing action to reverse-eng UKR-RU frontline. Works ok

```python
from skimage.color import rgb2gray, rgb2lab, deltaE_cie76
from skimage.segmentation import felzenszwalb
from skimage.morphology import binary_closing
from skimage import io, measure

threshold = 15
img = io.imread("ua-ukr-20220504.png")
lab = rgb2lab(img[:,:,[0,1,2]])
d1 = deltaE_cie76(rgb2lab(np.uint8(np.asarray([243,178,182])) ), lab)
d2 = deltaE_cie76(rgb2lab(np.uint8(np.asarray([253,35,36])) ), lab)
flt = rgb2gray(img.copy())
flt[(d1 < threshold)] = 1; flt[(d1 >= threshold)] = 0
flt[(d2 < threshold)] = 1; 
flt = flt.astype(bool)
flt = binary_closing(flt)
seg = felzenszwalb(flt, scale=50, sigma=2, min_size=8000)
fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
axes[0].imshow(img)
axes[1].imshow(seg)
contours = measure.find_contours(seg, 0.8)
for c in contours:
    axes[1].plot(c[:, 1], c[:, 0], color='white',linewidth=2)
```

<img width="350" src="https://pbs.twimg.com/media/FSWZvWtXwAAfZVv?format=png&name=small"/>

---

Al Monitor: "Yazidis displaced anew by north Iraq violence"

---

NI is seperated by the North Channel from UK just as UK is seperated
by the English Channel from EU mainland - yet the latter went through
Brexit, severing its connection to that mainland. Well here is another
Channel and maybe another "exit".

"Northern Island is so close to UK, it's logical they want to be
closely connected"

---

Aw man but UK is such a 'leader' in the RU/UKR fight (while also
quietly enjoying the mess it helped create inside European
landmass). Can't you cut them a little slack?

Politico: "Take a chill pill, EU tells UK over Northern Ireland
protocol.. London needs to 'dial down the rhetoric' and 'find
solutions' to trade issues within the framework of the deal, European
Commission Vice President Maros Sefcovic says"

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


