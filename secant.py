import numpy as np
tol = 0.000000001

x0=1.10

x1=1.29

def f(x):
   res = np.log(x)-np.cos(x)
   return res

y0 = f(x0)
y1 = f(x1)


while abs(y1)>tol:
    x = x1-y1*((x1-x0)/(y1-y0))
    y = f(x)
    x0=x1
    x1=x
    y0=y1
    y1=y
