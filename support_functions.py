# converts int or float number to list for comparisons.
# ie. 123.40 to [1, 2, 3, 4, 0]

def num_to_list(n):
    
    result = []
    
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

    while element < len(a):

        if a[element] == b[element]:
            compare_result.append(a[element])
            element += 1

        else:
            break
    
    return compare_result
    
    
##########################################################################
def pi_list_to_num(test):
      
    str_test = []
    
    for num in test:
        
        str_test.append(str(num))
        
    joined_test = ''.join(str_test)
    
    return int(joined_test)
    