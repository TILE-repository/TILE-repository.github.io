---
title: "Age statistics"
summary: "Calculating the age statistics."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Age statistics





Write a program that reads the age (an integer) of a set of people.
Data entry will end when a negative value is entered. Your program
has to calculate and display on the screen:

-   the average of the ages,

-   the maximum and minimum age, and

-   how many of them are people of working age, that is, their age
    is between 18 and 65 years old

```small
>>> %Run 
    Enter an age:50
    Enter an age:18
    Enter an age:0
    Enter an age:-2
    Average: 22.666666666666668
    Maximum age: 50
    Minimum age: 0
    People of working age: 2
>>> %Run 
    Enter an age:12
    Enter an age:16
    Enter an age:90
    Enter an age:65
    Enter an age:18
    Enter an age:17
    Enter an age:19
    Enter an age:66
    Enter an age:64
    Enter an age:-5
    Average: 40.77777777777778
    Maximum age: 90
    Minimum age: 12
    People of working age: 4
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
