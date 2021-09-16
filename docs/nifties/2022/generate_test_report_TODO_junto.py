import json
import xlwt 
from xlwt import Workbook

def get_failed_testcases(filename):
    """
    Expects filename to be a file that contains the output of a !pytest run.
    Returns the list of testcases that have failed.
    Throws FileNotFoundError exception if file does not exist.
    """

    #1: Abrir el fichero en file-handle llamado fhand
    fhand = open(filename, 'r')
    
    #Copia el contenido del fichero en content
    content = fhand.read()
    
    #3: Cerrar el fichero
    fhand.close()

    #buscamos si hay casos de test que han fallado
    
    if not ("= FAILURES" in content):
       return []
    else:
        #tenemos que buscar los test cases que han fallado, empiezan con "testcase = "
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
    #1: Abrir el fichero en file-handle llamado fhand
    python_file = open(filename, "r")

    #2: Recorrer el fichero hasta llegar a la linea donde
    #   empiezan los test cases (o al final del fichero si no hay)
    line = python_file.readline()
    
    while not (line.startswith("@pytest.mark.parametrize") or line==''):
        line = python_file.readline()
    
    #3: Cerrar el fichero
    python_file.close()
    
    #line now is the "@pytest.mark.parametrize" line
    # check it if you want, uncommenting this:
    #print ("Read Line: %s" % (line))
    
    #Now, we need to know what the structure of the test cases is,
    #i.e. how many inputs. So we first filter the characters that we do not need.
    filter_out = [',', "@pytest.mark.parametrize", "(", ")", "[", '"']
    for f in filter_out:
        line = line.replace(f, "")
    
    #Then we split, such that we get a list like
    #['testcase', input1, ..., inputn, output]
    test_signature = line.split()
    
    return test_signature 
    
def get_test_cases(filename, test_signature):
    
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
        
        test_case = line.rstrip().split(", ")[0:len(test_signature)]
                
        #Elimina los parentesis del test case. 
        test_case[0] = test_case[0].replace("(", "")
        test_case[-1] = test_case[-1].replace(")", "")
        
        test_cases.append(test_case)
                     
        line = python_file.readline() #go to next line in file
            
    return test_cases

    #3: Cerrar el fichero
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
            
            test_cases = get_test_cases(filenameTest, test_signature)
            
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
                    sheet.write(i+1, j , test_cases[i][j])
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
            
            test_cases = get_test_cases(filenameTest, test_signature)
            
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
            tc_dict["resultado"]= "----"
            test_cases_dicts.append(tc_dict)
        
        report_name = filenameTest.replace(".py", "")
        
        fhand_write = open(report_name + "test_case_report.json", "w")
        fhand_write.write(json.dumps(test_cases_dicts))
        fhand_write.close()
                
    except FileNotFoundError:
        print("El fichero no existe" + filenameTest)
   

def main():
    #para el testing
    #hay que chequear los ficheros output de forma manual
    
    file1_test = "pytests-for_testing_reports/union_test.py"
    file1_testres = "pytests-for_testing_reports/output_union_test.txt"
    
    file2_test = "pytests-for_testing_reports/min_max_list_test.py"
    file2_testres = "pytests-for_testing_reports/output_min_max_list_test.txt"
    
    file3_test = "pytests-for_testing_reports/filtrar_impares_test.py"
    file3_testres = "pytests-for_testing_reports/output_filtrar_impares_test.txt"
    
    file4_test = "pytests-for_testing_reports/interseccion_test.py"
    file4_testres = "pytests-for_testing_reports/output_interseccion_test.txt"
    
    generate_excell_test_report(file1_test, file1_testres)
    generate_JSON_test_report(file1_test, file1_testres)
    
    generate_excell_test_report(file2_test, file2_testres)
    generate_JSON_test_report(file2_test, file2_testres)
    
    generate_excell_test_report(file3_test, file3_testres)
    generate_JSON_test_report(file3_test, file3_testres)
    
    generate_excell_test_report(file4_test, file4_testres)
    generate_JSON_test_report(file4_test, file4_testres)
