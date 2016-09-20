
#fastest and calculates prime number below  n 
def primes_sieve_best(n):
    sieve=[True]*n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
def prime_biggy(n):
    biggy=[1]*(n+1)
    for i in xrange(2,int(n**0.5) + 1):
        if biggy[i]==1:
            j=2
            while j*i<=n:
                if biggy[j*i]==1:
                    biggy[j*i]=0
                j+=1
    biggy2=[]
    for i in range(2,n+1):
        if biggy[i]==1:
            biggy2.append(i) 
    return biggy2
print len(prime_biggy(1000000))
'''
# from m to n
def main(m, n):
    primes = [False for x in xrange(n-m+1)]
    p = 2
    while p*p <= n:
        r = m / p
        r *= p
        for j in xrange(r, n+1, p):
            if j != p and j >= m:
                primes[j-m] = True
        p += 1
 
    for i in xrange(n-m+1):
        if not primes[i] and m+i != 1:
            print m + i
 
 
if __name__ == "__main__":
    t = int(raw_input()) ## nb of test cases
 
    for k in xrange(t):
        m, n = map(int, raw_input().split())
        main(m, n)
        if k < t-1:
            print ""
'''
