L = 10**6
# sieve of Eratosthenes
primes = []
is_prime = [False]*2 + [True]*(L-1)
for p in xrange(2,L+1):
    if is_prime[p]:
        primes.append(p)
        for n in xrange(2*p,L+1,p):
            is_prime[n] = False
# calculate Euler's totient function
phi = [0]*(L+1)
for n in xrange(1,L+1):
    phi[n] = n
for p in primes:
    for n in xrange(p,L+1,p):
        phi[n] -= phi[n]/p
t=input()
while t>0:
    t-=1
    a,b,x=map(int,raw_input().split())
    if b<0:
        ans=pow(a,phi[x]-1,x)
        print pow(ans,-b,x)
    else:
        print pow(a,b,x)

