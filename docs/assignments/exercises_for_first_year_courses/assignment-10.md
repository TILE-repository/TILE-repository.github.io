---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Gross / net salary calculator





Implement a program that calculates the gross and net salary of an
employee. The program will request as data: the number of hours
worked (nh), the price of the hour (ph) and the applicable
withholding as a percentage (w). The gross (GS) and net (NS) salary
is calculated as:

1.  $$GS = nh * ph$$

2.  $$NS = GS - (w/100*GS)$$

```
>>> %Run 
    Enter the number of hours worked: 56
    Enter the price of the hour: 10
    Enter the applicable withholding in %: 25
    The gross salary is: 560.0
    The net salary is: 420.0
```

To test your program you can try with the following test cases:

| test case ID | inputs    |                 |       | expected output |               |
|--------------|-----------|-----------------|-------|-----------------|---------------|
|              | $$nh$$    | $$ph$$          | $$w$$ | gross salary    | net salary    |
| 1            | 56 hours  | 10 euros/hour   | 25%   | 560 euros       | 420 euros     |
| 2            | 2.5 hours | 20.4 euros/hour | 25.6% | 51.0 euros      | 37.944 euros  |
| 3            | 1 hour    | 25 euros/hour   | 0.1%  | 25.0 euros      | 24.975 euros  |
| 4            | 125 hours | 20 euros/hour   | 0%    | 2500.0 euros    | 2500.00 euros |


```testruntile
Add a table with test cases. Also added cases for values that are
less obvious like 2.5 hours and 0.1%. So they test again their
assumptions of the types of the variables.
```

# Metadata

| _Summary_ | Calculating gross / net salary |
| _TILE aspects_ | Test cases TILE-ing is applied. |
| _Topics_ | Input output, variables. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | Arithmetics |
| _Testing learning goals_ | Applying test cases. |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
| _Added by_                    | Tanja E.J. Vos |  