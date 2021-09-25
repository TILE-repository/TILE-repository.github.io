import pytest

def some_function(x1, x2, x3):
    """
     # This is a function that does nothing. We just want to able to write test
     # cases with different types for it to test our test case parser.
    """
    
    return "that's it!"


variable_name = "Look"

@pytest.mark.parametrize("testcase, i1, i2, i3, output",[
(1, {2,4.2,3,4,6.5,5}, [2,3,4], (3,4,5), "OK!"),   # sets, lists, tuples and strings with double quotes
(2, [], set(), (), 'this'),                        # empty set/lists/tuples and strings with single quotes      
(3, True, 4.5, (3,4), 'hoi'),                      # bool, float
(4, {5}, set(), "3.555", '3.67'),
(5, {4}, {4}, [2,2,3,4,3,5,4,3], "{2,4,7}"),       # comments
(6, '', None, "", {2,4,7}),                        # empty string and None        
])              

def test_some_function(testcase, i1, i2, i3, output):
    assert some_function(i1, i2, i3) == output,\
           "case {0}".format(testcase)