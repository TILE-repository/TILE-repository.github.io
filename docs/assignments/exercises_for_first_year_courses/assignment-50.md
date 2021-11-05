---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Quotient and remainder

By [Tanja E.J. Vos](https://www.tanjavos.com).

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

Write a program to calculate the quotient and remainder of the
integer division of two positive integers, using only the
subtraction operation.

Test your program with the following outputs:

```small
>>> %Run 
    Enter a positive integer number: 0
    Enter another positive integer number: 4
    The quotient is 0
    The reminder is 0
>>> %Run 
    Enter a positive integer number: 4
    Enter another positive integer number: 0
    It cannot be divided by 0
>>> %Run 
    Enter a positive integer number: 25
    Enter another positive integer number: 25
    The quotient is 1
    The reminder is 0
>>> %Run 
    Enter a positive integer number: 26
    Enter another positive integer number: 20
    The quotient is 1
    The reminder is 6
>>> %Run 
    Enter a positive integer number: 20
    Enter another positive integer number: 26
    The quotient is 0
    The reminder is 20
>>> %Run 
    Enter a positive integer number: -4
    Enter another positive integer number: 5
    Only positive integers
>>> %Run 
    Enter a positive integer number: 10
    Enter another positive integer number: -4
    Only positive integers
```

```testruntile
Insist that the students test their programs by giving them example
test executions. Note that the test cases have been chosen carefully
to make sure we cover a lot of combinations and take 0 into account.
```

# Metadata

| *Summary*                     | Calculate the quotient and the remainder of two positive numbers. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Arithmetic. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Calculating quotient and remainder |
| *Testing learning goals*      | Test completeness. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

