---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Density, mass or volume calculator





The density (d) of a substance is defined as the amount of mass (m)
it has per volume unit (v). Then:

$$d = \frac{m}{v} \;\;\leftrightarrow\;\; m = d \times v \;\;\leftrightarrow\;\; v = \frac{m}{d}$$

Write a program that asks the user what he wants to calculate
(density, mass or volume), then asks for the necessary data and at
the end prints the result on the screen.

Run the following examples to test that your program gives the same
outputs.

```small
>>> %Run 
    What do you want to calculate? (d, m, v):d
    Mass: 45
    Volume: 67
    The density is:  0.6716417910447762
>>> %Run 
    What do you want to calculate? (d, m, v):d
    Mass: 45
    Volume: 0
    Cannot be calculated
    >>> %Run 
    What do you want to calculate? (d, m, v):m
    Densidad: 34
    Volume: 67
    The mass is:  2278
>>> %Run 
    What do you want to calculate? (d, m, v):m
    Densidad: 0
    Volume: 25
    The mass is:  0
>>> %Run 
    What do you want to calculate? (d, m, v):v
    Densidad: 56
    Mass: 900
    The volume is: 16.071428571428573
>>> %Run 
    What do you want to calculate? (d, m, v):v
    Densidad: 0
    Mass: 568
    The mass is
>>> %Run 
    What do you want to calculate? (d, m, v): z
    Enter only d, m or v
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```

# Metadata

| *Summary*                     | Caluclator for different physic properties |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | User interaction, calculation, control flow |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Control flow, arithmetics |
| *Testing learning goals*      | Applying test cases |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   