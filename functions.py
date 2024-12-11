#!/usr/bin/env python
# coding: utf-8

# In[7]:





# In[2]:


def miller_rabin2(p,base): 
    '''
    Partially tests whether p is prime using the given base.
    Uses the ROO and FLT tests combined with Pingalas algorithm. 
    If False is output then  p is definitely not prime. 
    It True is output then p MIGHT be prime. 
    This test is far from perfect.
    '''
    
    n = 1
    exponent = p-1
    modulus = p
    bin_string = bin(exponent)[2:]        # Get 'exponent' in binary without the first '0b'
    
    for bit in bin_string:               # Iterate through the '0' and '1' of binstring
        n_squared = n * n % modulus      # We need this below
        
        if  n_squared == 1:              # Case when n * n = 1 mod p. 
            if (n != 1) and (n != p-1):  # Case when is neither 1 nor -1 mod p
                return False             # So ROO violated and False is output
        
        if bit == '1': 
            n = (n_squared * base) % modulus
        if bit == '0':
            n = n_squared 
    
    if n != 1:                          # I.e. base**(p-1) not = 1 mod p
        return False                    # FLT violated in this case and False is output

    return True                         # No FLT or ROO violation. p might be prime. 

from random import randint

def is_prime(p,num_wit=50): 
    ''' 
    Tests whether a positive integer p is prime.
    For p <= 37 p is prime iff p is in [2,3,5,7,11,13,17,19,23,29,31,37].
    For p > 37, if p is even then it is not prime, otherwise... 
    For p <= 2^64 the Miller-Rabin test is applied using the witnesses 
    in [2,3,5,7,11,13,17,19,23,29,31,37].
    For p > 2^64 the Miller-Rabin test is applied using 
    num_wit many randomly chosen witnesses. 
    '''
 
    # We need a direct test on numbers {0,1,...,37} 
    first_primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    if p < 38:
        return p in first_primes
    
    # If p is even and greater than 37 then p is not prime.  
    if p % 2 == 0: 
        return False

    # For 37 < p <= 2**64 we apply the miller_rabin test 
    # using as witnesess the prime numbers in first_primes
    if p <= 2**64: 
        verdict = True 
        for witness in first_primes: 
            if miller_rabin(p,witness) == False:
                return False
        return True      
    
    # For p > 2**64 we apply the miller_rabin test using
    # a sample of wit_num many randomly chosen witnesses
    else: 
        num_trials = 0
        while num_trials < num_wit: 
            num_trials = num_trials + 1
            witness = randint(2,p-2)
            if miller_rabin(p,witness) == False: 
                return False
        return True


# In[3]:


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
    


# In[4]:



def gcd(a,b):
    """Returns the greatest common divisor of integers a and b using Euclid's algorithm.
    The order of a and b does not matter and nor do the signs."""
    if not(a%1 ==0 and b%1==0):
        return "Need to use integers for gcd."
    if b==0:
        return abs(a)                           #Use abs to ensure this is positive
    else:
        return gcd(b,a%b)
    
    
    
def gcd_ext(a,b):
    """Wish to output (gcd,x,y) such that gcd=ax+by."""
    if not(a%1 ==0 and b%1==0):                         #Reject if trying to use for non-integers
        return "Need to use integers for gcd."          
    if a == 0:                                          #Base case is when a=0.
        return (abs(b), 0, abs(b)//b)                   #Then gcd =|b| and is 0*a+1*b or 0*a-1*b. Use abs(b)//b
    else:
        quot=b//a                                       #The rule is that g=gcd(a,b)=gcd(b%a,a).
                                                        #Let b=qa+r where r=b%a
        g, x, y = gcd_ext(b%a, a)                       #And if  g=x1*r + y1*a then since r=b-qa
        return (g, y - quot * x, x)                     #We get g = a*(y1-q*x1)+x1*b.
                                                        #So x=y1-q*x1 and y=x1.


# In[5]:



def decompose(n):
    """Generates a dictionary representing the prime decomposition."""
    factors={}
    current_number=n                            #divide current_number by the factors found until it reaches 1
    while current_number > 1:
        p=smallest_factor(current_number)
        if p in factors.keys():                 #if p is not a new factor, increase the power
            factors[p]+=1
        else:
            factors[p]=1                        #if p is a new factor, create a new entry
        current_number = current_number//p
    return factors


# In[ ]:





# In[ ]:




