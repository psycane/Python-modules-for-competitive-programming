def connected_components(graph):
    seen = set()
    def dfs(v):
        vs = set([v])
        component=[]
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
        return component
    ans=[]
    for v in graph:
        if v not in seen:
            d=dfs(v)
            ans.append(d)
    return ans

graph={1: [2, 3], 2: [1, 3], 3: [2, 1], 4: [5], 5: [4, 6], 6: [5, 7], 7: [6]}
n=7
print connected_components(graph)
