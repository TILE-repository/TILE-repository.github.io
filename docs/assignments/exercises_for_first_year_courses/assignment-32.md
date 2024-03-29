---
title: "Car insurance calculator"
summary: "Car insurance calculator."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals', 'imperative programming > functions > algorithms', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Car insurance calculator





Write a Python program that determines the cost of a car insurance
depending on: the age of the person to be insured, and the number of
years this person has a driver's license, and the number of
accidents the person has been involved in. The program will ask for
these data (in that order) to be entered by keyboard, and will
return the amount of insurance if possible, taking into account
that:

a)  The customer must be over 18 years of age to be able to insure.

b)  The base amount is 300 euros.

c)  200 euros are added if the license is less than 3 years old, 150
    euros are added between 3 (inclusive) and 5 years (not
    inclusive), or 100 euros are added between 5 and 10 years (both
    inclusive).

d)  200 euros are added if the age of the customer is under 25 years
    old.

e)  There is an additional charge depending on the number of
    accidents:


**Accidents** | **Charge (euros)** 
---------------|--------------------
1             | 50                 
2             | 125                
3             | 225                
4             | 375                
5             | 575                
6 or more     | Not insured        

```small
>>> %Run 
    Age: 10
    You have to be 18 or over to have car insurance.
>>> %Run 
    Age: 18
    Years with license: 0
    Number of accidents: 0
    The amount of the insurance is:  700 €
>>> %Run 
    Age: 30
    Years with license: 3
    Number of accidents: 1
    The amount of the insurance is:  500 €
>>> %Run 
    Age: 20
    Years with license: -4
    Enter an appropriate number of years
>>> %Run 
    Age: 20
    Years with license: 4
    Number of accidents: -7
    Enter a positive number
```

What other tests have you run to ensure that your program has the
desired behaviour?

Have you tried ages that lead to different behaviours? Try with the
test cases (`age \le 25`), (`age \ge 25`) and also when the age is
exactly 25, a value located between the two behaviour intervals.

Have you tested your program for all possible ranges of years that
the user can have the license? For example, the test cases for the
years intervals `[0, 3[`, `[3, 5[` and `[5, 10]`.

Have you tested your program with all possible values for the number
of accidents?

And how about different combinations of the cases mentioned above?

```testruntile
Insist that the students test their programs by giving them example
test executions. Moreover, guide them through a thinking process of
what else needs to be tested.
```
