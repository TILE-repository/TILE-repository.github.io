---
title: "Split a string into a list of unique words"
author: TILEd by Tanja E.J. Vos
...

# Split a string into a list of unique words

Design a function (`mySplit`) that gets a string and returns a list of all its words in lowercase. The returned list must not contain repeating words. You can't use Python's default `split`. For example, with the string:

```small
>>> mySplit('A phrase made up of words. Another phrase with other words.')
    ['a', 'phrase', 'made', 'up', 'of', 'words', 'another', 'with', 'other']
>>> mySplit('Hi! Helloooo HI')
    ['hi', 'helloooo']
```

To design your set of tests that you have to run automatically with
pytest, think about these cases:

-   the string is empty

-   the string has punctuation marks, like `,;.:-¿?+*()!¡`

-   the string ends with a point

-   the string does not end with a point

-   the string has numbers

-   que the string has repeated words, but some are capitalized and
    some are not (for example: `'HEllo hello heLlo'`

-   the string has more than 1 space between words

-   etc.


# Metadata

| *Summary*                     | Split a string into a list of unique words |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

