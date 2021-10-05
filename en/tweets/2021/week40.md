# Week 40


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hyundai Motor Group&#39;s Chairman, Euisun Chung, has announced that it will become the first global automaker to apply hydrogen fuel cells to all commercial vehicle (CVs) models by 2028. <a href="https://twitter.com/Hyundai_Global?ref_src=twsrc%5Etfw">@Hyundai_Global</a> <a href="https://t.co/0NTEc3woWq">pic.twitter.com/0NTEc3woWq</a></p>&mdash; Autocar India (@autocarindiamag) <a href="https://twitter.com/autocarindiamag/status/1435127959916924934?ref_src=twsrc%5Etfw">September 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

"New Rules from #European Parliament on Energy Infrastructure: “Boost
Hydrogen & Carbon Capture, Phase Out Natural Gas”. No more financial
support for natural gas projects. Funds should support hydrogen,
CCS"

[[-]](https://bit.ly/3upBRH5)

---

"Storing Hydrogen Safely: Fraunhofer-Institut für Windenergiesysteme
IWM Evaluates Materials For Tubular Storage Systems in the joint
project H2Wind"

[[-]](https://bit.ly/2Yp71Tb)

---

Coal prices are through [the roof](2019/05/stats.md#coal)

---

JC was not a miscast! He was better than this new guy.. The key to
impressions is to catch a key characteristic. JC's angle is a
pent-up-anger shtick which of course reminds you of *Pet Detective*,
or *Liar Liar*, it was good.

TDB: "Last season, Saturday Night Live navigated its way through the
transition from Trump to Biden, first by miscasting Jim Carrey
opposite Alec Baldwin.. 47th season [opened w]ith one of its brand new
cast members, James Austin Johnson as the 46th president"

---

Europe's answer to DARPA, Joint European Disruptive Initiative -
[JEDI](https://www.jedi.foundation/)

\#F24

---

Darpa funded the first mRNA tech in 2013 - the basis of today's
Moderna and Pfizer vax

\#F24

---

I have to say this is a fantastic application of mathematics to a
real-world problem. Based on two numbers the formula generates
near accurate counts for the entire grid structure. V cool.

---

Poisson distr is,

$$ f(x) = P(X=x) = e^{-\lambda}\frac{\lambda^{x}}{x!} $$

which gives probability of 1 event, 2 events, in a certain block of
time. But in geo you have to think little differently. You divide
London into grids, and count how many bombs fell on each, then count
how many grids had 1 bomb, 2 bombs, etc. Reproducing such counts from
formula,

```python
N = 576.
m = 537/N
c = N*np.exp(-m)
expb = [c*1, c*m, c*m**2/2, c*(m**3)/(3*2)]
[np.round(e,2) for e in expb]
```

```text
Out[1]: [226.74, 211.39, 98.54, 30.62]
```

Real counts were 229, 211, 93, 35, etc. Pretty close. I am sure a
statistical test wld agree. Clustering disproved. 

---

Why the Poisson distribution usage in this [post](../../2021/08/bermuda.md)?
Event counts tend to be distributed that way.. Let's take the London
bombing [example](https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/abs/an-application-of-the-poisson-distribution/F75111847FDA534103BD4941BD96A78E).
They were wondering if bombings were clustering at specific places.
Cld be important.. Maybe Nazis were focusing bombing somewhere? Poisson
is for natural counts, then if that is proven, clustering is disproved.

---

Maybe they are Israelis from America. Their great-great-great
grandfather was kicked out by a Palestenian's great-great-great
grandfather, and, like, now they are totally back. 🤣

---

US teenagers there..? "Like, totally, a game changer, I liked eeiiiit"

---

Laboratory grown meat served in a restaurant (they grow the meat right
next door actually), Israel.

<iframe width="340" src="https://www.youtube.com/embed/CzEDkMnJ5Bo?start=17" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

The tech is [too noisy](../../2021/03/unrivaled-beckley.md#sub)

"China has nuclear subs too"

---

Affirmative action works

"California outlawed the all-white-male boardroom. That move is
reshaping corporate America"

---

BBC: "Climate change: Stop smoke and mirrors, rich nations told"

---

"An ecologically minded experiment to make Paris a cycling capital of
Europe has led to a million people now pedaling daily — and to rising
tensions with pedestrians."

---

