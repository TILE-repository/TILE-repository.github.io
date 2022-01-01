---
title: "Integer series"
author: TILEd by Tanja E.J. Vos
...

# Integer series

Write a function that receives a number $$N$$ as a parameter and
generates a string with the numbers: $$1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, ... , 1, 2, 3, ... , N$$

Examples of test cases that you can automate with pytest are:

**testcase number** |  **input ($$N$$)**  | **expected output**
----------------- |------------- |-----------------------------------
1              |   4         |    "1, 1, 2, 1, 2, 3, 1, 2, 3, 4"
2            |     1       |      "1"
3            |     0       |      ""
4             |    -3      |      "-1, -1, -2, -1, -2, -3"

```testruntile
Insist that the students test their programs by giving them a table
of test cases.
```


# Metadata

| *Summary*                     |  |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

