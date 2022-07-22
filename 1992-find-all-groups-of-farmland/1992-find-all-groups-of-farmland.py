class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        ans = []
        v = [[0]*m for i in range(n)]
        
        def dfs(i,j,d):
            if i<0 or i>=n or j<0 or j>=m or land[i][j]==0 or v[i][j]:
                return 
            v[i][j]=1
            d[0] = min(i,d[0])
            d[1] = min(j,d[1])
            d[2] = max(i,d[2])
            d[3] = max(j,d[3])
            
            dfs(i-1,j,d)
            dfs(i+1,j,d)
            dfs(i,j-1,d)
            dfs(i,j+1,d)
      
        for i in range(n):
            for j in range(m):
                if land[i][j]==1 and not v[i][j]:
                    d = [n,m,0,0]
                    dfs(i,j,d)
                    ans.append(d)
        return ans
        