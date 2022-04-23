#Secant Method
import math
i=2
def f(x):
    result=math.exp(x)+2**(-x)+2*math.cos(x)-6 #function
    return result

TOL=10**(-5)
p0=1
p1=2  #initial setting

q0=f(p0)
q1=f(p1)
while True:
    p=p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
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