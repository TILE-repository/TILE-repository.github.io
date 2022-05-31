---
title: "Quotient and remainder"
summary: "Calculate the quotient and the remainder of two positive numbers."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Quotient and remainder

Write a program to calculate the quotient and remainder of the
integer division of two positive integers, using only the
subtraction operation.

Test your program with the following outputs:

```small
>>> %Run 
    Enter a positive integer number: 0
    Enter another positive integer number: 4
    The quotient is 0
    The reminder is 0
>>> %Run 
    Enter a positive integer number: 4
    Enter another positive integer number: 0
    It cannot be divided by 0
>>> %Run 
    Enter a positive integer number: 25
    Enter another positive integer number: 25
    The quotient is 1
    The reminder is 0
>>> %Run 
    Enter a positive integer number: 26
    Enter another positive integer number: 20
    The quotient is 1
    The reminder is 6
>>> %Run 
    Enter a positive integer number: 20
    Enter another positive integer number: 26
    The quotient is 0
    The reminder is 20
>>> %Run 
    Enter a positive integer number: -4
    Enter another positive integer number: 5
    Only positive integers
>>> %Run 
    Enter a positive integer number: 10
    Enter another positive integer number: -4
    Only positive integers
```