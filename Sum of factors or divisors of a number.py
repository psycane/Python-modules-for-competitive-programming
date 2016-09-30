def pf(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def sof(n):
    li=pf(n)
    k=li[0]
    i=0
    ct=0
    s=1
    while i<len(li):
        if li[i]==k:
            ct+=1
            i+=1
        else:
            s*=(k**(ct+1)-1)/(k-1)
            k=li[i]
            ct=0
    s*=(k**(ct+1)-1)/(k-1)
    return s

n=input()
print sof(n)
