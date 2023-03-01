---
title: "Password complexity checker"
summary: "Password complexity checker."
prerequisites: "['io > standard > input', 'imperative programming > variables']"
concepts practised: "[, 'data > types (built-in) > composite > sequence > strings', 'expressions > operators > relational operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Password complexity checker

Write a function that receives a password as a parameter and
determines its complexity, according to these rules:

-   A very weak password contains only numbers and is less than
    eight characters long.

-   A weak password contains only letters and is less than eight
    characters long.

-   A strong password contains letters and at least one number, and
    is at least eight characters long.

-   A very strong password contains letters, numbers, and special
    characters and is at least eight characters long.

-   Passwords that are not weak or strong are normal.

Remember that in theory class we have seen the following predefined
functions in Python:

- `isdigit`, to check if a string has digits.

- `isalpha` to check if a string only contains characters of the alphabet.

To test your function well, how many test cases have you run? Have
you thought about both lowercase and uppercase?

```testruntile
Insist that the students test their programs by asking them
questions on what would be good test cases.
```
