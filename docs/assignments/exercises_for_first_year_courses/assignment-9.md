---
title: "Python exercises for first year programming courses"
author:  Tanja E.J. Vos
...

# Variables as operator and operand

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

Copy and test the following program:

```python
a = int(input("Enter a value for a = "))
a = a + 1
print("The value of the variable a is now ", a);
```

As can be seen, the same variable can appear both as an operand and
as an operator. This is a normal and widely used programming
situation, so you should get used to it. Now replace the instruction
*a = a + 1* by *a += 1*.

```testruntile
This exercise would say: "copy and execute the following program",
the change to "copy and test the following program" is a very
subtle TILE.
```

# Metadata

| _Summary_ | Using variables as an operator and an operand. |
| _TILE aspects_ | Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | Arithmetics |
| _Testing learning goals_ | Test awareness |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ | n/a |