---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Calculate the maximum of real numbers



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

Implement a program that reads 12 real numbers and calculates the
maximum. Run the following test cases to test your program:

**test case ID** | **inputs**                                                   | expected outputs
--------- -----------------------------------------------------------------------| ------------------
1      |   12.2, 6.0, 3.3, 4, 5, 6.5, 7, 8, 9, 3.3, 11, 12.2                      | 12.2
2      |   -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12                     |  -1
3      |   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0                                    |  0
4      |   12.4, 21.005, -3.67, 4.43, 5.56, 4.2, 7, 8.3, -91.3, -1.0, 32.4, 12.1  | 32.4

```testruntile
Insist that the students test their programs by giving them example
test cases in a table.
```

# Metadata

| *Summary*                     | Calculate the maximum of twelve real numbers. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Arithmetics, loops, conditionals. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Determine the max of numbers using a loop, logical operators and conditional statements. |
| *Testing learning goals*      | Testing all relevant combinations of input. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

