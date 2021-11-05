---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Calculating the sum of the integers



------------------------------------------------------------------------

Python exercises used for first year programming courses that
have been adapted by using Test Informed Learning with Examples (TILE)
to integrate testing in programming education without it costing (much)
more time. The coloured boxes indicate how they were TILEd.

```testdomaintile
This colour box explains a TILE in the test domain.
```

```testruntile
This colour box explains a TILE related to test runs 
and/or test cases.
```
------------------------------------------------------------------------

# Assignment

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

