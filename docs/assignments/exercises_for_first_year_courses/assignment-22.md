---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Determine if a product is positive, negative or zero without calculating it



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

Implement a program that reads two integer numbers and says if their
product is positive, negative, or zero **without** doing the
calculation.

Run the following combinations of examples to test that your program
produces the same outputs:

-   the first number is 0,

-   the second number is 0,

-   both numbers are 0,

-   both numbers are positive,

-   both numbers are negative,

-   the first number is negative and the second is positive,

-   the first number is positive and the second is negative.

```small
>>> %Run
    Enter the first integer number: 0
    Enter the second integer number: -1
    The product is zero
>>> %Run 
    Enter the first integer number: 5
    Enter the second integer number: 0
    The product is zero
>>> %Run 
    Enter the first integer number: 0
    Enter the second integer number: 0
    The product is zero
>>> %Run 
    Enter the first integer number: 2
    Enter the second integer number: 7
    The product is positive
>>> %Run 
    Enter the first integer number: -4
    Enter the second integer number: -7
    The product is positive
>>> %Run 
    Enter the first integer number: -8
    Enter the second integer number: 3
    The product is negative
>>> %Run 
    Enter the first integer number: 10
    Enter the second integer number: -6
    The product is negative
```

```testruntile
Insist that the students test their programs by giving them example
test executions. Also pointing out that this way we try out all
possible combinations to test.
```


# Metadata

| *Summary*                     | Determine if a product of two numbers is positive, negative or zero without calculating it. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Programming puzzle with an arithmetic theme. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Conditionals and problems solving. |
| *Testing learning goals*      | Testing completeness. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

