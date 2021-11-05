---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Multiples of seven



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

Write a program that receives an integer $$N$$ and generates all the
multiples of 7 between 1 and $$N$$. Run the following test cases to
test your program:

**test case ID**  | **inputs** |  **expected outputs**              
--------------| --------| -------------------------------
1          |    0     |   there are no multiples of 7     
2          |    3     |   there are no multiples of 7     
3           |   -5   |    there are no multiples of 7     
4           |   -15   |   -7, -14                         
5           |   18   |    7, 14                           
6           |   57    |   7, 14, 21, 28, 35, 42, 49, 56   

```testruntile
Insist that the students test their programs by giving them example
test cases in a table. Again the chosen values will make them aware
that there program should also work for negative numbers.
```

# Metadata

| *Summary*                     | Calculating the multiples of 7 of a given number. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Loops, conditionals, arithmetics.  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with positive and negative numbers, calculation multiples of seven, determining the remainder of a division. |
| *Testing learning goals*      | Create awareness of test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

