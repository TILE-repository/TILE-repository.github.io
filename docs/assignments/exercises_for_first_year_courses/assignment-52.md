---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Is this character a digit? - part two

Write a program that reads a character from the keyboard and
determines with the function `is_digit` from the [previous exercise](assignment-51.md)
if it is one of the digits from 0 to 9. Write the program in such a
way that it can be used to read several different characters from
the keyboard until the user writes the word end.

```small
>>> %Run 
    Write a character or 'end' to finish: 4
    4 is a digit from 0 to 9
    Write a character or 'end' to finish: 56
    56 is not a digit from 0 to 9
    Write a character or 'end' to finish: z
    z is not a digit from 0 to 9
    Write a character or 'end' to finish: dfg
    dfg is not a digit from 0 to 9
    Write a character or 'end' to finish: 0
    0 is a digit from 0 to 9
    Write a character or 'end' to finish: end
>>>    
```

```testruntile
Insist that the students test their programs by giving them example
test runs.
```


# Metadata

| *Summary*                     | Calling another function to determine if a character is a digit. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | functions, strings |
| *Technology used*             | Python, pytest |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Using functions that return booleans, working with digits in strings. |
| *Testing learning goals*      | Structured design of test cases |
| *Prerequisites*               | Basic programming constructs and pytest |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   
