<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>


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

Why the Poisson distribution usage in this [post](2021/08/bermuda.md)?
Event counts tend to be Poisson.. Let's take the London bombing example
(link below). They were wondering if bombings were clustering
at specific places. Cld be important.. Maybe Nazis were focusing
bombing somewhere? So Poisson is for natural counts, then if that is proven,
clustering is disproved.


[[-]](https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/abs/an-application-of-the-poisson-distribution/F75111847FDA534103BD4941BD96A78E)

---

Maybe they are Israelis from America. Their great-great-great
grandfather was kicked out by a Palestenian's great-great-great
grandfather, and, like, now they are totally back. 🤣

---

US teenagers there..? "Like, totally, a game changer, I liked eeiiiit"

---

Laboratory grown meat served a restaurant (they grow it right next
door actually), Israel.

<iframe width="340" src="https://www.youtube.com/embed/CzEDkMnJ5Bo?start=17" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

The tech is [too noisy](2021/03/unrivaled-beckley.md#sub)

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


