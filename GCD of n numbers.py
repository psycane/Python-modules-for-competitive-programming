from fractions import gcd
import sys
li=list(map(int,sys.stdin.readline().split()))
print reduce(gcd,li)
