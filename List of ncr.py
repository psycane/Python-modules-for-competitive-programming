li=[]
for i in xrange(1,(10**1)+3):
    li.append([0]*(i))
li[0][0]=1
def ncr(n,r):
    if n==r:
        li[n][r]=1
        return li[n][r]
    if r==0:
        li[n][r]=1
        return li[n][r]
    if r==1:
        li[n][r]=n
        return li[n][r]
    if li[n][r]:
        return li[n][r]
    li[n][r]=ncr(n-1,r)+ncr(n-1,r-1)
    return li[n][r]

ncr(10,10)
print li
for i in xrange(1,(10**1)):
    for j in xrange(0,i+1):
        li[i][j]=ncr(i+1,j+1)
print li
