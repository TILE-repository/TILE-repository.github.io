---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Limit exceeding sum

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

Write a program that finds the first value $$N$$ for which the sum
$$0 + 1 + 2 + 3 + ... + N$$ exceeds a LIMIT value that is entered by
keyboard. Run the following test cases to test your program:

    **test case ID**  | **input**  | **expected output**
    ---------| -------| -----------------
    1    |    0    |   1
    2    |     1    |   2
    3    |     25   |   7
    4    |     -5  |    0
    5    |    -450  |  0
    6     |    45   |   10

```testruntile
Insist that the students test their programs by giving them example
test cases in a table. We have explicitly added 0 and negative
numbers to make sure these are tested.
```

# Metadata

| *Summary*                     | Limit exceeding sum |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | Loops |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with while loops. |
| *Testing learning goals*      | Testing for robustness. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

