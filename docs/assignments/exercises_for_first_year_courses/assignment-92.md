---
title: "Zipping sequences into tuples"
summary: "Zipping sequences into tuples."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Zipping sequences into tuples

`zip` is a function that is predefined in Python. It takes two or
more sequences and intersperses them. The name of the function
refers to a zipper, since it intersperses two rows of teeth.

This example zips a string and a list:

```small
>>> s = 'abc'
>>> t = [0, 1, 2]
>>> zip(s, t)
<zip object at 0x7f7d0a9e7c48>
```

The result is a **zip object** that contains pairs that can be
iterated over. The most common use of `zip` is in a `for` loop:

```small
>>> for pair in zip(s, t):
...     print(pair)
...
('a', 0)
('b', 1)
('c', 2)
```

We are going to write a `my_zip` function that does not return a zip
object, but directly the list with the tuples. You can assume that
the two sequences it receives have the same number of elements:

```small
>>> s = 'abc'
>>> t = [0, 1, 2]
>>> mi_zip(s,t)
[('a', 0), ('b', 1), ('c', 2)]
>>> s = (1,2,3)
>>> t = [4,5,6]
>>> mi_zip(s,t)
[(1, 4), (2, 5), (3, 6)]
```

Don't forget to test your function with pytests.
