M=2
V=3
a=[0.4,1]
t=[1,2]

def calc_x(V,M,a,t):
    x=[1]*(V+1)
    for n in range(1,V+1):
        sum=0
        for i in range(0,M):
            if n>=t[i]:
                sum += a[i]*t[i]*x[n-t[i]]
        x[n]=sum/n
    return x

def calc_p0(x):
  sum=0
  for n in range(0,V+1):
    sum+=x[n]
  return 1/sum

def calc_pn(X,V,M,a,t):
    P=[1]*(V+1)
    P[0]=calc_p0(X)
    for i in range(1,V+1):

        P[i]=(P[0]*X[i])
    return P

def calc_bn(P,V,t,i):
    sum=0
    for n in range(V-t[i-1]+1,V+1):
        sum+=P[n]

    return sum

def calc_all(V,t,a,M):
    X=calc_x(V,M,a,t)
    print(X)
    calc_p0(X)
    P=calc_pn(X,V,M,a,t)
    print(P)
    for n in range(1,M+1):
        print(calc_bn(P,V,t,n))
    
calc_all(V,t,a,M)
