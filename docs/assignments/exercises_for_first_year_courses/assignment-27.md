---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Money breakdown in bills and coins



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

Read an amount of euros and display the minimum breakdown in bills
and coins for that amount on the screen. This means that the minimum
number of bills/coins must be returned. We assume that there are
500, 200, 100, 50, 20, 10 and 5 bills, and 2 and 1 coins.

Write a version of this program that shows the breakdown on the
screen mentioning only the bills and coins we need.

```small

>>> %Run 
    Enter an amount of euros: 434
    2 bills of 200
    1 bill of 20
    1 bill of 10
    2 coins of 2
>>> %Run 
    Enter an amount of euros: 0
    There are no bills or coins
>>> %Run 
    Enter an amount of euros: -35
    There are no bills or coins
>>> %Run 
    Enter an amount of euros: 1
    1 coin of 1
>>> %Run 
    Enter an amount of euros: 5
    1 bill of 5
```

What other tests could you run to ensure that your program has the
desired behaviour? Have you tried, for example, entering different
amounts that return all the bills and coins at least once? For
example:

-   for quantity 2, a coin of 2 must be returned

-   for quantity 10, a bill of 10 must be returned

-   for quantity 20, ...

-   etc.

Have you tried, for example, entering different amounts to test
whether your program returns the minimum number of correct
combinations of bills and coins? For example:

-   for quantity 6, a bill of 5 and a coin of 1 must be returned
    (and not for example 3 coins of 2)

-   for quantity 12, a bill of 10 and a coin of 2 must be returned
    (and not for example two bills of 5 and two coins of 1)

-   for quantity 24, ...

-   etc.

```testruntile
Insisting that the students test their programs and think about all
possible combinations.
```

# Metadata

| *Summary*                     | Money breakdown in bills and coins |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Applying an algorithm. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Problem solving.  |
| *Testing learning goals*      | Designing test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

