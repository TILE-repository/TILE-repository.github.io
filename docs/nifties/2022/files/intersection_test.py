import pytest

def intersection(list1, list2, list3):
    i = 0
    res = []
    for i in range(len(list1)):
        if list1[i] in list2: 
            res.append(list1[i]) 
    return res + list3

@pytest.mark.parametrize("testcase, input1, input2, input3, output",[
(1, [], [], [], []),   # Cardinality
(2, [], [1,2,3], [], []),   # Cardinality
(3, [1,2,3], [], [2], [2]),   # Cardinality
(4, [1,1], [], [], []),   # Cardinality
(5, [], [1,1], [],  []),   # Cardinality
(6, ["hola", 2, 3, "abc"], ["hola", "hola", "de"], ["hi"], ["hola","hi"]), # Domain, Structure
(7, [1,1,2,2,3,3], [1,2,3], [8], [1,2,3,8]),   # Order (of parameters), Structure
(8, [3,4,5,6,6], [3,4,5,6,6], [], [3,4,5,6]), # Order (duplicates at the end of the list)
(9, (3,4,5,6,6), (3,4,5,6,6), [], [3,4,5,6])
])

def test_intersection(testcase, input1, input2, input3, output):
    assert intersection(input1, input2, input3) == output,\
           "case {0}".format(testcase)
