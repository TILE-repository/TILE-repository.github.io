# Learning about parsers and much more using Test Informed Learning with Examples
{:.no_toc}

1. Table of contents
{:toc}

## Introduction

These assignments are focussed on wrting programs to analyse structured information in the form of pytest testcases.
Some general usefull and somewhat advanced topics are applied such as processing files, parsing information and unit testing.
The assignments purposely revolve around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples (TILE) approach to learn students about testing largely for free.

## Learning goals and prerequisites

Programming learning goals:

-   work with plain text, Excel and JSON files
-   open/close, read and create files
-   process information coming from files with a specific goal in mind
-   working with grammers and parsers

Testing learning goals (that are learned for free with TILE):

-   remember how test outputs can be read/interpreted
-   remember how to parametrize tests with pytest

Prerequisites:

-   parametrized tests with pytest and be able to run them and interpret the results.
-   basic/primitive data types
-   functions
-   decision and control-flow structures
-   arrays, lists, etc. (sequence types)

The provided [warm up exercises](warmupexercises.md) can be helpful to work on these prerequisites.

## Main assignment

### Description

Write a function `get_test_cases` in Python that returns a list with the test cases that are defined in a python file containing pytests using the Lark[^1] parser.

#### Background information

Lark is a [parser](https://en.wikipedia.org/wiki/Parsing#Parser) for [context free grammers](https://en.wikipedia.org/wiki/Context-free_grammar).
We can use this to proces information written in formal languages.
In this assignment, the information are test cases written in Python using the pytest tool[^2].
We want to parse Python files to extract the testcases and generate reports with overviews of the testcases.

#### Example of generating a report

The file [union_test.py](files/union_test.py) contains a function `union` to determine the union of the two sets A and B (the union is the set that contains element that belong to either set A or to set B or to both). For example, the union of `{1, 2, 2, 3, 4}` and `{3, 4, 5, 6}` is `{1, 2, 3, 4, 5, 6}`.
The file also contains eight test cases written using pytest. It is listed here:

```python
{% include_relative files/union_test.py %}
```

If we use a parser to analyse the test cases in this file, we can generate the following output (the actuall output is longer, but for clarity it is truncated down to two test cases):

```python
>>> get_test_cases("union_test.py")
union_test.py
testcase
  1
  value
    list
  value
    list
  value
    list
  # Cardinality

(Token('SIGNED_NUMBER', '1'), [[]], [[]], [[]], Token('SH_COMMENT', '# Cardinality'))

[...]

testcase
  8
  value
    list
      number	3
      number	4
      number	5
      number	6
      number	6
  value
    list
      number	3
      number	4
      number	5
      number	6
      number	6
  value
    list
      number	3
      number	4
      number	5
      number	6
  # Order (duplicates at the end of the list)

(Token('SIGNED_NUMBER', '8'), [[Token('SIGNED_NUMBER', '3'), Token('SIGNED_NUMBER', '4'), Token('SIGNED_NUMBER', '5'), Token('SIGNED_NUMBER', '6'), Token('SIGNED_NUMBER', '6')]], [[Token('SIGNED_NUMBER', '3'), Token('SIGNED_NUMBER', '4'), Token('SIGNED_NUMBER', '5'), Token('SIGNED_NUMBER', '6'), Token('SIGNED_NUMBER', '6')]], [[Token('SIGNED_NUMBER', '3'), Token('SIGNED_NUMBER', '4'), Token('SIGNED_NUMBER', '5'), Token('SIGNED_NUMBER', '6')]], Token('SH_COMMENT', '# Order (duplicates at the end of the list)'))
```

**TODO explain output**

### Possible solution

This is a possible solution intended for the lecturer.

```python
{% include_relative files/get_test_cases.py %}
```

## Suggestions on how to use this assignment in the classroom

The usage of parsers can be a difficult and complex topic in CS programs. 
It helps if students discover the benefits of using parsers on their own to create an intrinsic motivation to dive into the application of a parser for a problem head first.

That is what we want to establish with this assignment. 
We provide three ["warmup" exercises](warmupexercises.md) of increasing complexity for the students. 
By letting students analyse test files in these exercises, we want them to experience the limitations of using the concepts they are familiar with such as conditional statements.
That is the moment to introduce them to the main assignment and the usage of parsers.

Depending on the prior knowledge and experience, it is possible to provide the students with the grammer definition that can be used to parse test files.
The aim of the assignment is not to teach them context free grammars in all their finesses, but more to introduce the students to the benefits and the application of parsers.
The assigment is based around parsing a context free grammar using Lark[^1]. 
Some, if not most, students will not be familiar with this context free grammer parser. 
Therefore we provide some information about the [usage of lark](lark.md) as support. 
Of course it is possible to provide a different or a part of the grammer to gradually increase the complexity, or to not provide the students with the grammar to increase the difficulty.
This is also depended on the available amount of time and many other factors of the educational setting.

## Known limitations of the assignment and the provided solution

**TODO**

## Files to use

The following files can be used as input for the program:

- [filter_odd_tests-test.py](files/filter_odd_tests-test.py)
- [filter_odd_tests-nocomments.py](files/filter_odd_tests-nocomments.py)
- [filter_odd_tests-YEScomments.py](files/filter_odd_tests-YEScomments.py)
- [filter_odd_tests-string-cases.py](files/filter_odd_tests-string-cases.py)
- [intersection_test.py](files/intersection_test.py)
- [min_max_list_test.py](files/min_max_list_test.py)
- [union_test.py](files/union_test.py)

The files of the possible solution:

- [get_test_cases.py](files/get_test_cases.py)
- [output.tx](files/output.txt)

The example grammer:

- [grammer.lark](files/grammer.lark)

## Conclusion

With this assignment we can teach students about parsing using context free grammar parsers using test files.
By using this approach, student both learn advances and useful programming techniques whilst also learning about the use of test cases and the handling of information about and from these test cases without the need to spent extra time on these testing topics or teaching them in isolation.
We provided exercises and suggestions on a didactic approach to use this assignment in the classroom.

## Metadata

| *Summary*      | Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: *early* - introduce students to testing from the very first example program they see and write themselves in exercises; *seamless* - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; *subtle* - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| *Topics*       | Testing, programming, file handling, data processing |
| *Audience*     | This assignment is appropriate for CS2 students. The TILE method can also very well be used on CS1 assignments. |
| *Difficulty*   | These are assignments for computer science students who completed a CS1 or similair course.|
| *Strengths*    | TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| *Weaknesses*   | Whilst the teaching doesn't put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an open databank [^3] with TILED assignments. |
| *Dependencies* | This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| *Variants*     | This assignment can be adapted in many ways, it can also be ported to other programming languages. |

# References

[^1]: [Lark homepage](https://lark-parser.readthedocs.io)
[^2]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)
[^3]: [TILE Repository](https://nielsdoorn.github.io/TILES/)