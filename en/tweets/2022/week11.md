# Week 11 

H2 Fuel News: "Unilever begins hydrogen fuel trial in its factory
boilers.. Unilever will be testing hydrogen fuel in the boilers of its
Port Sunlight factory located near Liverpool in the United
Kingdom. The decarbonization pioneering demonstration project involves
using low carbon H2. This hydrogen fuel test is a component of a
broader HyNet Industrial Fuel Switching program, which is focused on
the decarbonization of heavy industry in the northwest of
England. [The demo] is believed to be the first 100 percent H2 firing
demonstration of its nature in a consumer goods production
environment"

---

H2 View: "A brand-new hydrogen station is now fully operational in the
Netherlands – and it is refuelling 20 fuel cell buses in the town of
Heinenoord."

---

In my [costs](2022/02/costs-lcoe.md) doc I have the so-called nuclear
HTGR tech with a low LCOH (levelized cost of H2).  $17.55/Gigajoules
is pretty good. Initial (overnight) costs can be high, and there is
the waste issue, but hey, overall not too shabby.

H2 View: "Large-scale nuclear hydrogen generation to be explored in Ontario, Canada"

---

Power supply is tight..

The one pic I saw of Fin PM she had this Mmm-kay expression, now I
associate a lot of Fin news with that image; nuclear reactor on, had
to do it, m-kay?

WION: "Finland starts much-delayed nuclear plant, brings respite to power market"

---

Al Jazeera: "Oil concerns give Iran the upper hand in nuclear talks"

---

Gov is more at fault to be sure but most of the folks in Congress went
along with Russia Russia Russia when they didn't have to, and likely
contributed to a future crisis that could be averted.

---

Like 'we f--d shit up and hope now ppl forget we f--d shit up' kind of
clapping? I really wanna see that

---

Will there be clapping?

"Ukraine’s Zelenskyy to deliver virtual address to US Congress"

---

Dining Rooms - La Citta Nuda \#music

[[-]](https://youtu.be/qSElwl8aklw)

---

"Trumpublican"

---

Gravitas: US officials knew about China's Wuhan cover-up?

[[-]](https://youtu.be/j7X87oAKBuQ?t=10)

---

Most cryptos have predefined number of coins, no new money will be
created past certain time. Is this the answer?

I would not want a system that disallows new money creation by
design.. Money creation through private channels may not the way to
go, but through digital UBI maybe, which can be lent to businesses, as
"public credit"?

Such UBI could be somewhat inflationary but that's good, existing
wealth would be inflated away. 

---

'Private money creation has negative consequences' he says.. Because
it potentially allows limitless growth, with material usage
[implications](2021/03/less-is-more-hickel.md), and environmental
impact? He could be right.. 

---

He admitted bank credit is newly created money BTW. Most econs are not
even aware this is the case; their monkey theories always talk about
money being 'the veil of barter' - a completely false claim.

---

"In August the outgoing governor of the Bank of England, Mark Carney,
gave an interesting speech on ‘The growing challenges for monetary
policy in the current international monetary and financial system’, in
which he set out how the dollar based global monetary order is
untenable and will need replacing by a new system...

Carney has proposed a ‘synthetic hegemonic currency’ as a possible
basis for a new global monetary system. This would be comprised of a
number of central bank digital currencies (CBDCs), as put forward by
Positive Money. A CBDC would provide a trusted public alternative to
private banks’ monopoly on electronic money, and would move us towards
a system where commercial banks are not freely able to create new
money as debt, as they currently do to massive negative economic,
social and environmental consequences.

Carney said the introduction of such CBDCs would 'be to the benefit of
citizens and businesses', and is a reform to the monetary system which
'could happen.' In fact the Bank of England is currently exploring the
idea"

[[-]](https://positivemoney.org/2019/09/mark-carney-there-will-be-change-in-unsustainable-monetary-system)

---

The Times of India: "Kremlin doesn't rule out taking 'full control' of
major Ukraine cities"

---

The Independent: "What weapons does Russia have? The deadly arms Putin
could use in Ukraine war from cluster to vacuum bombs.. Thermobaric
rocket launchers have been seen moving towards Kyiv"

---

LA Times: "Russia strikes Ukraine army base near Poland as it widens
attacks"

---

Americans can ask their CIA, BDM used to do some work for them, they
should still have the code.

---

For full-blown game dynamic result talk to Dr Bruce M. He has a
consulting company now I hear.. But the final outcome will probably be
close to the one below.

---

68 suggests a final outcome closer to Russia's position. No Nato,
neutral, but maybe with some military presence, and some sanctions
remain in place?

---

```python
import pandas as pd, io
df = pd.read_csv(io.StringIO(data))

def weighted_mode(df):
    df['w'] = df.Clout*df.Salience 
    df['w'] = df['w'] / df['w'].sum()
    df['w'] = df['w'].cumsum()
    return float(df[df['w']>=0.5].head(1).Position)    
def mean(df):
    return (df.Clout*df.Position*df.Salience).sum() / \
           (df.Clout*df.Salience).sum()

print ('mean voter %0.2f' % mean(df))
```

```text
mean voter 68.83
```

---

I assigned salience 70 to US, bcz strategically I dont think they give
a shit; stuff goes bad, Russia is outcast, EU-RU relation is screwed,
they still win.

---

Here is my raw data. Agree?

```python
data = """
Stakeholder,Clout,Position,Salience
Russia,70,100,100
Ukraine,40,40,100
USA,80,40,70
Europe,50,60,100
China,60,80,100
India,40,80,80
"""
```

---

Encode decision range as 0: Sanctions, Ukraine gov remains, no promise
on Nato, pre-war status continues, 100: All sanctions lifted, Ukraine
is neutral, demilitarized, no Nato.

---

[Link](https://drive.google.com/uc?export=view&id=1XHVZ3G6muR29BGSAsV2zBOqtn9TIvJHA)

---

[Link](https://drive.google.com/uc?export=view&id=1GFoFGDg3N0PcnkrbW0lwUGjHwmmD0G-Y)

---

Curious abt the "mean voter position" of the UKR-RU dynamic, talks,
per [here](2015/07/mesquita-game-theory-greece.md). Cranking some
numbers...

---

Not referring to anything current

---

*qui Deo placeat et utilis sit regno*.. Nice

---

Arab News: "Cashless and flightless, Russian tourists stuck in Thailand"

---

CNBC: "Federal Reserve expected to raise interest rates in week ahead, as
Ukraine crisis adds volatility"

---

CNBC: "Russia restricts Instagram after its parent Meta allows violent
threats against military for Ukraine invasion"

---

Reuters: "Facebook allows war posts urging violence against Russian invaders"

---

CNBC: "Russian-backed cable news network RT America shuts down"

---

"Andrew Bacevich: Ukraine is Paying the Price for the U.S. 'Recklessly'
Pushing NATO Expansion"

[[-]](https://youtu.be/kCntlkpdr0k?t=89)

---

F24: "Russia forces encircle Kyiv and continue Mariupol siege"

---

RFERL: "Russia Says It Could Target Western Arms Supplies To Ukraine"

---

\#hedges \#justwar

[[-]](https://youtu.be/FVWIDi4mceg?t=972)

---

\#refugees 

[[-]](https://pbs.twimg.com/media/FNocmtIWQAEyI5O?format=jpg&name=small)

---

Ironically the mapping software itself, Leaflet, is written by a Ukranian.

---

My GDELT conflict map around Ukraine became massive (too many data
points, over 800 attack reports in 5 days). Had to downsample,
otherwise UI isn't responsive.

[[-]](2019/05/confstats.md#gdeltukr)

---

WION: "As the situation intensifies in Ukraine, with Russia dropping
bombs every day, one of the world's best snipers, 'Wali', has arrived
in the embattled nation to help them fight the Russian forces. He is a
veteran of the royal Canadian 22nd regiment"

---

