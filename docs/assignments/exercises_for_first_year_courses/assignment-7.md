---
title: "Python exercises for first year programming courses"
author:  Tanja E.J. Vos
...

# Working with expressions

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

Let us practice a bit with writing expressions. Implement a program that asks the user for two numbers, $$x$$ and $$y$$ and calculates the following:

1.  $$x+y$$

2.  $$(x+y)x$$

3.  $$xx + yy$$

4.  $$x^{5y}$$

5.  $$3x^5-5x^3+2x-7$$

6.  $$yx^5-(y+1)x^3+5x-y$$

7.  $$x^{yy+2^y}$$

Test your program (and your math skills) by:

-   First doing he exercises by hand for $$x=4$$ and $$y=6$$ to obtain
    the expected outputs.

-   Second, check the answers of your program with your expected
    outputs.

```testruntile
We ask the students to do the calculations by hand such that they
can use those to test their program. It makes them aware of the need
for an oracle with which they need to check the outputs.
```


# Metadata

| _Summary_ | Working with expressions. |
| _TILE aspects_ |Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output, variables. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ | n/a |