---
title: "Fruit classification using Artificial Intelligence"
summary: "Fruit classification using Artificial Intelligence."
prerequisites: "['io > standard > input', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['control flow > conditionals', 'data > user-defined structures > trees']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Fruit classification using Artificial Intelligence





An expert system is a type of artificial intelligence program that
uses a knowledge base and a set of rules to perform a task that a
human expert could do. They help self-diagnose a problem by
answering a series of questions. For example, many hardware and
software companies offer online troubleshooting tools to help people
solve simple technical problems before calling a human.

Create a program that guides the user through the process of
figuring out the type of fruit on hand. Use the following decision
tree to build the system:

![image](images/tree.png)

```small
>>> %Run 
    Color (green/yellow/red): green
    Size (big/medium/small): big
    Watermelon
>>> %Run 
    Color (green/yellow/red): yellow
    Shape (round/thin): round
    Size (big/small): big
    Grapefruit
```

To test your program very well you should have a test case for each
of the 9 fruits on the tree.

```testruntile
Insist that the students test their programs by giving them example
test executions and ask them to add more tests such that each
possible inputs occurs once.
```
