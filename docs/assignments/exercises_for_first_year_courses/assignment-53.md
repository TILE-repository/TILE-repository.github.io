---
title: "Checking if a number is prime"
author: TILEd by Tanja E.J. Vos
...

# Checking if a number is prime

Write a function `is_prime` which receives an integer as a parameter and returns a boolean. The function will return `True` when the number is a prime, otherwise it will return `False`).

You can use the following pytest to test your function.

```python
@pytest.mark.parametrize("testcase, input, expected_output",[(1, 0, False), (2, 1, False), (3, 2, True), (4, 25, False), (5, 23, True), (6, 97, True) ] )

def test_is_prime(testcase, input, expected_output): 
    assert is_prime(input) == expected_output, "case 0".format(testcase)
```

```testruntile
Insist that the students test their programs by giving them example
pytests.
```

# Metadata

| *Summary*                     | Testing if a number is prime |
| *TILE aspects*                | Test cases TILE-ing is applied. |
| *Topics*                      | Arithmetic |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

