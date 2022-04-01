---
title: "Checking if a number is prime"
summary: "Testing if a number is prime."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'control flow > conditionals', 'data > types (built-in) > primitive > boolean']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
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
