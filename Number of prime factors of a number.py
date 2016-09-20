def pf(n):
    primfac={}
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            try:
                primfac[d]+=1
            except:
                primfac[d]=1
            n //= d
        d += 1
    if n > 1:
       primfac[n]=1
    return primfac

n=input()
print pf(n)
