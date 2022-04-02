#'fixed-pt algorithm
import math
from random import *
def g(x):
    y=0.5*(x+3/x) #function 
    return y
a=1;b=2 #범위 [a,b]
i=1 ; p=1
N0=5 # 횟수
TOL=10**(-4) #Tolerance
y1=[]
p2=[]

#main code
while i<=N0:
    p1=g(p)
    p2.append(p)
    y1.append(p1)
    if abs(p1-p)<TOL:
        print('Pn값 : ',p)
        break
    i+=1
    p=p1
print('횟수(Pn의 n값) : ',i)