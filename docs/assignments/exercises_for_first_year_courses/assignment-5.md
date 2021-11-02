---
title: "Python exercises for first year programming courses"
author:  Tanja E.J. Vos
...

# More advanced calculator

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

Implement a program that reads two integer numbers, calculates and prints their addition, subtraction, product, division and modulus or remainder (`%`).

```
>>> %Run 
    Enter a integer number: 4
    Enter another integer number: 6
    The sum (4 + 6) is:  10
    The subtraction (4 - 6) is:  -2
    The product (4 * 6) is:  24
    The division (4/6) is:  0.6666666666666666
    The modulus or remainder (4 % 6) is:  4
>>> %Run 
    Enter a integer number: 0
    Enter another integer number: -100
    The sum (0 + -100) is:  -100
    The subtraction (0 - -100) is:  100
    The product (0 * -100) is:  0
    The division (0 / -100) is:  0
    The modulus or remainder (4 % -100) is:  0
```

```testruntile
TILEd by adding example test executions for them to test.
```


# Metadata

| _Summary_ | More advanced calculator. |
| _TILE aspects_ |Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output, variables. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ | None. |
| _Variants_ | n/a |