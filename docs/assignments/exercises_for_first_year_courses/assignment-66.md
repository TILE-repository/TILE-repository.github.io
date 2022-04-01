---
title: "Binary to decimal converter"
summary: "Binary to decimal converter."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Binary to decimal converter

Implement a module with a `main` that reads a string representing a binary number from the keyboard. If any character in the string is different from 0 or 1, the program will warn the user that the entered string does not represent a binary number and will ask to read the string again. Finally, the `main` will display the decimal integer value of the entered binary number.

In the `main` you must use 2 functions that you have to define, and
test with pytest:

-   `check_if_is_binariy` that given a text string, it returns
    `True` if the string is composed of only 0 and 1, and if it does
    not, it returns `False`.

-   `convert` to convert a string in binary format (i.e. only 0
    and 1) to decimal format.

What test cases would you run to test your main well? And for the 2 functions? Implement the tests with pytest.
