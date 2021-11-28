# Week 36

Research is not about specialization, it's about looking at a
problem "in depth", and utilizing all the tools necessary to deal with
problems related to that depth. A research problem can require
concepts from diverse fields that crosses university departments and
disciplines.

---

Not all researchers are good teachers. Not all good teachers are good
researchers (mathematician G. H. Hardy makes some rough comments about
this relation -and he is wrong-). But there are some, who are great at
both, and boy do they create wonders when they teach. We should not
put roadblocks on someone's path if they want to learn from the best.

If in 21st century we are still talking about "quality teachers" and
about "teachers pay" that are part of a system that can never scale,
that is a big disservice to our kids. If adult supervision is needed,
any professional can provide that by contributing his / her time
during the day. This kind of task does not require
specialization. Actually specialization as a concept is passe, part of
a collapsing modernist mindset. Hence my suggestion: Any teacher who
is not a researcher needs to be fired.

The Internet can distribute quality content to everyone, in the form
of video, lecture notes, problems / solutions. We only need a system
that will incentivize people to release their content as they make it

---

I saw Malcolm Gladwell on TV the other day.. He was on this CNN show
called Fareed Zakaria BLT. Or, GTE ...? TP? Something like
that. Anyway, Gladwell says university rankings are bunk, because say
#48 and #49 are such different universities that comparing them, let
alone having them in the same ranking is like comparing apples and
oranges.

Gladwell's TED talk had a similar theme. In it he proposed when it
comes to consumption, there is no "best of", but many "bests" to
choose from. We add, standardized rankings are part of industrial /
modernist mentality, a sign of a Taylorist mindset. From an earlier
post:

In the early decades of [20th] century Taylor decided that there was
one best (standard) way to perform each job, one best (standard) tool
to perform it with, and a stipulated (standard) tune in which to
complete it.

In the postmodern world, choices are many.

---

I sometimes hear scientists who are not good at math modeling to
justify why it's stupid to buy a lottery ticket. They calculate some
probabilities, and think "there are X number of tickets, and Y many
number combinations", etc and then say it's unlikely for anyone to
win, so why bother?

I argue their model is wrong. They are not taking into account cost /
benefit, and the probability of payoff properly. Here is an
alternative model:

Payoff = Benefit / Cost * probability of winning

In this model, if for example each lottery ticket is one in a million,
costs 1 dollar, potential payoff is 200K, calculation is

```python
benefit = 200000.

cost = 1.

prob = 1./1000000.

print ((benefit/cost)*prob)
```

```text
0.19999999999999998
```

But let's not leave it here. Let's calculate another entity to compare
this _to_. For example .. a paycheck. Guy earns 30K a year, and puts
in 100K of effort to earn that paycheck (employee has to be putting in
more than he gets, right, otherwise he is not a good employee), and he
gets that paycheck with probability 1. There is no chance he will
*not* get his paycheck, a paycheck in that sense is the opposite of a
lottery ticket -- it is almost impossible to win the lottery, it is
almost impossible not to get a paycheck. That calculation is

```python
benefit = 30000.
cost = 100000.
prob = 1.
print ((benefit/cost)*prob)
```

```text
0.3
```

The results are, for lottery 0.2, for paycheck 0.3. Paycheck wins, but
just barely. There is no difference in scale here, and numerical
difference certainly isn't something to sneer at. If our made up
numbers were massaged a little, the lottery ticket could well come
close. 

Then the question isn't why are so many people buying a lottery
tickets.. The question is why isn't everyone?

---

Palestinians' attempt for UN recognition is related to Arab Spring --
the message presented in front of Western public opinion is "at a time
when many Middle Eastern countries rid themselves of their dictators,
why shouldnt we rid ourselves of Israel?" -- Israel being their own
regional dictator. The timing is pretty good on their part. Nice move.

FT: "The diplomatic crisis at the UN triggered by the Palestinians’
attempt to win recognition as a state may or may not advance their
quest for justice and self-determination. But what it has started to
do is strip away layer after layer of the cant and duplicity that has
enveloped the so-called peace process.

The starting point for any consideration of the Palestinians’
diplomatic gambit is that the negotiations that appeared to promise so
much after the 1993-95 Oslo accords have not ended the Israeli
occupation of their land. Mahmoud Abbas, successor to the late Yassir
Arafat as Palestinian president, has eschewed violence and staked
everything on negotiations. He has nothing to show for it except the
ruin of his reputation.

Whereas Arafat was a feckless negotiator who kept the option of the
gun dangerously in play and preferred the trappings of statehood to
the statecraft needed to win a state, Mr Abbas and his prime minister,
Salam Fayyad, have chosen diplomacy and nation-building. But the
occupation continues.

Going all the way back to Oslo, the peace process has served as an
international smoke and mirrors screen for the inexorable expansion of
Israeli settlements on Palestinian land. It cannot be stated often
enough that the biggest single enlargement of the settlements took
place in 1992-96, at the high-water mark of the peace process under
Yitzhak Rabin and Shimon Peres, when the number of settlers grew by 50
per cent, or four times the rate of population growth inside Israel.

Since then, the colonisation of the West Bank and Arab east Jerusalem
has reached the point at which no viable Palestinian state is now
possible unless this is reversed. But these settlements are intended
to be permanent. The so-called Palestine Papers, leaked documents to
al-Jazeera in January detailing how Mr Abbas was willing to give up
nearly all of east Jerusalem but was still scorned by the previous,
allegedly moderate Israeli government, make this abundantly clear.

Benjamin Netanyahu, the current Likud premier who leads a coalition
freighted with irredentist believers in a Greater Israel, has never
himself believed in anything more than a sort of supra-municipal
government for Palestinians, on roughly half the land conquered by
Israel in the 1967 Arab-Israeli war.

The real story here, therefore, is not that UN recognition will
torpedo a peaceful resolution of the conflict negotiated by these two,
vastly unequal sides. There is no prospect whatsoever of that
happening. It is that international recognition of the Palestinians
right to a state would call Israel’s bluff and expose the hollowness
of the US role as a less-than-honest broker."

---

Biologist.org: "I'd like to suggest that our Ph.D. programs often do
students a disservice in two ways. First, I don't think students are
made to understand how hard it is to do research. And how very, very
hard it is to do important research. It's a lot harder than taking
even very demanding courses. What makes it difficult is that research
is immersion in the unknown. We just don't know what we're doing [..].

Second, we don't do a good enough job of teaching our students how to
be productively stupid – that is, if we don't feel stupid it means
we're not really trying. I'm not talking about `relative stupidity',
in which the other students in the class actually read the material,
think about it and ace the exam, whereas you don't. I'm also not
talking about bright people who might be working in areas that don't
match their talents.

Science involves confronting our `absolute stupidity'. That kind of
stupidity is an existential fact, inherent in our efforts to push our
way into the unknown. Preliminary and thesis exams have the right idea
when the faculty committee pushes until the student starts getting the
answers wrong or gives up and says, `I don't know'. The point of the
exam isn't to see if the student gets all the answers right. If they
do, it's the faculty who failed the exam. The point is to identify the
student's weaknesses, partly to see where they need to invest some
effort and partly to see whether the student's knowledge fails at a
sufficiently high level that they are ready to take on a research
project.

Productive stupidity means being ignorant by choice. Focusing on
important questions puts us in the awkward position of being
ignorant. One of the beautiful things about science is that it allows
us to bumble along, getting it wrong time after time, and feel
perfectly fine as long as we learn something each time. No doubt, this
can be difficult for students who are accustomed to getting the
answers right. No doubt, reasonable levels of confidence and emotional
resilience help, but I think scientific education might do more to
ease what is a very big transition: from learning what other people
once discovered to making your own discoveries. The more comfortable
we become with being stupid, the deeper we will wade into the unknown
and the more likely we are to make big discoveries"

---


When I learn from video lectures, I noticed how sporadic and irregular
my learning patterns are. For example, I might take lecture 18 from
its 30th minute until 30th minute of the next, lecture 19. I might
take two a day, one a day, or half. Physically, I might be in two or
more different cafes, eat something in between at yet another place,
finally, near the end of the day, finish things up on my couch at
home.

This is how "school" in 21st century feels like. My teachers are top
notch researchers in their field who are so good they make things as
simple as possible (but no simpler). They pepper their lectures with
useful tidbits which are in the "cool tricks" category, that also
reveal their researching, thinking approach -- and that is more
valueable than gold. Even after factoring in the recent price of gold
:)

As a result, this kind of learning is completely asynchronized.

The old approach with some average teacher "teaching" and the student
listening right then and there, in a synchronized fashion, is
dead. The old method can never scale. Liberals in US (they are
mislabeled by the way, they are more accurately described as "statist
left") need to stop bitching about teachers losing their jobs, and
start thinking more appropiately for 21st century. You might feel
nostalgic or sentimental about this, maybe you had teachers in your
family, maybe your mother was one. So was mine. You dont see me crying
do you?

---

Douglas Rushkoff: "The U.S. Postal Service appears to be the latest
casualty in digital technology's slow but steady replacement of
working humans. Unless an external source of funding comes in, the
post office will have to scale back its operations drastically, or
simply shut down altogether. That's 600,000 people who would be out of
work, and another 480,000 pensioners facing an adjustment in terms.

We can blame a right wing attempting to undermine labor, or a left
wing trying to preserve unions in the face of government and corporate
cutbacks. But the real culprit -- at least in this case -- is
e-mail. [..] New technologies are wreaking havoc on employment figures
-- from EZpasses ousting toll collectors to Google-controlled
self-driving automobiles rendering taxicab drivers obsolete.

We like to believe that the appropriate response is to train humans
for higher level work. Instead of collecting tolls, the trained worker
will fix and program toll-collecting robots. But it never really works
out that way, since not as many people are needed to make the robots
as the robots replace.

And so the president goes on television telling us that the big issue
of our time is jobs, jobs, jobs -- as if the reason to build
high-speed rails and fix bridges is to put people back to work. But it
seems to me there's something backwards in that logic. I find myself
wondering if we may be accepting a premise that deserves to be
questioned.

I am afraid to even ask this, but since when is unemployment really a
problem? I understand we all want paychecks -- or at least money. We
want food, shelter, clothing, and all the things that money buys
us. But do we all really want jobs?

We're living in an economy where productivity is no longer the goal,
employment is. That's because, on a very fundamental level, we have
pretty much everything we need. America is productive enough that it
could probably shelter, feed, educate, and even provide health care
for its entire population with just a fraction of us actually working
[..].

[I]n the digital age, we're using technology [..] to increase
efficiency, lay off more people, and increase corporate
profits. [..]While this is certainly bad for workers and unions, I
have to wonder just how truly bad is it for people. Isn't this what
all this technology was for in the first place? The question we have
to begin to ask ourselves is not how do we employ all the people who
are rendered obsolete by technology, but how can we organize a society
around something other than employment? Might the spirit of enterprise
we currently associate with "career" be shifted to something entirely
more collaborative, purposeful, and even meaningful?

Instead, we are attempting to use the logic of a scarce marketplace to
negotiate things that are actually in abundance. What we lack is not
employment, but a way of fairly distributing the bounty we have
generated through our technologies, and a way of creating meaning in a
world that has already produced far too much stuff. The communist
answer to this question was just to distribute everything evenly. But
that sapped motivation and never quite worked as advertised [..] But
there might still be another possibility -- something we couldn't
really imagine for ourselves until the digital era. As a pioneer of
virtual reality, Jaron Lanier, recently pointed out, we no longer need
to make stuff in order to make money. We can instead exchange
information-based products.

We start by accepting that food and shelter are basic human
rights. The work we do -- the value we create -- is for the rest of
what we want: the stuff that makes life fun, meaningful, and
purposeful"