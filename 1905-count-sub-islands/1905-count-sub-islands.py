class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid: List[List[int]]) -> int:
        def dfs(i,j,v):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]== 0 or v[i][j]:
                return
          
            v[i][j]=1
            dfs(i-1,j,v)
            dfs(i+1,j,v)
            dfs(i,j-1,v)
            dfs(i,j+1,v)
             
        n = len(grid)
        m = len(grid[0])
        count = 0
        v = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and grid1[i][j] != 1 and v[i][j]!=1:
                    dfs(i,j,v) 
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and v[i][j]!=1:
                    count+=1
                    dfs(i,j,v)
                    
        return count