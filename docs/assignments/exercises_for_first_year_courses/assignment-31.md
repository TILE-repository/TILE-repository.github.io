---
title: "Marathon selection"
summary: "Marathon selection."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > conditionals', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Marathon selection





Write a program that determines if an athlete is selected to run a
marathon. To be selected, the qualifying times are:

-   150 minutes for men under 40

-   175 minutes for men over 40

-   180 minutes for women

The data to be entered are: sex (possible values: M, F), age and
time. It is necessary to verify if the entered data have suitable
values, and if not, indicate it and stop the program. When the data
is correct, the program will display the message "Selected" or "Not
selected".

```small

>>> %Run 
    Sex M/F: Y
    Enter only the letters M or F
>>> %Run 
    Sex M/F: F
    Age: -4
    Enter a correct age
>>> %Run 
    Sex M/F: M
    Age: 14
    Time: -400
    Enter a correct time
>>> %Run 
    Sex M/F: M
    Age: 14
    Time: 300
    Not selected
>>> %Run 
    Sex M/F: M
    Age: 50
    Time: 170
    Selected
```

What other tests do you have to run to ensure that you have tried
all the possible combinations? (HINT: in the tests above we have
never tested the outputs when the sex is `F`)

```testruntile
Insist that the students test their programs by giving them example
test executions. Add a comment on tests that might be missing and
that they have to think about.
```
