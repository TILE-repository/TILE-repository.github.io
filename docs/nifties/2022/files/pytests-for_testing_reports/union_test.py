import pytest

def union(lista1, lista2):
    i = 0
    res = lista1
    for i in range(len(lista2)):
        if not lista2[i] in res: 
            res.append(lista2[i])
    return res

@pytest.mark.parametrize("testcase, input1, input2, output",[
(1, [], [], []),   #Cardinalidad
(2, [], [1,2,3], [1,2,3]),   #Cardinalidad
(3, [1,2,3], [], [1,2,3]),   #Cardinalidad
(4, [1,1], [], [1]),   #Cardinalidad
(5, [], [1,1], [1]),   #Cardinalidad
(6, ["hola", 2, 3, "abc"], ["hola", "hola", "de"], ["hola", 2, 3, "abc", "de"]), #Dominio, Estructura
(7, [1,1,2,2,3,3], [], [1,2,3]),   #Orden (de parametros), Estructura
(8, [3,4,5,6,6], [3,4,5,6,6], [3,4,5,6]), #Orden (duplicados al final de la lista)
])

def test_union(testcase, input1, input2, output):
    assert union(input1, input2) == output,\
           "caso {0}".format(testcase)