def gcd(x,y):
    while(y!=0):
        temp=x%y
        x=y
        y=temp
    return x
def gcd_n(l):
    if(len(l)>=2):
        x=gcd(l[0],l[1])
        for i in range(2,len(l)):
            x=gcd(x,l[i])
        return x
    else:
        return l[0]
'''l=list(map(int,raw_input().split()))
print gcd_n(l)
'''
