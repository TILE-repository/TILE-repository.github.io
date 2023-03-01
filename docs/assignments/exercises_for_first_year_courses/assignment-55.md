---
title: "Convert a letter to upper case"
summary: "Convert a letter to upper case."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables']"
concepts practised: "['data > types (built-in) > composite > sequences > strings']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...



# Convert a letter to upper case

Write a function `lower_to_upper` which receives as a parameter a lowercase `letter` and returns that same character, uppercase. To do this you must use the functions `chr` y `ord`. If the `letter` does not belong to the lowercase alphabet, it must be returned the same `letter`.

Remember that:

-   `chr`: returns the character corresponding to an integer within
    the ASCII table. The ASCII table is based on the international
    alphabet with all 26 letters. The first letter `'a'` esta en la
    posición 97, por eso `chr(97)` returns `'a'` and 25 characters
    later (i.e. 97 + 25 = 122) is the `chr(122)`, that returns
    `'z'`.

-   `ord`: returns the integer value of a character in the ASCII
    table. Capital letters of the international alphabet range from
    `ord("A")`, that returns `65`, to `ord("Z")`, that returns `90`.

This is the last time we give you the pytests that you can use to
test your function. From now on you will have to do it yourself.

```python
@pytest.mark.parametrize("testcase, input, expected_output",[(1, 'a', 'A'), (2, 'z', 'Z'), (3, 'ñ', 'Ñ'), (4, '\*', '\*'), (5, 'Q', 'Q'), (6, ' ] )

def test_lower_to_upper(testcase, input, expected_output): 
    assert lower_to_upper(input) == expected_output, "case 0".format(testcase)
```

```testruntile
Insist that the students test their programs by giving them example
pytests.
```
