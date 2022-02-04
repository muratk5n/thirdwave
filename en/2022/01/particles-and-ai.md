# Particles, Science and AI

Neural Net Expert Yann LeCun: "The cargo cult approach to
aeronautics—for actually building airplanes—would be to copy birds
very, very closely; feathers, flapping wings, and all the rest. And
people did this back in the 19th century, but with very limited
success... The equivalent in AI is to try to copy every detail that we
know of about how neurons and synapses work, and then turn on a
gigantic simulation of a large neural network inside a supercomputer,
and hope that AI will emerge. That’s cargo cult AI"

This statement is misleading.. With the NN approach, deep neural
networks what came to be called "AI" today, that is *exactly* what
they are doing. If not in the tiniest detail, certainly in spirit, in
the overall approach to the problem. Implicitly they believe what's
known about the human brain so far is final, X number of neurons are
there, they somehow "connect" and do stuff together, so if we start
from tiny particles (software neurons) and build up in code, we will
reach human level intelligence. This is the belief -- yet no cigar. A
decade ago they could be forgiven bcz the hardware "wasn't there
yet". Now it is. Where is Artif. General Intelligence?...

Fluids

One could say one of the most difficult computations in physics is
simulation of fluids (for which we have the proper equations for). But
we don't use particles to simulate fluids. Then why use such approach
for "brain particles (neurons)"?... It's all about the formula. If one
looks at fluid dynamics formulas, there is a term there that says 'if
there is a pressure difference between two regions there will be a
force between those regions, from high to low'. Declerative, broad
statement... Later when we compute the FD formula we cut its field
into little regions, and either average over them (one method), or
look at the edge points (another method). IOW we work with things we
can measure, and relate them, discretize later.

Nature doesn't give a shit about pressure. It can send off one
trillion particles one way, another trillion another way, the ones
that hit a surface are what we see as pressure, the ones that jiggle
too much are what we see as heat, Nature could not care less. We
cannot compete with Nature at that level... If we tried we'd have to
create a computer as big as Nature. So we need to use our math to
generalize, inventing relations, sometimes inventing different math
for better relations between attributes we measure....

The term particle in compsci needs to be clarified.. Some hear about a
method called SPH, smoothed particle hydrodynamics. But in SPH what's
used are not real particles, they are 'pockets' in the fluid that are
followed around. The act of following somewhat resembles following
around a particle, that's where the P comes from... But look
carefully, there is the Navier-Stokes formula lurking in there, which
uses concepts such as pressure, viscosity, heat, concocted at a macro
level, not micro. Without the formula, there is no SPH...

Brogrammers

A lot of the NN "buzz" originates from S. Valley, which is full of IT
programmers not applied math professionals. IT people don't understand
mathematical programming.

Computation split into two cultures almost at its inception; one is
scientific computation (discretizing formulas), the other business
coding, w databases, "UI". The two cultures gathered around their own
computer languages, Fortran for sci, Cobol for biz. These are two
different ways of thinking about computation.. Silicon Valley is full
of the latter type - the business brogrammers. They pretty much have
zero understanding of science and how it is conducted. So it behooves
all tech watchers to pay attention to that difference as the typical
tech CEO is sci ignorant, bereft of any understanding on what makes it
tick.

For IT programmers the particle, and their interactions, simulation
viewpoint is comfortable. Their bean counting is done discretely,
item-by-item basis, which makes sense you are automating an office
work, keeping lists, adding stuff, checking them off...  The so-called
object-orientation took hold in the industry possibly for this reason.
Interesting its widely used language C++ was based on an older
language called Simula, the first OO language, literally built for
simulations.

With OO the idea was coders would create "Customer objects" which
interacted with "Order objects", so the entire system would be seen as
a "simulation" btw these little particles. OO was seen as a way to be
more "scientific" about IT software. The approach did not save
projects which typically went over-time and over-budget at a rate of
1/2. They still do. For bigger projects the failure rate is even
higher, a whopping 4/5.

<a name='econ'/>

Economics

A parallel to the economics profession might be apt here; in econ
there are "actors" -- these could be seen as particles in a fluid, or
"neurons" in the network. There are <8 billion people, so we should be
able to simulate their economics decisions, right? 8 billion is
certainly a number we can handle these days on a computer.

Yet this isn't done. Imagine what it would take for such a simulation;
we start with a cool 8 billion but every decision, every interaction
with another actor, the backdrop where this takes place increases the
difficulty of such a computation considerably. It makes such a
simulation almost impossible to plan.

Instead, what do the economists (the good ones at least) do?
[They](../../2018/02/keen_math.md) take broad, general measures we can
see, measure, such as inflation, employment, credit, market conditions
and form relationships between them, akin to using pressure,
viscosity, density in a fluid. If the measurements are good, and the
relations are captured correctly, this formula can then be manipulated
to yield interesting results perhaps suggesting new relations
previously unseen, allow discovery, concoction of functions to make
precise calculations, predictions. The latter is science. The former,
dreaming of the day "if I had a bigger computer" so all monkey
particles could be accounted for and "then whole of economics will be
simulated" is not.

[[⇪Up]](../../2020/07/ai.md)
