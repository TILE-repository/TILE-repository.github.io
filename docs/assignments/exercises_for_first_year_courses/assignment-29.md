---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Water company billing system






The water company is implementing a new billing system. For each
house, the invoice is made as follows:

1.  The first 50 litres are free.

2.  Between 50 and 200 litres, each litre is charged at 0.10 euros.

3.  From 200 litres on, each litre is charged at 0.30 euros.

4.  The minimum fee is 6 euros, that is, if the amount to pay is
    less than 6 euros, then the payment will be 6 euros.

Write a program that calculates the water consumption of a family in
a month given the number of litres used.

```small

>>> %Run 
    Enter the litres of water used: 0
    The expense is 6.00€
>>> %Run 
    Enter the litres of water used: -500
    Please enter a correct value
>>> %Run 
    Enter the litres of water used: 300
    The expense is 90.00€
>>> %Run 
    Enter the litres of water used: 55
    The expense is 6.00€
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```


# Metadata

| *Summary*                     | Water company billing system with conditional discounts. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Conditional application of rules. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Conditional statements, calculating percentages. |
| *Testing learning goals*      | Boundary value testing. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

