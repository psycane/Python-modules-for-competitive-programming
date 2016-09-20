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
