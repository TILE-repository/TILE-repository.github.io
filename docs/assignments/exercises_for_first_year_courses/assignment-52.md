---
title: "Is this character a digit? - part two"
summary: "Calling another function to determine if a character is a digit."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables']"
concepts practised: "['expressions > operators > relational operators', 'control flow > conditionals', 'data > types (built-in) > primitive > boolean']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
... 

# Is this character a digit? - part two

Write a program that reads a character from the keyboard and
determines with the function `is_digit` from the [previous exercise](assignment-51.md)
if it is one of the digits from 0 to 9. Write the program in such a
way that it can be used to read several different characters from
the keyboard until the user writes the word end.

An example of a test session you can execute manualy via the shell could be:

```small
>>> %Run 
    Write a character or 'end' to finish: 4
    4 is a digit from 0 to 9
    Write a character or 'end' to finish: 56
    56 is not a digit from 0 to 9
    Write a character or 'end' to finish: z
    z is not a digit from 0 to 9
    Write a character or 'end' to finish: dfg
    dfg is not a digit from 0 to 9
    Write a character or 'end' to finish: 0
    0 is a digit from 0 to 9
    Write a character or 'end' to finish: end
>>>    
```

```testruntile
Insist that the students test their programs by giving them example
test runs.
```
