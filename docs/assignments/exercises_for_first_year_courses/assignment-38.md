---
title: "The sum of the odds and even numbers"
summary: "Calculating the sum of the odds and of the even numbers."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# The sum of the odds and even numbers





Implement a program to read 10 positive numbers and independently
calculate the sum of the odd and even numbers. If a negative number
is entered, the program will display an error message and ask for
the number again.

```small
>>> %Run 
    Enter a number: 4
    Enter a number: 5
    Enter a number: 6
    Enter a number: 7
    Enter a number: 8
    Enter a number: 9
    Enter a number: 12
    Enter a number: -4
    Please enter only positive numbers
    Enter a number: 0
    Enter a number: 3
    Enter a number: 209
    Sum of the even numbers:  30
    Sum of the odd numbers:  233
>>> %Run
    Enter a number: -4
    Please enter only positive numbers
    Enter a number: -0
    Enter a number: 4
    Enter a number: 4
    Enter a number: 5
    Enter a number: 5
    Enter a number: 6
    Enter a number: 6
    Enter a number: 7
    Enter a number: 7
    Enter a number: 8
    Sum of the even numbers:  28
    Sum of the odd numbers:  24
>>> %Run 
    Enter a number: 2
    Enter a number: 4
    Enter a number: 6
    Enter a number: 8
    Enter a number: 0
    Enter a number: 16
    Enter a number: 18
    Enter a number: 20
    Enter a number: 36
    Enter a number: 90
    Sum of the even numbers:  200
    Sum of the odd numbers:  0
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
