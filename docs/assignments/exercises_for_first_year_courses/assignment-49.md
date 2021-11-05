---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Determine dividers



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

Implement a program that, given two integers, returns if one is a
divisor of the other. To do this, you must detect which is the
smallest. You cannot use the division or remainder operation. In
your implementation you must also take into account negative numbers
and 0 (all numbers are divisors of 0).

For your program, perhaps the `abs()` function from the Python
standard library is useful. The `abs()` function returns the
absolute value of the given number. The absolute value of a number
is the value regardless of its sign. Therefore, the absolute of 10
is 10, and hte absolute of -10 is also 10.

Test your program with the following outputs:

```small
>>> %Run 
    Enter an integer number: 0
    Enter another integer number: 0
    There are no divisors of 0
>>> %Run 
    Enter an integer number: 0
    Enter another integer number: 2
    2 is a divisor of 0
>>> %Run 
    Enter an integer number: 4
    Enter another integer number: 0
    4 is a divisor of 0
>>> %Run 
    Enter an integer number: -5
    Enter another integer number: 0
    -5 is a divisor of 0
>>> %Run 
    Enter an integer number: 0
    Enter another integer number: -6
    -6 is a divisor of 0
>>> %Run 
    Enter an integer number: 25
    Enter another integer number: 5
    5 is a divisor of 25
>>> %Run 
    Enter an integer number: 4
    Enter another integer number: 16
    4 is a divisor of 16
>>> %Run 
    Enter an integer number: 3
    Enter another integer number: 17
    3 is not a divisor of 17
>>> %Run 
    Enter an integer number: 17
    Enter another integer number: 4
    4 is not a divisor of 17
```

```testruntile
Insist that the students test their programs by giving them example
test executions. Note that the test cases have been chosen carefully
to make sure we cover a lot of combinations and take 0 into account.
```

# Metadata

| *Summary*                     | Determine if one or bothe of two numbers are dividers of each other. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Arithmetic. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Remainder of devisions, using build-in functions. |
| *Testing learning goals*      | Test completeness |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

