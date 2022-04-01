---
title: "Grading statistics"
summary: "Calculate basic grading statistics."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'control flow > conditionals', 'data > types (built-in) > composite > sequences > string']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Grading statistics





Write a program that reads the grades of the students of a certain
subject until the user enters the word "exit". The exit of your
program must write at the end the number of passed, the number of
failed, and the average grade. Remember that a string can be
converted to a float, by calling `float`. Test it:

```small
>>> s = "3.456"
>>> float(s)
3.456
>>> s = "-3.456"
>>> float(s)
-3.456
```

Some examples of program executions are below. There you can see how
your program should handle negative numbers.

```small
>>> %Run 
    Enter a grade or 'exit': 3.5
    Enter a grade or 'exit': 0
    Enter a grade or 'exit': 10
    Enter a grade or 'exit': 9.99
    Enter a grade or 'exit': 5
    Enter a grade or 'exit': 6
    Enter a grade or 'exit': 8
    Enter a grade or 'exit': exit
    Passed: 5
    Failed: 2
    Average grade: 6.07
>>> %Run 
    Enter a grade or 'exit': -4
    You cannot enter negative amounts.
    Enter a grade or 'exit': 4
    Enter a grade or 'exit': -6.4
    You cannot enter negative amounts.
    Enter a grade or 'exit': 0
    Enter a grade or 'exit': 3
    Enter a grade or 'exit': exit
    Passed: 0
    Failed: 3
    Average grade: 2.3333333333333335  
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
