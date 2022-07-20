class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        v = [[0]*m for i in range(n)]
        
        def dfs(i,j,v):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or v[i][j]:
                return 0 
            v[i][j]=1 
            return 1+ dfs(i-1,j,v)+ dfs(i+1,j,v) + dfs(i,j-1,v) + dfs(i,j+1,v)
        
        area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not v[i][j]:
                    area = max(area,dfs(i,j,v))
        return area