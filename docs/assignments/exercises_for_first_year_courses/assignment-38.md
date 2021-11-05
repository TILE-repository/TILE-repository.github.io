---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# The sum of the odds and even numbers

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

Implement a program to read 10 positive numbers and independently
calculate the sum of the odd and even numbers. If a negative number
is entered, the program will display an error message and ask for
the number again.

```small
>>> %Run 
    Enter a number: 4
    Enter a number: 5
    Enter a number: 6
    Enter a number: 7
    Enter a number: 8
    Enter a number: 9
    Enter a number: 12
    Enter a number: -4
    Please enter only positive numbers
    Enter a number: 0
    Enter a number: 3
    Enter a number: 209
    Sum of the even numbers:  30
    Sum of the odd numbers:  233
>>> %Run
    Enter a number: -4
    Please enter only positive numbers
    Enter a number: -0
    Enter a number: 4
    Enter a number: 4
    Enter a number: 5
    Enter a number: 5
    Enter a number: 6
    Enter a number: 6
    Enter a number: 7
    Enter a number: 7
    Enter a number: 8
    Sum of the even numbers:  28
    Sum of the odd numbers:  24
>>> %Run 
    Enter a number: 2
    Enter a number: 4
    Enter a number: 6
    Enter a number: 8
    Enter a number: 0
    Enter a number: 16
    Enter a number: 18
    Enter a number: 20
    Enter a number: 36
    Enter a number: 90
    Sum of the even numbers:  200
    Sum of the odd numbers:  0
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```

# Metadata

| *Summary*                     | Calculating the sum of the odds and of the even numbers. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Determining odd and even numbers numbers |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Loops |
| *Testing learning goals*      | Testing for robustness |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

