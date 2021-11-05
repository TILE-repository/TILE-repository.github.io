---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Calculating discounts



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

A bakery sells slices of bread for 3.49 euros each. A day old bread
gets a discount of 60 percent. Write a program that asks the user
for the number of day old loaves of bread they want to buy. Then
your program should show the price of bread, the discount for being
a day old and the total price. Each one of these amounts must be
shown on their own line with a suitable label. Every values should
be displayed using two decimal places, and decimal points in all
numbers should line up when the user enters reasonable values.

You have to test your program to see if it works well.

```small
>>> %Run 
    Enter the number of day old loaves: 45
    -------------------------
    Regular price:     157.05
    Discount:           94.23
    -------------------------
    Total:              62.82

>>> %Run 
    Enter the number of day old loaves: 0
    -------------------------
    Regular price:       0.00
    Discount:            0.00
    -------------------------
    Total:               0.00

>>> %Run 
    Enter the number of day old loaves: -4
    You cannot buy negative amounts of bread
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```


# Metadata

| *Summary*                     | Calculating discounts. |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | String formatting, number formatting. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | String formatting, number formatting. |
| *Testing learning goals*      | Applying and designing test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

