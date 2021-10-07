```python

#file union_test.py

import pytest

def union(list1, list2):
    i = 0
    res = list1
    for i in range(len(list2)):
        if not list2[i] in res: 
            res.append(list2[i])
    return res

@pytest.mark.parametrize("testcase, input1, input2, output",[
(1, [], [], []),   # Cardinality
(2, [], [1,2,3], [1,2,3]),   # Cardinality
(3, [1,2,3], [], [1,2,3]),   # Cardinality
(4, [1,1], [], [1]),   # Cardinality
(5, [], [1,1], [1]),   # Cardinality
(6, ["hola", 2, 3, "abc"], ["hola", "hola", "de"], ["hola", 2, 3, "abc", "de"]), # Domain, Structure
(7, [1,1,2,2,3,3], [], [1,2,3]),   # Order (of parameters), Structure
(8, [3,4,5,6,6], [3,4,5,6,6], [3,4,5,6]), # Order (duplicates at the end of the list)
])

def test_union(testcase, input1, input2, output):
    assert union(input1, input2) == output,\
           "case {0}".format(testcase)
```
