import numpy as np

x0=8.0
x1=9.0
x2=-10.0
tol = 0.0010
max_iter = 200

def f(x):
    res = np.sin(x)/x
    return res


h1 = x1-x0
h2 = x2-x1

delta1= (f(x1)-f(x0))/h1
delta2 = (f(x2)-f(x1))/h2
d = (delta1-delta2)/(h1+h2)
i = 2

while i<=max_iter:
    b = delta2+h2*d
    D=abs(b**2-4*f(x2)*d)**(0.5)
    if abs(b-D)<abs(b+D):
       E=b+D
    else:
       E=b-D
    h = -2*(f(x2)/E)
    p = x2+h
    if abs(h)<tol:
       print p
       break
    x0=x1
    x1=x2
    x2=p
    h1=x1-x0
    h2=x2-x1
    i=i+1
else:
    print "Root not found"
     
