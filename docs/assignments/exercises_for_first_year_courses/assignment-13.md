---
title: "Calculating PIN codes"
summary: "Basic cryptography."
prerequisites: "['data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Calculating PIN codes


Implement a program that reads three integer values: day, month, and
year of a person's birth. Using this data, the program should show a
four-digit PIN associated with the date of birth. The PIN is
calculated as:

1.  p1 = (d1 + d2)% 10.

2.  p2 = (m1 + m2)% 10.

3.  p3 = (y1 + y4)% 10.

4.  p4 = (y2 + y3)% 10.

For example, if the date entered is 29 9 1975, the PIN would be 1 9
6 6:

1.  p1 = (2 + 9)% 10 = 1.

2.  p2 = (0 + 9)% 10 = 9.

3.  p3 = (1 + 5)% 10 = 6.

4.  p4 = (9 + 7)% 10 = 6.

```small
>>> %Run 
    Enter your day of birth: 29
    Enter your month of birth: 9
    Enter your year of birth: 1975
    Your PIN is 1 9 6 6 
```

**test case ID** | **inputs** |    |   | **expected output (PIN)** 
------------------|------------|-------|------|---------------------------
                    | day        | month | year |                           
1                | 10         | 12    | 1522 | 1 3 7 2                   
2                | 1          | 1     | 1    | 1 1 1 0                   
3                | 27         | 3     | 1978 | 9 3 9 6                   
4                | 55         | 28    | 300  | 0 0 0 3                   
5                | 356        | 903   | 1568 | 1 3 9 1                   

Look at test cases 4 and 5. Are they valid? Inputs 55 and 356 are
not valid numbers for a day of birth. However, our program works and
calculates a PIN. Python does not know what birthdays are and when
they are valid. For Python the 3 inputs are simply whole numbers. If
we want our program not to calculate a PIN when the date is not
valid, then we should add conditions that verify the inputs. We will
see how we can do it in the next thematic unit with decision
statements like `if - then - else`.

```testruntile
A table with test cases was added and the student were made aware of
the test cases that not really contained valid dates but still
calculated a PIN number.
```
