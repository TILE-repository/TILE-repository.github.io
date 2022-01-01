---
title: "Determining if a string only contains unique characters"
author: TILEd by Tanja E.J. Vos
...

# Determining if a string only contains unique characters

Write a function that receives a text string and says whether it
only has unique characters or not. This function should return True
if it has no repeating characters and False otherwise. Write a
pytest using the following parameterization:

```python
@pytest.mark.parametrize('testcase, input, expected_output',[ (1, 'Hola', True), (2, 'HolaO', False), (3, ", True), (4, 'cC', False), (5,'0123', True), (6, '33&44', False), (7, '!+&/', True), (8, '!++&/', False), ])
```

# Metadata

| *Summary*                     | Determining if a string only contains unique characters |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

