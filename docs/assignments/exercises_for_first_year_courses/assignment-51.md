---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Is this character a digit?



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

Write a function `is_digit` which receives a character as a
parameter and returns a boolean. The function will return `True`
when the character is a digit from 0 to 9, otherwise it will return
`False`).

You can use the following test cases to test your function:

    test_case_ID  | test_input  | expected_output  | reason for testing this
    --------------| ------------| ----------------- |-----------------------------------
    1          |    `'0'`      |  `True`          |  smallest digit
    2            |  `'9'`      |  `True`         |   largest digit
    3            |  `'5'`      |  `True`         |   other digit
    4            |  `'12'`    |   `False`        |   it is not a digit between 0 and 9
    5            |  `'-2'`     |  `False`        |  negative digit
    6           |   `'hello'`  |  `False`        |  string

In pytest these could be implemented like:

```python
@pytest.mark.parametrize("test_case_ID, test_input, expected_output",[ (1, '0', True), #smallest digit (2, '9', True), #largest digit (3, '5', True), #other digit (4, '12', False), #it is not a digit between 0 and 9 (5, '-2', False), #negative digit (6, 'hello', False), #string ] )

def test_is_digit(test_case_ID, test_input, expected_output): 
    assert is_digit(test_input) == expected_output, "case 0".format(test_case_ID)
```

```testruntile
Insist that the students test their programs by giving them example
pytests. And make the connection to the tables with test cases they
have seen before.
```

# Metadata

| *Summary*                     | Determine if a given character is a digit and using pytest to test it. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | unit testing, strings, functions |
| *Technology used*             | Python, pytest |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Using functions that return booleans, working with digits in strings. |
| *Testing learning goals*      | Structured design of test cases |
| *Prerequisites*               | Basic programming constructs and pytest |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   