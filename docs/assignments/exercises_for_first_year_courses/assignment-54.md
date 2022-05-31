---
title: "Testing if a number is prime - part two"
summary: "Testing if a number is prime - part two."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables']"
concepts practised: "['expressions > operators > relational operators', 'control flow > conditionals', 'data > types (built-in) > primitive > boolean']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Testing if a number is prime - part two

Write a program that reads an integer number from the keyboard and
determines with the function `is_prime` from the [Checking if a number is prime](exercises_for_first_year_courses/assignment-53.md) exercise if it is a prime number. Write the program in such a way that it can be used to read several different numbers from the keyboard until the user writes the word end. When the user types something that is not an integer, you have to indicate it and give him the opportunity to write a number again.

You can test your program with the following tests:

```small
>>> %Run 
    Write an integer number, or 'end' to finish: end
>>> %Run 
    Write an integer number, or 'end' to finish: 4
    4 it is not a prime number
    Write an integer number, or 'end' to finish: 97
    97 is a prime number
    Write an integer number, or 'end' to finish: -4
    -4 it is not a prime number
    Write an integer number, or 'end' to finish: hello?
    just integer numbers or 'end' to finish!
    Write an integer number, or 'end' to finish: x
    just integer numbers or 'end' to finish!
    Write an integer number, or 'end' to finish: end
>>> 
```

```testruntile
Insist that the students test their programs by giving them example
test runs.
```
