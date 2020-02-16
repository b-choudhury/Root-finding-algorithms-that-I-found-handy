import numpy as np

a=1.0
b=2.0
eps = b-a
tol = 0.000001


def f(x):
   res = np.log(x)-np.cos(x)
   return res


while eps>tol:
     m = (a+b)/2
     fnctn = f(m)
     if fnctn<0:
        a = m
     else:
        b = m
     eps = b-a

p0 = b

def BisectAitkins(p0,tolerance):
    while True:
        p1=f(p0); p2=f(p1);
        if abs(p1-p0)<tolerance: break
        p0 = p0 - (p1-p0)**2/(p0+p2-2*p1)
    return p0       
