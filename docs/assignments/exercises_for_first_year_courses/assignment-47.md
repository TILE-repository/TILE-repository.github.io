---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Armstrong numbers



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

A three-digit number is called an Armstrong number if the sum of the
cube of its digits equals the number itself. For example, 153 is an
Armstrong number because ($$1 ^ 3$$) + ($$5 ^ 3$$) + ($$3 ^ 3$$) = 153.
Write all Armstrong numbers between 100 and 500.

To test your program consider these numbers, which are the only
Armstrong numbers:

$$153=1^3+5^3+3^3$$

$$370=3^3+7^3+0^3$$

$$371=3^3+7^3+1^3$$

$$407=4^3+0^3+7^3$$

```testruntile
Insist that the students test their programs by giving them the
expected outcome of their program.
```

# Metadata

| *Summary*                     | Calculating armstrong numbers. |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | Arithmetics,  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with individual digits of numbers, calculating the power of a number. |
| *Testing learning goals*      | Test completeness |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

