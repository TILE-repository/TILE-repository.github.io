---
title: "Python exercises for first year programming courses"
author: Tanja E.J. Vos
...

# Celsius to Fahrentheit converter

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

Implement a program that calculates the temperature in degrees Celsius from the temperature in degrees Fahrenheit. 
The formula is as follows: $$C = \frac{5}{9}(F-32)\;.$$ 
The input to the program is degrees Fahrenheit introduced by the user. 
We will save this value in a variable, for example `F`. 
Then, the program calculates the expression given by the formula and stores the result in another variable, for example `C`. The last step will consist of printing the result for the user.

```
>>> %Run
    Enter the degrees Fahrenheit: 84
    84.0 degrees Fahrenheit are 28.9 degrees Celsius
```

Run more tests of your program and use the following online
converter to check the outputs of your program:

<https://www.metric-conversions.org/es/temperatura/fahrenheit-a-celsius.htm>

```testruntile
We invite the student to test their program more and compare their
outcomes with a parallel oracle that they can find on the web.
```

# Metadata

| _Summary_ | Celsius to fahrenheit converter. |
| _TILE aspects_ |Test run TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output, variables. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ | None. |
| _Variants_ | n/a |
