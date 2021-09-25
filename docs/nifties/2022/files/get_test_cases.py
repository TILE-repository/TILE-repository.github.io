from lark import Lark
from lark import Transformer

# Below is the grammar describing test cases.
# test case lines look like: '(num, i1, i2,...,in o),   #any type of comments'
# - starts with (
# - ends with ),
# - the first argument is a number, the ID of the test case
# - after the end test case ), commenst starting with #can be discarded
# - different parts of the test case are separated by ", "
# - i1, i2, ..., in and o can be of any Python type (int, float, bool, strings, lists, tuples, variables, sets)
# - the exercise explicity indicates that we assume there are no operators (unary, binary operators), variable names, dictionaries, function calls

testcase_parser = Lark(r"""
    testcase : "(" DEC_NUMBER "," value ("," value)* ")" [","] [SH_COMMENT]
    
    value: list
         | tuple
         | emptyset
         | set
         | string
         | number
         | "True"    -> true
         | "False"   -> false
         | "None"    -> none

    list : "[" [value ("," value)*] "]"

    tuple: "(" [value ("," value)*] ")"

    set  : "{" value ("," value)* "}"

    emptyset: "set()"
    
    number: DEC_NUMBER | FLOAT_NUMBER 
  
    string: /[ubf]?r?("(?!"").*?(?<!\\)(\\\\)*?"|'(?!'').*?(?<!\\)(\\\\)*?')/i

    DEC_NUMBER: /0|[1-9][\d_]*/i
    FLOAT_NUMBER: /((\d+\.[\d_]*|\.[\d_]+)([Ee][-+]?\d+)?|\d+([Ee][-+]?\d+))/
        
    %import common.ESCAPED_STRING
    %import common.SH_COMMENT
    %import common.CNAME
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='testcase')

# Evaluate the tree, using a Transformer.
# A transformer is a class with methods corresponding to branch names.
# For each branch, the appropriate method will be called with the children
# of the branch as its argument, and its return value will replace the branch
# in the tree. We want to transform the parse tree into a tuple containing the
# test case values.

class MyTransformer(Transformer):
    def testcase(self, items):
        *vs, c = items
        if c==None: #it means it is a comment (see SH_COMMENT), so we can discard
            return tuple(vs)
        else:
            return tuple(items)
    
    def SH_COMMENT(self,n):
        return None
    
    def value(self, items):
        [res] = items
        return res
    
    def pair(self, key_value):
        k, v = key_value
        return k, v
    
    def string(self, s):
        (s,) = s
        return s[1:-1]
    
    def number (self, n):
        (n,) = n
        return n
    
    def FLOAT_NUMBER (self, n):
        return float(n)
    
    def DEC_NUMBER(self, n):
        return int(n)
    
    def emptyset(self, items):
        return set()
    
    def set(self, items):
        res  = set()
        for i in items:
            res.add(i)
        return res
        
    list = list
    tuple = tuple
    dict = dict
   
    none = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
       


def get_test_cases(filename):
    
    """
    This function returns a list of the test cases that are defined in the
    file with "@pytest.mark.parametrize". If it is not a pytest file it returns
    the empty list
    
    Throws FileNotFoundError exception if file does not exist.
    """
    
    # 1: Open the file
    python_file = open(filename, "r")

    # 2: Read the file until you encounter the line where the testcases
    #   start (that is @pytest.mark.parametrize)
    line = python_file.readline()
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
      
    # read one more line, to point line to the first test case
    line = python_file.readline() 
     
    test_cases = []
    while (line.startswith("(")): #each test case starts with "("
        
        #parse the line
        tc_tree = testcase_parser.parse(line)
        
        #reduce the parse tree to a tc tuple like (num, i1, i2,...,in o)
        tc = MyTransformer().transform(tc_tree)
        
        #add the testcase to the list of test cases
        test_cases.append(tc)             
        
        line = python_file.readline() #go to next line in file
            
    # 3: Close the file
    python_file.close()

    return test_cases


#testing the parser with main, tester should manually check the output
def main():

    file = "pytest_file_to_test_parser.py"
    
    # Generate a basic report
    print("using", file)
    for tc in get_test_cases(file):
        print("testcase:",tc)


if __name__ == "__main__":
    # execute only if run as a script
    main()        