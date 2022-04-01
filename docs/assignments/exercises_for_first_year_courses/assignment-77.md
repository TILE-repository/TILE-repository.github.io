---
title: "Determine if a student has passed based on input from a file"
summary: "Determine if a student has passed based on input from a file."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'control flow > loops', 'io > files > text > plain', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Determine if a student has passed based on input from a file

We have the following format for a text file:

```small
23 2.5 3.0 1.1
34 2.0 1.0 1.0
17 1.0 1.0 1.1
450 4.0 2.1 2.2
55 4.0 4.0 2.0
```

In each line we have:

-   the student's file number, which is an integer

-   the grade of the first partial, a real value

-   the grade of the second partial, a real value

-   the attendance grade, a real value

Write a function `calculate_notes` in Python that receives as a parameter the name of a text file that has the format as `thenotes.txt`, and writes on the screen the total number of students and how many of them have passed. A student will be deemed to have passed when the sum of his three grades is greater than or equal to 5.

```small
>>> calculate_grades("threegrades.txt")
    number of students: 5
    number of students who have passed: 3
>>> 
```