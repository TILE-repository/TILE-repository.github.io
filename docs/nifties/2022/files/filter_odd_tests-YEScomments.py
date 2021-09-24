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
(12, {2,4.2,3,4,6.5,5}, {2,4,3}),   #hello comment 4
(13, {1,1,1,1}, set()),   # comments etc etc .           
])              

def test_filter_odd(testcase, input, output):
    assert filter_odd(input) == output,\
           "caso {0}".format(testcase)