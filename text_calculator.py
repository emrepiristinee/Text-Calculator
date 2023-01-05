
def operations(input): #check errors, calculates if there are no errors 
    input_txt = open(input, "r")
    for a in input_txt:
        if len(a) !=  1:
            if end_of_line_check(a) == False: #checks end of line, i.e. 3+5-7*
                f.write("ERROR\n")
                print("ERROR")
            elif head_of_line_check(a) == False: #checks head of line, i.e. *5/2+1
                f.write("ERROR\n")
                print("ERROR")
            elif twice_equals_control(a) == False: #checks how many equals, i.e. 10 == 8 + 2 == 10
                f.write("ERROR\n")
                print("ERROR")
            else:
                calculation(a) #calculation function
        elif len(a) == 1: #if there is a space in the txt, it will print a space in the output.
            f.write(" \n")
            print(" ")
    input_txt.close()



def infinite_divice_control(operation_list, number_list): #checks for undefined "/0" operations, i.e. 2/0
    for x in range(len(operation_list)):
        if operation_list[x] == '/' and number_list[x+1] == '0': #if 0 after /
            return False
        else:
            return True



def twice_operations_control(operation_list, number_list): # i.e. (3 ++ 5), i.e. (21 + 1 3 - 16)
    if len(operation_list) + 1 != len(number_list): #if the numbers are not more than 1 of the operations
        return False
    else:
        return True
    
    

def twice_equals_control(sentence): #checks how many equals, i.e. 10 == 8 + 2 == 10
    how_many_equal = 0
    for x in range(len(sentence)):
        if sentence[x:x+2] == '==' or sentence[x:x+1] == ">" or sentence[x:x+1] == "<" or sentence[x:x+1] == ">=" or sentence[x:x+2] == "<=" or sentence[x:x+2] == '!=':
            how_many_equal += 1
    
    if how_many_equal > 1:
        return False
    else:
        return True



def end_of_line_check(sentence): #checks end of line, i.e. 3 + 1 -
    a = sentence[-2]
    if ord(a) < 48 or ord(a) > 57:
        return False
    else:
        return True
      
    
    
def head_of_line_check(sentence): #checks head of line, i.e. + 3 - 5
    a = sentence[0]
    if ord(a) < 48 or ord(a) > 57:
        return False
    else:
        return True



def is_big_or_small(operation_list, number_list): #calculates which numbers are bigger, i.e. 5<3
    result = ""
    if len(operation_list) == 1 and (operation_list[0] == ">" or operation_list[0] == "<" or operation_list[0] == ">=" or operation_list[0] == "<=" or operation_list[0] == "==" or operation_list[0] == '!='):              
        i = 0
        if operation_list[i] == '>': #returns true if greater than
            if number_list[i] > number_list[i+1]:
                print("TRUE")
                result = "TRUE"
            elif number_list[i] < number_list[i+1]:
                print("FALSE")
                result = "FALSE"
            else:
                print("ERROR")
                result = "ERROR"
                          
        elif operation_list[i] == '>=': #returns true if greater than or equal to        
            if number_list[i] >= number_list[i+1]:
                print("TRUE")
                result = "TRUE"
            elif number_list[i] <= number_list[i+1]:
                print("FALSE")
                result = "FALSE"
            else:
                print("ERROR")
                result = "ERROR"
            
        elif operation_list[i] == '<': #returns true if less than
            if number_list[i] < number_list[i+1]:
                print("TRUE")
                result = "TRUE"
            elif number_list[i] > number_list[i+1]:
               print("FALSE")
               result = "FALSE"
            else:
               print("ERROR")
               result = "ERROR"
               
        elif operation_list[i] == '<=': #returns true if less than or equal to
            if number_list[i] <= number_list[i+1]:
                print("TRUE")   
                result = "TRUE"
            elif number_list[i] >= number_list[i+1]:
              print("FALSE")
              result = "FALSE"
            else:
              print("ERROR")
              result = "ERROR"

        elif operation_list[i] == '!=': #returns true if not equal
            if number_list[i] != number_list[i+1]:
                print("TRUE")
                result = "TRUE"
            elif number_list[i] == number_list[i+1]:
               print("FALSE")
               result = "FALSE"
            else:
               print("ERROR")
               result = "ERROR"
               
        elif operation_list[i] == '==': ##returns true if equal
            if number_list[i] == number_list[i+1]:
                print("TRUE")
                result = "TRUE"
            elif number_list[i] != number_list[i+1]:
               print("FALSE")
               result = "FALSE"
            else:
               print("ERROR")
               result = "ERROR"

        if result == "TRUE": #if above returned true
            f.write("TRUE\n")
        elif result == "FALSE":
            f.write("FALSE\n")
        else:
            f.write("ERROR\n")
                


def calculation(sentence):
    number_list = [] #numbers for list
    operation_list = [] #operations for list
    for x in range(len(sentence)):
        #operation detection query
        if sentence[x:x+2] == '==' or sentence[x:x+2] == '//' or sentence[x:x+2] == '**' or sentence[x:x+1] == '*' or sentence[x:x+1] == '/' or sentence[x:x+1] == '+' or sentence[x:x+1] == '-' or sentence[x:x+1] == '%' or sentence[x:x+1] == '<' or sentence[x:x+2] == '<=' or sentence[x:x+1] == '>' or sentence[x:x+2] == '>=' or sentence[x:x+2] == '!=':  
            #Operations query with 2 indexes
            if sentence[x:x+2] == '==' or sentence[x:x+2] == '//' or sentence[x:x+2] == '**' or sentence[x:x+2] == '<=' or sentence[x:x+2] == '>=' or sentence[x:x+2] == '!=': 
                operation_list.append(sentence[x:x+2]) #adds the operation to the list
                sentence = sentence[0:x] + '  ' + sentence[x+2:] #deletes the operation in the process adds a space instead
            #Operations query with 1 index
            elif sentence[x:x+1] == '*' or sentence[x:x+1] == '/' or sentence[x:x+1] == '+' or sentence[x:x+1] == '-' or sentence[x:x+1] == '%' or sentence[x:x+1] == '<' or sentence[x:x+1] == '>':
                operation_list.append(sentence[x:x+1]) #add operation in list
                sentence = sentence[0:x] + ' ' + sentence[x+1:] #deletes the operation in the process adds a space instead
                
    sentence = sentence.split() #splits string where only numbers remain
    for x in sentence:
        number_list.append(x) #add numbers in list
        
        
    if twice_operations_control(operation_list, number_list) == False:  # i.e. (3 ++ 5), i.e. (21 + 1 3 - 16)
        f.write("ERROR\n")
        print("ERROR")
        
    elif infinite_divice_control(operation_list, number_list) == False: #checks for undefined "/0" operations, i.e. 2/0
        f.write("ERROR\n")
        print("ERROR")
        
    #calculates which numbers are bigger, i.e. 5<3
    elif (len(operation_list) == 1) and (operation_list[0] == ">" or operation_list[0] == "<" or operation_list[0] == ">=" or operation_list[0] == "<=" or operation_list[0] == "==" or operation_list[0] == '!='):
        is_big_or_small(operation_list, number_list)
        
    else:
        #if there are no error, calculate
        # Booleans for action priority
        boolean_plus_mines = False
        boolean_equals = False
        boolean_equals2 = True
        boolean_exponentation = True
        boolean_multip_division = False
        boolean_mod = False
        boolean_division_roll = False
        boolean_error_check = True
        i = 0
        while len(operation_list) != 0 and boolean_error_check == True:
            if i >= len(operation_list): #to check that the process is finished
                i=-1
                
            elif boolean_exponentation == True: #exponentiation
                if operation_list[i] == '**':
                    number_list[i] = float(number_list[i]) ** float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                    number_list.remove(number_list[i+1]) #delete number to the right of the operation
                    operation_list.remove(operation_list[i]) #delete operation
                    i -=1
                
                if i == len(operation_list) - 1:
                    boolean_exponentation = False #boolean is false because exponentation is finished
                    boolean_multip_division = True #multiplication and division in order of operations are true
                    i = -1                   
            
            elif boolean_multip_division == True: #multiplication and division operations
                if operation_list[i] == '/': 
                    number_list[i] = float(number_list[i]) / float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                    number_list.remove(number_list[i+1]) #delete number to the right of the operation
                    operation_list.remove(operation_list[i]) #delete operation
                    i -=1
                elif operation_list[i] == '*':
                    number_list[i] = float(number_list[i]) * float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                    number_list.remove(number_list[i+1]) #delete number to the right of the operation
                    operation_list.remove(operation_list[i]) #delete operation
                    i -=1
                elif i == len(operation_list) - 1:
                    boolean_multip_division = False #boolean is false because division and multiply is finished
                    boolean_division_roll = True #division roll in order of operations are true
                    i = -1
                                          
            elif boolean_division_roll == True: #division roll operations
                 if operation_list[i] == '//':
                     if float(number_list[i]) >= float(number_list[i+1]): 
                         (number_list[i]) = int(number_list[i]) // int(number_list[i+1]) #The result is written instead of the number to the left of the operation
                         number_list.remove(number_list[i+1]) #delete number to the right of the operation
                         operation_list.remove(operation_list[i]) #delete operation
                         i -= 1
                         
                     elif number_list[i+1] == 0: #throw an error if the operation is "2 // 0"  
                         print("ERROR")
                         f.write("ERROR\n")
                         boolean_error_check = False
                        
                     else:
                         print("ERROR")
                         f.write("ERROR\n")
                         boolean_error_check = False
                         
                 if i == len(operation_list) - 1:
                     boolean_division_roll = False #boolean is false because division roll is finished
                     boolean_mod = True #mod in order of operations are true
                     i = -1
            
            elif boolean_mod == True: #mod operations
                if operation_list[i] == '%':
                    number_list[i] = float(number_list[i]) % float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                    number_list.remove(number_list[i+1]) #delete number to the right of the operation
                    operation_list.remove(operation_list[i]) #delete operation
                    i -= 1
                elif number_list[i+1] == 0: #throw an error if the operation is "2 % 0"
                    print("ERROR")
                    f.write("ERROR\n")
                    boolean_error_check = False
                    
                if i == len(operation_list) - 1:
                    boolean_mod = False #boolean is false because mod is finished
                    boolean_plus_mines = True #plus and minus roll in order of operations are true
                    i = -1             
                
            elif boolean_plus_mines == True: #plus and minus operations
                if operation_list[i] == '+' or operation_list[i] == '-':
                    if operation_list[i] == '+':
                        number_list[i] = float(number_list[i]) + float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                        number_list.remove(number_list[i+1]) #delete number to the right of the operation
                        operation_list.remove(operation_list[i]) #delete operation
                        i -=1
                    elif operation_list[i] == '-':
                        number_list[i] = float(number_list[i]) - float(number_list[i+1]) #The result is written instead of the number to the left of the operation
                        number_list.remove(number_list[i+1]) #delete number to the right of the operation
                        operation_list.remove(operation_list[i]) #delete operation
                        i -=1
                
                #if only one operation is left and the operation is equal
                elif len(operation_list) == 1 and (operation_list[i] == '==' or operation_list[i] == '<=' or operation_list[i] == '>=' or operation_list[i] == '<' or operation_list[i] == '>' or operation_list[i] == '!='):
                        if qeuals(number_list[0],number_list[1],operation_list[0]) == True: #goes to the equals function and checks
                            boolean_equals = True
                            break
                        else:
                            boolean_equals = False
                            boolean_equals2 = False #second boolean for print-to-screen control
                            break

            #if only one operation is left and the operation is equal
            elif len(operation_list) == 1 and operation_list[i] == '==':
                if qeuals(number_list[0],number_list[1],operation_list[0]) == True: #goes to the equals function and checks
                    boolean_equals = True
                    break
            i+= 1
            
            
        if boolean_equals == True: #if the equals function above returned true
            print("TRUE")
            f.write("TRUE\n")
        elif boolean_equals == False and boolean_equals2 == False: #if the equals function above returned false
            print("FALSE")
            f.write("FALSE\n")
        elif (boolean_error_check == True): #prints operation results that are not ERROR, TRUE, FALSE
            print(format(number_list[0], '.2f'))
            f.write((format(number_list[0], '2f')) +"\n" )
            
        
        
    
def qeuals(a, b, c): # returns true or false by operation
    if c == '==':
        if float(a) == float(b):
            return True
        else:
            return False
    elif c == '>=':
        if float(a) >= float(b):
            return True
        else:
            return False
    elif c == '<=':
        if float(a) <= float(b):
            return True
    elif c == '>':
        if float(a) > float(b):
            return True
        else:
            return False
    elif c == '<':
        if float(a) < float(b):
            return True
        else:
            return False
    elif c == '!=':
        if float(a) != float(b):
            return True
        else:
            return False
    else:
        return False

    


def main():
    try:
        operations("input.txt")
        
    except TypeError:    
        print("Wrong type of main function")
    except NameError:
        print("Wrong name of main function")
    except FileNotFoundError:
        print("File in main function not found")
    except SyntaxError:
        print("invalid syntax in main function")
    except:
        print("Something went wrong in main function")
    
        
    

f = open("2020510118_emre_piristine_output.txt", "w")
main()
f.close()