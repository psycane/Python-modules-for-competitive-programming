def findMin(key,mstSet,n):
    m=float("inf")
    for v in xrange(n):
        if not mstSet[v] and key[v]<m:
            m,ind=key[v],v
    return ind

def primsMST(graph,n):
    parent=[-1]*n
    key=[float("inf")]*n
    mstSet=[False]*n

    key[0]=0

    for ct in xrange(n-1):
        u=findMin(key,mstSet,n)
        mstSet[u]=True
        for v in xrange(n):
            if graph[u][v] and not mstSet[v] and graph[u][v]<key[v]:
                parent[v],key[v]=u,graph[u][v]
    return parent    

n=5
graph=[[0, 2, 0, 6, 0],
       [2, 0, 3, 8, 5],
       [0, 3, 0, 0, 7],
       [6, 8, 0, 0, 9],
       [0, 5, 7, 9, 0]]

mst=primsMST(graph,n)
for i in xrange(n):
    print "Parent of {} = {}".format(i,mst[i])
