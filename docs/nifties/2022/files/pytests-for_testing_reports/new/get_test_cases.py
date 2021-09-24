from lark import Lark
from lark import Transformer

class MyTransformer(Transformer):
    def testcase(self, items):
        n, *vs= items
        return (n,) + tuple(vs)
    
    def value(self, items):
        return items
    
    def pair(self, key_value):
        k, v = key_value
        return k, v
    
    def string(self, s):
        (s,) = s
        return s[1:-1]
    
    def number(self, n):
        (n,) = n
        return n
    
    list = list
    tuple = tuple
    dict = dict
    set = set

    none = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
    
    
# python strings are double quotes ad single quotes

#   SINGLEQUOTES: "'"
#   DOUBLEQUOTES: "\""
    
#   string: SINGLEQUOTES [(character|digit|symbol)*] SINGLEQUOTES
#         | DOUBLEQUOTES [(character|digit|symbol)*] DOUBLEQUOTES


#Cannot use this
#       | "'" _STRING_ESC_INNER "'"


testcase_parser = Lark(r"""
    testcase : "(" SIGNED_NUMBER "," value ("," value)* ")" [","] [SH_COMMENT]
    
    value: dict
         | list
         | tuple
         | set
         | string
         | variable_name
         | SIGNED_NUMBER    -> number
         | "True"    -> true
         | "False"   -> false
         | "None"    -> none
    
    dict : "{" [pair ("," pair)*] "}"

    pair : string ":" value

    list : "[" [value ("," value)*] "]"

    tuple: "(" [value ("," value)*] ")"

    set  : "set" "(" [value ("," value)*] ")"
         |"{" [value ("," value)*] "}"
    
    string : ESCAPED_STRING
    
    variable_name: CNAME
                
    %import common.ESCAPED_STRING
    %import common.SH_COMMENT
    %import common.CNAME
    %import common.SIGNED_NUMBER
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



file1 = "pytests-for_testing_reports/filtrar_impares_test-nocomments.py"
file2 = "pytests-for_testing_reports/filtrar_impares_test-YEScomments.py"
file3 = "pytests-for_testing_reports/filtrar_impares_test-string-cases.py"
file4 = "pytests-for_testing_reports/interseccion_test.py"
file5 = "pytests-for_testing_reports/min_max_list_test.py"
file6 = "pytests-for_testing_reports/union_test.py"


for file in {file1, file2,file3, file4, file5, file6}: 
    print(file)
    for tc in get_test_cases(file):
        print(tc.pretty())
        print(MyTransformer().transform(tc))
        print("\n")
    
