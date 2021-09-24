import pytest

def filter_odd(input):
    """
     # Returns a set consisting of the input pair elements.
     # It only works if input is a list, set or tuple whose elements are ints or floats.
    """
    res = set()
    for x in input:
        if (x % 2 == 0):
            res.add(x)
    return res

@pytest.mark.parametrize("testcase, input, output",[
(14, {2,4.2,3,4,6.5,5}, {2,4,3}, "hello"), 
(15, "testdata", {2,4,3}, 345)
])              

def test_fiter_odd(testcase, input, output):
    assert filter_odd(input) == output,\
           "case {0}".format(testcase)