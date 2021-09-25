---
title: "Learning about parsers and much more using TILE"
...

# Learning about parsers and more using Test Informed Learning with Examples
{:.no_toc}

By [Niels Doorn](mailto:niels.doorn@ou.nl), [Tanja Vos](mailto:tanja.vos@ou.nl) and [Beatriz Marín](mailto:bmarin@dsic.upv.es).

- Table of contents
{:toc}

## Introduction

This assignment is focussed on using a parser to analyse python files containing test cases.
It purposely revolve around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples (TILE) approach to learn students about testing largely for free.
Students work on a assignment to learn certain programming concepts and meanwhile they are working with test related materials.

### Learning goals and prerequisites of the assignment

Programming learning goals:

-   open/close, read and create files
-   process information coming from files with a specific goal in mind
-   working with grammers and parsers, specifically Lark.

Testing learning goals (that are learned for free with TILE):

-   remember how test outputs can be read/interpreted
-   remember how to parametrize tests with pytest

Prerequisites:

-   parametrized tests with pytest and be able to run them and interpret the results.
-   basic/primitive data types
-   functions
-   decision and control-flow structures
-   arrays, lists, etc. (sequence types)

### Grammars, Parsers and Lark

Lark[^1] is a parsing toolkit using context free grammers for Python.
It is built with a focus on ergonomics, performance and modularity.
Lark can parse all context-free languages. 
To put it simply, it means that it is capable of parsing almost any programming language out there, and to some degree most natural languages too.

Lark provides:

- Advanced grammar language, based on EBNF
- Three parsing algorithms to choose from: Earley, LALR(1) and CYK
- Automatic tree construction, inferred from your grammar
- Fast unicode lexer with regexp support, and automatic line-counting

Lark can be installed using `pip`:

```bash
$ pip install lark --upgrade
```

## Suggestions on how to use this assignment in the classroom

The assigment is based around parsing a context free grammar using Lark[^1]. 
The concept of grammars and the usage of parsers can be a difficult and complex topic in CS programs. 
It helps if students discover the benefits of using parsers on their own to create an intrinsic motivation to dive into the application of a parser for a problem head first.

That is what we want to establish with this assignment. 
We provide three ["warmup" exercises](warmupexercises.md) of increasing complexity for the students. 
By letting students analyse test files in these exercises, we want them to experience the **limitations** of using the techniques they are familiar with such as conditional statements.
Either students themselves will at some point question the approach they follow when their code becomes unmaintainable, or lecturers can actively engage students and discuss the problems they will encounter if they continue with using if-then-else constructs to support all possible test case constructs.
That is the moment to introduce them to a better way using the main assignment and the introduction of **parsers** and grammars.

The aim of the assignment is not to teach them context free grammars in all their finesses, but more to introduce the students to the benefits and the application of parsers.
Depending on the prior knowledge and experience, it is possible to provide the students with the [grammer definition](files/grammar.lark) that can be used to parse test files.
This reduces the complexity considerably.

It is advisable to introduce the concept of parsers and context free grammars to the student.
Depending on the educational setting and the background of the students, this can be done by one or more lectures or workshops, but it can also be done individually, in pairs or in small groups. A [tutorial](https://lark-parser.readthedocs.io/en/latest/json_tutorial.html) on parsing JSON using Lark can also be used by the students to get a good understanding of the features and the way to use Lark.

## The assignment: parse Python files containing test cases and generate a simple report

Write a function `get_test_cases(filename)` in Python that generates a simple report with the test cases that are defined in a Python file containing pytests using Lark.

### Grammar description

In this assignment we want Lark to parse files containing parameterized test cases for pytest[^2].

Test case lines look like: 

```python
(num, i1, i2,...,in o),   #any type of comments
```

Each test case:

- starts with (
- ends with ),
- the first argument is a number, the ID of the test case
- after the end test case ), commenst starting with #can be discarded
- different parts of the test case are separated by ", "
- i1, i2, ..., in and o can be of any Python type (int, float, bool, strings, lists, tuples, variables, sets)

To reduce complexity, we assume there are no operators (unary, binary operators), variable names, dictionaries or function calls.

### Example of analysing the provided test file and generating a simple report

The file [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.py) contains a dummy function and test cases with all the by the grammar supported elements. 

It is listed here:

```python
{% include_relative files/pytest_file_to_test_parser.py %}
```

If we analyse the test cases in this file, we can generate the following report:

```python
>>> get_test_cases("pytest_file_to_test_parser.py")
using pytest_file_to_test_parser.py
testcase: (1, {2, 3, 4.2, 4, 6.5, 5}, [2, 3, 4], (3, 4, 5), 'OK!')
testcase: (2, [], set(), (), 'this')
testcase: (3, True, 4.5, (3, 4), 'hoi')
testcase: (4, {5}, set(), '3.555', '3.67')
testcase: (5, {4}, {4}, [2, 2, 3, 4, 3, 5, 4, 3], '{2,4,7}')
testcase: (6, '', None, '', {2, 4, 7})
```

## Possible solution

This is a possible solution (intended only for the lecturer):

```python
{% include_relative files/get_test_cases.py %}
```

## Files to use for this assignment

The following files can be used as input for the warm up exercises:

- [filter_odd_tests-test.py](files/filter_odd_tests-test.py)
- [filter_odd_tests-nocomments.py](files/filter_odd_tests-nocomments.py)
- [filter_odd_tests-YEScomments.py](files/filter_odd_tests-YEScomments.py)
- [filter_odd_tests-string-cases.py](files/filter_odd_tests-string-cases.py)
- [intersection_test.py](files/intersection_test.py)
- [min_max_list_test.py](files/min_max_list_test.py)
- [union_test.py](files/union_test.py)

Here is a file to use as input for the main assignment:

- [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.py)
  
The possible solution and it's output:

- [get_test_cases.py](files/get_test_cases.py)
- [output.tx](files/output.txt)

The Lark grammer as a seperate file which can be provided to the students:

- [grammar.lark](files/grammar.lark)

## Known limitations of the assignment and the provided solution

There are many possible and advanced test cases that can be constructed using pytest.
Since the aim of this assignment is to understand the usefullness of applying a parser and not a complete course in compiler building or formal languages, it goed beyond the scope of this assignment to create complete support for all possible test cases. 
In fact, to do so, a parser for the Python language itself would have to be created (which is possible in Lark).
To keep the focus of the assignment on the application of parser, the grammar should only support for the basic datatypes: int, float, bool, strings, lists, tuples, variables and sets and not for operators (unary, binary), variable names, dictionaries and function calls.

## Conclusion

With this assignment we can teach students about parsing using context free grammar parsers using test files.
By using this approach, student both learn advances and useful programming techniques whilst also revisit their prior knowledge about the usage of test cases and the handling of information about and from these test cases to generate reports.
One of the main programming learning goals is to learn the application of parsers.
This is done by using the context free grammer parser Lark.
We provided exercises and suggestions on a didactic approach to use this assignment in the classroom.
To make the assignment complete, we also provide possible solutions and output files.

## Metadata

| *Summary*      | Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: *early* - introduce students to testing from the very first example program they see and write themselves in exercises; *seamless* - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; *subtle* - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| *Topics*       | Testing, programming, file handling, data processing |
| *Audience*     | This assignment is appropriate for CS2 students. The TILE method can also very well be used on CS1 assignments. |
| *Difficulty*   | These are assignments for computer science students who completed a CS1 or similair course.|
| *Strengths*    | TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| *Weaknesses*   | Whilst the teaching doesn't put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an open databank[^3] with TILED assignments. |
| *Dependencies* | This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| *Variants*     | This assignment can be adapted in many ways, it can also be ported to other programming languages. |

# References

[^1]: [Lark homepage](https://lark-parser.readthedocs.io)
[^2]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)
[^3]: [TILE Repository](https://nielsdoorn.github.io/TILES/)