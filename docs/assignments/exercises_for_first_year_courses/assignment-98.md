---
title: "Sieve of Eratosthenes"
author: TILEd by Tanja E.J. Vos
...

# Sieve of Eratosthenes

Write a `generate_eratosthenes` function that, using the Sieve of
Eratosthenes [^4], obtains the prime numbers between 2 and 120. The
algorithm is based on having in a set the numbers between 2 and 120,
and then eliminate from that set the multiples of 2, then those of
3, then those of 5, and so on. Pseudocode would be as can be seen
below:

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

To test your function, you can compare the numbers you obtain with
those that appear below on this [website](https://www.transum.org/Software/Sieve_of_Eratosthenes/).

# Metadata

| *Summary*                     | Sieve of Eratosthenes |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

[^4]: <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>