def bfs(graph, start, path=[]):
    '''iterative breadth first search from start'''
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path=path+[v]
            q=q+graph[v]
    return path

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print bfs(graph,'A')
