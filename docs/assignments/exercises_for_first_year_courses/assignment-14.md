---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# ASCII art generator



------------------------------------------------------------------------

Python exercises used for first year programming courses that
have been adapted by using Test Informed Learning with Examples (TILE)
to integrate testing in programming education without it costing (much)
more time. The coloured boxes indicate how they were TILEd.

```testdomaintile
This colour box explains a TILE in the test domain.
```

```testruntile
This colour box explains a TILE related to test runs 
and/or test cases.
```
------------------------------------------------------------------------

# Assignment

Write a Python program that asks the user for something that seems
important to him and returns the following ASCII art
(<https://en.wikipedia.org/wiki/ASCII_art>):

```small
>>> %Run
    Name something important: Testing your own code

                \|||||/               
                ( O O )                
|---------ooO-----(_)-----------------|
|                                     |
| Testing your own code is important! |
|                                     |
|-------------------------Ooo---------|
                |_||_|                 
                ||  ||                 
                ooO  Ooo                
```

You can use the `len()` Python function that returns the length of a
String (for example, `len("Python")` returns 6).

Your program must work with any length name:

```small
>>> %Run
    Name something important: Testing your program with all kinds of different input values

                                    \|||||/                                   
                                    ( O O )                                    
|-----------------------------ooO-----(_)-------------------------------------|
|                                                                             |
| Testing your program with all kinds of different input values is important! |
|                                                                             |
|---------------------------------------------Ooo-----------------------------|
                                    |_||_|                                     
                                    ||  ||                                     
                                    ooO  Ooo                                                                               
```

```testdomaintile
This TILE contains the message that testing is important.
```



# Metadata

| *Summary*                     | ASCII Art generator using test domain. |
| *TILE aspects*                | Test domain TILE-ing is applied. |
| *Topics*                      | String formatting. |
| *Technology used*             | Python. |
| *Audience*                    | CS1 |
| *Programming learning goals*  | String formatting. |
| *Testing learning goals*      | Test awareness. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

