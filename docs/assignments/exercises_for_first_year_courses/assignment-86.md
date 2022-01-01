---
title: "Scrabble game score calculator"
author: TILEd by Tanja E.J. Vos
...

# Scrabble game score calculator

In the Scrabble game, each letter has scores associated with them.
The total score of a word is the sum of its letter scores. The most
common letters are worth less points, while the less common letters
are worth more points. We are going to use a dictionary that maps
from letters to point values. The points associated with each letter
are shown below:

```python
points = "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
```

Write a function that calculates and displays the Scrabble score for
a given word. Use the dictionary to calculate the score.

The Scrabble board includes some cells that multiply the value of a
letter or the value of a whole word. We will ignore these squares in
this exercise.

Write pytests to test your function, for example for the following
test cases:

    **testcase number**   |**input**                |  **expected output**
    -----------------| ---------------------- |-----------------
    1                | `''`                  | 0
    2                | `'Hello!'`            | 8
    3                | `'zzz'`               | 30
    4                | `'Surprise'`          | 10
    5                | `'1234'`              | 0
    6                | `'And with spaces?'`  | 24




# Metadata

| *Summary*                     | Scrabble game score calculator |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

