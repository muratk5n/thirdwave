# Week 36

"@prettyhuman@piipitin.fi

1000 richest people are approched. 'The end of the world is here. Time
to go to your doomsday bunker', they are told. The billionaires
nodded. They knew this was coming. They were prepared.

So they gathered their loved ones and locked themselves in luxury
bunkers. No contact to outside world.

10 years later they emerge. The world has healed. The air is
breathable, people are happy. 'What was the catastrophy?' they ask the
first person they meet.

She screams: "THEY GOT OUT!!!""

---

Sirota: "One study found that for every 1 dollar of corporate
donations, a business gets more than $6 of state tax breaks. Another
study found a correlation between unlimited campaign spending and a
reduction in corporate taxes. Still another study found that the more
freely corporations are allowed to spend in elections, the more likely
lawmakers are to pass laws that protect corporate management"

---

The article mentions McCain who achieved some success on campaign
finance only to see this work overturned by SCOTUS due to a new
pro-rich tilt of the institution thanks to the *masterplan*. The
sabotaging of Harriet Miers nomination was one of those acts. I
remember the media storm around Miers, one corp pundit even called her
"the cleaning lady" (she was W's personal lawyer). Corporate powers
got their wish, her nomination was withdrawn, more corp friendly judge
(Samuel Alito) was appointed who played a crucial role later in
the *Citizens United* ruling.

---

Sirota, *Rolling Stone*: "Th[e] untold story [of corruption] began a
half century ago amid a golden age of democratic reforms. As America’s
government was responding to public discontent by creating Medicare,
Medicaid, environmental regulation, and a war on poverty, a genteel
tobacco industry lawyer authored a 1971 manifesto sounding an
alarm. In his now-famous memo, the soon-to-be Supreme Court justice
Lewis Powell cast corporations and oligarchs as persecuted victims,
and urged them to use their outsized resources to assume 'a broader
and more vigorous role in the political arena' to halt a government
becoming too responsive to popular demands...

Some have cast Powell’s blueprint as little more than a 1970s version
of a meaningless Reddit rant rather than the foundational text that
some liberals believe it to be. But if anything, the significance of
Powell’s screed has been understated... [I]n response to the memo,
leaders of the country’s most powerful corporations organized task
forces to implement its directives. One of their goals was
deregulating the campaign finance system. Why? Because they understood
that in a properly functioning one-person-one-vote democracy, they
would never be able to gain control of the political system and enact
their self-enriching, wealth-concentrating agenda. They knew that to
get their way, they must be allowed to buy elections, legislation,
court rulings, and public policy.

And so in short order, corporations and moguls inspired by Powell
began funding think tanks, political advocacy organizations, and
conservative law firms — and victories followed. First, with the
support of conservative philanthropist John Olin’s political machine,
Congress quietly added loopholes to the post-Watergate anti-corruption
laws allowing for the explosion of corporate political action
committees that could buy legislators... These early wins unleashed a
tidal wave of corporate money flooding into politics, which birthed an
era of neoliberal tax, deregulatory, and anti-union policies, just as
the master planners wanted. It also delivered an attendant epoch of
corruption scandals, from Abscam, to the Keating Five, to Enron, to
Jack Abramoff and the K Street Project"..

[[-]](https://www.rollingstone.com/politics/political-commentary/trump-harris-supreme-court-corruption-2024-election-1235091964/)

---

The Verge: "Opening your Threads account up to the fediverse is as
easy as a click..

- On Threads’ mobile app, tap your profile icon in the lower-right
  corner, tap the two lines in the upper-right corner, and select
  Account > Fediverse sharing.

- On the web version, tap the two lines in the upper right, then
  select Settings > the Account tab > Fediverse sharing"

---

How come email was interoperable from the start? Because when people
started using the Internet it already had email and the service was
already being provided by diverse server software. It was too late for
any single commercial player to monopolize it. Social networks were
not this lucky.

---

Requiring social network to interoperate over ActivityPub is like
requiring email servers to talk to each other, GMail being able to
send messages to Yahoo Mail (which they can do now, over another
protocol called SMTP).

---

"Beaches are for people who enjoy the bureaucracy of going to the
beach"

[[-]](https://interconnected.org/home/2024/08/29/beaches)

---

Mentioned this before, every piece of code, every data file used in these
pages can be retrieved from the site itself. Below there is a reference to
`schiller.csv`, that file can be retrieved via `/en/mbl/2024/schiller.csv`
[here](schiller.csv). Data / code resides in the same directory
as the article.

---

SP 500 data, combined with Schiller PE, shifted by 10 years,

```python
df = util.get_yahoo_tickers(1900, ["^GSPC"]).columns = ['SPY']
df = df.resample('MS').mean()
df = pd.read_csv('sp500.csv',index_col='Date',parse_dates=True)
df['schiller'] = pd.read_csv('schiller.csv',index_col='Date',parse_dates=True)['Schiller']
df['SPY10'] = df.SPY.shift(-12*10)
df['chg'] = ((df.SPY10 - df.SPY) / df.SPY)*100
u.two_plot(df.chg, 'spy', df['schiller'], 'schiller')
```

<img width='340' src='https://cdn.fosstodon.org/media_attachments/files/113/060/585/549/753/822/small/f68942145f31ea1e.jpg'/>

It looks correct.

Note recent Schiller trend is up (overvaluation) so the market must
come down, 10 year returns are about to go to the gutter if this
thesis is correct.

---

Looking at SP 500 10-year returns since 1920s. One signal people use
is overlaying Schiller's P/E ratio on top, lows and highs arrive 10
years after the market is most expensive and cheapest, respectively.
If the shifts are done right, the two graphs should show
perfect reverse correlation.

---

Al-Monitor: "Israel set for general strike after Gaza hostages found dead"

---

Fear and greed index not looking good... \#SP500

```python
import requests, pandas as pd
url = "https://api.alternative.me/fng/?limit=0&format=json"
response = requests.get(url).json()['data']
cols =['timestamp', 'value','value_classification']
df = pd.DataFrame(response, columns=cols).set_index('timestamp')
df.index = pd.to_datetime(df.index, unit='s')
print (df.head(10))
```

```text
           value value_classification
timestamp                            
2024-08-31    29                 Fear
2024-08-30    34                 Fear
2024-08-29    29                 Fear
2024-08-28    30                 Fear
2024-08-27    48              Neutral
2024-08-26    55                Greed
2024-08-25    54              Neutral
2024-08-24    56                Greed
2024-08-23    34                 Fear
2024-08-22    39                 Fear
```

---

Clearly thought leaders were able to change the discourse in a new
direction. Time to build on this, expand and implement.

---

"Americans overwhelmingly oppose corporate monopolies and believe big
businesses have amassed too much power and influence, according to a
major new poll of seven geographically diverse states commissioned by
More Perfect Union Foundation"

[[-]](https://substack.perfectunion.us/p/new-poll-government-must-take-on)

---

"@rms@mastodon.xyz

60% of Americans think big business is too powerful.  But the
politicians who protect business's power will continue call
themselves, misleadingly, 'centrist'"

---

Hanson's model is a quintessential American one.. talks of expansion,
dreamy shit that is unfounded that lends itself easily to scifi,
flashy, marketable narrative delivered by a Feynman-like energetic
speaker conjuring up a mad scientist image whose words are
interspersed with jokes. We should've learned not to expect much from
this type... US, and Americans have not been good stewards of
sciences.

---

Colonizing (grabby) aliens model.. first time Im hearing it oddly
enough, it made huge waves a year ago.. Interesting, the math is fine
but if a few of its assumptions are incorrect the model will come
apart... [Desslers idea](../../2024/01/fermi-paradox.html), or the great
filter theory is more likely.

---

BTW AP is an open standard World Wide Web Consortium played a role in
its design, which puts it at the same level as HTML, WebAssembly, CSS,
truly foundational technologies.

---

Crazy coincidence... Now go implement ActivityPub bitch

Wiki: "Lantian 'Jay' Graber.. is an American software engineer and the
CEO of Bluesky.. Graber was born in 1991 in Tulsa, Oklahoma. Her
mother named her Lantian, meaning 'blue sky' in Mandarin Chinese"

---

Governments need to mandate interoperability between messaging
platforms, Threads users should be able to see Bluesky users and vica
versa.. They can all adapt a common protocol (Threads did this
already), the one Mastadon uses, ActivityPub is ready and
available. Gov could encourage them towards this adoption. It will
benefit consumers, as the move will increase competition. Platforms
will compete on the speed, ease-of-use of their software as they won't
be able to keep users simply by being the one platform you *have* to
be on in order to communicate.

---

"@Daojoan@mastodon.social

twitter brazil gone. mass exodus to bluesky"

---

BBC: "X, formerly Twitter, has been banned in Brazil after failing to
meet a deadline set by a Supreme Court judge to name a new legal
representative in the country... Alexandre de Moraes ordered the
'immediate and complete suspension' of the social media platform until
it complies with all court orders and pays existing fines"

---

Diehl: "[A study](https://www.sciencedirect.com/science/article/abs/pii/S0269749122017663)
published on Science Direct in 2023, Outcomes of the Halliburton
Loophole: Chemicals regulated by the Safe Drinking Water Act in US
fracking disclosures, 2014–2021, reveals that fracking companies used
over 282 million pounds of hazardous chemicals from 2014 to 2021 with
ZERO federal oversight..

The paper is the first to examine the 'Halliburton Loophole' which
exempts fracking from federal regulation provided by the Safe Drinking
Water Act. The exemption was passed by Congress as part of the Energy
Policy Act of 2005, and endorsed at the time by Vice President Dick
Cheney, not coincidentally the former CEO of Halliburton, the world's
second-largest oil service company also responsible for most of the
world's largest fracking operations.

I could easily go on about Halliburton famously profiteering from a $7
billion closed bid contract in the Iran-Iraq War, or their involvement
in the Deep Water Horizon oil spill, and a litany of other
environmental crimes... Let’s just point out that Cheney retired from
Halliburton [before VP] with a 36 million severance package. Then
Halliburton got a 7 billion contract [during Dubya-Dick
admin]. Coincidence, I’m sure"

---

Diehl: "In 2005, when fracking ramped up on the way to making the US
the world’s largest oil producer, atmospheric CO2 stood at just under
380 ppm (parts per million). As of August 22, it’s over 423.16
ppm. There’s a daily count to be found of this inexorable killer rise
at CO2Earth. Preindustrial levels well established through ice core
samples were just 280 ppm, and scientific consensus agrees that 350
ppm is the most CO2 in the atmosphere we can tolerate without the
profound climate change catastrophes we are experiencing today,
worsening drastically"

---

When Russians were commies I understand the "ideological struggle"
angle for the RU animosity. But after Russia became a market economy
the animosity, provocations did not end. It is clear Russians were
turned into an enemy for other reasons. Did muneeee play a role? MIC
loves its muneeeee.

---

When you are at war with a larger opponent you are at a disadvantage
defending, they have more people, more industrial capacity. When you
invade, go after their land you are still at a disadvantage - they
have more of it than you do. 

---

You can invade Russia, sure.. it's not like it hasn't been done
before.. Some of the toughest, pipe hitting mofos
tried. Hitler. Napoleon. What happened to them?

---

TASS: "Russia tells Israel that Palestinian issue can’t be resolved by
force — Lavrov"

---
