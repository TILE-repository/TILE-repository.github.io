---
title: "Variables as operator and operand"
summary: "Using variables as an operator and an operand."
prerequisites: "['data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Variables as operator and operand





Copy and test the following program:

```python
a = int(input("Enter a value for a = "))
a = a + 1
print("The value of the variable a is now ", a);
```

As can be seen, the same variable can appear both as an operand and
as an operator. This is a normal and widely used programming
situation, so you should get used to it. Now replace the instruction
*a = a + 1* by *a += 1*.

```testruntile
This exercise would say: "copy and execute the following program",
the change to "copy and test the following program" is a very
subtle TILE.
```
