---
title: "Travel times for conference speakers"
summary: "Travel times for conference speakers."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > tuples', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > primitive > numeric', 'control flow > loops', 'data > types (built-in) > composite > sequences > tuples']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Travel times for conference speakers

A common use of tuples is as records. And of course, displaying
those records in a table is a standard thing for programs to do. In
this exercise, we'll do a bit of both: reading a list of tuples and
displaying them in table format for the user.

Imagine that we organize a conference on testing and we know from
each speaker her name and the time he needs to travel to the
conference venue.

```python
speakers = [('Jeff', 'Offutt', 7.85), ('James', 'Bach', 3.626), ('Lisa', 'Crispin', 10.603) ]
```

Write a `format_sort_records` function in Python that allows
scheduling and returns the following table:

    James      Bach        3.63
    Jeff       Offutt      7.85
    Lisa       Crispin    10.60

This trip planner does not need the level of precision that the
entry provides; it is enough for us to have two digits after the
decimal point. Also note that the last name is printed after the
first name, followed by a decimal-aligned indication of how long
each proponent will take to arrive in increasing order. Each name
must be printed in a 10-character field, and the time must be
printed in a 5-character field, with a padding space character
between each of the columns.
