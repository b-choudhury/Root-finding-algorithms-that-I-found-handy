import numpy as np

tol = 0.001
cond = True
x0 = 1.29
x=[x0]

def f(x):
    res = np.log(x)-np.cos(x)
    return res

def der(x):
    res = (1/x)+np.sin(x)
    return res

while cond:
    y=x[-1]-(f(x[-1])/der(x[-1]))
    x.append(y)
    if abs(x[len(x)-1]-x[len(x)-2])>tol:
       cond=True 
    else:
       cond=False

root = x[-1]

