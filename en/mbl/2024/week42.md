# Week 42

Manufacturers Monthly: "Construction begins on $65 million VIC
renewable hydrogen park...The Gas Appliance Manufacturers Association
of Australia (GAMAA) has welcomed a milestone in renewable hydrogen as
construction commenced on the 65.46 million Hydrogen Park Murray
Valley near Wodonga, Victoria"

<img width='340' src='https://www.manmonthly.com.au/wp-content/uploads/2024/05/AdobeStock_667048929-768x563.jpeg'/>

---

Politico: "The nation’s housing affordability crisis has become so
acute that even our presidential candidates are paying attention to
it...

But the number of  housing units in the nation has grown faster than
the number of households since the turn of the century. Something else
is happening here.

That’s because demand for real estate is not just about the number of
people who need homes, it’s also about the amount of money buyers are
bringing into the market. People without money cannot push up
prices. It’s the people with money — especially those with a lot of
money — who drive up prices for everyone else"

---

"@andrewdessler@mastodon.world

if only scientists had been predicting this"

<img width='340' src='https://s3.eu-central-2.wasabisys.com/mastodonworld/media_attachments/files/113/295/826/443/187/617/small/68e8fbefee374007.png'/>

---

Schahill, *Blackwater*: "[Naomi] Klein, who traveled to Iraq during
Bremer's tenure in the country and has written extensively on.. the
effects of his edict-based governance as such:

>[Bremer] enacted a radical set of laws unprecedented in their
>generosity to multinational corporations. There was Order 37, which
>lowered Iraq's corporate tax rate from roughly 40 percent to a flat 15
>percent. There was Order 39, which allowed foreign companies to own
>100 percent of Iraqi assets outside of the natural-resource
>sector. Even better, investors could take 100 percent of the profits
>they made in Iraq out of the country; they would not be required to
>reinvest and they would not be taxed. Under Order 39, they could sign
>leases and contracts that would last for forty years. Order 40
>welcomed foreign banks to Iraq under the same favorable terms. All
>that remained of Saddam Hussein's economic policies was a law
>restricting trade unions and collective bargaining...

It seems appropriate, then, that Bremer, the senior U.S. official in
Iraq, the public face of the occupation, would not be protected by
U.S. government forces or Iraqi security but rather by a private
mercenary company"

---

"@antijingoist@hackers.town

Actually yahoo search has been pretty good recently

*changes defaults*"

---

Need I remind people 1979 Iranian revolution saw expulsions and even
execution of a lot of high-ranking officials in the Iranian military,
yet the country was able to fight the Iran-Iraq war that would start
only a year later, with what was left.

---

*Penguin* is still going strong, S01E03.

---

"@sluttymayo@jorts.horse

Modern technology is great. A rich guy will be like 'our new
innovation is an app for ignoring the regulations around something
that already exists. This will let everyone make money via a sort of
petty landlordism'

Then they burn heaps of investor money for like a year while people
start to depend on it because they undercut everything else, then they
just take all the money that the gig workers had been making and turn
those petit landlords back into serfs"

---

Leaders of TR, Czechia, FR have low net approvals.. -30%, -52%, -56%
respectively.. Data for Sept. 25-Oct. 1.

[[-]](https://morningconsult.com/global-leader-approval)

---

"@nobodyinperson@fosstodon.org

Looks like the @unituebingen won't continue its \#Matlab license due
to the high cost and lack of state partners to share the financial
load.

I very much appreciate this! This is money better spent
elsewhere. Teach students \#Python, #Rstats et al., not some weird
proprietary software they can't use freely afterwards.

Now let the heated discussions in the institutes begin 😉 🍿

Glad that we @umphy are using #FOSS"

---

\#MSNBCB \#TaNehisiCoates

[[-]](https://www.youtube.com/embed/Had6L6O_KtA?start=216&end=301)

---

Enjoy your rules-based order

---

Let's note the situation is not one of ISR shoots at Hezbollah but
hits UN who are also in the area. No. ISR wants UN out of there, so
they shoot directly at UNIFIL soldiers, to force them out.

---

Hassan Jouni: "[Israel] wants the fighting space to be open to the
Israeli military.. UNIFIL forces [in Lebanon] hold important and
sensitive positions they could hinder the process of the Israeli
military. If they withdraw, these positions could see heavy clashes
between the Israeli army and Hezbollah"

---

The Guardian: "‘Not a normal war’: doctors say children have been
targeted by Israeli snipers in Gaza"

---

Some pushback from SAF. Gains west of Sennar, Khartoum and around Bakhit.

\#Sudan \#SAF \#RSF \#Frontline 09/25 - 10/14

[[-]](sdndata/map6-ext.html)

---

They could've performed tests.. possible. Politically time is right for it.
I'm just saying it's not clear in the data.

---

Quakes together with NPP and other facilities.. Not sure if there is a pattern.

```python
import json
irn = json.loads(open("iran-nuke.json").read())
irn.update(res)
u.map_coords(irn, zoom=7, outfile="map7.html")	    
```

[[-]](map7.html)

---

Locations of quakes, one in the North one in the South

```python
res = dict((k + " magnitude:" + str(v['mag']),
            [v['lat'],v['lon']]) for k,v in df.iterrows())
u.map_coords(res, zoom=4, outfile="map6.html")	    
```

[[-]](map6.html)

---

Data is from USGS.

---

There were not one, but two quakes

```python
df = u.eq_at(35.59431085, 53.395109027, 800, 8)
df
```

```text
Out[1]: 
                     mag      lat      lon  ago
date                                           
2024-10-05 06:29:26  4.1  32.3247  56.4756    8
2024-10-05 22:15:34  4.5  35.3597  52.8989    7
```

---

Earthquakes in Iran.. were they nuclear weapon tests?

---

Al-Monitor: "'Very challenging': Israel faces Hezbollah in tricky
terrain..As Israel undertakes its fourth ground offensive in southern
Lebanon in 50 years, its troops again face rocky terrain mined with
explosives and full of hiding places that previous generations of
soldiers have battled over"

---

F24: "Israel's decision to begin ground attacks against Hezbollah in
Lebanon has sparked a debate about the wisdom of opening up a second
front and presents Israeli soldiers with a different challenge from
the dense urban environment of Gaza. Analysts believe Hezbollah has
built an intricate network of tunnels cut deep into the hills of
southern Lebanon, a tall order for the Israeli military."

---

F24: "Forty nations that contribute to the UN peacekeeping force in
Lebanon said in a statement on Saturday that they 'strongly condemn
recent attacks' on the peacekeepers."

---

