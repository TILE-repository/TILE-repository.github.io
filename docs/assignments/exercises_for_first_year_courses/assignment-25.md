---
title: "Relational operators"
summary: "Working with relational operators."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > conditionals', 'data > types (built-in) > primitive > boolean', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Working with relational operators





Implement a program that asks the user for a relational operator
(`<, <=, >, >=, ==, !=`) and 2 values. Your program has to display
on screen the result (`True` or `False`) of the given operation
applied to the two values.

You can design the layout of the input and output of your program as
you want. Run the following test cases to test the operation of your
program:

**test case ID** | **inputs** |         |         | **expected output** 
------------------|------------|------------|------------|---------------------
                    | operator   | value1     | value2     |                     
1                | `<`        | 12         | 4          | `False`             
2                | `>`        | 100        | 40         | `True`              
3                | `==`       | `"Hello!"` | 40         | `False`             
4                | `!=`       | 100        | `"Python"` | `True`              
5                | `>=`       | 98.67      | 0.45       | `True`              
6                | `<=`       | -100       | 40         | `True`              
7                | `<`        | 24         | `"24K"`    | `True`              
8                | `>=`       | `"email"`  | `"correo"` | `True`              



```testruntile
Insist that the students test their programs by giving them example
test cases in a table. Again the chosen values will make them aware
that this is not only for numerical values.
```
