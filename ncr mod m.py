""" Works only if 'm' is prime """
def mod_inv(n,m):
    n=n%m
    return pow(n,m-2,m)
def nCr(n,r,m):
    numerator=1
    for i in xrange(r):
        numerator=(numerator*(n-i))%m
    denomenator=1
    for i in xrange(2,r+1):
        denomenator=(denomenator*i)%m
    return (numerator*mod_inv(denomenator,m))%m
mod=10**9+7
print nCr(10000,500,mod)
