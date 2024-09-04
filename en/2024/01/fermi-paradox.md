# Where Is Everybody

Fermi's Paradox asked 'Where is everybody?'  meaning extraterrestrial
aliens, implying given the vastness of the universe and long time it
has existed, there should be advanced extraterrestrial civilizations
throughout the universe. The Drake equation aimed to answer that
question quantitatively, estimates how many active civilizations there
are in the galaxy right now. Using numbers by Andrew Dessler,

$$
N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L
$$

$R_*$: Number of civilizations with which humans could
communicate. Recent estimates suggest about 2 new stars are formed in
the Milky Way every year.

$f_P$: The average number of planets that can potentially support life
per star that has planets. Most stars have planets, estimate 0.9.

$N_e$: Assume 1 in 5 of stars with planets has a planet in the
habitable zone, 0.2.

$f_l$, $f_i$, $f_c$ : The fraction of planets that could support life
that actually develop life at some point, develop intelligent life,
and develop a technology that releases detectable signs. Wild guess
all 0.1.

$L$: The length of time for which such civilizations release
detectable signals. Unknown, Dessler assumes advanced civilizations
last for ten million years.

```python
"%d planets" % (2 *  0.9 * 0.2 * 0.1 * 0.1 * 0.1 * 10*1e6)
```

```text
Out[1]: '3600 planets'
```

But if "instead of 10,000,000 years, advanced civilizations last only
10,000 years", then

```python
"%d planets" % (2 *  0.9 * 0.2 * 0.1 * 0.1 * 0.1 * 10000)
```

```text
Out[1]: '3 planets'
```

If advanced civilizations last on average only 1,000 years, due to,
well perhaps some kind of catastropy hits them all, then

```python
"%0.2f planets" % (2 *  0.9 * 0.2 * 0.1 * 0.1 * 0.1 * 1000)
```

```text
Out[1]: '0.36 planets'
```

which shows why we are the only one, and "there is no one else". And
btw we will likely go extinct, lose the civilization we built before
our 1000 years are up due to the climate, nuclear war or some other
artifact of modernity.

That is the answer to "where is everyone?", they are all dead due to
one catastrophy or another, not reaching and staying at the level
where they could contact anyone alive like them (us, in this case).

[[-]](https://www.theclimatebrink.com/p/where-is-everyone-the-fermi-paradox)

