import json
import xlwt 
from xlwt import Workbook
from lark import Lark
from lark import Transformer

def get_failed_testcases(filename):
    """
    Expects filename to be a file that contains the output of a !pytest run.
    Returns the list of testcases that have failed.
    Throws FileNotFoundError exception if file does not exist.
    """

    #1.Open the file and name the file-handle fhand
    fhand = open(filename, 'r')
    
    #2.Copy the content of the file in variable content
    content = fhand.read()
    
    #3: Close the file
    fhand.close()

    #Look for the failed test cases
    
    if not ("= FAILURES" in content):
       return [] #There are no failed test cases
    else:
        # Find the testcases that have failed, they
        # start with "testcase = " in the file
        lss_lines = content.splitlines()
        testcases = []
        for l in lss_lines:
            if "testcase =" in l:
                testcases.append(l)
        return testcases
        

def get_test_signature(filename):
    """
    Given a Python file containing "@pytest.mark.parametrize", it returns a list that
    represents the signature of the test. If there are no pytests in the file, it returns
    the empty list
    
    Throws FileNotFoundError exception if file does not exist.
    """
    #1: Open the file and name the file-handle fhand
    python_file = open(filename, "r")

    #2: Read through the file to find the line that indicates that
    #   the test cases start (i.e. @pytest.mark.parametrize)
    line = python_file.readline()
    
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
    
    #3: Close the file
    python_file.close()
    
    #line now is the "@pytest.mark.parametrize" line
    
    #Now, we need to know what the structure of the test cases is,
    #i.e. how many inputs. So we first filter the characters that we do not need.
    filter_out = [',', "@pytest.mark.parametrize", "(", ")", "[", '"']
    for f in filter_out:
        line = line.replace(f, "")
    
    #Then we split, such that we get a list like
    #['testcase', input1, ..., inputn, output]
    test_signature = line.split()
    
    return test_signature 



# Below is the grammar describing test cases.
# test case lines look like: '(num, i1, i2,...,in o),   #any type of comments'
# - starts with (
# - ends with ),
# - the first argument is a number, the ID of the test case
# - after the end test case ), commenst starting with #can be discarded
# - different parts of the test case are separated by ", "
# - i1, i2, ..., in and o can be of any Python type (int, float, bool, strings, lists, tuples, variables, sets)
# - the exercise explicity indicate that we assume there are no operators (unary, binary operators), variable names, dictionaries, function calls


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
    
    #1: Open the file
    python_file = open(filename, "r")

    #2: Read the file until you encounter the line where the testcases
    #   start (that is @pytest.mark.parametrize)
    line = python_file.readline()
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
      
    #read one more line, to point line to the first test case
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
            
    
    return test_cases

    #3: Close the file
    python_file.close()


def fill_excell_headers(test_signature, wb):
      
    """
    # This function fills the headers of a test report with number_of_inputs input values
    """
    
    #We know the structure we need to create for the excell file from the test_signature
    number_of_inputs = len(test_signature)-2
    
    # add_sheet is used to create sheet for Test Report
    sheet = wb.add_sheet('Test Report') 
  
    # add test case ID colum at 0,0
    sheet.write(0, 0, 'test case ID')
    
    # add input columns for each test case input
    for i in range (1, number_of_inputs+1):
        sheet.write(0, i, 'input'+str(i))
    
    # add input columns for the expected outcome and the result
    sheet.write(0, number_of_inputs+1 , 'expected outcome')
    sheet.write(0, number_of_inputs+2 , 'result')
    
    return sheet


def generate_excell_test_report(filenameTest, filenameTestRes):
    """ filenameTest es el nombre de fichero .py de testing y 
        filenameTestRes es el nombre de fichero .txt con test results
    """
    try:
        test_signature = get_test_signature(filenameTest)
        
        if (test_signature == []):
            print("This is not a pytest file")
        else:
            
            test_cases = get_test_cases(filenameTest)
                        
            failed_test_cases = get_failed_testcases(filenameTestRes)
            
            failed_test_cases_numbers = []
            for f in failed_test_cases:
                failed_test_cases_numbers.append(f.split()[2].replace(",",""))
            
            # Workbook is created 
            wb = Workbook()
          
            #fill with headers for the columns
            sheet = fill_excell_headers(test_signature, wb)
          
            #write ID, inputs y output in excell        
            for i in range(len(test_cases)):
                for j in range(len(test_cases[i])):
                    sheet.write(i+1, j , str(test_cases[i][j]))
                    
                if test_cases[i][0] in failed_test_cases_numbers:
                    sheet.write(i+1, len(test_cases[i]) , "FAILED")
                else:
                    sheet.write(i+1, len(test_cases[i]) , "PASSED")
                
            report_name = filenameTest.replace(".py", "")
            # Save the Workbook
            wb.save(report_name + 'TestReport.xls') 
 
    except FileNotFoundError:
        print("El fichero no existe" + filenameTest + " o " + filenameTestRes)


def generate_JSON_test_report(filenameTest, filenameTestRes):
    """ filenameTest es el nombre de fichero .py de testing y 
        filenameTestRes es el nombre de fichero .txt con test results
    """
    
    try:

        test_signature = get_test_signature(filenameTest)
        
        if (test_signature == []):
            print("This is not a pytest file")
        else:
            
            test_cases = get_test_cases(filenameTest)
            
            failed_test_cases = get_failed_testcases(filenameTestRes)
            
            failed_test_cases_numbers = []
            for f in failed_test_cases:
                failed_test_cases_numbers.append(f.split()[2].replace(",",""))
            
            test_cases_dicts = []
            for tc in test_cases:
                tc_dict = {"id":tc[0]}
                out = tc[-1]
                tc = tc[1:len(tc)-1]
                inputs = []
                for t in tc:
                    inputs.append(t)
                tc_dict["inputs"]=inputs
                tc_dict["output esperado"]=out
                if tc[0] in failed_test_cases_numbers:
                    tc_dict["resultado"]= "FAILED"
                else:
                    tc_dict["resultado"]= "PASSED"
                test_cases_dicts.append(tc_dict)
            
            report_name = filenameTest.replace(".py", "")
            
            fhand_write = open(report_name + "test_case_report.json", "w")
            fhand_write.write(json.dumps(test_cases_dicts))
            fhand_write.close()
                
    except FileNotFoundError:
        print("El fichero no existe" + filenameTest)
   

def main():
    #test the report generatiom
    #you need to check the output manualy as follows:
    # 1) see if the files were generated in the directory
    # 2) check the data in the files corresponds to the testcases in the .py file,
    #    and the outputs in the .txt file
    
    file1_test = "pytests-for_testing_reports/union_test.py"
    file1_testres = "pytests-for_testing_reports/output_union_test.txt"
    
    file2_test = "pytests-for_testing_reports/min_max_list_test.py"
    file2_testres = "pytests-for_testing_reports/output_min_max_list_test.txt"
    
    file3_test = "pytests-for_testing_reports/interseccion_test.py"
    file3_testres = "pytests-for_testing_reports/output_interseccion_test.txt"
    
    file4_test = "pytests-for_testing_reports/filtrar_impares_test.py"
    file4_testres = "pytests-for_testing_reports/output_filtrar_impares_test.txt"
    
    generate_excell_test_report(file1_test, file1_testres)
    generate_JSON_test_report(file1_test, file1_testres)
    
    generate_excell_test_report(file2_test, file2_testres)
    generate_JSON_test_report(file2_test, file2_testres)
    
    generate_excell_test_report(file3_test, file3_testres)
    generate_JSON_test_report(file3_test, file3_testres)
    
    generate_excell_test_report(file4_test, file4_testres)
    generate_JSON_test_report(file4_test, file4_testres)
