import sys
t=int(sys.stdin.readline())
for i in xrange(t):
    n,m=map(int,sys.stdin.readline().split())
    li=list(map(int,sys.stdin.readline().split()))
    temp=0
    s=[]
    maxx=-1
    for i in xrange(n):
        temp=(temp+li[i])%m
        s.append([temp,i])
        if temp>maxx:
            maxx=temp
    s.sort()
    minn=m+1
    for i in xrange(n-1):
        if s[i][1]>s[i+1][1]:
            minn=min(s[i+1][0]-s[i][0],minn)
    print max(maxx,m-minn)
