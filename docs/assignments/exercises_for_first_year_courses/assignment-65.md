---
title: "Counting numbers in a String"
summary: "Counting numbers in a String."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Counting numbers in a String


Design a function that given a text string, returns the numbers that appear in the string. For example, the string 'a 1, a 201, and 2 ones' contains 3 numbers: 1, 201, and 2.

```small
>>> nums_in_string("a 1, a 201 and 2 ones")
    3
>>> nums_in_string("without numbers")
    0
>>> nums_in_string("2345543")
    1
```

Write pytests to test your function in an automated way.

