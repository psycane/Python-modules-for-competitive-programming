def subset_sum(li,total):
    l=len(li)
    dp=[[False for _ in xrange(total+1)] for _ in xrange(l+1)]
    for i in xrange(l+1):
        dp[i][0]=True
    for i in xrange(1,l+1):
        for j in xrange(1,total+1):
            if li[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-li[i-1]]
    return dp[-1][-1]

A=[3,34,4,12,5,2,124,421,412,125,1325,35,3,351,35,351,35,12312,1242142]
s=8
print subset_sum(A,s)
