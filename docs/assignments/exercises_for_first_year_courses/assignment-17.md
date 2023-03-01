---
title: "Calculating discounts"
summary: "Calculating discounts."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
... 

# Calculating discounts





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
