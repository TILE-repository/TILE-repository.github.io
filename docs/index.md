---
title: "Nifty TILE Assignments"
...

# Nifty TILE Assignments

By Niels Doorn [^1], Tanja Vos [^2] and Beatriz Marín [^3]

## Introduction

Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory programming courses in the following ways:

early 
:	introduce students to testing from the very first example program they see and write themselves in exercises;

seamless 
:	testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity;

subtle
:	we will make use of clever and indirect methods to teach them testing knowledge and skills.

## Background

Test Informed Learning with Examples was inspired by Test-driven learning (TDL). 
TDL was coined in 2006 by Janzen and Saiedian [^4]. 
It describes a pedagogical approach to teaching computer programming that involves introducing and exploring new programming concepts using examples and exercises that evolve around testing. 
When teaching programming many examples are being given, programming is often learned through examples. 
Examples related to testing take the same effort to present than other examples.
Janzen et. al. [^5] [^6] continued their work more in the direction of Test Driven Development (TDD) such they diverted from their initial TDL ideas. 
As a consequence, at this moment, there does not exist a clearly defined approach that can be used by any teacher to effortless introduce TDL in their programming course. 
To fill this gap, we developed TILE, Test Informed Learning with Examples.

## Types of TILES

There are three main types of TILES:

test run TILES
:	tiles in students are encouraged to write tests

test cases TILES
:	dafdsf

test domain TILES
:	dafsdf

## TILES of each type

Here we provide one assigments of each type of the approach.

### A test run TILE:

Make a program in Python that receive values for three variables `a`,
`b` and `c`, and interchange their values as follows:

-   `b` takes the value of `a`,

-   `c` takes the value of `a`, and

-   `a` takes the value of `c`.

This must be done WITHOUT using auxiliary variables, that is, additional
helper variables that are not a, b or c, and are used to store some
values.

The execution of the program should result in the following:

```
>>> %Run
  Enter the value of the variable a: 4
  Enter the value of the variable b: 2
  Enter the value of the variable c: 7
  The value of a is 7
  The value of b is 4
  The value of c is 4
```


Execute tests through the console and check the output. 
Does your program work for negative numbers? 
Does it work for characters? 
Does it work for reals? Can `a`, `b` and `c` have different types? 
Should your program work for all these cases?

<div class="howTILEd">

This exercise was TILEd by adding the last paragraph. We explicitly ask
the students to test for different types of values. Most students,
because of the example execution convert the user input to int, but that
is not necessary for the swapping, anything can be swappped. Asking them
to test with all kinds of values makes them aware of the assumptions
they made when reading the exercises and hence how testing is good to
find errors.

</div>

### A test cases TILE:



### A test domain TILE:

Mad Libs is a phrase template word game where a player asks others for a list of words to substitute for blanks in a story, often comical or nonsensical, and which will be read aloud later. 
We are going to make a little Mad Libs.

![MadLib example](MadLib-testing.jpg "a madlib example")

So for these examples, our program returns:

`Whether you write computer programs to solve problems or just for fun, it is very important that you ALWAYS TEST your code for bugs. `

Try other inputs and try to come up with a funny phrase.

<div class="domainTILEd">

This TILE contains the message that testing is important.

</div>

## Metadata

| Summary 		| Test Informed Learning by Example (TILE) based assignments. |
| Topics 		| Testing, programming. |
| Audience 		| Appropriate for a CS1 course. |
| Difficulty 	| These are assignments for novice computer science students, but TILE can be used for more advanced assignments as well. |
| Strengths 	| TILE offers the potential of teaching testing "for free" as early as possible without adding any additional strain on the course schedule. |
| Weaknesses 	| Whilst the teaching doesn't put strain on the course schedule, this approach does require effort to change existing course material in order to apply. We aim to reduce this effort by providing an open databank with assignments. |
| Dependencies 	| This approach integrated into existing programming courses. |
| Variants 		| We identified three main type of TILES, however, this taxonomy can be extended into sub-types or other main types. |


## Acknowledgements

This work was funded by the Erasmus+ project QPeD under contract number 2020-1-NL01-KA203-064626.

## Footnotes                                                                                    

[^1]: [niels.doorn@ou.nl](mailto:niels.doorn@ou.nl)
[^2]: [tanja.vos@ou.nl](mailto:tanja.vos@ou.nl)
[^3]: [bmarin@dsic.upv.es](mailto:bmarin@dsic.upv.es)
[^4]: [Test-driven learning: intrinsic integration of testing into the CS/SE curriculum](http://dl.acm.org/citation.cfm?id=1121419)
[^5]: [Test-driven learning in early programming courses](https://dl.acm.org/doi/10.1145/1352322.1352315) 
[^6]: [Implications of integrating test-driven development into CS1/CS2 curricula](https://dl.acm.org/doi/10.1145/1508865.1508921) 