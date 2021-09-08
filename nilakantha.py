
##########################################################################
# iterate through nikantha series with while loop
# each pass through the while loop adds a term to the nilakantha series
# the digits in the series are stored in an interable list
# after each loop, we check to see if the latest digit is same as previous loop
# if it is, then store it in a separate list for the "real value of pi"

import support_functions as sf
from decimal import Decimal as dec


### main function
def pi_nilakantha():

    # take some user input to represent number of digits to approximate pi
    user = input('How many digits (decimals) of Pi would you like to approximate?')
    user_num = int(user)+1

    # initialize two empty lists, iteration_a and iteration_b of length equivalent to number of decimal places desired
    iteration_a = [0]*user_num
    iteration_b = [0]*user_num

    # set variables for while loop
    complete = False
    operator = True
    error = False

    # counter variable to break out if over a certain limit
    count = 0

    # first value of pi is 3
    pi = 3
    # first variable value in nikantha series
    n = 2

    # while user_num digit buckets are not selected yet, keep performing nikantha series
    while complete == False:


        # denominator of nikantha series for readability
        denom = dec(n)*dec(n+1)*dec(n+2)

        # fraction of nikantha series
        frac = dec(4) / dec(denom)

        # alternate between pos & neg elements
        if operator == True:
            # assign iteration_b to list
            pi = dec(pi) + dec(frac)
            operator = False

        # alternate between pos & neg elements
        elif operator == False:
            pi = dec(pi) - dec(frac)
            operator = True

        # add 2 for every iteration of the nikantha series
        n += 2

        # convert pi approximation to iterable list. assign this iterable list to B and move B to A
        pi_list = sf.num_to_list(pi)

        iteration_a = iteration_b
        iteration_b = pi_list

        # compare list a and list b. this is how we determine if the latest digit is done iterating or not
        result = sf.compare_list(iteration_a, iteration_b)

        # breaks out of while loop if the number of digits (selected by user) has been satisfied
        if len(result) == user_num:
            complete = True
            break

        # at end of while loop, add one to counter variable to keep track of number of iterations
        count += 1
        
        # set default maximum number of iterations to 5 million. 
        if count > 5000000:
            error = True
            print("You've exceeded the alotted number of iterations!")
            break

    ### end of while loop ###
    
    # only return results of while loop if "error" was not achieved
    if error != True:
        
        # convert list to integer
        my_pi = sf.pi_list_to_num(result)
        
        # convert integer to pi approximation using decimal library for extra accuracy!
        my_pi = dec(my_pi) / dec((10** (user_num-1)))
        
        return my_pi
    else:
        pass

    
##########################################################################
##########################################################################
##########################################################################

answer = pi_nilakantha()
print(answer)


