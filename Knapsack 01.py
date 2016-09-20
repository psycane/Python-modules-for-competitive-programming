def knapsack01(weight,value,max_weight):
    n=len(value)
    dp=[[0 for i in xrange(max_weight+1)] for j in xrange(n+1)]
    for i in xrange(1,n+1):
        for j in xrange(1,max_weight+1):
            if j<weight[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(value[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
    return dp[i][j]

weight=[1,2,3,2,2]
value=[8,4,0,5,3]
max_weight=4
print knapsack01(weight,value,max_weight)
