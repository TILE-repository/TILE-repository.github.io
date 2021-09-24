import pytest

def filtrar_impares(entrada):
    """
     # Returns a set consisting of the input pair elements.
     # It only works if input is a list, set or tuple whose elements are ints or floats.
    """
    res = set()
    for x in entrada:
        if (x % 2 == 0):
            res.add(x)
    return res

@pytest.mark.parametrize("testcase, input, output",[
(1, {2,4.2,3,4,6.5,5}, {2,4,3}),   
(2, {1,1,1,1}, set()),              
(3, set(), set()),
(4, {5}, set()),
(5, {4}, {4}),
(6, [2,2,3,4,3,5,4,3], {2,4,7}),   
(7, [1,1,1,1], set()),              
(8, [], set()),
(9, [777.7], set()),
(10, [200], {200}),
(11, (1,2,3,4,5,6,7), {2,4})
])              

def test_filtrar_impares(testcase, input, output):
    assert filtrar_impares(input) == output,\
           "case {0}".format(testcase)