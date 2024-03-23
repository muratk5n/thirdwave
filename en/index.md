
The American Prospect: "The Airbus Advantage.. Why Europe’s mixed
economy produces safer planes than America’s financialized
capitalism.. Airbus’s clear leadership over Boeing in matters of
flight safety stem in good measure from their differences in ownership
and worker power—that is, from the European model of mitigating
laissez-faire capitalism with a measure of public and worker power,
and from the American model of subjecting corporate policy almost
entirely to the demands of investment institutions"

---

Turchin, *End Times*: "A key development in shutting down the wealth
pump [that transfers money from low income to high-income] was the
passage of the immigration laws of 1921 and 1924. Although much of the
proximate motivation behind these laws was to exclude 'dangerous
aliens,' such as Italian anarchists and Eastern European socialists,
their broader effect was a reduction in labor oversupply, something
that business elites were well aware of. Shutting down immigration
reduced the labor supply and provided a powerful boost to real wages
for many decades to come.

---

Being a "Semite" doesn't automatically imply Zionist, nor you are
scheming to end up in powerful positions. The majority manuevers them
into those positions, just like the disproportionate Catholic presence
at scotus, Jews can be overrepresented in some places. Need to
understand how the private industrial-Likud-complex thinks.. They
would prefer a guy who could be *a little more* anti-government due to
his minority status (as in scotus), *a little more* pro-genocide,
pro-Zionist due to this religious affiliation... These fuckers play
the odds. Very smart.. and they've been winning the long-game aren't
they?

---

Bama was surely accepted by the donor-controlled establishment before
prez, when he redistricted in Chicago (mmmhmmm, yes he did) the
regions he chose [tell the tale](0119/2008/07/obamas-district.html).
Affluent, rich, white collar regions were included, the Loop, Gold
Coast, with Republicans, and Jewish presence (most of whom were surely
Zionist dipshits).

---

Obamacare was [rebranded Clintoncare](2023/06/evil-geniuses.html#clintoncare),
let's not forget

---

"The Obama-Biden administration" seems to have dropped the ball,
missed a huge chance. 

Andersen: "[The Obama] administration and the Democratic congressional
leadership seem to have punted when it came to pushing for a law that
included a 'public option,' some form of Medicare-for-anybody coverage
that people could buy as an alternative to private insurance. For his
first few months in office, Obama seemed to be all for it, as did all
the Democratic chairs of all the congressional committees that would
create the reform law. But the insurance industry and the physicians’
trade group, the American Medical Association, were against it. The
most conservative Democrats in the House, the Blue Dog Coalition, were
iffy, but only a dozen of those fifty would be required to pass a
bill. Over the summer, however, Obama got publicly wobbly on the
public option—as Paul Krugman wrote at the time, “weirdly unable to
show passion on the issue, weirdly diffident even about the blatant
lies from the right”—and by Labor Day, the Democrats surrendered.

That same summer of 2009, Democrats also gave in to big business in an
important showdown with organized labor. A bill was moving through
Congress that had a provision to make unionization easier—instead of
winning a secret-ballot referendum in a workplace, labor organizers
would just have to convince a majority of the workers face-to-face to
sign up. The Business Roundtable lobbied hard against it. A few
moderate Democratic senators were persuaded—and without their votes
the forty Senate Republicans could kill the whole bill by sticking
together and filibustering it, so despite the (theoretically)
filibuster-proof majority, it got dropped. A year later big business
was still making sure that the measure stayed dead: on Business
Roundtable letterhead, the CEOs of Verizon and Caterpillar warned
Obama’s budget director that any such change remained “foremost among
our companies’ labor concerns” because it would have “a devastating
impact on business” and “significantly and negatively impact global
competitiveness, job creation and economic recovery.” As it happened,
six weeks after he got that letter, the OMB director left the
administration and soon went to work for a member of the Business
Roundtable, the CEO of Citigroup, as his vice-chairman of corporate
and investment banking"

---

Purchasing power for the bottom 40% rose under Trump fell under
Biden. As data points I use salary after tax measure from FRED, for PP
calculation, divide by CPI. The CPI measure represents cost of a
basket of goods, the calc in essense shows how many of those baskets
can people buy.

```python
df = u.get_fred(1990, ['CXUINCAFTTXLB0102M','CXUINCAFTTXLB0103M','CPIAUCSL']).interpolate()
df['Lowest 20%'] = df.CXUINCAFTTXLB0102M / df.CPIAUCSL
df['20-40%'] = df.CXUINCAFTTXLB0103M / df.CPIAUCSL
df[['Lowest 20%','20-40%']].plot(title='Purchasing Power of the Bottom 40%')
```

[[-]](https://cdn.fosstodon.org/media_attachments/files/112/132/794/157/946/164/original/c26ea48611c823b1.jpg)

---

If WWI caused WWII then there isn't much to learn from the second
war... Even the rise of fascism is, leaving aside the atrocities, a
symptom, an after-effect and we won't learn much from
after-effects. If people are in a bad situation economically, anything
can happen.. That should not be suprising. "Preparing" for the
after-effect, Nazism and such, is less effective than curing the
conditions that caused it. But the corp propagandists already know
that, they use misdirection, gaslighting for a reason. If you let
people down, you will pay the price.

---

*Beacon 23* S1, a mix of *The Expanse* and *Lost*. The boring parts
remind me of the latter. The leads were good, there were some nice
scifi ideas. 3 out of 5. I will check out S2.

---

Algeria vetoed too.. 

Al-Jazeera: "The United Nations Security Council has failed to pass a
United States draft resolution calling for, but not demanding, a
ceasefire in Israel’s continuing war on Gaza after two permanent
members chose to veto it"

---

Woodword was used like a chump in the process of Watergate. One of
modern journalism's main job is uncovering secrets, obviously the US
private complex and its surface state has the best ones.. But if you
are getting secrets from such sources, who is leaking to you, why? You
could be privy to info for a purpose, IMO that is exactly what the
confidential source did to Woodward. He was led around by the nose,
used, to take down someone who was essentially a good
president. Woodword's reporting was essentially a disservice to
society. He did better on his later books; but Watergate is a black
mark on his record.

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
