---
title: "Intersecting two sets"
summary: "Intersecting two sets."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite', 'control flow > loops', 'data > types (built-in) > composite > sequences > tuples']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Intersecting two sets

Write a `tuple_inter` function that receives two sets. The function
must return a tuple that contains the intersection of the two sets
and the result of erasing the intersection in the first set.

For example you can test your function with:

```small
>>> firstSet  = {23, 42, 65, 57, 78, 83, 29}
>>> secondSet = {57, 83, 29, 67, 73, 43, 48}

>>> tuple_inter(firstSet, secondSet)
    ({57, 83, 29}, {65, 42, 78, 23})
>>> tuple_inter(firstSet, firstSet)
    ({65, 83, 23, 57, 42, 29, 78}, set())
>>> tuple_inter(set(), set())
    (set(), set())
```