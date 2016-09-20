import heapq
n,k=map(int,raw_input().split())
li=list(map(int,raw_input().split()))
heap=[]
for i in xrange(k):
    while heap!=[] and li[i]>=li[heap[-1]]:
        heap.pop()
    heapq.heappush(heap,i)
for i in xrange(k,n):
    print li[heap[0]]
    while heap!=[] and heap[0]<=i-k:
        heap.pop(0)
    while heap!=[] and li[i]>=li[heap[-1]]:
        heap.pop()
    heapq.heappush(heap,i)
print li[heap[0]]


    
