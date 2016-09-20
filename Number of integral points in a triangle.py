#PICK'S THEOREM

from fractions import gcd
from math import ceil
import sys
t=int(sys.stdin.readline())
for i in xrange(t):
    x1,y1,x2,y2,x3,y3=map(int,sys.stdin.readline().split())
    a = abs(((x1-x2)*(y1+y2) + (x2-x3)*(y2+y3) + (x3-x1)*(y3+y1)))
    g1=gcd(abs(x1-x2), abs(y1-y2))
    g2=gcd(abs(x2-x3), abs(y2-y3))
    g3=gcd(abs(x3-x1), abs(y3-y1))
    i = a + 2 - (g1+g2+g3)
    print i/2
