def preprocess(li,aux,n,m):
    for i in xrange(m):
        aux[0][i]=li[0][i]
    for i in xrange(1,n):
        for j in xrange(m):
            aux[i][j]=li[i][j]+aux[i-1][j]
    for i in xrange(n):
        for j in xrange(1,m):
            aux[i][j]+=aux[i][j-1]
    return aux

def calculateSum(li,lj,ri,rj):
    res=aux[ri][rj]
    if li>0:
        res-=aux[li-1][rj]
    if lj>0:
        res-=aux[ri][lj-1]
    if li>0 and lj>0:
        res+=aux[li-1][lj-1]
    return res

aux,li=[],[]
li=[[1, 2, 3, 4, 6],
    [5, 3, 8, 1, 2],
    [4, 6, 7, 5, 5],
    [2, 4, 8, 9, 4]]
n,m=4,5
aux=[[0 for i in xrange(m)] for i in xrange(n)]
aux=preprocess(li,aux,n,m)
print calculateSum(0,0,1,1)

