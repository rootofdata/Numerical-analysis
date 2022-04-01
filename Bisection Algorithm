#bisection algorithm
#initial value
def f(x):
    y=x**3+4*x**2-10 #function
    return y
a=1;b=2  #범위 [a,b]
fa=f(a); fb=f(b)
TOL=10**(-4) #Tolerance

tot=0
p1=[]
y1=[]
while True:
    p=a+(b-a)/2
    tot+=1
    fp=f(p)
    y1.append(fp)
    p1.append(p)
    if fp==0 or (b-a)/2<TOL:
        print('횟수(Pn의 n값)',tot)
        print(p)
        break
    if fa*fp>0:
        a=p
    else: b=p