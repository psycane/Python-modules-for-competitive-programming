def max_subarray_sum_mod_m(li,n,m):
    temp=0
    s=[]
    maxx=-1
    for i in xrange(n):
        temp=(temp+li[i])%m
        s.append([temp,i])
        if temp>maxx:
            maxx=temp
    s.sort()
    minn=m+1
    for i in xrange(n-1):
        if s[i][1]>s[i+1][1]:
            minn=min(s[i+1][0]-s[i][0],minn)
    return max(maxx,m-minn)

print max_subarray_sum_mod_m([10,15,23,28,30],5,6)
