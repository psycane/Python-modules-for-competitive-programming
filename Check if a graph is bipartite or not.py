# When graph is in dictionary form:
def isBipartite(graph,n):
    color=[-1 for _ in xrange(n)]
    for i in xrange(n):
        if color[i]!=-1:
            continue
        queue=[i]
        color[i]=1
        while queue:
            u=queue.pop(0)
            for v in graph[u]:
                if color[v]==-1:
                    color[v]=1-color[u]
                elif color[v]==color[u]:
                    return False
    return True

# When graph is in adjacency matrix form:
def isBipartite2(graph,n):
    color=[-1 for _ in xrange(n)]
    for i in xrange(n):
        if color[i]!=-1:
            continue
        queue=[i]
        color[i]=1
        while queue:
            u=queue.pop(0)
            for v in xrange(n):
                if graph[u][v] and color[v]==-1:
                    color[v]=1-color[u]
                    queue.append(v)
                elif graph[u][v] and color[v]==color[u]:
                    return False
    return True


graph={0:[1,3],1:[0,2],2:[1,3],3:[0,2]}
n=4
print isBipartite(graph,n)

graph=[[0,1,0,1],
       [1,0,1,0],
       [0,1,0,1],
       [1,0,1,0]]
print isBipartite2(graph,n)
