---
title: "Split a string into a list of unique words"
summary: "Split a string into a list of unique words."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'control flow > loops', 'data > types (built-in) > composite > sequences > lists']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
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
