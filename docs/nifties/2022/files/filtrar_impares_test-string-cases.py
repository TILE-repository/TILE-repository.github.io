import pytest

def filtrar_impares(entrada):
    """
     # Devuelve un conjunto que consiste de los elementos pares de entrada.
     # Solo funciona si entrada es una list, conjunto o tupla cuyos elementos son ints o floats.
    """
    res = set()
    for x in entrada:
        if (x % 2 == 0):
            res.add(x)
    return res

@pytest.mark.parametrize("testcase, input, output",[
(14, {2,4.2,3,4,6.5,5}, {2,4,3}, "hello"), 
(15, "testdata", {2,4,3}, 345)
])              

def test_filtrar_impares(testcase, input, output):
    assert filtrar_impares(input) == output,\
           "caso {0}".format(testcase)