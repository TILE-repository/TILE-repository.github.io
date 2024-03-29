---
title: "Converting time"
summary: "Convert a number of seconds into days, hours,..."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Converting time





Write a program that converts a number of seconds into days, hours,
minutes, and seconds. The output of your program must have the
layout as in the following examples:

```small

>>> %Run 
    Enter a number of seconds: 184
    The equivalent duration is 0:00:03:04.
>>> %Run 
    Enter a number of seconds: 6756456
    The equivalent duration is 78:04:47:36.
>>> %Run 
    Enter a number of seconds: -2
    Only positive values
```

To test your program, think about the inputs you want to use for the
test cases and check the output by using the following converter:

<https://www.convert-me.com/en/convert/time/second/second-to-dhms.html>

In this way we are using another program to test the output of our
program. The other program tells us what the expected results are,
to compare them with the actual results of the program we are
testing. In testing it is called an *oracle*.

The term oracle derives from the Latin oraculum that means the
answer of a divinity to the questions that are posed to them. In
testing, the question we ask is: what are the expected outputs of
this program? A test oracle can be an existing system, a user
manual, the exercise description, or the specialist knowledge of the
programmer, but it should not be the code.

```testruntile
We invite the student to test their program more and compare their
outcomes with a parallel oracle that they can find on the web.
Moreover, we explain the terminology oracle.
```
