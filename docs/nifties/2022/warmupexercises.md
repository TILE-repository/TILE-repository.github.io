[<< Back to the main assignment](nifty2022.md)

# Warmup exercises

Here we provide three warmup exercises for the students. This is especially usefull for student who have no prior experience with pytest or with file handling in Python. For each exercise we provide a possible solution.

## Exercise 1: Find failed test cases

### Description

Write a function `get_failed_testcases` in Python that, given the name of a `.txt` file with the outcomes of a pytest testrun, will return a list with the testcases that have failed, for example for the pytest results of the union test from above this would be:

```python
>>> get_failed_testcases("union_test_output.txt")
[
    'testcase = 4, input1 = [1, 1], input2 = [], output = [1]', 
    'testcase = 7, input1 = [1, 1, 2, 2, 3, 3], input2 = [], output = [1, 2, 3]'
]
```

### Possible solution

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

## Exercise 2: Find test signatures

### Description

Write a Python function that given a *.py* file that contains parametrized pytests, returns a list with the test signature. (A test signature is the format of the test cases, i.e. ID, inputs, outputs.) (HINT: read through the file until you find: .mark.parametrize@). For example, for the results of the union_test.py file from above:

```python
>>> get_test_signature("union_test.py") 
['testcase', 'input1', 'input2', 'output']
```

### Possible solution

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

## Exercise 3: Find test cases

### Description

### Possible solution