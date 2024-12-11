# The primitive_roots module containing the functions:  
# is_sg_prime, is_prime_root_safe

from miller_rabin import is_prime

def is_sg_prime(n): 
    '''
    Boolean function (so returns True or False) which, on 
    input n tests whether n is a Saint Germain prime, i.e. 
    whether or not both n and 2*n + 1 are prime. 
    '''
    if is_prime(n): 
        if is_prime(2*n + 1): 
            return True 
    return False 

  
def is_prim_root_safe(b,p):
    '''
    Boolean function (so returns True or False) which, given 
    as input (b,p) with p a safe prime and b a positive integer
    tests whether b is a primitive root modulo p. If p is not 
    a safe prime 'Input is inconsistent' is printed and returned. 
    '''
    # Test for bad input to start with
    ic_message = 'Input is inconsistent'
    q = (p-1)//2 
    if not p % 2 == 1 or not is_sg_prime(q): 
        print(ic_message)
        return ic_message
    
    # Main part of the function (only 4 steps!)
    exponents = [1,2,q,2*q]
    for e in exponents:   
        # Remember that pow(b,e,p) is the built in python function that 
        # computes b**e % p efficiently 
        if pow(b,e,p) == 1: 
            return e == 2*q
    
    # The function will never get this far. 
    # So the last return would be redundant  
    # return None 
    ### END SOLUTION
    

