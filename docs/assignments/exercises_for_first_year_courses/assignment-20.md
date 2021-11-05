---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Maximum and minumum



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

Implement a program that reads three values and displays on the
screen the maximum and the minimum. Run the following examples to
test that your program gives the same outputs:

```small
>>> %Run 
    Enter the first value: 3
    Enter the second value: 6
    Enter the third value: 8
    The maximum is 8 and the minimum is 3
>>> %Run 
    Enter the first value: -4
    Enter the second value: 6
    Enter the third value: 12
    The maximum is 6 and the minimum is -4
>>> %Run
    Enter the first value: 4.567
    Enter the second value: 9
    Enter the third value: 12.9
    The maximum is 9 and the minimum is 12.9
>>> %Run 
    Enter the first value: a
    Enter the second value: c
    Enter the third value: h
    The maximum is h and the minimum is a
>>> %Run 
    Enter the first value: hello
    Enter the second value: hola
    Enter the third value: bonjour
    The maximum is hola and the minimum is bonjour
>>> %Run 
    Enter the first value: 4
    Enter the second value: oh!
    Enter the third value: 4.89
    The maximum is oh! and the minimum is 4
```

```testruntile
Insist that the students test their programs by giving them example
test executions. The values used in the example test executions will
make then aware that the program was not only for numerical values
but for any value.
```


# Metadata

| *Summary*                     | Determine minimum and maximum of three values. |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      | Comparing numbers. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Comparing numbers. |
| *Testing learning goals*      | Determine usefull test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

