class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        n = len(dp)
        m = len(dp[0])
        if dp[n-1][m-1]==1 or dp[0][0]==1:
            return 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if dp[i][j]==1:
                    dp[i][j]=-1
                    
        for i in range(n-1,-1,-1):
            if dp[i][m-1]==-1:
                break
            else:
                dp[i][m-1]=1
        
        for i in range(m-1,-1,-1):
            if dp[n-1][i]==-1:
                break
            else:
                dp[n-1][i]=1
        
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                if dp[i][j]!=-1:
                    if dp[i][j+1]!=-1 and dp[i+1][j]!=-1:
                        dp[i][j]=dp[i+1][j] + dp[i][j+1]
                    elif dp[i][j+1]!=-1 and dp[i+1][j]==-1:
                        dp[i][j] = dp[i][j+1]
                    elif dp[i][j+1]==-1 and dp[i+1][j]!=-1:
                        dp[i][j] = dp[i+1][j]
        return dp[0][0]