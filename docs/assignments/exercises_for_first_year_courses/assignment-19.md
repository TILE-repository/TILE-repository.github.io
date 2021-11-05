---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Odd or even

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

Write a program that reads an integer number and tells whether it is
odd or even. Run the following examples to test that your program
gives the same outputs:

```small
>>> %Run 
    Enter an integer number: 1
    The number 1 is odd
>>> %Run 
    Enter an integer number: 0
    The number 0 is even
>>> %Run 
    Enter an integer number:111
    The number 1 is odd
>>> %Run 
    Enter an integer number: 23
    The number 23 is odd
>>> %Run 
    Enter an integer number: -34
    The number 0 is even
>>> %Run 
    Enter an integer number: -11
    The number -11 is odd
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```


# Metadata

| *Summary*                     | Tell wether a number is odd or even. |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | Odd and even numbers |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Determining if a number is odd or even. |
| *Testing learning goals*      | Designing and applying test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

