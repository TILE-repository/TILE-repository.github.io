---
title: "Test Informed Learning with Examples assignment"
author: Tanja E.J. Vos
...

# Calculating many squares


Most of the programs that we implement:

1.  obtain input data (for example through the keyboard),

2.  do something with this data (for example perform some type of computation)

3.  display the result as an output (for example on the screen).

Sometimes the combination keyboard/screen is known by the name of
the *console*, with which both are indistinctly identified.

1\. Input data entry is carried out by using the instruction `input`
such as in the following example:

```python
n = int(input("Enter a number: "))
```

Using this instruction we ask the user for a number through the
keyboard. Obviously, this data will have to be stored somewhere in
memory, that is, in a variable. The previous instruction indicates
that the data entered by the user will be interpreted as an integer
(`int`) and will be stored in the variable `n`.

2\. Calculate the square of the given number is an example of a
computation:

```python
square = n * n
```

The previous instruction calculates the square on `n` and stores the
result in the variable `square`.

3\. Displaying data is done by using the instruction `print` such as
in the following example:

```python
print("The square is", square)
```

When we test this program by executing it in the console, we can
obtain for example:

```
>>> %Run
    Enter a number: 5
    The square is 25
```

Note that the program must work whatever has been the number entered
by the user. When we write programs with which we can interact
through the console, we can test our program by entering test input
data through the keyboard en checking the resulting output on the
screen. To test our program to see whether is also works for other
numbers, we could execute the following tests through the console:

```
>>> %Run
Enter a number: 0
The square is 0
>>> %Run
Enter a number: -6
The square is 36
>>> %Run
Enter a number: 1000000
The square is 1000000000000
```

```testruntile
UnTILEd this exercise said: When executing this program in the
console, the user will give input through the keyboard en the
results will be shown on the screen

When we TILE the exercise, instead of just saying that we can
execute programs through the console, we say we can *test* our
program this way like we do above. This way we also introduce the
students with the terminology:

-   test your program

-   test input

-   checking the resulting output

Then with sample executions we invite then to do more tests. And all
of this in one of the very first exercises.
```

# Metadata

| _Summary_ |Calculating squares from the command line interface. |
| _TILE aspects_ | Test run TILE-ing is applied. |
| _Topics_ | Input output |
| _Technology used_ | Python. |
| _Audience_ | CS1 |
| _Programming learning goals_ | command line in-/output. |
| _Testing learning goals_ | Creating test awareness |
| _Prerequisites_ |  Basic programming constructs.  |
| _Variants_ |  Many options are possible, including porting to other programming languages. |
| _Added by_                    | Tanja E.J. Vos |  
