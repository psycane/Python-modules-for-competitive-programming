def combinations(iterable, r):
    temp=[]
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    temp.append( tuple(pool[i] for i in indices))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return temp
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        temp.append(tuple(pool[i] for i in indices))
        
# combinations(li,k) will print all tuples of length k from the list li
li=[1,2,3,4,5]
print combinations(li,3)
