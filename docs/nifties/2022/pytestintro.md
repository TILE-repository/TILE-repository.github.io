[<< Back to the main assignment](nifty2022.md)

# A brief introduction on running pytest

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries [^1]. 

## Installation

To install pytest, run the following command in a terminal:

```bash
$ pip install -U pytest
```

## Running Pytest and capturing the output

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

# References

[^1]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)
