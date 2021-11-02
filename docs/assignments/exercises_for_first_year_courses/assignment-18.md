---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Letter exchanger

By [Tanja E.J. Vos](https://www.tanjavos.com).

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


Write a Python program that asks the user for a word $$p$$ and it
returns in the output another word in which the first and last
characters of $$p$$ have been exchanged. Use the chain cutter
operator. Run the following tests to test the operation of your
program:

**test case ID** | **input** | **expected output** 
------------------|-----------|---------------------
1                | `""`      | `""`                
2                | `"a"`     | `"a"`               
3                | `"ab"`    | `"ba"`              
4                | `"ab ba"` | `"ab ba"`           


```testruntile
Insist that the students test their programs by giving them a table
of test cases.
```

# Metadata

| *Summary*                     | Exchange letters of the input. |
| *TILE aspects*                | Test case TILE-ing is applied. |
| *Topics*                      | String idexation |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Accessing elements of strings. |
| *Testing learning goals*      | Designing test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

