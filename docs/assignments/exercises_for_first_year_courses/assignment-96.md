---
title: "Mortal set theory"
summary: "Mortal set theory."
prerequisites: "['data > types (built-in) > composite > sets', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > primitive > boolean', 'data > types (built-in) > composite > sets', 'control flow > conditionals', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Mortal set theory

A famous syllogism says:

All humans are mortal.

Socrates is human.

Therefore Socrates is mortal.

In the following code, you will see multiple sets. 
The first contains all things (I know some are missing, but consider it complete for this problem). 
he second is a set of all people (assuming that the first set is really complete).
The third contains everything that is mortal (again, assuming that is complete).

```python
all = "Socrates", "Plato", "Eratosthenes", "Zeus", "Hera", "Athene", "Acropolis", "Cat", "Dog" 
people = "Socrates", "Plato", "Eratosthenes" 
mortals = "Socrates", "Plato", "Eratosthenes", "Cat", "Dog"
```

Use the set operators and their methods to show that it is true
that:

a\) all humans are mortal,

b\) Socrates is human and

c\) Socrates is mortal.

\(d\) there are mortal things that are not human, and

\(e\) there are things that are not mortal.
