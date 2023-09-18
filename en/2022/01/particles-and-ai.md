# Particles, Science and AI

Functions

Neural nets are known to be efficient function approximators. If they
can approximate anything, then they can learn, model anything, right?
Input is the video of the road, output is pressing the pedals, turning
the wheel, if I learn the "function" of driving with given inputs and
outputs, I could learn how to drive. Right?

But the formulation of the real-world, theorizing requires more than
"functions". We learned that lesson in science of the past 300
years. In materials science a steel beam under stress has the
displacement formula $E I \frac{d^4 y}{d X_1^4} = q$ , a fourth order
differential equation, it is not a function. When solved with given
conditions result is one way, a different way for a different
condition; all from the same base formula. Mathematics has much
broader reach, broader mechanisms than mere functions, it captures
patterns, and relations that don't immediately have to compute
anything.

Particles, Formulas

Neural Net Expert Yann LeCun: "The cargo cult approach to
aeronautics—for actually building airplanes—would be to copy birds
very, very closely; feathers, flapping wings, and all the rest. And
people did this back in the 19th century, but with very limited
success... The equivalent in AI is to try to copy every detail that we
know of about how neurons and synapses work, and then turn on a
gigantic simulation of a large neural network inside a supercomputer,
and hope that AI will emerge. That’s cargo cult AI"

But with deep neural networks what came to be called "AI" today, that
is *exactly* what they are doing. They believe all it takes to
simulate brain is to have as many of its contituens as possible
(neurons) and simulating those little pieces will work up to a brain,
i.e. intelligence, the "I" of AI.

Established science does not work this way. Take fluid dynamics. Water
has particles and we can simulate those right? But we don't simulate
fluids with particles. There is a fluid dynamics *formula* that works
for any point in space, point in time, at macro level.. We
"discretize" that formula, chop it up into pieces for computation and
program that into the computer, much later. This is a different
approach from using micro particles trying to build up to a system. As
with many other things bottom up approach doesn't work, top-down
design is necessary. High organization / design matters.

There is a term in FD formulas that says 'if there is a pressure
difference between two regions there will be a force between those
regions, from high to low' for example. This is the type of formula
AI, or AGI needs, not "neurons". Observe external variables (via
experiments, trial/error), then using mathematics create releations
among them. AGI needs to follow the same approach adopted by nearly
all natural sciences. What are the variables of intelligence? What is
the Calculus that can bind them together? These need to be
invented. It isn't about "computation", not at first, brogrammers are
slow to grasp this..  It's about declarative, broad relations, finding
the ever-present pattern among them, like making a cat's
cradle. Starting with one set of relations, transforming it another,
it goes on.. Then as a *last* step, you can compute.

But how does nature know how to create speed, acceleration or
pressure?  Nature doesn't give a shit about pressure. It can send off
one trillion particles one way, another trillion another way, the ones
that hit a surface are what we see as pressure, the ones that jiggle
too much are what we see as heat, Nature could not care less. We
cannot compete with Nature at that level... If we tried we'd have to
create a computer as big as Nature. So we need to use our math to
generalize, inventing relations, sometimes inventing different math
for better relations between attributes we measure....

Good economics works the same way. [They](../../2018/02/keen_math.html)
take broad, general measures we can see, measure, such as inflation,
employment, credit, market conditions and form relationships between
them, akin to using pressure, viscosity, density in a fluid. If the
measurements are good, and the relations are captured correctly, this
formula can then be manipulated to yield interesting results perhaps
suggesting new relations previously unseen, allow discovery,
concoction of functions to make precise calculations, predictions. The
latter is science. The former, dreaming of the day "if I had a [bigger
computer](../../2020/07/ai-comments.html#parrot)" so all monkey
particles could be accounted for, "or more data", "then whole of
economics could be simulated" is not.

SPH

Some hear about a method called SPH, smoothed particle
hydrodynamics. But in SPH what's used are not real particles, they are
'pockets' in the fluid that are followed around. The act of following
somewhat resembles following around a particle, that's where the P
comes from... But look carefully, there is the Navier-Stokes formula
lurking in there, which uses concepts such as pressure, viscosity,
heat, concocted at a macro level, not micro. Without the formula,
there is no SPH...

[[Up]](../../2020/07/ai.html)
