---
title: "Calculating the sum of the integers"
summary: "Calculating the sum of the integers."
prerequisites: "['data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'expressions > operators > arithmetic operators']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Metadata

| *Summary*                     | Calculating the sum of the integers |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Calculating the sum of integers between two values. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Loops and assigning values to a variable multiple times. |
| *Testing learning goals*      | Robustness testing. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   


# Calculating the sum of the integers





Write a program to calculate the sum of the integers between $$N$$ and
$$M$$, where $$N$$ and $$M$$ are values entered by the user. `result` =
$$\sum_{n = N}^{M} n$$


```small
>>> %Run 
    Enter a number: 0
    Enter a number: 3
    The sum from 0 to 3 is:  6
>>> %Run 
    Enter a number: -5
    Enter a number: 3
    The sum from -5 to 3 is: -9
>>> %Run 
    Enter a number: -8
    Enter a number: 8
    The sum from -8 to 8 is:  0
>>> %Run 
    Enter a number: 4
    Enter a number: 4
    The sum from 4 to 4 is:  4
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
