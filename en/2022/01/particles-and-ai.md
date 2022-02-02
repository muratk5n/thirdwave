# Particles, Science and AI

NN Expert Yann LeCun: "The cargo cult approach to aeronautics—for
actually building airplanes—would be to copy birds very, very closely;
feathers, flapping wings, and all the rest. And people did this back
in the 19th century, but with very limited success... The equivalent
in AI is to try to copy every detail that we know of about how neurons
and synapses work, and then turn on a gigantic simulation of a large
neural network inside a supercomputer, and hope that AI will
emerge. That’s cargo cult AI"

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

One could say one of the most difficult computations in physics is the
simulation of fluids (for which we have the proper equations for). But
we don't use particles to simulate fluids, then why use such approach
for "brain particles (neurons)"?... 

It's all about the formula. If one looks at fluid dynamics formulas,
there is a term there that says 'if there is a pressure difference
between two regions there will be a force between those regions, from
high to low'. Declerative, broad statement... works brilliantly. Later
when we compute the FD formula we cut its field into little regions,
and either average over them (one method), or look at the edge points
(another method). IOW we work with things we can measure, and relate
them, discretize later.

Nature doesn't give a shit about pressure. It can send off one
trillion particles one way, another trillion another way, the ones
that hit a surface are what we see as pressure, the ones that jiggle
too much are what we see as heat, Nature could not care less. We
cannot compete with Nature at that level... If we tried we'd have to
create a computer as big as Nature. So we need to use our math to
generalize, inventing relations, methods to represent better relations
between attributes we measure....

Some might get confused at times following the publications on compsci.
You hear about a method called SPH, smoothed particle hydrodynamics.
How is that not about particles?

But those are not real particles, they are 'pockets' in the fluid that
are followed around. The act of following somewhat resembles following
around a particle, that's where the P comes from... But look
carefully, there is the Navier-Stokes formula lurking in there, which
uses concepts such as pressure, viscosity, heat, concocted at a macro
level, not micro. Without the formula, there is no SPH.

We use mathematics to compute fluids dynamics (FD), not particles.
True AI research should follow the same path.

A lot of the "buzz" around NNs comes from S. Valley, which is full of
IT programmers not applied math professionals. For IT programmers the
particle, and their interactions, simulation viewpoint was
comfortable.. Their bean counting is done discretely, item-by-item
basis, which makes sense you are automating an office work, keeping
lists, checking them off...  The so-called object-orientation took
hold in the industry possibly for this reason.  Interesting its widely
used language C++ was based on an older language called Simula, the
first OO language, literally built for simulations.

With OO the idea was coders would create "Customer objects" which
interacted with "Order objects", so the entire system would be seen as
a "simulation" btw these little particles. OO was seen as a way to be
more "scientific" about IT software. The approach did not save
projects which typically went over-time and over-budget at a rate of
1/2. They still do. For bigger projects the failure rate is even
higher, a whopping 4/5. 

