
Business Green: "UK Infrastructure Bank makes first green hydrogen
investment.. Public investment bank announces £30m of funding for
hydrogen power unit maker GeoPura The UK Infrastructure Bank (UKIB)
has announced its first ever green hydrogen investment, confirming a
£30m investment in a manufacturer of hydrogen power units.

The deal forms part of a £56m fund raising round completed by GeoPura
to support the roll out of hydrogen power units that can replace
emissions-intensive diesel generators. GeoPura is aiming to deploy a
fleet of more than 3,600 hydrogen power units by 2033 from its hubs in
Nottingham, Matlock, Sheffield, and Newcastle. The firm is also hoping
to become a supplier of renewable hydrogen, as part of a joint venture
with JG Pears to undertake green hydrogen production at the site of an
old power station in the East Midlands.

---

Nobel Prize–winning economist Gary Becker's mentor was Milton
Friedman. And Becker was a mentor to the junk bond felon Mike
Milken. Dam cuh

---

Even Swedes got part of the action.. 

Africa News: "[2023/09] Two former executives at a Swedish oil company
go on trial in Stockholm on Tuesday accused of complicity in war
crimes committed by Sudan's regime between 1999 and 2003. Swede Ian
Lundin and Swiss national Alex Schneiter are accused of asking Sudan's
government to make its military responsible for security at the site
of one of Lundin Oil's exploration fields, which later led to aerial
bombings, killing of civilians and burning of entire villages,
according to the prosecution"

---

"[2001] The scorched earth: Oil and war in Sudan.. [A] report.. shows
how the presence of international oil companies is fuelling the
war... In the name of oil, government forces and government-supported
militias are emptying the land of civilians, killing and displacing
hundreds of thousands of southern Sudanese. Oil industry
infrastructure - the same roads and airstrips which serve the
companies - is used by the army as part of the war. In retaliation,
opposition forces have attacked government-controlled towns and
villages, causing further death and displacement"

---

Chevron in Sudan? Say no more. There is your culprit.

"There is chaos in Sudan. Do you think involvement of Chevron contributed... "

---

Butler, *War is a Racket*: "[1935, A key] step in this business of
smashing the war racket is to make certain that our military forces
are truly forces for defense only.  At each session of Congress the
question of further naval appropriations comes up. The swivel-chair
admirals of Washington (and there are always a lot of them) are very
adroit lobbyists. And they are smart. They don’t shout that 'We need a
lot of battleships to war on this nation or that nation.' Oh,
no. First of all, they let it be known that America is menaced by a
great naval power. Almost any day, these admirals will tell you, the
great fleet of this supposed enemy will strike suddenly and annihilate
our 125,000,000 people. Just like that. Then they begin to cry for a
larger navy.  For what?..

The ships of our navy.. should be specifically limited, by law, to
within 200 miles of our coastline. Had that been the law in 1898 the
Maine would never have gone to Havana Harbor. She never would have
been blown up. There would have been no war with Spain with its
attendant loss of life. Two hundred miles is ample, in the opinion of
experts, for defense purposes. Our nation cannot start an offensive
war if its ships can’t go farther than 200 miles from the coastline.
Planes might be permitted to go as far as 500 miles from the coast for
purposes of reconnaissance. And the army should never leave the
territorial limits of our nation"

---

The `corr` function returns values between -1 and 1. Negative value
for rates and prices make sense, lower rates do push house prices up.
But excessive wealth concentration has 5 times the effect compared to
any rate changes.

---

Rate rises did not help lowering house prices. Analysis below shows
the highest correlation is between high wealth and house prices, not
between rates and house prices. 

```python
df = u.get_fred(2000,['FEDFUNDS','MSPUS','WFRBST01134'])
df.columns = ['rate','house price','top 1% wealth']
df = df.interpolate()
df.corr()
```

```text
Out[1]: 
                   rate  house price  top 1% wealth
rate           1.000000    -0.121352      -0.327207
house price   -0.121352     1.000000       0.766769
top 1% wealth -0.327207     0.766769       1.000000
```

---

Inequality skews demand towards the upside. A median house cannot cost
nearly half a million fucking dollars. This is serious, as in
pitchfork level serious.

---

NBC News: "New data shows the median sale price for a home rose to
nearly $380,000 in January — the seventh increase in a row"

---

Euronews: "Spain is banning some short-haul domestic flights as part
of its plan to reduce carbon emissions... Flights with a rail
alternative that takes less than two and a half hours will no longer
be allowed, 'except in cases of connection with hub airports that link
with international routes'"

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


