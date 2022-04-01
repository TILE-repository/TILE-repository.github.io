---
title: "Multiples of three"
summary: "Multiples of three."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > relational operators', 'expressions > operators > arithmetic operators', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Multiples of three

Write a function that, given an integer $$n$$ greater than zero, returns a list of the multiples of 3 that exist between 3 and $$n$$. Write another function that, given an integer $$n$$ greater than zero, returns a list of the divisors of $$n$$. Test your functions with pytest, for example:

```python
@pytest.mark.parametrize('testcase, input, expected_output',[ (1, 10, [3, 6, 9]), (2, 0, []), (3, 1, []), (4, -5, []), (5, 12, [3, 6, 9, 12]), (6, 3, [3]) ]) 

def test_multiples_of_3(testcase, input, expected_output): 
    assert multiples_of_3(input) == expected_output, 'case 0'.format(testcase)

@pytest.mark.parametrize('testcase, input, expected_output',[ (1, 10, [1, 2, 5, 10]), (2, 18, [1, 2, 3, 6, 9, 18]), (3, 1, [1]), (4, -5, []), (5, 12, [1, 2, 3, 4, 6, 12]), (6, 0, []) ]) 

def test_divisors_of(testcase, input, expected_output): 
    assert divisors_of(input) == expected_output, 'case 0'.format(testcase)
```

Now, use these functions to write a `main` program that asks the user for a number greater than zero through the keyboard that returns the following:

```small
>>> %Run 
    Type an integer greater than zero: 1
    There are no multiples of 3
>>> %Run 
    Type an integer greater than zero: 2
    There are no multiples of 3
>>> %Run 
    Type an integer greater than zero: 3
    multiple = 3, divisors of 3 = [1, 3]
>>> %Run 
    Type an integer greater than zero: 12
    multiple = 3, divisors of 3 = [1, 3]
    multiple = 6, divisors of 6 = [1, 2, 3, 6]
    multiple = 9, divisors of 9 = [1, 3, 9]
    multiple = 12, divisors of 12 = [1, 2, 3, 4, 6, 12]
>>> 
```
