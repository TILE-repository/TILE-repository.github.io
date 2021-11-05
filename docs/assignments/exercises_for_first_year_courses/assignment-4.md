---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Simple calculator



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

The expressions on the right of the assignment can be all complex that we want. 
Implement a program that reads two real numbers, calculates and prints their sum (`+`), subtraction (`-`), product (`*`) and division (`/`).

```
>>> %Run 
    Enter a real number: 2.5
    Enter another real number: 34.903
    The sum is: 37.403
    The subtraction is: -32.403
    The product is: 87.2575
    The division is: 0.07162708076669627
>>> %Run 
    Enter a real number: 0
    Enter another real number: 4
    The sum is: 4.0
    The subtraction is: -4.0
    The product is: 0.0
    The division is: 0.0
>>> %Run 
    Enter a real number: 2000
    Enter another real number: 45.88
    The sum is: 2045.88
    The subtraction is: 1954.12
    The product is: 91760.0
    The division is: 43.59197907585004
```

What happens when you test your programs with two zeros? Why does
that happen? What could we do about that?

```testruntile
TILEd by adding example test executions for them to test.
```


# Metadata

| _Summary_ | Simple calculator. |
| _TILE aspects_ |Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output, variables. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
| _Added by_                    | Tanja E.J. Vos |  