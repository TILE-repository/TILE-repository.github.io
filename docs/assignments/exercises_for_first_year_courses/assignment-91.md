---
title: "Calculating sums of the even- and the odd-indexed numbers"
summary: "Calculating sums of the even- and the odd-indexed numbers."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > tuples', 'imperative programming > variables']"
concepts practised: "['data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > tuples', 'control flow > conditionals', 'control flow > loops', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Calculating sums of the even- and the odd-indexed numbers

Write a `odd_sum` function that takes a list or tuple of numbers. It
should return a two-element tuple, containing (respectively) the sum
of the even-indexed numbers and the sum of the odd-numbered numbers.
Example:

```small
>>> odd_even_sum([2,4,6,1,12,3,4])
    (24, 8)
>>> odd_even_sum([0,2,4,6,1,12,3,4])
    (8, 24)
>>> odd_even_sum((1,2,1,2,1,2))
    (3, 6)
>>> odd_even_sum((2,1,2,1,2,1,2))
    (8, 3)
>>> odd_even_sum(())
    (0, 0)
>>> odd_even_sum([])
    (0, 0)
```

