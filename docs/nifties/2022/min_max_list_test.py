import pytest


def min_max_num_in_list( list ):
    if (len(list)==0):
        return "undefined"
    max = min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
        elif a > max:
            max = a
    return (min,max)

 
@pytest.mark.parametrize("testcase, input, output",[
(1, [1,2,3,6,8,0], (0,8)),  #comentario
(2, [0,8,2,3], (0,8)),    
(3, [2,8,1,5,3], (1,8)),     
(4, [8,0,2,3,0], (0,8)),   
(5, [1,2,3,-6,0,1], (-6,3)),    
(6, [1], (1,1)),
(7, (8,0,2,3), (0,8,3)),   
(8, (1,2,3,-6,0,1), (-6,3)),    
(9, [1,1,1,9], (1,1)),
(10, [], ())
]) 

def test_min_max_list(testcase, input, output):
    assert min_max_num_in_list(input) == output, "caso {0}".format(testcase)
 
 