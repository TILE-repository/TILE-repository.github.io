---
title: "Currency symbol lookup"
summary: "Currency symbol lookup."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables']"
concepts practised: "['data > types (built-in) > composite > dictionaries', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Currency symbol lookup

Write a program that stores in a variable the following dictionary:

`{'Euro':'€', 'Dollar':'$', 'Yen':'¥'},`

It should ask the user for a currency and display its symbol or a
warning message if the currency is not in the dictionary.

```small
>>> %Run 
    Enter a currency: Euro
    €
>>> %Run 
    Enter a currency: Dollar
    $
>>> %Run 
    Enter a currency: Wow
    That currency is not in the dictionary
```
