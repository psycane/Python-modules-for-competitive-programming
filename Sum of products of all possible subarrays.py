from itertools import izip, chain

l = [2]*10000
x = [1]    
for i in l:
    x = [a + b*i for a,b in izip(chain([0],x), chain(x,[0]))]
print x[2]%(10**9+7)
