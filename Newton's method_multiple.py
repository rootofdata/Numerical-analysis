import math
from scipy.misc import derivative #미분값 구하기.
i=1

def f(x):  #define function
    result=x**2-2*x*math.exp(-x)+math.exp(-2*x)
    return result

def f1(x): #setting f'(x) 
    result=2*x-2*math.exp(-2*x)+2*x*math.exp(-x)-2*math.exp(-2*x)
    return result
def f2(x): #setting f''(x)
    result=2+4*math.exp(-x)-2*x*math.exp(-x)+4*math.exp(-2*x)
    return result

def g(x): #setting g(x) with f,f',f''
    result=x-((f(x)*f1(x))/(f1(x)**2-f(x)*f2(x)))
    return result
TOL=10**(-5)
p0=0
p1=1 #initial setting
  
q0=f(p0)
q1=f(p1)
while True:
    p=g(p0)
    if abs(p-p1)<TOL :
        print(p)
        break
    else:
        i+=1
        p0=p1
        q0=q1
        p1=p
        q1=f(p)
print(i)