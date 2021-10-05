---
title: "Generating test reports using Test Informed Learning with Examples"
author: Niels Doorn, Tanja Vos, Beatriz Marín
...

# Generating test reports using Test Informed Learning with Examples
{:.no_toc}

By [Niels Doorn](mailto:niels.doorn@ou.nl), [Tanja Vos](mailto:tanja.vos@ou.nl) and [Beatriz Marín](mailto:bmarin@dsic.upv.es).

- Table of contents
{:toc}

## Introduction

This assignment is focussed on analysing files containing test cases to generate reports using a parser.
It purposely revolve around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples (TILE) approach to learn students about testing largely for free.
Students work on a assignment to learn certain programming concepts and meanwhile they are working with test related materials.

## Learning goals and prerequisites of the assignment

Programming learning goals:

-   Extract, Transform and Load (ETL) data using test files.
-   Processing Python, plain text, Excel and JSON files.
-   working with grammers and parsers, specifically Lark.

Testing learning goals (that are learned for free with TILE):

-   Remember how test outputs can be read/interpreted.
-   Remember how to parametrize tests with pytest.
-   Working with test cases and test results.

Prerequisites:

-   Understand parametrized tests with pytest[^2] and be able to run them and interpret the results.
-   Basic/primitive data types
-   Functions
-   Decision and control-flow structures
-   Arrays, lists, etc. (sequence types)

## Suggestions on how to use this assignment in the classroom

The focus of this assignment is to create reports of test cases and the results of these test cases.
Before students can do this, they need to distill information from both Python files containing pytest[^2] test cases and text files containing output from pytest.

The assigment address several interesing programming topics of which the most advanced topic is the application of a context free grammar using Lark[^1]. 
The concept of grammars and the usage of parsers can be a difficult and complex topic in CS programs. 
It helps if students discover the benefits of using parsers on their own to create an intrinsic motivation to dive into the application of a parser for a problem head first.

That is what we want to establish with this assignment. 
We provide three ["warmup" exercises](warmupexercises.md) of increasing complexity for the students. 
By letting students analyse test files in these exercises, we want them to experience the **limitations** of using the techniques they are familiar with such as conditional statements.
Either students themselves will at some point question the approach they follow when their code becomes unmaintainable, or lecturers can actively engage students and discuss the problems they will encounter if they continue with using if-then-else constructs or maybe regular expressions to support all possible test case constructs.
That is the moment to introduce them to a better way using the main assignment and the introduction of **parsers** and **grammars**.

We don't want to teach the students context free grammars in all their finesses, but we only want to introduce the students to the benefits and the application of parsers.
To support the students, we provide some information about [lark](lark.md) and with the [grammer definition](files/grammar.lark) to get them started.
Depending on the prior knowledge and experience, it is possible for the students to first try to define their own grammar.
This puts the focus on the application of the parser and less on understanding the grammar.

It is advisable at some point to introduce the concept of parsers and context free grammars to the student.
Depending on the educational setting and the background of the students, this can be done by one or more lectures or workshops, but it can also be done individually, in pairs or in small groups. A [tutorial](https://lark-parser.readthedocs.io/en/latest/json_tutorial.html) on parsing JSON using Lark can also be used by the students to get a good understanding of the features and the way to use Lark, but there are many general introductions to parsers and grammars available, such as this [introduction to Parsers](https://medium.com/@chetcorcos/introduction-to-parsers-644d1b5d7f3d).

The assignment can be further simplified to focus mostly on the report generation by providing the students with the results of step one, the parsing of the test case and with the results of step two, the processing of test results.

## The assignment: generate a report combing test cases and test results 

Create a Python program to generating a test report in which the test cases and the results of the test run from pytest[^2] are combined. 
The output needs to be in Excel and in JSON. 

For example, using a set of pytests (e.g. in the file `test_union.py`), and a textfile `test_union_output.txt`) containing the output of those pytests, the final generated test report in Excel would be:

![Generated Excel report](pics/excel-testcases-report.png "Generated Excel report")

And in JSON it would be (similar to) this:

```json
{% include_relative files/pytests-for_testing_reports/union_testtest_case_report.json %}
```

We approach this assignment in three steps:

1. First we parse Python files containing test cases,
2. then we read test results from a text file and combine those with the test cases,
3. and finally, we can generate the report in Excel or JSON.

### Step one: parse Python files containing test cases

Write a function `get_test_cases(filename)` in Python that generates a report with the test cases that are defined in a Python file containing pytests. 

We need to find out what test cases are defined in a Python test file.
For this, we can create a function with the folowing signature and specification:

```python
def get_test_cases(filename):
    
    """
    This function returns a list of the test cases that are defined in the
    file with "@pytest.mark.parametrize". If it is not a pytest file it returns
    the empty list
    
    Throws FileNotFoundError exception if file does not exist.
    """
```

To implement this function, we need to parse the Python test file.
This can be done using the Lark[^1] parser.
If you are not familiar with Lark, then you can start with this [introduction](lark.md) to get started.

#### Grammar description

We need Lark to parse files containing parameterized test cases for pytest[^2].

Test case lines look like this: 

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

For Lark to understand this format, we need to write a grammar describing this format.
Since this assignment is focussed on generating reports and not on fully understanding grammars and parsers, we already created the grammar for you. 
You are encouraged to try to create the grammar first and compare it with the one provided.

```python
{% include_relative files/grammar.lark %}
```

#### Example of analysing a test file

The file [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.py) contains a dummy function and test cases with all the by the grammar supported elements. 

It is listed here:

```python
{% include_relative files/pytest_file_to_test_parser.py %}
```

If we analyse the test cases in this file, we can, for example, generate the following output:

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

### Step two: process the test results

First we describe how to save the output of pytest into a text file, then we explain how to process the text file.

#### Saving the test results to a text file

We need textfiles containing the outcomes of the tests that is normally written to the standard output in the command line interface (or in an IDE). 
For example, let us consider the program in `union_test.py` that contains the definition of the function
`union`, together with 8 parameterized test cases and a test driver `test_union`:

```python
{% include_relative files/union_test.py %}
```

The output of running the pytests can be saved in a text file like this:

```bash
>>> pytest union_test.py > union_test_output.txt
```

This will give us the txt file that contains for example the following information:

```python
{% include_relative files/union_test_pytest_output.txt %}
```

Indicating that testcase with identifier 4 failed because our function returned 
`[1,1]` but we expected `[1]`. 
The testcases 7 and 8 also failed.

#### Finding the test results in the text file

We can create a function in Python that returns a list of failed test cases with a signature and a specification like this:

```python
def get_failed_testcases(filename):
    """
    Expects filename to be a file that contains the output of a !pytest run.
    Returns the list of testcases that have failed.
    Throws FileNotFoundError exception if file does not exist.
    """
```

Now that we have the output of the test results in a text file, we can filter out the results of the test cases.
There is a short test summary in which lines indicating failed test cases start with the all caps word `FAILED`.
We can use this to see if there are any failed test cases in the file.
If so, we can look for lines starting with `testcase = ` that contain information about the failed test cases. 
For example:

```python
testcase = 4, input1 = [1, 1], input2 = [], output = [1]
```

This line contains the input and output of testcase 4.

We can assume that test cases that didn't fail have passed, so we only need to look for failed test cases in the output of pytest.

### Step three: generate the Excel and JSON reports

Now we have all information we need, we have the test cases from step one and the test results from step two.
We want to combine this information into a test report in Excel and in JSON format.
To create Excel files we can use [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl), which can be installed using Pip:

```bash
$ pip install openpyxl
```

Or [xlwt](https://github.com/python-excel/xlwt), which can be installed in a similar way:

```bash
$ pip install xlwt
```

Handling JSON is supported by Python by default, so no extra modules need be installed. 
There is official Python documentation on the [json](https://docs.python.org/3/library/json.html) module, but there are many other examples to find on the internet.

We need two functions to generate the reports, one for the Excel files with the folowing signature:

```python
def generate_excel_test_report(filenameTest, filenameTestRes):
    """ 
        filenameTest is the file name .py with testcase 
        and filenameTestRes is the file name .txt with test results
    """
```

And a similar function for the JSON reports. 

```python
def generate_JSON_test_report(filenameTest, filenameTestRes):
    """ 
        filenameTest is the file name .py with testcase 
        and filenameTestRes is the file name .txt with test results
    """
```

Both these functions use the functions from the first two steps to collect the data for te reports, and of course can use other functions if good craftmanship requires as well.

## Possible solution

This is a possible solution that can be used as a reference (intended only for the lecturer):

```python
{% include_relative files/generate_test_report_all.py %}
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

Here is a file that can be used as input for the main assignment covering the whole grammar:

- [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.py)
  
The possible solution (for lecturers only):

- [generate_test_report_all.py](files/generate_test_report_all.py)

Input and output files for the solution:

- [union_test.py](pytests-for_testing_reports/union_test.py)
- [output_union_test.txt](files/pytests-for_testing_reports/output_union_test.txt)
- [min_max_list_test.py](files/pytests-for_testing_reports/min_max_list_test.py)
- [output_min_max_list_test.txt](files/pytests-for_testing_reports/output_min_max_list_test.txt)
- [interseccion_test.py](files/pytests-for_testing_reports/interseccion_test.py)
- [output_interseccion_test.txt](files/pytests-for_testing_reports/output_interseccion_test.txt)
- [filtrar_impares_test.py](files/pytests-for_testing_reports/filtrar_impares_test.py)
- [output_filtrar_impares_test.txt](files/pytests-for_testing_reports/output_filtrar_impares_test.txt)

Generated JSON and Excel files for the union test:

- [union_testtest_case_report.json](files/pytests-for_testing_reports/union_testtest_case_report.json)
- [union_testTestReport.xls](files/pytests-for_testing_reports/union_testTestReport.xls)

The Lark grammer as a seperate file:

- [grammar.lark](files/grammar.lark)

## Known limitations of the assignment and the provided solution

There are many possible and advanced test cases that can be constructed using pytest.
Since the aim of this assignment is to understand the usefullness of applying a parser and not a complete course in compiler building or formal languages, it goed beyond the scope of this assignment to create complete support for all possible test cases. 
In fact, to do so, a parser for the Python language itself would have to be created (which is possible in Lark).
To keep the focus of the assignment generating reports and not only on the application of parser, the grammar should only support for the basic datatypes: int, float, bool, strings, lists, tuples, variables and sets and not for operators (unary, binary), variable names, dictionaries and function calls.

## Conclusion

We can use this assignment to teach students about extracting data from different sources and transforming that data into reports with useful information about testing.
The main learning goal is to work with different types of files to extract the data from and to write the information to.
In this assignment, the students need to extract all test cases from an existing Python test file and the results of these test cases from an existing text file to combine these in new Excel and JSON files.
Depending on the prior knowledge of the students, learning to work with parsers and grammars can be achieved as a possible positive side effect.
This happens when students themselves realise the limitations of using basic programming constructs while extracting data from python files containing test cases.
The context free grammer parser Lark is used for this.
During this assignment, student learn new programming concepts and techniques using data related to software testing, thus refreshing and possibly expanding their testing knowledge at the same time.
We provide exercises and suggestions on a didactic approach to use this assignment in the classroom.
The assignment can be adapted to reduce or increase complexity or to incorporate other learning goals.
To make the assignment complete, we also provide a possible solution and input- and output files.

## Metadata

| *Summary*      | Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: *early* - introduce students to testing from the very first example program they see and write themselves in exercises; *seamless* - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; *subtle* - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| *Topics*       | Testing, programming, file handling, data processing, parsing, generatin reports. |
| *Audience*     | This assignment is appropriate for CS2 students. The TILE method itself can very well be used in CS1 assignments. |
| *Difficulty*   | These are assignments for computer science students who completed a CS1 or similair course. |
| *Strengths*    | TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| *Weaknesses*   | Whilst the teaching doesn't put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an open databank[^3] with TILED assignments. |
| *Dependencies* | This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| *Variants*     | This assignment can be adapted in many ways, it can also be ported to other programming languages. The parser can be improved to support a more elaborate grammer. The report part can be alter to generate files of different types, for example pdf documents. This assignment can also be used to introduce students to compilers in general or to a course on compiler building. |

# References

[^1]: [Lark homepage](https://lark-parser.readthedocs.io)
[^2]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)
[^3]: [TILE Repository](https://tile-repository.github.io/)