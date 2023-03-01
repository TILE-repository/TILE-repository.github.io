---
title: "Calculating the mean of positive and negative numbers"
summary: "Calculating the mean of positive and negative numbers."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Calculating the mean of positive and negative numbers





Implement a program that reads 12 real numbers and calculates the
mean of the positive and negative numbers. Afterwards, the result
must be displayed to a maximum of 4 decimal places. Run the
following test cases to test your program:

**test case ID** | **inputs**                                                            |                | **expected outputs** 
------------------|-----------------------------------------------------------------------|-------------------|----------------------
                    |                                                                       | mean of positives | mean of negatives    
1                | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12                                 | 6.5               | 0                    
2                | -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12                     | 0                 | -6.5                 
3                | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0                                    | 0                 | 0                    
4                | 12.4, 21.005, -3.67, 4.43, 5.56, 4.2, 7, 8.3, -91.3, -1.0, 32.4, 12.1 | 11.9327           | -31.99               


```testruntile
Insist that the students test their programs by giving them example
test cases in a table. Series with only positive numbers, series
with only negative numbers, all zeros, and mix of positive/negative.
```
