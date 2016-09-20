def lcsd(x,y):
    m=len(x)
    n=len(y)
    global c
    c=[]
    for j in range(n+1):
        c.append([0]*(m+1))
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1] :
                c[j][i]=str(c[j-1][i-1])+str(x[i-1])
                
            else:
                c[j][i]=max(str(c[j-1][i]),str(c[j][i-1]))
                
    return c[n][m]
    



a=raw_input()
b=raw_input()
m=lcsd(a,b)
ff=m.replace('0','')
print ff,len(ff)
