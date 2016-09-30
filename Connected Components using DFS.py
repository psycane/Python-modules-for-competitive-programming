def connected_components(graph,n):
    visited=[False]*n
    ans=[]
    for i in graph:
        if visited[i-1]==False:
            ans.append(dfs(graph,i,visited,[]))
    return ans

def dfs(graph,v,visited,ans):
    visited[v-1]=True
    ans.append(v)
    for i in graph[v]:
        if visited[i-1]==False:
            dfs(graph,i,visited,ans)
    return ans

graph={1: [2, 3], 2: [1, 3], 3: [2, 1], 4: [5], 5: [4, 6], 6: [5, 7], 7: [6]}
n=7
print connected_components(graph,n)
