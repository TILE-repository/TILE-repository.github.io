---
title: "Greatest common divisor"
summary: "Greatest common divisor using Euclid's algorithm."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables']"
concepts practised: "['expressions > operators > relational operators', 'expressions > operators > arithmetic operators', 'control flow > loops', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...


# Greatest common divisor

Write a function to calculate the greatest common divisor (`gcd`) of its two parameters $$x$$ and $$y$$, which are integers and greater than zero.

1. Use Euclid's algorithm. Let $$x$$ e $$y$$ be the original values of the variables $$a$$ and $$b$$, the algorithm says:

As long as a and b are not equal, change the greater of the two for
the difference between the greater and the lesser. When they have
the same value, that's the `gcd` of $$x$$ and $$y$$.

Properties on which the Euclid algorithm is based:

-   At the end of each iteration: `gcd`($$x$$, $$y$$)= `gcd`($$a$$, $$b$$)

-   This property is a consequence of the mathematical property:

    -   `gcd`($$a$$, $$b$$) = `gcd`($$a - b$$, $$b$$) when $$a > b$$

    -   `gcd`($$a$$, $$b$$) = `gcd`($$a$$, $$b - a$$) when $$b > a$$

-   When finally $$a = b$$, `gcd`($$x$$, $$y$$) = `gcd`($$a$$, $$b$$)

Write pytests to test your implementation. If we read the
description of the exercise well, we see that the function does not
have to work for numbers that are not greater than 0.

```testruntile
Insist that the students test their programs by adding a line
telling them to do it and make sure they read well what the function
is supposed to do.
```
