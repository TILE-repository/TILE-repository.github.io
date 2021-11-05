---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Months by number



------------------------------------------------------------------------

Python exercises used for first year programming courses that
have been adapted by using Test Informed Learning with Examples (TILE)
to integrate testing in programming education without it costing (much)
more time. The coloured boxes indicate how they were TILEd.

```testdomaintile
This colour box explains a TILE in the test domain.
```

```testruntile
This colour box explains a TILE related to test runs 
and/or test cases.
```
------------------------------------------------------------------------

# Assignment

Implement a program that reads an integer corresponding to a month
of the year and displays the name of the corresponding month. If the
entered number does not belong to the range [1, 12], an error
message will be displayed.

```small

>>> %Run 
    Enter the number of the month: 5
    May
>>> %Run 
    Enter the number of the month: 12
    December
>>> %Run 
    Enter the number of the month: 13
    Error: enter a number between 1 y 12
>>> %Run 
    Enter the number of the month: -3
    Error: enter a number between 1 and 12
>>> %Run 
    Enter the number of the month: 0
    Error: enter a number between 1 and 12
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```

# Metadata

| *Summary*                     | Determine the name of the month based on the number. |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | Using key value pairs, dictionaries. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Using dictionaries. |
| *Testing learning goals*      | Applying oundary value testing. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   