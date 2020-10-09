# [1] Transistor

Introduction to transistors and semiconductors.

```py
dur_sec = 0 # in sec
dur_min = 0 # in min
timestamp = '00:00min'
```

## script

`[00:00] chapter 1`

```py
>>> intro_anim = 'lambda_intro.mp4'
>>> len(intro_anim)
>>> 6 # in sec
```

`[06:00] chapter 2`

Hey everyone!

The last time I already teased that to understand logic gates we have to understand transistors.

Because logic gates are pretty much just transistors combined together in a specific way, depending on the particular logic gate.

But we will get to that in the next video. In this video, we will take a look at what a transistor does and how it works.

`[] chapter 3`

A transistor is a semiconductor. Which simply means it is not an insulator like glass but also not really a conductor like copper.
And that is precisely why semiconductors are so useful.

They only conduct in certain circumstances that we can manipulate.
___
Probably the simplest semiconductor is a diode. It only conducts electrons in one direction. At least up to a relatively high threshold.
This works because of the material that a semiconductor is made of.

You probably already guessed it, we are talking about silicon.
But the funny thing is, silicon in its pure form is in fact an insulator, meaning it doesn't conduct electrons at all. After all, silicon is what glass is made of.
___
But if we mix it up with some phosphorus and barium, it starts to conduct a bit.
These mixtures are called doped silicon. And we use either phosphorus or boron.

When we dope silicon with phosphorus, the silicon has a slight surplus of valence electrons that are free to move around in the silicon crystal.
On the other hand, if we dope silicon with boron, the crystal has a slight shortage of valence electrons that can engage in a convalent bond.
___
Now, if you hook up a phosphorus doped (or n-type) silicon chrystal to a battery, the surplus electrons flow to the positive terminal of the battery, leaving behind holes in the n-type chrystal. Electrons from the negative terminal of the battery then can take up the holes and the n-type chrystal has a surplus of electrons again and the process repeats.
In simple words that means: it conducts.

Now, a boron doped (or p-type) silicon chrystal does pretty much the same only that it starts with having holes where electrons from the battery can move to and then exit the chrystal and flow back to the positive terminal of the battery.
___
Watch what happens if we combine an n-type chrystal with a p-type chrystal.
When we connect the n-type side to the negative terminal, it gets even more electrons, that then populate the p-type chrystal and exit the semiconductor on the other side.

But when we connect the semiconductor the other way around, the positive terminal attracts electrons from the n-type chrystal, reducing the surplus and the negative terminal provides electrons to the p-type chrystal, reducing the number of holes. This leads to an expansion of the deplition area in the middle and none of the remaining electrons in the n-type chrystal can jump over to the p-type chrystal an continue to flow to the positive terminal.
The semiconductor has become an insulator.

`[] Chapter 4`

So, how does this help us with understanding transistors?
Well, transistors also use these n & p-type materials. But instead of one n-type side and one p-type side like the diode uses, the common npn-transistor uses as the name gives away: a n-p-n combination.

If you now say: 'But that means that current can flow in neither direction!', then you are absolutely right.
But if you recall, a transistor has three wires. And that's actually what throws most people off when they think about a transistor. How can a component have three connectors if a battery only has two. Like, we have + and -, so what's up with the third one?

And the answer is actually pretty simple: It just connects to the positive terminal as well. That's it. Mystery solved.
Well, no entirely.
___
If we connect the input (or emitter) to the negative terminal and the output (or collector) to the positive terminal, the transistor does not conduct any electricity because the deplition area in the middle is simple too large for electrons to jump from atom to atom.

The third wire actually connects to the middle part of the transistor and is called the base. If we now hook up the base to the positive terminal of the battery, electrons do not have to jump all the way to the collector but only to the base and can escape the transistor this way. But now that they can get further in the middle, the distance to the collector shrinks and electrons can now also reach the collector. As we usually only allow a small current flowing through the base by adding a resistor afterwards, the p-type chrystal in the middle only lets a few electrons escape. The majority therefore escapes through the collector, whose naming now makes totally sense.

The ratio for most npn-transistors is typically 1:100, meaning a current flowing through the base of 1 allows for a current to flow through the collector of 100. Which is why you often here that a transistor multiplies the current.



## src

```py
PATH = '/youtube/src/ep_1/'
TOTAL_FILES = 0
```
