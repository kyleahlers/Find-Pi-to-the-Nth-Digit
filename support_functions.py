# this function converts int or float number to list for comparisons.
# ie. 123.40 to [1, 2, 3, 4, 0]

def num_to_list(n):
    
    # assign empty list to result variable
    result = []
    
    # converts input (n) to a iterable string. Appends all integers to list
    for element in str(n):
        if element.isdigit() == True:
            result.append( int(element) )
            
    return result


##########################################################################
# compares two lists of equivalent length up to n digits

def compare_list(a,b):
    green_light = True
    compare_result = []
    element = 0

    # compares two entire lists and appends all equivalent values. when element 
    # is no longer equal it breaks out
    while element < len(a):

        if a[element] == b[element]:
            compare_result.append(a[element])
            element += 1

        else:
            break
    
    return compare_result
    
    
##########################################################################
# converts list of numbers (validates as pi approximation) and converts 
# it to a float number
def pi_list_to_num(test):
      
    str_test = []
    
    for num in test:
        
        str_test.append(str(num))
        
    joined_test = ''.join(str_test)
    
    return int(joined_test)
    
