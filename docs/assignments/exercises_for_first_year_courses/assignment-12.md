---
title: "String formatting using test case data"
summary: "String formatting with test related content."
prerequisites: "['data > types (built-in) > composite > sequences > strings', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'data > types (built-in) > composite > sequences > strings']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# String formatting using test case data





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
