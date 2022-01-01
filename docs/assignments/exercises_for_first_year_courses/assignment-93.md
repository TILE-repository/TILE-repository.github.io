---
title: "Intersecting two sets"
author: TILEd by Tanja E.J. Vos
...

# Intersecting two sets

Write a `tuple_inter` function that receives two sets. The function
must return a tuple that contains the intersection of the two sets
and the result of erasing the intersection in the first set.

For example you can test your function with:

```small
>>> firstSet  = {23, 42, 65, 57, 78, 83, 29}
>>> secondSet = {57, 83, 29, 67, 73, 43, 48}

>>> tuple_inter(firstSet, secondSet)
    ({57, 83, 29}, {65, 42, 78, 23})
>>> tuple_inter(firstSet, firstSet)
    ({65, 83, 23, 57, 42, 29, 78}, set())
>>> tuple_inter(set(), set())
    (set(), set())
```


# Metadata

| *Summary*                     | Intersecting two sets |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

