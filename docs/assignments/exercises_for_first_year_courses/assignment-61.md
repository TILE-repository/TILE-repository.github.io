---
title: "Integer series"
summary: "Integer series."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > loops', 'data > types (built-in) > composite > sequence > strings']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Integer series

Write a function that receives a number $$N$$ as a parameter and
generates a string with the numbers: $$1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, ... , 1, 2, 3, ... , N$$

Examples of test cases that you can automate with pytest are:

**testcase number** |  **input ($$N$$)**  | **expected output**
----------------- |------------- |-----------------------------------
1              |   4         |    "1, 1, 2, 1, 2, 3, 1, 2, 3, 4"
2            |     1       |      "1"
3            |     0       |      ""
4             |    -3      |      "-1, -1, -2, -1, -2, -3"

```testruntile
Insist that the students test their programs by giving them a table
of test cases.
```
