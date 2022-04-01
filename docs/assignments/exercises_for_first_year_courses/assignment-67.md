---
title: "Fibonacci sequences"
summary: "Fibonacci sequences."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals', 'data > types (built-in) > composite > sequences > lists']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Fibonacci sequences

Implement a function `fib(n)` that returns a list with the first `n` numbers of Fibonacci. If `n == 0`, the function must return the list `[1]`, if `n == 1`, the function must return the list `[1,1]`. When `n < 1`, then start with the list `[1,1]` and add the next Fibonacci number by adding the previous numbers in the list.

For example by typing:

```small
>>> print(fib(0))
    [1]
>>> print(fib(1))
    [1, 1]
>>> print(fib(2))
    [1, 1, 2]
>>> print(fib(12))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
```

Don't forget your pytests to automate the tests!
