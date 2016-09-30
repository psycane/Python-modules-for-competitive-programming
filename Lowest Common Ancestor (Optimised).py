class RangeMin:
    def __init__(self,X):
        self._data = list(X)
        if len(X) > 1:
            big = map(max, self._ansv(False), self._ansv(True))
            parents = dict([(i,big[i][1]) for i in range(len(X)) if big[i]])
            self._lca = LCA(parents)
        
    def __getslice__(self,left,right):
        right = min(right, len(self._data)) 
        if right <= left:
            return None 
        return self._data[self._lca(left,right-1)]
    
    def __len__(self):
        return len(self._data)

    def _ansv(self,reversed):
        stack = [None] 
        output = [0]*len(self._data)
        for xi in _pairs(self._data,reversed):
            while stack[-1] > xi:
                stack.pop()
            output[xi[1]] = stack[-1]
            stack.append(xi)
        return output
        
    def _lca(self,first,last):
        return 0

class LCA:
    def __init__(self,parent):
        children = {}
        for x in parent:
            children.setdefault(parent[x],[]).append(x)
        root = [x for x in children if x not in parent]
        levels = []
        self._representatives = {}
        self._visit(children,levels,root[0],0)
        self._rangemin = _RestrictedRangeMin(levels)
            
    def __call__(self,*nodes):
        r = [self._representatives[x] for x in nodes]
        return self._rangemin[min(r):max(r)+1][1]

    def _visit(self,children,levels,node,level):
        self._representatives[node] = len(levels)
        pair = (level,node)
        levels.append(pair)
        for child in children.get(node,[]):
            self._visit(children,levels,child,level+1)
            levels.append(pair)

class _RestrictedRangeMin:
    def __init__(self,X):
        self._blocksize = _log2(len(X))//2
        self._blockmask = (1 << self._blocksize) - 1
        blocklen = 1 << self._blocksize
        blocks = []           
        ids = {} 
        blockmin = [] 
        self._prefix = [None]
        self._suffix = []
        for i in range(0,len(X),blocklen):
            XX = X[i:i+blocklen]
            blockmin.append(min(XX))
            self._prefix += _PrefixMinima(XX)
            self._suffix += _PrefixMinima(XX,reversed=True)
            id = len(XX) < blocklen and -1 or self._blockid(XX)
            blocks.append(id)
            if id not in ids:
                ids[id] = PrecomputedRangeMin(_pairs(XX))
        self._blocks = [ids[b] for b in blocks]
        self._blockrange = LogarithmicRangeMin(blockmin)
        self._data = list(X)

    def __getslice__(self,left,right):
        firstblock = left >> self._blocksize
        lastblock = (right - 1) >> self._blocksize
        if firstblock == lastblock:
            i = left & self._blockmask
            position = self._blocks[firstblock][i:i+right-left][1]
            return self._data[position + (firstblock << self._blocksize)]
        else:
            best = min(self._suffix[left], self._prefix[right])
            if lastblock > firstblock + 1:
                best = min(best, self._blockrange[firstblock+1:lastblock])
            return best

    def _blockid(self,XX):
        id = 0
        for i in range(1,len(XX)):
            id = id*2 + (XX[i] > XX[i-1])
        return id

class PrecomputedRangeMin:

    def __init__(self,X):
        self._minima = [_PrefixMinima(X[i:]) for i in range(len(X))]
    
    def __getslice__(self,x,y):
        return self._minima[x][y-x-1]
        
    def __len__(self):
        return len(self._minima)
        
class LogarithmicRangeMin:
    
    def __init__(self,X):
        self._minima = m = [list(X)]
        for j in range(_log2(len(X))):
            m.append(map(min, m[-1], m[-1][1<<j:]))

    def __getslice__(self,x,y):
        j = _logtable[y-x]
        row = self._minima[j]
        return min(row[x],row[y-2**j])
        
    def __len__(self):
        return len(self._minima[0])

def _PrefixMinima(X,reversed=False):
    current = None
    output = [None]*len(X)
    for x,i in _pairs(X,reversed):
        if current is None:
            current = x
        else:
            current = min(current,x)
        output[i] = current
    return output

def _pairs(X,reversed=False):
    indices = range(len(X))
    if reversed:
        indices.reverse()
    return [(X[i],i) for i in indices]

_logtable = [None,0]
def _log2(n):
    while len(_logtable) <= n:
        _logtable.extend([1+_logtable[-1]]*len(_logtable))
    return _logtable[n]


'''TREE LOOK LIKE THIS:
      1
      | 
      2
     / \
    3   4
        |
        5
'''
tree={2: 1, 3: 2, 4: 2, 5: 4}
pre_lca=LCA(tree)
print pre_lca(2,3)
print pre_lca(5,3)
