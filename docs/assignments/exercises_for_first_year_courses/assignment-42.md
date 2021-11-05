---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Counting test case failures



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

We have a total of 15 test cases of a Python program. From each test
we run, we take note of the number of failures that it finds. So at the
end we have a set of 15 natural numbers: From $$n_1$$ to $$n_{15}$$.

We are going to write a program that asks for these 15 natural
numbers through the keyboard and determines:

-   How many tests have not found any error, that is, 0.

-   How many tests have found between 1 and 3 errors.

-   How many have found more than 4 errors.

In the execution example below you can see how your program should
handle negative numbers.

```small
>>> %Run 
    Enter the number of bugs found by test 1: 3
    Enter the number of bugs found by test 2: 4
    Enter the number of bugs found by test 3: -5
    You cannot enter negative amounts.
    Enter the number of bugs found by test 3: 5
    Enter the number of bugs found by test 4: 6 
    Enter the number of bugs found by test 5: 7
    Enter the number of bugs found by test 6: 0
    Enter the number of bugs found by test 7: 0
    Enter the number of bugs found by test 8: 1
    Enter the number of bugs found by test 9: 2
    Enter the number of bugs found by test 10: 6
    Enter the number of bugs found by test 11: 1
    Enter the number of bugs found by test 12: 2
    Enter the number of bugs found by test 13: 0
    Enter the number of bugs found by test 14: 0
    Enter the number of bugs found by test 15: 2
    Number of tests that have found 0 errors:  4
    Number of tests that have found between 1 and 3 errors:  6
    Number of tests that have found more than 4 errors:  5
```

```testdomaintile
Categorising series of inputs, where the inputs are related to test
cases. Test cases can find errors!
```

# Metadata

| *Summary*                     | Failures per test case |
| *TILE aspects*                | Test domain TILE-ing is applied. |
| *Topics*                      | Conditionals, assignments, loops. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Basic calculations, loops and conditionals. Basic statistical analysis. |
| *Testing learning goals*      | Creating awareness of test failures. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   