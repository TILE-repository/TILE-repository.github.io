---
title: "Travel times for conference speakers"
author: TILEd by Tanja E.J. Vos
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


# Metadata

| *Summary*                     | Travel times for conference speakers |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

