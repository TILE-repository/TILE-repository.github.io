# Learning about parsers and much more using Test Informed Learning with Examples
{:.no_toc}

1. Table of contents
{:toc}

## Introduction

These assignments are focussed on wrting programs to analyse structured information in the form of pytest testcases.
Some general usefull and somewhat advanced topics are applied such as processing files, parsing information and unit testing.
The assignments purposely revolve around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples (TILE) approach to learn students about testing largely for free.

## Goals and prerequisites

Programming learning goals:

-   work with plain text, Excel and JSON files
-   open/close, read and create files
-   process information coming from files with a specific goal in mind
-   working with grammers and parsers

Testing learning goals (that are learned for free with TILE):

-   remember how test outputs can be read/interpreted
-   remember how to parametrize tests with pytest

Prerequisites:

-   parametrized tests with pytest and be able to run then and interpret the results.
-   basic/primitive data types
-   functions
-   decision and control-flow structures
-   arrays, lists, etc. (sequence types)

The provided [warm up exercises](warmupexercises.md) can be helpful to forfill these prerequisites.

## Main assignment

### Suggestions on how to use this assignment in the classroom

**TODO**
I want to use a growth mindset approach (Open Informatics) to see if we can provide some ideas for lectures on how to let students work on this assignment, for example, work in groups of two on the warm up exercises, discuss the problems, discuss benefits of testing, ask what paramaterized testing is.

Then maybe an example of the usage of parsers and formal languages

Make them understand that a file with pytest cases is also a formal language

And finally work towards the main assignment
**/TODO**

We provide three ["warmup" exercises](warmupexercises.md) for the students to get aquintad with the techniques.

For students who don't have prior experience with using pytest, a short [pytest introduction](pytestintro.md) is also available. 

The assigment is based around parsing a context free grammar using Lark. 
Some, if not most, students will not be familiar with this context free grammer parser. 
Therefore we provide some information about the [usage of lark](lark.md) as support. 

### Description

Write a function `get_test_cases` in Python that returns a list with the test cases that are defined in a python file containing pytests using the Lark [^1] parser.

#### Background information

Lark is a [parser](https://en.wikipedia.org/wiki/Parsing#Parser) for [context free grammers](https://en.wikipedia.org/wiki/Context-free_grammar).
We can use this to as a step to interpret information written in a formal language.
In this assignment, the information are test cases written in Python using the pytest tool [^2].
With pytest, developers can write unit tests for there code.
To properly test functionality, it is necessary to write as much test cases as needed to cover all possible exectution scenario's of your functions.
These test cases can be written using features provided by pytest.
We want to parse Python files to extract the testcases and generate reports with overviews of the testcases.

#### Example of a generating a report

The file [union_test.py](files/union_test.py) contains a function `union` to determine the union of the two sets A and B (the union is the set that contains element that belong to either set A or to set B or to both). For example, the union of `{1, 2, 2, 3, 4}` and `{3, 4, 5, 6}` is `{1, 2, 3, 4, 5, 6}`.
The file also contains eight test cases written using pytest. It is listed here:

```python
{% include_relative files/union_test.py %}
```

If we use a parser to analyse the test cases, we can generate the following output:

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

### Files to use

The following files can be used as input for the program:

- [filter_odd_tests-test.py](files/filter_odd_tests-test.py)
- [filter_odd_tests-nocomments.py](files/filter_odd_tests-nocomments.py)
- [filter_odd_tests-YEScomments.py](files/filter_odd_tests-YEScomments.py)
- [filter_odd_tests-string-cases.py](files/filter_odd_tests-string-cases.py)
- [intersection_test.py](files/intersection_test.py)
- [min_max_list_test.py](files/min_max_list_test.py)
- [union_test.py](files/union_test.py)

The Lark grammer can also be provided as scaffolding:

- [grammer.lark](files/grammer.lark)

### Possible solution

```python
{% include_relative files/get_test_cases.py %}
```

This solution can also be downloaded [here](files/get_test_cases.py), and the produced output on execution can be found [here](files/output.txt).

## Conclusion

With this assignment we can teach students about parsing using context free grammar parsers using test files.
By using this approach, student both learn advances and useful programming techniques whilst also learning about the use of test cases and the handling of information about and from these test cases without the need to spent extra time on these testing topics or teaching them in isolation.
We provided exercises and suggestions on a didactic approach to use this assignment in the classroom.

## Metadata

| *Summary* 		| Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: early - introduce students to testing from the very first example program they see and write themselves in exercises; seamless - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; subtle - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| *Topics* 		| Testing, programming, file handling, data processing |
| *Audience* 		| This assignment is appropriate for CS2 students. The TILE method can also very well be used on CS1 assignments. |
| *Difficulty* 	| These are assignments for computer science students who completed a CS1 or similair course.|
| *Strengths* 	| TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| *Weaknesses* 	| Whilst the teaching doesn't put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an open databank [^3] with TILED assignments. |
| *Dependencies* 	| This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| *Variants* 		| This assignment can be adapted in many ways, it can also be ported to other programming languages. |

# References

[^1]: [Lark homepage](https://lark-parser.readthedocs.io)
[^2]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)
[^3]: [TILE Repository](https://nielsdoorn.github.io/TILES/)