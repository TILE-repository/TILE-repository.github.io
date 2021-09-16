from lark import Lark

testcase_parser = Lark(r"""
    testcase : "(" NUMBER "," value ("," value)* ")" [","] ["#" comments*]
    
    comments : (character|digit|symbol)*
    
    character: ("a".."z")+ | ("A".."Z")+
    
    digit: ("0".."9")+
    
    symbol: (" " | "_" | ","  | "}" | "(" | ")" )+
    
    value: dict
         | list
         | tuple
         | set
         | string
         | variable_name
         | NUMBER
         | "True"
         | "False"
         | "None"

    variable_name: character [(character|digit|symbol)*]
    
    SINGLEQUOTES: "'"
    DOUBLEQUOTES: "\""
    
    string: SINGLEQUOTES [(character|digit|symbol)*] SINGLEQUOTES
          | DOUBLEQUOTES [(character|digit|symbol)*] DOUBLEQUOTES
    
    dict : "{" [pair ("," pair)*] "}"

    pair : STRING ":" value

    list : "[" [value ("," value)*] "]"

    tuple: "(" [value ("," value)*] ")"

    set  : "set" "(" [value ("," value)*] ")"
         |"{" [value ("," value)*] "}"
                
    %import common.ESCAPED_STRING   -> STRING
    %import common.SIGNED_NUMBER    -> NUMBER
    %import common.WS
    %ignore WS

    """, start='testcase')


def get_test_cases(filename):
    
    """
    This function returns a list of the test cases that are defined in the
    file with "@pytest.mark.parametrize". If it is not a pytest file it returns
    the empty list
    
    Throws FileNotFoundError exception if file does not exist.
    """
    
    #1: Abrir el fichero en file-handle llamado fhand
    python_file = open(filename, "r")

    #2: Recorrer el fichero hasta llegar a la linea donde
    #   empiezan los test cases
    line = python_file.readline()
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
      
    #cuando llamamos una vez mas a readline() seguimos leyendo los primeros test cases parametrizados
    line = python_file.readline() #line ahora apunta al primer test case de forma (ID, input1, .., inputn, output)
    
    #test case line for two inputs looks likelooks like: '(num, i1, i2, o),   #Cardinalidad\n'
    #- starts with (
    #- ends with ),
    #- all after ), commenst starting with #can be discarded
    #- different parts are separated by ", "
    #- i1, i2, and o can be anything (also tuples so cannot rely on position of ")" )
    
    test_cases = []
    while (line.startswith("(")): #each test case starts with "("
        
        #parse the line
        
        tc = testcase_parser.parse(line)
        test_cases.append(tc)             
        
        line = python_file.readline() #go to next line in file
            
    
    return test_cases

    #3: Cerrar el fichero
    python_file.close()



file1 = "pytests-for_testing_reports/filtrar_impares_test.py"
file2 = "pytests-for_testing_reports/interseccion_test.py"
file3 = "pytests-for_testing_reports/min_max_list_test.py"
file4 = "pytests-for_testing_reports/union_test.py"

for file in {file1,file2,file3,file4}:
    print(file)
    for tc in get_test_cases(file):
        print(tc)
        print("\n")
    
