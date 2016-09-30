import heapq
def subarray_max(li,n,k):
    ans=[]
    heap=[]
    for i in xrange(k):
        while heap!=[] and li[i]>=li[heap[-1]]:
            heap.pop()
        heapq.heappush(heap,i)
    for i in xrange(k,n):
        ans.append(li[heap[0]])
        while heap!=[] and heap[0]<=i-k:
            heap.pop(0)
        while heap!=[] and li[i]>=li[heap[-1]]:
            heap.pop()
        heapq.heappush(heap,i)
    ans.append(li[heap[0]])
    return ans
n,k=6,3
li=[5,1,4,2,3,9]
print subarray_max(li,n,k)

    
