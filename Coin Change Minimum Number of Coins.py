def min_coins(coins,total):
    len_coins=len(coins)
    dp=[[0 if i==0 else float("inf") for i in xrange(total+1)] for _ in xrange(len_coins)]
    for i in xrange(len_coins):
        for j in xrange(1,total+1):
            if j>=coins[i]:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
coins=[1,5,6,8]
total=11
print min_coins(coins,total)
