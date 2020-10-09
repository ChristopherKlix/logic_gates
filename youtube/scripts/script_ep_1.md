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

`[00:06] chapter 2`

Hey everyone!

The last time I already teased that to understand logic gates we have to understand transistors.

Because logic gates are pretty much just transistors combined together in a specific way, depending on the particular logic gate.

But we will get to that in the next video. In this video, we will take a look at what a transistor does and how it works.

`[00:26] chapter 3`

A transistor is a semiconductor. Which simply means it is not an insulator like glass but also not really a conductor like copper.
And that is precisely why semiconductors are so useful.

They only conduct in certain circumstances that we can manipulate.

In case of the transistor, it only conducts if a third wire, the base, is connected to the positive terminal of a battery.
___
Probably the simplest semiconductor is a diode. It only conducts electrons in one direction. At least up to a relatively high threshold.
This works because of the material that a semiconductor is made of.

You probably already guessed it, we are talking about silicon.
But the funny thing is, silicon in its pure form is in fact an insulator, meaning it doesn't conduct electrons at all. After all, silicon is what glass is made of.
___
But if we mix it up with some phosphorus and boron, it starts to conduct a bit.
These mixtures are called doped silicon. And we use either phosphorus or boron.

When we dope silicon with phosphorus, the silicon crystal has a slight surplus of valence electrons that can engage in a convalent bond. Therefore, they are free to move around in the silicon crystal.
On the other hand, if we dope silicon with boron, the crystal has a slight shortage.
___
```py
link = 'video about semiconductors by Ben Eater'
```
___
Now, if you hook up a phosphorus doped (or n-type) silicon crystal to a battery, the surplus electrons flow to the positive terminal of the battery, leaving behind holes in the n-type crystal. Electrons from the negative terminal of the battery then can take up the holes and the n-type crystal has a surplus of electrons again and the process repeats.
In simple words that means: it conducts.

Now, a boron doped (or p-type) silicon crystal does pretty much the same only that it starts with having holes where electrons from the battery can move to and then exit the crystal and flow back to the positive terminal of the battery.
___
Watch what happens if we combine an n-type crystal with a p-type crystal.
The electrons in the middle fill up some of the holes of the p-type crystal.

This leaves the middle relatively stable.

When we connect the n-type side to the negative terminal, it gets even more electrons.

Some of them get close to the p-type crystal and then populate the p-type crystal and exit the semiconductor on the other side.
```py
>>> Pixil art
```

But when we connect the semiconductor the other way around, the positive terminal attracts electrons from the n-type crystal, reducing the surplus and the negative terminal provides electrons to the p-type crystal, reducing the number of holes. This leads to an expansion of the deplition area in the middle and none of the remaining electrons in the n-type crystal can jump over to the p-type crystal an continue to flow to the positive terminal.
The semiconductor has become an insulator.
___
`[03:05] Chapter 4`

So, how does this help us with understanding transistors?
Well, transistors also use these n & p-type materials. But instead of one n-type side and one p-type side like in a diode, the common npn-transistor uses as the name gives away: a n-p-n combination.

If you now say: 'But that means that current can flow in neither direction!', then you are absolutely right.
But if you recall, a transistor has three wires. And that's actually what throws most people off when they think about a transistor. How can a component have three connectors if a battery only has two. Like, we have + and -, so what's up with the third one?

And the answer is actually pretty simple: It just connects to the positive terminal as well. That's it. Mystery solved.
Well, no entirely.
___
If we connect the input (or emitter) to the negative terminal and the output (or collector) to the positive terminal, the transistor does not conduct any electricity because the deplition area in the middle is simple too large for electrons to jump from atom to atom.

The third wire actually connects to the middle part of the transistor and is called the base. If we now hook up the base to the positive terminal of the battery, electrons do not have to jump all the way to the collector but only to the base and can escape the transistor this way. But now that they can get further into the middle, the distance to the collector shrinks and electrons can now also reach the collector.
___
It's like allowing a small current through the damn of a river that only seconds later breaks down the entire damn through momentum.
___
As we usually only allow a small current flowing through the base by adding a resistor afterwards, the p-type crystal in the middle only lets a few electrons escape. The majority therefore escapes through the collector, whose naming now makes totally sense.

The ratio for most npn-transistors is typically 1:100, meaning a current flowing through the base of 1 allows for a current to flow through the collector of 100. Which is why you often here that a transistor multiplies the current.
___
`[04:54] chapter 5`

And that is pretty much it.

Now, you might be confused by one thing: 'I thought electricity flows from + to -?'
And the answer to this is: 'Well, you have been taught a lie!'

When Benjamin Franklin first discovered electricity in the 1800s - which he actually didn't but that is a story for a different time - he didn't know about electrons. So, he had a 50/50 chance of getting it right... and he got it wrong.
It wasn't after almost 2 centuries later that scientists discovered electrons and realized: 'Oh, shoot, we were wrong the whole time'.

But by then engineers had so gotten used to drawing electricty flowing from + to - that it was hard to get the word out.

And as we know, humans are convinient creatures.

And after all, we would have to flip all the circuit symbols to make sense of them.
A diode has a symbol with an arrow pointing from + to -. A transistor has a symbol where the arrow points to the emitter.

But the truth is, electrons flow from negative to positive.

One thing that might help for the diode is to imagine that if the current flows in the direction of the arrow, the plate blocks the electrons.

And the arrow in an npn-transistor indicates the emitter.
___
`[06:00] chapter 6`

So, let's see how a transistor integrates into an electric circuit.

Think about a transistor as an electrically operated switch.
Here we have a simple electric circuit. A battery with 5V, a resistor and an LED.

Let's add a regular switch.

If we close the switch, electrons can flow and the LED turns on.
We use the electron flow way to show how electrons actually move throught the wires.
___
If we replace the switch with a transistor, we need to somehow hook up the third wire, the so-called 'base', to the positive part of the battery.

We can either hardwire it, which will leave the transistor on constantly, or we again add a switch that allows current to flow through the base.

In reality, this would be a microchip for example controlling the flow through the base. Because otherwise it wouldn't make a difference to just using a switch after the LED. But as the current through the base is relatively low, we can use a control current to control different transistors with a microchip and not control an LED but actually the inputs of a 6502 microchip for example.
___
Now, if we close the switch, the LED lights up. But this is only one condition that has to be true to light up the LED.

The goal is to light up the LED based on two control currents.

___
`[07:22] chapter 7`

In the next video we will finally take a look at the simplest of all logic gates, the AND-gate.
If you still feel a little bit unsure about transistors, we will also take a look at some more examples as an AND-gate is - spoiler - simply two transistors combined together.
But if you want to learn more about semiconductors before check out this video made by Khan Academy about semiconductors. They go a bit more into detail when it comes to what is happening on the molecular level in doped silicon crystals.
Also, this video explains a bit more about the history of electron flow and conventional flow, links for both videos are in the description.

Otherwise, I will see you in the next video.
___
`[07:58] end card`

20sec

```py
# links in end card
link_nx_ep = 'link to [1] AND-gate'
link_ch_lambda = 'channel of lambda'
link_playlist = 'playlist of logic gates'
```
___
`[08:18] end`

## src

```py
PATH = '/youtube/src/ep_1/'
TOTAL_FILES = 0
```
