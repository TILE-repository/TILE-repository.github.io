---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Working with relational operators



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

Implement a program that asks the user for a relational operator
(`<, <=, >, >=, ==, !=`) and 2 values. Your program has to display
on screen the result (`True` or `False`) of the given operation
applied to the two values.

You can design the layout of the input and output of your program as
you want. Run the following test cases to test the operation of your
program:

**test case ID** | **inputs** |         |         | **expected output** 
------------------|------------|------------|------------|---------------------
                    | operator   | value1     | value2     |                     
1                | `<`        | 12         | 4          | `False`             
2                | `>`        | 100        | 40         | `True`              
3                | `==`       | `"Hello!"` | 40         | `False`             
4                | `!=`       | 100        | `"Python"` | `True`              
5                | `>=`       | 98.67      | 0.45       | `True`              
6                | `<=`       | -100       | 40         | `True`              
7                | `<`        | 24         | `"24K"`    | `True`              
8                | `>=`       | `"email"`  | `"correo"` | `True`              



```testruntile
Insist that the students test their programs by giving them example
test cases in a table. Again the chosen values will make them aware
that this is not only for numerical values.
```

# Metadata

| *Summary*                     |  |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Logical operators |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with logical operators |
| *Testing learning goals*      | Testing for robustness |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

