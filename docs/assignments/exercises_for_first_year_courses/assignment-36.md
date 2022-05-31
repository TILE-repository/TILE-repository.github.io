---
title: "Calculating and verifying serial numbers based on dates"
summary: "Calculating and verifying serial numbers based on dates."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals', 'imperative programming > functions > algorithms', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...  

# Calculating and verifying serial numbers based on dates





Implement a Python program that asks the user for four inputs: a
serial number, a day, a month, and a year of production date. First
your program has to verify that the given day, month and year
correspond to a correct date. If not, your program will notify that
on the screen and it will stop. You can finish a program with the
instruction `exit()`.

If the date is correct, then you have to check if the serial number
corresponds to the production date and print the result on the
screen.

The serial number has to be 8 numbers long (remember the use of the
`len()` function), any number with another length is wrong.

Then we should check whether the serial number is correct and inform
the user. A serial number is correct when:

1.  The first 4 digits of the number (n1, n2, n3 and n4) meet the
    following properties:

    1.  n1 = (d1 + d2)% 10.

    2.  n2 = (m1 + m2)% 10.

    3.  n3 = (y1 + y4)% 10.

    4.  n4 = (y2 + y3)% 10.

2.  The sum of the last 4 digits of the number (n5, n6, n7 and n8)
    must be less than 25.

What tests have you run to ensure that your program has the desired
behaviour? Note that dates can be incorrect in many ways, make sure
your program detects them all and stops when you enter:

-   day that is $$\leq 0$$

-   month that is $$\leq 0$$

-   year that is $$< 0$$ (do we accept the year 0?)

-   days $$>=31$$ for months that only have 30 days

-   days $$>=32$$ for months that only have 31 days

-   29th of February when it is not a leap year

Then for correct dates, calculate some serial numbers by hand such
that you can test the output of your program.

```testruntile
Insist that the students test their programs by giving them hints on
what to test.
```
