---
title: "Sieve of Eratosthenes"
summary: "Sieve of Eratosthenes."
prerequisites: "['data > types (built-in) > composite > sets', 'data > types (built-in) > primitive > sets', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sets', 'control flow > conditionals', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Sieve of Eratosthenes

Write a `generate_eratosthenes` function that, using the Sieve of
Eratosthenes [^4], obtains the prime numbers between 2 and 120. The
algorithm is based on having in a set the numbers between 2 and 120,
and then eliminate from that set the multiples of 2, then those of
3, then those of 5, and so on. Pseudocode would be as can be seen
below:

```
    Create a set and initialize it with the numbers between 2 and 120
    Initialize p to 2
    As long as p is between 2 and 120
        As long as p is not within the set
            increase p
        Initialize k to 2 * p
        As long as k is less than 120
            Eliminate k from the set
            Update k to k + p
        Increase p
```

To test your function, you can compare the numbers you obtain with
those that appear below on this [website](https://www.transum.org/Software/Sieve_of_Eratosthenes/).


[^4]: <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>