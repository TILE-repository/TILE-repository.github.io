---
title: "Python exercises for first year programming courses"
author: Tanja E.J. Vos
...

# Swapping values

By [Tanja E.J. Vos](https://www.tanjavos.com).

---

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

---

# Assignment

Given two variables `a` and `b`, write a Python program that allows
the user to enter two values for them, swap their values and display
them on the screen. The execution of the program should result in
the following:

```
>>> %Run
    Enter the value of the variable a: 4
    Enter the value of the variable b: 2
    The value of a is 2
    The value of b is 4
```

Assuming that 4 and 2 are the values entered by the user. This
should work for any pair of user-entered values.

Execute tests through the console and check the output. Does your
program work for negative numbers? Does it work for strings? Does it
work for characters? Does it work for reals? Can `a` and `b` have
different types? Should your program work for all these cases?

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
| _Prerequisites_ | None. |
| _Variants_ | n/a |
