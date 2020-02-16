#https://stackoverflow.com/questions/58709213/how-do-i-add-aitken-sequence-in-my-root-finding-algorithm

import numpy as np
from numpy import log as ln
                 
def g(x):
    return ln(4+x-x**2)

def FixedPoint(p0,tolerance):                     
    p = g(p0)                                
    abs_error = abs(p-p0)                    
    p0 = p                          
    while abs_error>=tolerance:                 
        p = g(p0)                                
        abs_error = abs(p-p0)                    
        p0 = p                                   
    return p

starting_point = 2
tolerance = 10**-10
fixed_point = FixedPoint(starting_point,tolerance)


def FixedPointAitken(p0,tolerance):                     
    while True:                 
        p1=g(p0); p2=g(p1);   
        print(p0,p1,p2)
        if abs(p1-p0)<tolerance: break
        p0 = p0 - (p1-p0)**2/(p0+p2-2*p1) 
    return p0
