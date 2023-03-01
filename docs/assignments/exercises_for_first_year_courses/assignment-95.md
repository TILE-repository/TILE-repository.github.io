---
title: "Determining if a string only contains unique characters"
summary: "Determining if a string only contains unique characters."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables']"
concepts practised: "['data > types (built-in) > primitive > boolean', 'data > types (built-in) > composite > sequences > strings', 'control flow > conditionals', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Determining if a string only contains unique characters

Write a function that receives a text string and says whether it
only has unique characters or not. This function should return True
if it has no repeating characters and False otherwise. Write a
pytest using the following parameterization:

```python
@pytest.mark.parametrize('testcase, input, expected_output',[ (1, 'Hola', True), (2, 'HolaO', False), (3, ", True), (4, 'cC', False), (5,'0123', True), (6, '33&44', False), (7, '!+&/', True), (8, '!++&/', False), ])
```