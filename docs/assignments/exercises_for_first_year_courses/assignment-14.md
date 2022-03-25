---
title: "ASCII art generator"
summary: "ASCII Art generator using test domain."
prerequisites: "['data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'data > types (built-in) > composite > sequences > strings']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# ASCII art generator





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
