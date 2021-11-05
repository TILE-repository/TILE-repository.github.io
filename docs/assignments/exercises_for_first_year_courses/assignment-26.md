---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Triangle classification



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

Implement a program that reads three integer numbers: `a`, `b` and
`c`. The program must indicate whether the numbers can represent the
sides of a triangle. For this, each value must be less than the sum
of the other two. If so, the program must indicate if it is a:

-   scalene triangle (if all three sides are different),

-   equilateral triangle (if all three sides are equal), or

-   isosceles triangle (two equal sides and one different).

This triangle challenge is well known. It was proposed by Jerry
Weinberg[^1], a famous computer scientist, and described by Glenford
Myers, who wrote the first book on software testing, the classic The
Art of Software Testing[^2].

Test your program with the set of test cases proposed below:

**test case ID** | **inputs** |   |   | **expected output** 
------------------|------------|------|------|---------------------
                    | `a`        | `b`  | `c`  |                     
1                | 1          | 50   | 50   | Isosceles           
2                | 2          | 50   | 50   | Isosceles           
3                | 99         | 50   | 50   | Isosceles           
4                | 100        | 50   | 50   | Not a Traingle      
5                | 50         | 50   | 50   | Equilateral         
6                | 50         | 1    | 50   | Isosceles           
7                | 50         | 2    | 50   | Isosceles           
8                | 50         | 99   | 50   | Isosceles           
9                | 50         | 100  | 50   | Not a Triangle      
10               | 50         | 50   | 1    | Isosceles           
11               | 50         | 50   | 2    | Isosceles           
12               | 50         | 50   | 99   | Isosceles           
13               | 50         | 50   | 100  | Not a Triangle      


```testruntile
Insist that the students test their programs by giving them test
cases. Also include a bit of anecdotal history on the triangle
program and first book on software testing.
```

# Metadata

| *Summary*                     | Triangle classification |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Classic assignment to classify triangles.  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Problem solving, applying algorithms. |
| *Testing learning goals*      | Applying more abstract test cases. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    

[^1]: <https://en.wikipedia.org/wiki/Gerald_Weinberg>

[^2]: <https://onlinelibrary.wiley.com/doi/book/10.1002/9781119202486>