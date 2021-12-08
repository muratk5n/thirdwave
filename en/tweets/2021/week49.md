



The Atlantic: "So what work is actually valuable? It’s incredibly
unclear. Many knowledge workers, ourselves included, find themselves
insecure in some capacity about the work they’re doing: how much they
do, whom they do it for, its value, their value, how their work is
rewarded and by whom. We respond to this confusion in pretty confusing
ways. Some become deeply disillusioned or radicalized against the
extractive, capitalist system that makes all of this so muddled. And
others throw themselves into work, centering it as the defining
element of their self-worth. In response to the existential crisis of
personal value, they jump on the productivity treadmill, praying that
in the process of constant work they might eventually stumble across
purpose, dignity, and security... The treadmill rarely provides the
kind of value and meaning that we hope it will. People are growing
more certain in the notion that the status quo of American working
life is untenable. But the pandemic has created an opportunity to
reconsider and reimagine the structure of our lives and, perhaps,
remove the vestigial, extractive elements. We believe that flexible
work—not flexible work during a pandemic, not flexible work under
duress—can change your life"

[[-]](https://www.theatlantic.com/ideas/archive/2021/12/how-care-less-about-work/620902/)

---

"Never mind that in the three years that had passed since the
withdrawal [from the Iran nuclear deal], Trump’s strategy was, on its
own terms, clearly not succeeding: Renewed and increased sanctions on
Iran — dubbed “maximum pressure” — had not forced Tehran to capitulate
and negotiate a better deal, nor had the economic damage to the
Islamic Republic led to its overthrow by a restless public. To
Israel’s possible surprise, moreover, Trump never followed through on
threats to strike Iran directly despite growing nuclear violations and
multiple attacks against Washington’s regional allies.

Bucking the official line, some Israeli security officials, many of
whom were heading into retirement, admitted that the policy was a
failure"

[[-]](https://newlinesmag.com/reportage/why-israel-sort-of-misses-the-iran-deal/)

---

This is good

"8 Women and 8 Men: Germany Gets Its First Gender-Equal Cabinet"

---

"US says it will send troops to eastern Europe if Russia invades Ukraine"

---

Some good info here on Russia/India relationship

[[-]](https://youtu.be/exlRuebKgqA)

---

NYT: "India and Russia Expand Defense Ties, Despite Prospect of
U.S. Sanctions.. India’s purchase of a missile defense system signaled
that it was more worried about an emboldened China at its borders than
about angering the United States"

---

TDB: "The Deadly Cargo Inside MH370: How Exploding Batteries Could
Explain the Mystery.. There were two pallets of lithium-ion batteries
in [MH370] cargo"

[[-]](https://www.thedailybeast.com/the-deadly-cargo-inside-mh370-how-exploding-batteries-explain-the-mystery)

---

<img width="340" src="https://pbs.twimg.com/media/FF165CoXoAAus0z?format=jpg&name=small"/>

---

Hypersonics are not a panacea.. Every capability invites its defense,
for HS case, now the other side will consider attacking missile
launches at a mere hint of a launch, at its source. Then you're kind of
back to square one; trying to defend the homeland, makes attack on
the homeland more likely.

---

I describe such people as sophisticated tourists.. knowing more abt
a country than many others, but not *of* them.

---

Culturally Dr Oz is straight-up American (he grew up in US), wout an
iota of tigger in him. Immigrant parents cannot shape the cultural
make-up of a child, nor vacation visits to the "homeland". "It takes a
village" is correct in more ways than one. The village has your child,
not you

---

Toto did the score for *Dune* 1984? 

---

In my system there is extreme flipping (while flipping the bird to
teachers), and no grades, but at the very least schools should flip
the classroom as it's generally described.

"In fact, in one study, 200 teachers flipped their classrooms, and 85%
of them saw an overall increase in grades"

---

Heard of this DSP guy, he used 4th order poly approx for a signal proc
approach, and it worked *better* than using the periodic function
itself 😶

---

Working on a new time series structural break test approach..
Need to remove trend, and peridocity

---

Why fourth order? Has to do with the Taylor expansion probably..

TE is supposed to mirror derivatives of the approximated func, and,
for $\sin$,

$\sin^{\prime}(x)=\cos(x),\quad$
$\sin^{\prime\prime}(x)=-\sin(x),\quad$,
$\sin^{\prime\prime\prime}(x)=-\cos(x),\quad$,
$\sin^{(4)}(x)=\sin(x)$.

The fourth order derivative came back to the sine function itself.

---

Approximating periodic functions with 4th degree polynomial works well.

---

I was wondering about that; if electrolysis could be bypassed
altogether, with the method below elec generation is not needed, plant
goes from the Sun to H2 fuel, direct. Great news. Fantastic research.

---

"Synlight: Researchers expect that within 10 years, Concentrated Solar
Power (CSP) can be used to split water to hydrogen chemically using
the world’s desert sun... light is concentrated on a demonstration
system containing a cerium oxide lattice. If steam is led into the
reaction chamber, the oxygen it contains will combine with the metal
at around 800 °C and will be absorbed by it, so that hydrogen is the
only product left. Hoffschmidt said that the gas was 'an alchemist’s
dream,' as 'this high-energy fuel can be used to create virtually
anything.'"

[[-]](http://www.solarpaces.org/splitting-hydrogen-10000-suns-concentrated-solar-power/)

---

"Bloom energy used its electrolyzer powered by Heliogen’s CSP
technology for the green hydrogen fuel production. According to
Heliogen, its ..  CSP technology is capable of producing electricity
for longer spans of time than traditional solar photovoltaic (PV)
technology. By storing the solar energy, it can operate for just about
24 hours per day and seven days per week"

[[-]](https://www.hydrogenfuelnews.com/hydrogen-fuel-production-csp/8549517/)

---

CSP generated H2 from Africa, or Australia through pipelines cld
supply the entire world with cheap energy. 

---

Ukraine is short of coal supplies, Russia cut off its exports and
since invaded Donbass with coal mines, they are now controlled by
Russia. Plus there is an NG crunch pushing coal prices up.. Ukraine is
desperately trying to import from US, Latin America while winter is
approaching..

What a f-ing mess. 

---

Replication of its duration histogram. It is exponential distribution. 

```python
import pandas as pd
df = pd.read_csv('../../2021/12/empires.csv',sep=';')
df.Duration.hist(bins=5)
```

<img width="200" src="https://pbs.twimg.com/media/FF5RUwoWYAEafqk?format=png&name=small"/>

---

Empires and durability. Interesting paper. [Data](2021/12/empires.csv).

[[PDF]](https://pdodds.w3.uvm.edu/files/papers/others/2011/arbesman2011a.pdf)

---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Our micro fuel cell technology creates a unique market position for industrial trucks and robots that requires relatively low power levels where we intend to target and address a major part of the market, says Michael Glantz CEO myFC. <a href="https://t.co/fnxDgxcKWv">https://t.co/fnxDgxcKWv</a></p>&mdash; myFC Power (@myfcpower) <a href="https://twitter.com/myfcpower/status/1442436886069452811?ref_src=twsrc%5Etfw">September 27, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

H2 View: "Norwegian-based Kongsberg Gruppen has successfully tested
and verified a new hydrogen fuel cell powered drivetrain for ships and
ferries"

---

H2 View: "BayoTech officially unveils 1,000kg per day hydrogen hub for
New Mexico, US"

---

H2 View: "Australia to gain hydrogen production project with a 900
tonne per day capacity by 2031"

---

CNBC: "Wood's main exchange-traded fund, which trades under ticker
ARKK, is down more than 12% this week, on pace of its worst week since
February"

---

"Massive protests in Serbia against Rio Tinto’s lithium mining
ambition"

[[-]](https://balkangreenenergynews.com/massive-protests-in-serbia-against-rio-tintos-lithium-mining-ambition-pollution/)

---

Jane's Defense: "US Army donates [47] M1117 armoured security vehicles
to Greece"

---

Maybe some anti-vaxxers are just scared of needles. Should docs offer
anesthesia? Knock them out, apply the vax, done.

---

Someone was caught using one of those things, saw it on the news the
other day

---

🤣 🤣 🤣 

"Anti-vaxxer sells $1,500 prosthetic arm to escape getting vaccinated;
post goes viral"

[[-]](https://www.firstpost.com/world/anti-vaxxer-sells-1500-prosthetic-arm-to-escape-getting-vaccinated-post-goes-viral-10087731.html)

---

*Moonfall*, trailer looks promising.

---

Kayrros claims they have satellite based methane monitoring? Checked
out the site; need to open up ur data. 

---

UAE was busted while allowing a CH base construction.. Mending fences
w TR - which is fine. And now buying a lot of mil hard from FR. Some
changes over there.

"UAE signs ‘historic’ deal to buy 80 French-made Rafale fighter jets"

---

Dennis Miller on RT America? 

---

Looking at the [sunshine
map](https://pbs.twimg.com/media/FCtre5sWEAgFFp9?format=png&name=small)
for Africa again, the four countries with maximum sunshine are Libya,
Egypt, Chad, Sudan. All had lots of unrest recently.. In the South,
Angola, Namibia, Tanzania.

---

