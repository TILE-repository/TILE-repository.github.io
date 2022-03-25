---
title: "Interest calculator"
summary: "Calculating interest."
prerequisites: "['data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Interest calculator


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
