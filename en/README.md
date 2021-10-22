<img src="https://drive.google.com/uc?export=view&id=1B2wf9R7AMH1d7Vw6e2mucLbIQ5NSjir7"/>


Good for Barbados

"Barbados has elected its first president, a key step in preparations
to become a republic and remove Britain's Queen Elizabeth II as head
of state of the Caribbean island"

[[-]](http://u.afp.com/wZe6)

---

Hi-Fi Companions A Night In Trimisoara \#music

[[-]](https://youtu.be/jGw3EdlthWQ?t=58)

---

Literally ran that code while writing this post. So right now 25 mil
ratings, for 58K movies, by anonymous 280K users are in notebook's
memory. This is not a drill. We have ample computing capabilities..

---

How to? Full zip file is [here](https://grouplens.org/datasets/movielens/latest/),
unzip, then for example read all ratings with,

```python
from scipy.sparse import csr_matrix
import pandas as pd
r = pd.read_csv("ratings.csv")
m = csr_matrix((r.rating, (r.userId , r.movieId)))
```

Let's check the rating of user Id 2 for movie Id 2707

```python
m[2,2707]
```

```text
Out[1]: 3.5
```

*Arlington Road* apparently. Rating was 3.5 (out of 5.0)

.. and go from there. 

---

Big Tech marketing calls similarly rudimentary, or shoddy approaches
"AI", they are similarly wrong.

---

:) No it is not "AI". Just simple linear algebra

---

Algo chose this movie by [geek] reducing the user-movie rating matrix
through singular value decomposition and searching in the reduced
space for users matching my record, and recommending their top liked
movies. Since the matrix is sparse `csr_matrix` can be used, speeds up
the process [/geek].

---

My DIY recommender chose *Equalizer 2*. It was good 

---

"@astreaos

no emoji can replicate the sheer joy that this guy :D radiates"

---

The fluidic theories of course need to be tied to the rest of phy. An
advice to their theoreticians while they do that; feel free to ignore
parts of "known physics" as needed. Much of recent physics is a mess..
"Theory doesn't fit with CMB" shld be able to trigger "does that
matter?". That background could well be misinterpreted signals from
f-ing Jersey shore (instruments were [near there](https://bit.ly/2CMq76V))
and birdshit on the antennas.

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


