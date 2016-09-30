def factors(n):    
    l1, l2 = [], []
    for i in range(1, int(n ** 0.5) + 1):
        q,r = n/i, n%i     
        if r == 0:
            l1.append(i) 
            l2.append(q)    
    if l1[-1] == l2[-1]:
        l1.pop()
    l2.reverse()
    return l1 + l2

n=128
print factors(n)
