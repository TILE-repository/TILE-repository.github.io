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
    
    # 1: Open the file in file-handle called fhand
    python_file = open(filename, "r")

    # 2: Go through the file until you reach the line where
    #   the test cases begin
    line = python_file.readline()
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
      
    # when we call readline() once again we continue reading the first parameterized test cases
    line = python_file.readline() # line now points to the first test case of form (ID, input1, .., inputn, output)
    
    # test case line for two inputs looks likelooks like: '(num, i1, i2, o),   #Cardinality\n'
    # - starts with (
    # - ends with ),
    # - all after ), commenst starting with # can be discarded
    # - different parts are separated by ", "
    # - i1, i2, and o can be anything (also tuples so cannot rely on position of ")" )
    
    test_cases = []
    while (line.startswith("(")): #each test case starts with "("
        
        #parse the line
        
        tc = testcase_parser.parse(line)
        test_cases.append(tc)             
        
        line = python_file.readline() #go to next line in file
            
    
    return test_cases

    # 3: Close the file
    python_file.close()

files = {
    "filter_odd_tests-nocomments.py",
    "filter_odd_tests-YEScomments.py",
    "filter_odd_tests-string-cases.py",
    "intersection_test.py",
    "min_max_list_test.py",
    "union_test.py"
}

for file in files: 
    print(file)
    for tc in get_test_cases(file):
        print(tc.pretty())
        print(MyTransformer().transform(tc))
        print("\n")