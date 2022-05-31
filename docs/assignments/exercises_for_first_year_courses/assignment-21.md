---
title: "Months by number"
summary: "Determine the name of the month based on the number."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > conditionals', 'data > types (built-in) > composite > dictionaires']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Months by number





Implement a program that reads an integer corresponding to a month
of the year and displays the name of the corresponding month. If the
entered number does not belong to the range [1, 12], an error
message will be displayed.

```small

>>> %Run 
    Enter the number of the month: 5
    May
>>> %Run 
    Enter the number of the month: 12
    December
>>> %Run 
    Enter the number of the month: 13
    Error: enter a number between 1 y 12
>>> %Run 
    Enter the number of the month: -3
    Error: enter a number between 1 and 12
>>> %Run 
    Enter the number of the month: 0
    Error: enter a number between 1 and 12
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
