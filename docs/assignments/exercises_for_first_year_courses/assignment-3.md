---
title: "Python exercises for first year programming courses"
author:  Tanja E.J. Vos
...

# Three way value swapping

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

Make a program in Python that receive values for three variables

`a`, `b` and `c`, and interchange their values as follows:

-   `b` takes the value of `a`,

-   `c` takes the value of `a`, and

-   `a` takes the value of `c`.

This must be done WITHOUT using auxiliary variables, that is,
additional helper variables that are not a, b or c, and are used to
store some values.

Execute tests through the console and check the output. Does your
program work for negative numbers? Does it work for characters? Does
it work for reals? Can `a`, `b` and `c` have different types? Should
your program work for all these cases?

```testruntile
This exercise was TILEd by adding the last paragraph. We explicitly
ask the students to test for different types of values. Most
students, because of the example execution convert the user input to
int, but that is not necessary for the swapping, anything can be
swappped. Asking them to test with all kinds of values makes them
aware of the assumptions they made when reading the exercises and
hence how testing is good to find errors.
```

# Metadata

| _Summary_ | Swapping values. |
| _TILE aspects_ |Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output, variables. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ | n/a |