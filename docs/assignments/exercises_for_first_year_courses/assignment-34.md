---
title: "Calculate areas "
summary: "Calculate areas."
prerequisites: "['data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration']"
concepts practised: "['io > standard > input', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Metadata

| *Summary*                     | Calculate areas |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | User interactions |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Calculating areas, working with user input. |
| *Testing learning goals*      | Designing test cases for path coverage |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

# Calculate areas





You want to create a Python program to calculate different areas. To
do this, the program will present the option of area to be
calculated. The possible options are:

1.  Calculation of the area of a square: area = side\*\*2

2.  Calculation of the area of a triangle: area = (base \* height)/2

3.  Calculation of the area of a rectangle: area = side1 \* side2

Once the option has been chosen, the necessary data will be
requested and the corresponding result will be presented. In the
event that the specified option was not correct, the phrase
"incorrect value" would be displayed on the screen.

```small
>>> %Run 
    Area (square/triangle/rectangle): square
    Side: 3.56
    The area of the square is: 12.6736
>>> %Run 
    Area (square/triangle/rectangle): triangle
    Base: 18
    Height: 4
    The area of the triangle is: 36.0
>>> %Run 
    Area (square/triangle/rectangle): rectangle
    Side 1: 4.67
    Side 2: 9
    The area of the rectangle is: 42.03
>>> %Run 
    Area (square/triangle/rectangle): hello
    Wrong value
>>> %Run 
    Area (square/triangle/rectangle): square
    Side: -4
    Wrong value
```

```testruntile
Insist that the students test their programs by giving them example
test executions.
```
