def lcsd(x,y):
    m=len(x)
    n=len(y)
    global c
    c=[]
    for j in range(n+1):
        c.append([['@']]*(m+1))
    for i in range(1,m+1):
        
        for j in range(1,n+1):
            if x[i-1]==y[j-1] :
                c[j][i]=list(c[j-1][i-1])
                c[j][i].append((x[i-1]))
      
            else:
                if len(c[j-1][i])>=len(c[j][i-1]):
                    c[j][i]=list(c[j-1][i])
                else:
                    c[j][i]=list(c[j][i-1])           
    return c[n][m]
    
a=list(map(int,raw_input().split()))
b=list(map(int,raw_input().split()))
m=lcsd(a,b)
for i in m:
    if(i!='@'):
        print i,

