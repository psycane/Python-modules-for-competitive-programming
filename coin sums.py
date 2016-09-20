l=[1,2,5,10,20,50,100,200]
t=input()
while t:
    t-=1
    n=input()
    w=[]
    for i in range(n+1):
        if i==0:
            w.append(1)
        else:
            w.append(0)
    for i in range(len(l)):
        x=l[i]
        for j in range(x,n+1):
            w[j]+=w[j-x]
    print w[n]
