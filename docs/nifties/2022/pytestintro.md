[<< Back to the main assignment](nifty2022.md)

# A brief introduction on running pytest
{:.no_toc}

- Table of contents
{:toc}

## Introduction

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
{% include_relative files/union_test.py %}
```

The output of running the pytests will give us a file that contains the following information when tests have failed:

```txt
{% include_relative files/union_test_pytest_output.txt %}
```

Indicating that testcase with identifier 4 failed because our function returned 
`[1,1]` but we expected `[1]`. 
Also testcase 7 failed.

# References

[^1]: [Pytest homepage](https://docs.pytest.org/en/6.2.x/contents.html)

[<< Back to the main assignment](nifty2022.md)