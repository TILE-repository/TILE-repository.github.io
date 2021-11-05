---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Grading statistics



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

Write a program that reads the grades of the students of a certain
subject until the user enters the word "exit". The exit of your
program must write at the end the number of passed, the number of
failed, and the average grade. Remember that a string can be
converted to a float, by calling `float`. Test it:

```small
>>> s = "3.456"
>>> float(s)
3.456
>>> s = "-3.456"
>>> float(s)
-3.456
```

Some examples of program executions are below. There you can see how
your program should handle negative numbers.

```small
>>> %Run 
    Enter a grade or 'exit': 3.5
    Enter a grade or 'exit': 0
    Enter a grade or 'exit': 10
    Enter a grade or 'exit': 9.99
    Enter a grade or 'exit': 5
    Enter a grade or 'exit': 6
    Enter a grade or 'exit': 8
    Enter a grade or 'exit': exit
    Passed: 5
    Failed: 2
    Average grade: 6.07
>>> %Run 
    Enter a grade or 'exit': -4
    You cannot enter negative amounts.
    Enter a grade or 'exit': 4
    Enter a grade or 'exit': -6.4
    You cannot enter negative amounts.
    Enter a grade or 'exit': 0
    Enter a grade or 'exit': 3
    Enter a grade or 'exit': exit
    Passed: 0
    Failed: 3
    Average grade: 2.3333333333333335  
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```

# Metadata

| *Summary*                     | Calculate basic grading statistics. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Loops, conditionals. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Working with do..while |
| *Testing learning goals*      | Input validation |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   