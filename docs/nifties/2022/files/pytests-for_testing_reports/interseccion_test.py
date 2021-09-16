import pytest

def interseccion(lista1, lista2, lista3):
    i = 0
    res = []
    for i in range(len(lista1)):
        if lista1[i] in lista2: 
            res.append(lista1[i]) 
    return res + lista3

@pytest.mark.parametrize("testcase, input1, input2, input3, output",[
(1, [], [], [], []),   #Cardinalidad
(2, [], [1,2,3], [], []),   #Cardinalidad
(3, [1,2,3], [], [2], [2]),   #Cardinalidad
(4, [1,1], [], [], []),   #Cardinalidad
(5, [], [1,1], [],  []),   #Cardinalidad
(6, ["hola", 2, 3, "abc"], ["hola", "hola", "de"], ["hi"], ["hola","hi"]), #Dominio, Estructura
(7, [1,1,2,2,3,3], [1,2,3], [8], [1,2,3,8]),   #Orden (de parametros), Estructura
(8, [3,4,5,6,6], [3,4,5,6,6], [], [3,4,5,6]), #Orden (duplicados al final de la lista)
(9, (3,4,5,6,6), (3,4,5,6,6), [], [3,4,5,6])
])

def test_interseccion(testcase, input1, input2, input3, output):
    assert interseccion(input1, input2, input3) == output,\
           "caso {0}".format(testcase)
