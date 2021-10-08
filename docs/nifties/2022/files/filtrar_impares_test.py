import pytest

def filtrar_impares(entrada):
    """
     # Devuelve una tupla que consiste de los elementos pares de entrada.
     # Solo funciona si entrada es una list, conjunto o tupla cuyos elementos son ints o floats.
    """
    res = ()
    for x in entrada:
        if (x % 2 == 0):
            res.add(x)
    return res

@pytest.mark.parametrize("testcase, input, output",[
(1, [2,4.2,3,4,6.5,5], (2,4,3)),   
(2, [1,1,1,1], ()),              
(3, (), ()),
(4, [5], ()),
(5, [4], (4)),
(6, [2,2,3,4,3,5,4,3], (2,4,7)),   
(7, [1,1,1,1], ()),              
(8, [], ()),
(9, [777.7], ()),
(10, [200], (200)),
(11, (1,2,3,4,5,6,7), [2,4])
])              

def test_filtrar_impares(testcase, input, output):
    assert filtrar_impares(input) == output,\
           "caso {0}".format(testcase)