---
title: "Removing first and last digits from and interger"
summary: "Removing first and last digits from and interger."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'expressions > operators > arithmetic operators', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Removing first and last digits from and interger

Write a function that, given an integer $$N1$$, returns another integer $$N2$$ that is the result of removing the first and last digit of $$N1$$. Note: If $$N1$$ has 2 digits or only one, then $$N2$$ must be 0. Examples of test cases that you can automate with pytest are:

**testcase number**   |**input ($$N1$$)**   |**expected output ($$N2$$)**
-----------------|-------------- |------------------------
1              |   42635    |      263
2             |    23       |      0
3              |   5        |      0
4             |    0         |     0
5             |    -3456     |     -45

```testruntile
Insist that the students test their programs by giving them a table
of test cases.
```
