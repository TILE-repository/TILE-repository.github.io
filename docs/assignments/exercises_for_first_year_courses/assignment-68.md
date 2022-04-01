---
title: "Delete negative values from a list"
summary: "Delete negative values from a list."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'control flow > loops', 'control flow > conditionals', 'data > types (built-in) > composite > sequences > lists']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Delete negative values from a list

Write a Python function `delete_negatives` that takes a list as an
argument and returns the same list but without the negative
elements.

```small
>>> delete_negatives([0,-1,-11,2,33,-100,5])
    [2, 33, 5]
>>> delete_negatives([-1,-11,-3])
    []
>>> delete_negatives([4,68,111])
    [4, 68, 111]
```

Run more automated tests with pytest. Don't forget a test for the
empty list and the list with 1 element.
