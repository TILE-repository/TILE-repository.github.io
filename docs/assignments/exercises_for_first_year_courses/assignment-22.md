---
title: "Determine if a product is positive, negative or zero without calculating it"
summary: "Determine if a product of two numbers is positive, negative or zero without calculating it."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Determine if a product is positive, negative or zero without calculating it





Implement a program that reads two integer numbers and says if their
product is positive, negative, or zero **without** doing the
calculation.

Run the following combinations of examples to test that your program
produces the same outputs:

-   the first number is 0,

-   the second number is 0,

-   both numbers are 0,

-   both numbers are positive,

-   both numbers are negative,

-   the first number is negative and the second is positive,

-   the first number is positive and the second is negative.

```small
>>> %Run
    Enter the first integer number: 0
    Enter the second integer number: -1
    The product is zero
>>> %Run 
    Enter the first integer number: 5
    Enter the second integer number: 0
    The product is zero
>>> %Run 
    Enter the first integer number: 0
    Enter the second integer number: 0
    The product is zero
>>> %Run 
    Enter the first integer number: 2
    Enter the second integer number: 7
    The product is positive
>>> %Run 
    Enter the first integer number: -4
    Enter the second integer number: -7
    The product is positive
>>> %Run 
    Enter the first integer number: -8
    Enter the second integer number: 3
    The product is negative
>>> %Run 
    Enter the first integer number: 10
    Enter the second integer number: -6
    The product is negative
```

```testruntile
Insist that the students test their programs by giving them example
test executions. Also pointing out that this way we try out all
possible combinations to test.
```
