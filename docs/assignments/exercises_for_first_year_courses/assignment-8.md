---
title: "Test Informed Learning with Examples assignment"
author: Tanja E.J. Vos
...

# Interest calculator

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

Implement a program that calculates the interest produced from a
total accumulated capital of an amount _c_, invested at an interest _r_
(as a percentage) during _t_ days. The formula used to calculate
interest is:

$$I=\frac{c \times r \times t}{360 \times 100}$$

To test your program you can try with the following test cases:

| **test case ID** | **inputs** |        |     | **expected output** |
| ---------------- | ---------- | ------ | --- | ------------------- |
| $$c$$            | $$r$$      | $$t$$  |
| 1                | 10000      | 5.5%   | 360 | 550 euros           |
| 2                | 25000      | 60%    | 45  | 1875 euros          |
| 3                | 0          | 50%    | 200 | 0.0                 |
| 4                | -2000      | 45%    | 2   | -5.0                |
| 5                | 12.345     | 56.78% | 900 | 17.0                |

```testruntile
Instead of sample executions for them to check, we add a table with
test cases. This teaches them what test cases are made up of:

-   identifier

-   inputs

-   expected outputs
```

# Metadata

| _Summary_ | Calculating interest |
| _TILE aspects_ | Test cases TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | Arithmetics |
| _Testing learning goals_ | Applying test cases. |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
