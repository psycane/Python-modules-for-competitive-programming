from sys import stdin as ip
from bisect import bisect_left as bl
from bisect import bisect_right as br
aa,bb=500,500
n=int(ip.readline())
li=list(map(int,ip.readline().split()))
q=int(ip.readline())
li.sort()
for i in xrange(q):
    a,b=map(int,ip.readline().split())
    i1= br(li,b)
    i2= bl(li,a)
    print i1-i2
