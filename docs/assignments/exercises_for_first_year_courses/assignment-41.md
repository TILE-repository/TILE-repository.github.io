---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Multiples of 7 not divisible by 3



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

Modify the previous program so that it displays only those multiples
of 7 between 1 and $$N$$ that are not divisible by 3. Execute the
following test cases to test your program:

**test case ID**   |**inputs**   |**expected outputs**                
-------------- |-------- ------------------------------- --
1              |0       | there are no multiples of 7     
2              |3        |there are no multiples of 7     
3             | -5     |  there are no multiples of 7     
4             | -65     | -7, -14, -28, -35, -49, -56     
5             | 18     |  7, 14                           
6             | 77      | 7, 14, 28, 35, 49, 56, 70, 77   

```testruntile
Insist that the students test their programs by giving them example
test cases in a table.
```

# Metadata

| *Summary*                     | Multiples of 7 not divisible by 3 |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Loops, conditionals, arithmetics. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with positive and negative numbers, calculation multiples of seven, determining the remainder of a division. |
| *Testing learning goals*      | Create awareness of test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   