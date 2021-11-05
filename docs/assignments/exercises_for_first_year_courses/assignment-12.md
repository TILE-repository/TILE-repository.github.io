---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# String formatting using test case data



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

Suppose you need to test a program that takes two floats as input
and produces a boolean as the result. A test case for this program
consists of:

-   an identifier

-   two float type inputs

-   an expected bool type output

-   the result of the test test: "PASS" or "FAIL"

Write a Python program that asks the user for the following data:

-   an integer (`i`)

-   two floats (`f1` and `f2`)

-   a bool (`out`)

-   a String (`result`)

Your program must generate a string that uses the requested data and
that describes the test case. For example, if:

`i = 2`

f1 = 123.456

f2 = 12345.67

out = True

result = PASS

your program should produce:

`TEST_ID_002 --- inputs: 1.23e+02, 1.23e+04 --- output: True --- result: PASS`

The first part of the string is used to classify test cases: it
always has to start with `'test_ID_'` followed by an identifier of
maximum 3 digits. If `i` has fewer digits then it must be filled
with leading zeros.

Floats must be presented in scientific format.

You have to do 2 different implementations of your program. One
using the String module operator % to format, and another with the
`str.format()`.

```testdomaintile
This exercise is about creating strings that have certain patterns
using string manipulation. It used to be about file names, it was
TILEd by making it about test cases and their components.
```


# Metadata

| _Summary_ | String formatting with test related content. |
| _TILE aspects_ | Test domain TILE-ing is applied. |
| _Topics_ | String formatting. |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | Strings, replacing strings, formatting strings. |
| _Testing learning goals_ | Creating test awareness and applying test cases. |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
| _Added by_                    | Tanja E.J. Vos |  