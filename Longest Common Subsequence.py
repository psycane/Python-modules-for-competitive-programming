def lcs(s1,s2):
    len_s1=len(s1)
    len_s2=len(s2)
    dp=[[0 for i in xrange(len_s2+1)] for i in xrange(len_s1+1)]
    ans=''
    for i in xrange(1,len_s1+1):
        for j in xrange(1,len_s2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]+=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    while len_s1!=0 and len_s2!=0:
        if dp[len_s1][len_s2]==dp[len_s1-1][len_s2]:
            len_s1-=1
        elif dp[len_s1][len_s2]==dp[len_s1][len_s2-1]:
            len_s2-=1
        else:
            if s1[len_s1-1]==s2[len_s2-1]:
                ans=s1[len_s1-1]+ans
                len_s1-=1
                len_s2-=1
    return (ans,dp[i][j])

print lcs("teacher","cheater")
        
