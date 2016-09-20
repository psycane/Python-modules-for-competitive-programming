t=input()
while t>0:
    t-=1
    le=0
    fact=[0]*(100001)
    fact[0]=1
    m=input()
    for k in range(2,m+1):
        r=0
        arr=[0]*(100001)
        for i in range(le+1):
            arr[i]=fact[i]
        for i in range(le+1):
            fact[i]=(arr[i]*k+r)%10
            r=(arr[i]*k+r)/10
        i+=1
        if r!=0:
            while r!=0:
                fact[i]=r%10
                r/=10
                i+=1
        le=i-1
    x=((fact[:le+1])[::-1])
    for i in range(len(x)):
        x[i]=str(x[i])
    print ''.join(x)
    
