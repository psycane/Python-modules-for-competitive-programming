def primes_sieve(n):
    sieve=[True]*n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
t=input()
for ii in range(t):
    n=input()   
    primes=primes_sieve(n+1)
    ways=[0 for i in range(n+1)]
    ways[0]=1
    for i in range(len(primes)):
        for j in range(primes[i],n+1):
            ways[j]+=ways[j-primes[i]]
    print ways[n]
