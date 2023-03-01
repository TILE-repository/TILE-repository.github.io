---
title: "Triangle classification"
summary: "Triangle classification."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals', 'imperative programming > functions > algorithms']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Triangle classification





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

[^1]: <https://en.wikipedia.org/wiki/Gerald_Weinberg>

[^2]: <https://onlinelibrary.wiley.com/doi/book/10.1002/9781119202486>