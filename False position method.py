#False position method
from numpy import log as ln
def f(x):  #define f(x)
    result=math.exp(6*x)+3*(ln(2)**2)*math.exp(2*x)-ln(8)*math.exp(4*x)-(ln(2))**3
    return result
def f1(x): #define f'(x)
    result=6*math.exp(6*x)+6*(ln(2)**2)*math.exp(2*x)-4*ln(8)*math.exp(4*x)
    return result
TOL=10**(-4)*2 #set initial
p0=0
i=0
while 5: #main
    p=p0-f(p0)/f1(p0)
    if abs(p-p0)<TOL:
        print(p)
    i+=1
    p0=p
print(i)