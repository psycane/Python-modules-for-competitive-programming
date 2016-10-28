def getsum(BITTree,i):
    s = 0
    i = i+1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

def updatebit(BITTree , n , i ,v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)
        
def construct(arr, n):
    BITTree = [0]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = construct(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5)))
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6)
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5)))
