<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>

---

H2 View: "[DNV, independent risk management org] assess hydrogen
pipeline possibilities in Hungary.. Hungary is looking to decarbonise
its gas grid with hydrogen as it strives to achieve climate neutrality
by 2050"

---

H2 View: "According to a new report from Rethink Energy today.. the
impending hydrogen revolution will send shockwaves throughout the
energy market and prompt one of the largest shakedowns in its
history."

---

H2 View: "South Korea and Saudi Arabia prepare hydrogen talks.. The
South Korean President, Moon Jae-in has arrived in Saudi Arabia to
discuss various topics with Crown Prince Mohammed bin Salma with
hydrogen set to be a key aspect."

---

"IRENA: Hydrogen could cover up to 12% of global energy use by 2050,
with over 30% of the energy carrier being traded across borders, a
higher share than natural gas today"

---

H2 View: "Australia’s Fortescue Future Industries (FFI) is set to
supply high-tech polymer materials supplier Covestro with up to 100,00
tonnes of green hydrogen equivalent annually"

---

What happens if there's an earthquake near the storage site? One
shudders at the thought.

---

That is what it takes to keep nuke waste away...

[[-]](https://youtu.be/kYpiK3W-g_0?t=286)

---

I mean, seriously, how could this stuff *not* leak, especially at the
end-user level? Pipeline goes into homes, into some crack-ass
mechanism built by god-knows-who, with average design.. Unless it was
built with complete containment in mind, which in regular market
conditions would be hard, and hard to regulate, stuff would invariably
leak.

---

Yep - natgas pipelines leak. The end user (home/business) leaks,
possibly worse.  Fossil in any shape or form should not move from
source to customer, bcz anywhere in that chain it can leak. The only
thing that moves, and used at end-user must be green fuel.

"The study suggests many of these [natgas.. ] leaks come from homes and
businesses.. The team's analyses suggest the five biggest urban areas
studied—which together include about 12% of the nation's
population—emit about 890,000 tons of methane each year.. The vast
majority of that, at least 750,000 tons, comes from methane leaks from
homes, businesses, and gas distribution infrastructure"

[[-]](https://www.science.org/content/article/major-us-cities-are-leaking-methane-twice-rate-previously-believed)

---

Asia Minor culture has lots of Greek in it, as well as early Celts,
Christianity, then Islam. As the discoverer of organized farming the
region has the longest experience with the structures around it, ie
feudalism. But of course, thanks to varied fresh ingredients good
gastranomy. Migrants arriving into that such as "Turks" were
assimiliated. Their arrival on the whole pretty much meant nothing.

---

One such fritters is widely prepared known in Asia Minor, called
*mücver*. The dish is actually based on a Greek one (like many other
things) *kolokithokeftedes*.  Vegans can subtract the eggs, and put
other ingreds in its place.

---

People just want a pill for everything. Potassium can serve as muscle
[relaxant](https://www.goodhousekeeping.com/health/diet-nutrition/g796/sleep-inducing-foods/),
zuccini, bananas; do fritters for the former, eat that at night

"I want to sleep better, which drug does that?"

---

When u calculate it from principles, the number hits you all of a
sudden with how much energy it indicates. Lot is spent on heating..

I look at the params used, we have leaky homes.. The constant used is
actually high (bad insulation). Bulding materials are shit. Styrofoam
has conductivity of 0.01, one **80th** of concrete brick. Can't we mix
some of that shit into the building materials? Isn't this stuff cheap?
We all used styrofoam cups right? It's light, cheap ass shit.

---

We can use the heat conduction formula due to Fourier,

$$
P = \frac{dQ}{dT} = \frac{k A (T_2 - T_1)}{d}
$$

Formula will calculate the power of the heat transfer between two
temperatures, for our needs from an ideal inside to a known
outside. Therefore to keep the inside at that temp level, we'll know
how much power we have to add in the inside (with a heating unit).

Formula needs surface size $A$, the surface through which heat flows
(or leaks), which will be all four walls roof and floors. Material
heat conductivity $k$, wall thickness $d$, a target temperature $T_2$,
and outside temperature $T_1$.

Target temperature is room temperature 22 degrees C.

Outside temperature can be annual world average temperature (the one
that keeps rising, and everyone is freaked out about), 13.7 deg C. We
can assume it's always at that level outside for everyone all the
time, and people want room temperature on the inside. What was that
movie line? "It's chilly outside, and it's Chilly inside". We just
want chilly outside.

Home sizes differ from country to country, as average we'll take
Denmark, 150 m2. Multiply by 4 meter height, get home volume. Assume a
cube for volume, so we w/ cube root calc one side, then using sides
side^2 x 6 gives a complete outside surface area.

Material heat conductivity? Units $W/m \cdot C$, or $J/s \cdot m \cdot C$.
We have concrete brick 0.84, plasterboard 0.16, wood 0.10. I dont know..
what would average material be? Better than mere bricks, but little worse
than wood? Let's take 0.15.

We'll further assume 4.2 people per home (I looked this up), a 2013
world population of 7.17 billion (I am trying to reach an annual
energy needed for heating, worldwide), so


```python
ppl_per_home = 4.2
pop = 7.17*1e9 # world 2013
world_t =  13.7 # C
room_temp = 22
home_vol = 150*4 # m3
d = 11 # cm, wall width
k = 0.15 # W/m*C = J/s*m*C

side = np.power(home_vol,1/3.)
A = (side**2)*6

P = k*(room_temp-world_t)*A / (d*0.01)

total = (pop/ppl_per_home)*P*24*365
print ('home heating %d twh' % (total / 1e12))
```

```text
home heating 72244 twh
```

The entire world energy consumption for that year was 157,481
Terrawatt Hours. The number above is a good chunk of that.

---

Don't believe the previous home heating calculation? It used a
precooked constant.. It's good to doubt.. Let's dig in the basics (see
above).

---

"@jasonhickel

The ten richest billionaires have doubled their wealth during the
pandemic... and 160 million have been pushed into poverty"

---

CNBC: "The pandemic has made the rich richer while the income of the
rest of the world — about 99% of humanity — dropped, according to a
new Oxfam report titled 'Inequality Kills.'"

---

"@benphillips76

Inequality kills"

[[-]](https://twitter.com/benphillips76/status/1482963054887415808)

---

Tryna help a brother here.. Pitchforks will be coming 4 your ass, not
mine..

---

Not saying get rid of money now.. How about single-payer?

---

Trek TNG episode S01E26; Crew rescues three humans preserved in cryo
from 20th century. They wake up, one guy is a fin speculator, he keeps
wondering about his portfolio Picard nearly decks him. In fact the
entire episode is written just to shit on that guy.

---

He wanted a female first officer yes. Great... But let's remember the
(Trek) universe has **no money**. So, no. He was a full-blown
progressive not a lukewarm tool.

"Gene Roddenberry always wanted to have a female first officer in the
ship, was he a Dem style shitlib?"

---

Tetris - Morning Glory \#music

[[-]](https://youtu.be/RwmWZ0B5GAg)

---

It's a nice act, but systemic fix is better.

---

He used to drive a hummer now he doesn't have a condo. I bought him a
house so he could live

"Arnold Schwarzenegger celebrated the holiday season by donating 25
tiny homes to homeless veterans"

---

Jane's Defence: "UK supplies anti-tank weapons to Ukraine"

---

The India-Philippines missile sale is a big deal; first of all, the
missile was a joint RU/IN product. CH should not count on RU as a
staunch ally, or anyone in that region for that matter. The missiles,
with considerable capability, were sold to PH, other nations there
showed interest. Supersonic missile with 400 km range. No joke.

---

Awww.. more *emmerder* for my boy Novax. [Denied](https://drive.google.com/uc?export=view&id=1j4y1VQ6ROeu_a9gJbT5Z89zrjIgDbmiR).

Reuters: "No vaccine, no French Open for Novak Djokovic, says French
Sports ministry"

---

But Novax is setting a bad example. Serbia's vaccination rate is below
50%.. so kinda funny haha, and kinda not.

---

Haha some nicknamed Novak Djokovic as *Novax* Djokovic.. good one

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


