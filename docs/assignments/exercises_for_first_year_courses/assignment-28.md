---
title: "Phone costs calculator"
summary: "Phone costs calculator."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals', 'expressions > operators > relational operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Phone costs calculator





Implement a program that reads the duration in seconds of a phone
call and determines the total amount to be paid. The business rule
is: *if the call lasts less than 1 minute it costs 10 cents, and
each additional minute from the first one costs 5 cents*.

For example, if the call lasts 35 seconds, the cost will be 10
cents. If it lasts 3 minutes and 40 seconds (that is, the user will
enter the value 220), it will cost 20 cents: 10 cents for the first
minute plus 5 cents for the next 2 minutes. The remaining 40 seconds
are free.

```small

>>> %Run 
    Enter the number of seconds the call has lasted: 0
    The call has a cost of 0 cents
>>> %Run 
    Enter the number of seconds the call has lasted: 5
    The call has a cost of 10 cents
>>> %Run 
    Enter the number of seconds the call has lasted: 59
    The call has a cost of 10 cents
>>> %Run 
    Enter the number of seconds the call has lasted: 125
    The call has a cost of 15 cents
>>> %Run 
    Enter the number of seconds the call has lasted: 200
    The call has a cost of 20 cents
>>> %Run 
    Enter the number of seconds the call has lasted: -5
    Please enter a correct value
```

What other tests have you run to ensure that your program has the
desired behaviour?

```testruntile
Insist that the students test their programs by giving them example
test executions and ask them to think about more tests.
```
 