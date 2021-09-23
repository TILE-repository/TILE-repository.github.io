# Essential data processing assigment using Test Informed Learning with Examples

## Overview

This is a set of assignments focussed on wrting programs to analyse structured information. 
Some general usefull and somewhat advanced topics are handled such as processing files, parsing information and generating reports. 
The assignments puposely revolve around the testing domain.
This is one of the ways to apply the Test Informed Learning with Examples (TILE) approach to learn students about testing largely for free.

The presented assignments are TILEs to practice file manipulation by reading and writing different formats (plain text, Excel and JSON) using testing files. The first three are exercises to get used to the used techniques, the last assignment is the most daunting assignment.

- The [first assignment](#ex1)
- The [second assignment](#ex2)
- The [third assignment](#ex3)
- The [fourth assignment](#ex4)

## Goals and prerequisites

Programming learning goals:

-   work with plain text, Excel and JSON files
-   open/close, read and create files
-   process information coming from files with a specific goal in mind

Testing learning goals (that are learned for free with TILE):

-   remember how test outputs can be read/interpreted
-   remember how to parametrize tests with pytest

Prerequisites:

-   Parametrized tests with pytest and be able to run then and interpret the results.
-   basic/primitive data types
-   decision and control-flow structures
-   arrays, lists, etc. (sequence types)

## A brief introduction on running pytest

What is described in this section, the students are supposed to know
already (see prerequisites).

When we have python programs with pytests, we can save the outcome of
the pytest run in a `.txt` file as follows:

```bash
>>> !pytest union_test.py > union_test_output.txt
>>> !pytest interseccion_test.py > interseccion_test_output.txt
>>> !pytest min_max_list_test.py > min_max_list_test_output.txt
```

The `.txt` files summarize the outcome of the tests.

For example, let us consider the program in `union_test.py` that
contains the definition of the function `union` , together with 8 parameterized
test cases and a test driver:

```python
{% include_relative files/pytests-for_testing_reports/union_test.py %}
```

The output of running the pytests will give us a file that contains the following information when tests have failed:
```
=================================== FAILURES ===================================
____________________ test_union[4-input13-input23-output3] _____________________

testcase = 4, input1 = [1, 1], input2 = [], output = [1]

    @pytest.mark.parametrize("testcase, input1, input2, output",[
    (1, [], [], []),   # Cardinality
    (2, [], [1,2,3], [1,2,3]),   # Cardinality
    (3, [1,2,3], [], [1,2,3]),   # Cardinality
    (4, [1,1], [], [1]),   # Cardinality
    (5, [], [1,1], [1]),   # Cardinality
    (6, ["hi", 2, 3, "abc"], ["hi", "hi", "de"], ["hi", 2, 3, "abc", "de"]), # Domain, Structure
    (7, [1,1,2,2,3,3], [], [1,2,3])   # Order of the parameters, Structure
    ])
    
    def test_union(testcase, input1, input2, output):
>       assert union(input1, input2) == output,\
                "case {0}".format(testcase)
E       AssertionError: case 4
E       assert [1, 1] == [1]
E         Left contains one more item: 1
E         Use -v to get the full diff

union_test.py:22: AssertionError
____________________ test_union[7-input16-input26-output6] _____________________

testcase = 7, input1 = [1, 1, 2, 2, 3, 3], input2 = [], output = [1, 2, 3]

    @pytest.mark.parametrize("testcase, input1, input2, output",[
    (1, [], [], []),   # Cardinality
    (2, [], [1,2,3], [1,2,3]),   # Cardinality
    (3, [1,2,3], [], [1,2,3]),   # Cardinality
    (4, [1,1], [], [1]),   # Cardinality
    (5, [], [1,1], [1]),   # Cardinality
    (6, ["hi", 2, 3, "abc"], ["hi", "hi", "de"], ["hi", 2, 3, "abc", "de"]), # Domain, Structure
    (7, [1,1,2,2,3,3], [], [1,2,3])   # Order of the parameters, Structure
    ])
    
    def test_union(testcase, input1, input2, output):
>       assert union(input1, input2) == output,\
                "case {0}".format(testcase)
E       AssertionError: case 7
E       assert [1, 1, 2, 2, 3, 3] == [1, 2, 3]
E         At index 1 diff: 1 != 2
E         Left contains 3 more items, first extra item: 2
E         Use -v to get the full diff

union_test.py:22: AssertionError
=========================== short test summary info ============================
FAILED union_test.py::test_union[4-input13-input23-output3] - AssertionError:...
FAILED union_test.py::test_union[7-input16-input26-output6] - AssertionError:...
========================= 2 failed, 5 passed in 0.05s ==========================
```

Indicating that testcase with identifier 4 failed because our function returned 
`[1,1]` but we expected `[1]`. 
Also testcase 7 failed.

All these are basic pytest concepts that can be taughed in a course after functions have been treated as a concept.

### Exercise 1: Find failed test cases {: ex1 }

#### Description

Write a function `get_failed_testcases` in Python that, given the name of a `.txt` file with the outcomes of a pytest testrun, will return a list with the testcases that have failed, for example for the pytest results of the union test from above this would be:

```python
>>> get_failed_testcases("union_test_output.txt")
[
    'testcase = 4, input1 = [1, 1], input2 = [], output = [1]', 
    'testcase = 7, input1 = [1, 1, 2, 2, 3, 3], input2 = [], output = [1, 2, 3]'
]
```

#### Possible solution

The function `get_failed_testcases` could look something like this:

```python
def get_failed_testcases(filename):
    """
    Expects filename to be a file that contains the output of a !pytest run.
    Returns the list of testcases that have failed.
    Throws FileNotFoundError exception if file does not exist.
    """
    
    # 1.Open the file and name the file-handle fhand
    fhand = open(filename, 'r')
    
    # 2.Copy the content of the file in variable content
    content = fhand.read()
    
    # 3: Close the file
    fhand.close()

    # Look for the failed test cases
    
    if not ("= FAILURES" in content):
       return [] # There are no failed test cases
    else:
        # Find the testcases that have failed, they
        # start with "testcase = " in the file
        lss_lines = content.splitlines()
        testcases = []
        for l in lss_lines:
            if "testcase =" in l:
                testcases.append(l)
        return testcases
```

### Exercise 2: Find test signatures {: ex2 }

#### Description

Write a Python function that given a *.py* file that contains parametrized pytests, returns a list with the test signature. (A test signature is the format of the test cases, i.e. ID, inputs, outputs.) (HINT: read through the file until you find: .mark.parametrize@). For example, for the results of the union_test.py file from above:

```python
>>> get_test_signature("union_test.py") 
['testcase', 'input1', 'input2', 'output']
```

#### Possible solution

The function would look something like this:

```python
def get_test_signature(filename):
    """
    Given a Python file containing "@pytest.mark.parametrize", 
    it returns a list that represents the signature of the test. 
    If there are no pytests in the file, it returns  the empty list.
    
    Throws FileNotFoundError exception if file does not exist.
    """
    
    # 1: Open the file and name the file-handle fhand
    python_file = open(filename, "r")

    # 2: Read through the file to find the line that indicates that 
    # the test cases start (i.e. @pytest.mark.parametrize)
    line = python_file.readline()
    
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
    
    # 3: Close the file
    python_file.close()
    
    # line now is the "@pytest.mark.parametrize" line
    
    # Now, we need to know what the structure of the test cases is,
    # i.e. how many inputs. So we first filter the characters that we do not need.
    filter_out = [',', "@pytest.mark.parametrize", "(", ")", "[", '"']
    for f in filter_out:
        line = line.replace(f, "")
    
    #Then we split, such that we get a list like: ['testcase', input1, ..., inputn, output]
    test_signature = line.split()
    
    return test_signature 
```

### Exercise 3: Find test cases {: ex3 }

#### Description

#### Possible solution

### Exercise 4: The nifty assignment, working with Lark {: ex4 }

#### Description

#### Possible solution

#### Installing Lark

[Lark](https://github.com/lark-parser/lark) is a parsing toolkit for Python, built with a focus on ergonomics, performance and modularity.

Lark can parse all context-free languages. To put it simply, it means that it is capable of parsing almost any programming language out there, and to some degree most natural languages too.

It can be installed using `pip`:

```bash
$ pip install lark --upgrade
```

## Metadata

| Summary 		| Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory and advanced programming courses in the following ways: early - introduce students to testing from the very first example program they see and write themselves in exercises; seamless - testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity; subtle - we will make use of clever and indirect methods to teach them testing knowledge and skills. This is a TILE based programming assignment that applies general applicable programming techniques such as file handling, parsing and data processing using a context related to testing. This way, students are not only learning those programming concepts, but they are learning testing concepts as well without the need to spend extra time. |
| Topics 		| Testing, programming, file handling, data processing |
| Audience 		| This assignment is appropriate for a CS2 course. The method can also be used on CS1 assignments. |
| Difficulty 	| These are assignments for computer science students who completed a CS1 or similair course, but the principles of TILE can be used for more basic assignments as well. |
| Strengths 	| TILE offers the potential of teaching testing "for free" and as early as possible without adding any additional strain on the course schedule. |
| Weaknesses 	| Whilst the teaching doesn't put strain on the course schedule itself, this approach does require effort to change existing course material in order to apply the method. We aim to reduce this effort by providing an open databank with more of these assignments. This databank can be found on [https://nielsdoorn.github.io/TILES/](https://nielsdoorn.github.io/TILES/). |
| Dependencies 	| This approach integrates into existing programming courses. The assignment presented here requires knowledge of basic programming concepts such as conditional statements, datatypes and artithmetic operations as well as more advanced topics such as using Python modules and the `pytest` tool. |
| Variants 		| This assignment can be adapted in many ways, it can also be ported to other programming languages. |