from sys import stdin as ip
aa,bb=500,500
n=int(ip.readline())
li=[]
ans=-1
for i in xrange(n):
    k=int(ip.readline())
    li.append(k)

li.sort(reverse=True)
k=li[0]
for i in li:
    if i!=k:
        print i
        break
else:
    print 0
