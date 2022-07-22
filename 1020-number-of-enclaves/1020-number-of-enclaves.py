class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j,v):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or v[i][j]:
                return
            
            v[i][j]=1
            one_count[0]-=1
            dfs(i-1,j,v)
            dfs(i+1,j,v)
            dfs(i,j-1,v)
            dfs(i,j+1,v)
        
        n = len(grid)
        m = len(grid[0])
       
        v = [[0]*m for i in range(n)]
        one_count = [0]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    one_count[0]+=1 
                    
        for i in range(m):
            if grid[0][i]==1 and v[0][i]!=1:
                dfs(0,i,v)
                
        for i in range(m):
            if grid[n-1][i]==1 and v[n-1][i]!=1:
                dfs(n-1,i,v)
                
        for j in range(n):
            if grid[j][0]==1 and v[j][0]!=1:
                dfs(j,0,v)
        
        for j in range(n):
            if grid[j][m-1]==1 and v[j][m-1]!=1:
                dfs(j,m-1,v)
               
        return one_count[0]