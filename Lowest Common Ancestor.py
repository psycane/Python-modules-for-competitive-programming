def min_set_ancestor(tree, childrens):
    m = min(childrens)
    result = []
    for node in childrens:
        if node != m and node in tree:
            result.append(tree[node])
    result.append(m)
    result = list(set(result))
    return result
 
n = int(raw_input().strip())
data = raw_input().strip()
n1 = int(raw_input().strip())
nodes = raw_input().strip()
node_data = [int(d.strip()) for d in data.split(' ')]
childrens = [int(d.strip()) for d in nodes.split(' ')]
 
tree_data = {i : node_data[i-1] for i in range(1, len(node_data)+1)}
 
print tree_data
while len(childrens) > 1:
    childrens = min_set_ancestor(tree_data, childrens)
 
print childrens[0]

'''Test Input:

           0
         /   \
        1      2
     /  |  \     \
    3   4   5     6
    /   / \
    7   8 9

10
0 0 1 1 1 2 3 4 4
3
7 8 9
'''
