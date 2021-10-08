---
title: "Generating test reports using Test Informed Learning with Examples"
author: Niels Doorn, Tanja Vos, Beatriz Marín
...

# Generating test reports using Test Informed Learning with Examples
{:.no_toc}

By [Niels Doorn](https://research.nielsdoorn.nl/), [Tanja Vos](https://tanjavos.nl/) and [Beatriz Marín](mailto:bmarin@dsic.upv.es).

- Table of contents
{:toc}

## Introduction

This assignment is about (1) analysing files containing test cases and test results, (2) parsing strings to uncover the underlying structure, and (3) generating test reports in different formats like Excell and JSON.
It purposely revolves around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples [(TILE)](https://tile-repository.github.io/), an approach to help students learn about testing.
The idea behind TILE is that students work on a assignment to learn certain programming concepts, and meanwhile they are also learn about test related concepts because of the domian chosen for the exercise.

## Learning goals and prerequisites of the assignment

Programming learning goals:

-   Extract, Transform and Load (ETL) data using test files.
-   Process plain text, Excel and JSON files.
-   Work with grammers and parsers, specifically Lark.

Testing learning goals (that are learned for free with TILE):

-   Remember how test outputs can be read/interpreted.
-   Remember how to parametrize tests with pytest.
-   Working with test cases and test results.

Prerequisites:

-   Understand parametrized tests with pytest and be able to run them and interpret the results.
-   Basic/primitive data types
-   Functions
-   Decision and control-flow structures
-   Strings, lists, etc. (sequence types)

## Suggestions on how to use this assignment in the classroom

The learning objectives of this assignment are to practice with file manipulation and to apply a context free grammar using the [Lark](https://github.com/lark-parser/lark) parser in Python. The students' aim is to create a test report containing the test cases together with the results of test execution. Students need to distill information from both Python files (.py) containing [pytest](https://docs.pytest.org/en/6.2.x/contents.html) test cases and plain text files (.txt) containing output from pytest.

It is advisable to introduce the concept of parsers and context free grammars at some point to the student.
Depending on the educational setting and the background of the students, this can be done by one or more lectures or workshops, but it can also be done individually, in pairs or in small groups. 
A [tutorial](https://lark-parser.readthedocs.io/en/latest/json_tutorial.html) on parsing JSON using Lark can also be used by the students to get a good understanding of the features and the way to use Lark, but there are many general introductions to parsers and grammars available, such as this [introduction to Parsers](https://medium.com/@chetcorcos/introduction-to-parsers-644d1b5d7f3d). Depending on the prior knowledge and experience, it is possible for the students to first try to define their own grammar.

The assignment can be simplified to focus mostly on the file manipulatin part and the report generation by providing the students with the results of step one, the parsing of the test case and with the results of step two, the processing of test results. 

## The assignment: generate a report combining test cases and test results 

The aim of this assignment in to create a Python program to generate a test report in which the test cases and the results of the test run from [pytest](https://docs.pytest.org/en/6.2.x/contents.html) are combined. 
The output needs to be in Excel and in JSON. 

For example, using a set of pytests (e.g. in the file [union_test.py](files/union_test.md)), and a textfile containing the output of those pytests
(e.g. [output_union_test.txt](files/output_union_test.md)), the final generated test report in Excel would be:

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

Write a function `get_test_cases(filename)` that, given a .py file with pytests, generates a list with the test cases that are defined in a Python file containing pytests. 

The function should have the folowing signature and specification:

```python
def get_test_cases(filename):
    
    """
    This function returns a list of the test cases that are defined in the
    file with "@pytest.mark.parametrize". If it is not a pytest file it returns
    the empty list.
    
    Throws FileNotFoundError exception if file does not exist.
    """
```

To implement this function, we need to parse the "@pytest.mark.parametrize()" part that exists in the Python test file to obtain the test cases. 
For example in the file [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.md) the 6 test cases are found in this part are:

```python
@pytest.mark.parametrize("testcase, i1, i2, i3, output",[
(1, {2,4.2,3,4,6.5,5}, [2,3,4], (3,4,5), "OK!"),   #sets, lists, tuples and strings with double quotes
(2, [], set(), (), 'this'),                        #empty set/lists/tuples and strings with single quotes      
(3, True, 4.5, (3,4), 'hoi'),                      #bool, float
(4, {5}, set(), "3.555", '3.67'),
(5, {4}, {4}, [2,2,3,4,3,5,4,3], "{2,4,7}"),       #comments
(6, '', None, "", {2,4,7}),                        #empty string and None        
])
```

This parsing can be done using Lark.
If you are not familiar with Lark, then you can start with this [introduction](files/lark.md) to get started.

#### Grammar description

As indicated, the test cases start below the "@pytest.mark.parametrize" definition and look like this: 

```python
(num, in_1, in_2, ..., in_n, out),   #any type of comments
```

Each test case:

- starts with (
- ends with ),
- the first argument is a number, the ID of the test case
- after the end test case ), comments starting with #can be discarded
- different parts of the test case are separated by ", "
- in_1, in_2, ..., in_n, and out can be of any Python type (int, float, bool, strings, lists, tuples, variables, sets)

To reduce complexity, we assume there are no operators (unary, binary operators), variable names, dictionaries or function calls.

For Lark to understand this format, we need to write a grammar describing this format.
Depending on the depth we want to go into grammars and parsing, we can give part of the grammar and parser already to the students. The grammar can be found in this (.lark) file: [grammar.lark](files/gammar.lark.md).

#### Example of analysing a test file

The file [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.md) contains a dummy function and test cases with all the by the grammar supported elements. 

We can use it to test our function `get_test_cases(filename)` as follows:

```python
#testing the parser with main, tester should manually check the output
def test_your_implementation():

    file = "pytest_file_to_test_parser.py"
    
    # Generate a basic report
    print("using", file)
    for tc in get_test_cases(file):
        print("testcase:",tc)
```

We then get:

```python
>>> test_your_implementation(get_test_cases("pytest_file_to_test_parser.py"))
using pytest_file_to_test_parser.py
testcase: (1, {2, 3, 4.2, 4, 6.5, 5}, [2, 3, 4], (3, 4, 5), 'OK!')
testcase: (2, [], set(), (), 'this')
testcase: (3, True, 4.5, (3, 4), 'hoi')
testcase: (4, {5}, set(), '3.555', '3.67')
testcase: (5, {4}, {4}, [2, 2, 3, 4, 3, 5, 4, 3], '{2,4,7}')
testcase: (6, '', None, '', {2, 4, 7})
```

### Step two: process the test results

Now that we can generate the list of test cases, next we need to obtain the results of executing these tests. 
When we execute pytests, we can save the output into a text file. 
Subsequently, we can inspect that file to know which test cases have failed.

#### Saving the test results to a text file

The outcomes of pytests are normally written to the standard output in the command line interface (or in an IDE). 
They can be saved in a text file redirecting it as follows:

```bash
>>> pytest union_test.py > union_test_pytest_output.txt
```

For example, let us consider the program in [union_test.py](files/union_test.md) that contains the definition of the function `union`, together with 8 parameterized test cases and a test driver `test_union`. Running pytest and redirecting the results in a file like above will give us the txt file [output_union_test.txt](files/output_union_test.md) that contains the results of the test cases.

As we can see, it contains enough information to deduce that the testcase with identifier 4 failed because our function returned `[1,1]` but we expected `[1]`. 
The testcases 7 and 8 also failed.

#### Finding the test results in the text file

Now you should create a function `get_failed_testcases(filename)` in Python that returns a list of failed test cases with a signature and a specification like this:

```python
def get_failed_testcases(filename):
    """
    Expects filename to be a file that contains the output of a pytest run.
    Returns the list of testcases that have failed.
    Throws FileNotFoundError exception if file does not exist.
    """
```

Looking at the output of the test results in the text file, we can filter out the results of the test cases.
There is a short test summary in which lines indicating failed test cases start with the all caps word `FAILED`.
For example, this is the part of the output of `union_test.py` containing the information about the failed test cases.

```python
union_test.py:23: AssertionError
=========================== short test summary info ============================
FAILED union_test.py::test_union[1-input10-input20-output0] - AssertionError:...
FAILED union_test.py::test_union[4-input13-input23-output3] - AssertionError:...
FAILED union_test.py::test_union[7-input16-input26-output6] - AssertionError:...
FAILED union_test.py::test_union[8-input17-input27-output7] - AssertionError:...
========================= 4 failed, 4 passed in 0.08s ==========================
```

We can use this to see if there are any failed test cases in the file.
If there are, we can look for lines starting with `testcase = ` that contain information about the failed test cases. 
For example:

```python
____________________ test_union[1-input10-input20-output0] _____________________

testcase = 1, input1 = [], input2 = [], output = set()

    @pytest.mark.parametrize("testcase, input1, input2, output",[
    (1, [], [], set()),   #Cardinalidad
    (2, [], [1,2,3], [1,2,3]),   #Cardinalidad
    (3, [1,2,3], [], [1,2,3]),   #Cardinalidad
    (4, [1,1], [], [1]),   #Cardinalidad
    (5, [], [1,1], [1]),   #Cardinalidad
    (6, ["hola", 2, 3, "abc"], ["hola", "hola", "de"], ["hola", 2, 3, "abc", "de"]), #Dominio, Estructura
    (7, [1,1,2,2,3,3], [], [1,2,3]),   #Orden (de parametros), Estructura
    (8, [3,4,5,6,6], [3,4,5,6,6], [3,4,5,6]), #Orden (duplicados al final de la lista)
    ])
    
    def test_union(testcase, input1, input2, output):
>       assert union(input1, input2) == output,\
               "caso {0}".format(testcase)
E       AssertionError: caso 1
E       assert [] == set()
E         Use -v to get the full diff

union_test.py:23: AssertionError
```

We can use the first line that contains the input and output of testcase 1.
We can assume that test cases that did not fail have passed, so we only need to look for failed test cases in the output of pytest.

```python
>>> get_failed_testcases("union_test_pytest_output.txt")
['testcase = 1, input1 = [], input2 = [], output = ()', 
 'testcase = 4, input1 = [1, 1], input2 = [], output = [1]', 
 'testcase = 7, input1 = [1, 1, 2, 2, 3, 3], input2 = [], output = [1, 2, 3]', 
 'testcase = 8, input1 = [3, 4, 5, 6, 6], input2 = [3, 4, 5, 6, 6]'
]
```

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

Both these functions use the functions from the first two steps to collect the data for the reports, and of course can use other functions if good craftmanship requires as well.

You can test your functions using the following Python files containing pytests:

- [union_test.py](pytests-for_testing_reports/union_test.py)
- [min_max_list_test.py](files/pytests-for_testing_reports/min_max_list_test.py)
- [interseccion_test.py](files/pytests-for_testing_reports/interseccion_test.py)
- [filtrar_impares_test.py](files/pytests-for_testing_reports/filtrar_impares_test.py)

And their corresponding pytest outputs:

- [output_union_test.txt](files/pytests-for_testing_reports/output_union_test.txt)
- [output_min_max_list_test.txt](files/pytests-for_testing_reports/output_min_max_list_test.txt)
- [output_interseccion_test.txt](files/pytests-for_testing_reports/output_interseccion_test.txt)
- [output_filtrar_impares_test.txt](files/pytests-for_testing_reports/output_filtrar_impares_test.txt)

You should check the outputs of your functions manualy by inspecting the Excel and JSON files.

## Possible solution

The file [generate_test_report_all.py](files/generate_test_report_all.md) is a possible solution that can be used as a reference (intended only for the lecturer).

## Files to use for this assignment
  
The possible solution (for lecturers only):

- [generate_test_report_all.py](files/generate_test_report_all.py)

Input and output files for step 3:

- [union_test.py](files/pytests-for_testing_reports/union_test.py)
- [min_max_list_test.py](files/pytests-for_testing_reports/min_max_list_test.py)
- [interseccion_test.py](files/pytests-for_testing_reports/interseccion_test.py)
- [filtrar_impares_test.py](files/pytests-for_testing_reports/filtrar_impares_test.py)
- [output_union_test.txt](files/pytests-for_testing_reports/output_union_test.txt)
- [output_min_max_list_test.txt](files/pytests-for_testing_reports/output_min_max_list_test.txt)
- [output_interseccion_test.txt](files/pytests-for_testing_reports/output_interseccion_test.txt)
- [output_filtrar_impares_test.txt](files/pytests-for_testing_reports/output_filtrar_impares_test.txt)

The test file for the parser (containing all python types supported by the grammar):

- [pytest_file_to_test_parser.py](files/pytest_file_to_test_parser.py)

Generated JSON and Excel files:

- [interseccion_testtest_case_report.json](files/pytests-for_testing_reports/interseccion_testtest_case_report.json)
- [interseccion_testTestReport.xls](files/pytests-for_testing_reports/interseccion_testTestReport.xls)
- [union_testtest_case_report.json](files/pytests-for_testing_reports/union_testtest_case_report.json)
- [union_testTestReport.xls](files/pytests-for_testing_reports/union_testTestReport.xls)
- [min_max_list_testtest_case_report.json](files/pytests-for_testing_reports/min_max_list_testtest_case_report.json)
- [min_max_list_testTestReport.xls](files/pytests-for_testing_reports/min_max_list_testTestReport.xls)

The Lark grammer as a seperate file:

- [grammar.lark](files/grammar.lark)

## Known limitations of the assignment and the provided solution

There are many possible and advanced test cases that can be constructed using pytest.
Since the aim of this assignment is to understand the usefulness of applying a parser and not a complete course in compiler building or formal languages, it goes beyond the scope of this assignment to create complete support for all possible test cases. 
In fact, to do so, a parser for the Python language itself would have to be created (which is possible in Lark).
To keep the focus of the assignment generating reports and not only on the application of parser, the grammar should only support for the basic datatypes: int, float, bool, strings, lists, tuples, variables and sets and not for operators (unary, binary), variable names, dictionaries and function calls.

## Conclusion

We can use this assignment to teach students about extracting data from different sources and transforming that data into reports with useful information about testing.
The main learning goal is to work with different types of files to extract the data from and to write the information to.
In this assignment, the students need to extract all the test cases from an existing Python test file and the results of these test cases from an existing text file to combine these in new Excel and JSON files.
Depending on the prior knowledge of the students, learning to work with parsers and grammars can be achieved as a possible positive side effect.
This happens when students themselves realise the limitations of using basic programming constructs while extracting data from python files containing test cases.
The context free grammer parser Lark is used for this.
During this assignment, students learn new programming concepts and techniques using data related to software testing, thus refreshing and possibly expanding their testing knowledge at the same time.
We provide exercises and suggestions on a didactic approach to use this assignment in the classroom.
The assignment can be adapted to reduce or increase complexity or to incorporate other learning goals.
To make the assignment complete, we also provide a possible solution and input- and output files.

## Metadata

| *Summary*      | Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: *early* - introduce students to testing from the very first example program they see and write themselves in exercises; *seamless* - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; *subtle* - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| *Topics*       | Testing, programming, file handling, data processing, parsing, generating reports. |
| *Audience*     | This assignment is appropriate for CS2 students. The TILE method itself can very well be used in CS1 assignments. |
| *Difficulty*   | These are assignments for computer science students who completed a CS1 or similair course. |
| *Strengths*    | TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| *Weaknesses*   | Whilst the teaching does not put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an [open databank](https://tile-repository.github.io/) with TILED assignments. |
| *Dependencies* | This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| *Variants*     | This assignment can be adapted in many ways, it can also be ported to other programming languages. The parser can be improved to support a more elaborate grammer. The report part can be alter to generate files of different types, for example pdf documents. This assignment can also be used to introduce students to compilers in general or to a course on compiler building. |
