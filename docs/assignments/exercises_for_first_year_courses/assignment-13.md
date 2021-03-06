---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
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


# Metadata

| _Summary_ | Basic cryptography |
| _TILE aspects_ | Test run TILE-ing is applied. |
| _Topics_ | Using modulo operator |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | Using modulo to do basic cryptography. |
| _Testing learning goals_ | Applying test cases, input validation. |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
| _Added by_                    | Tanja E.J. Vos |  