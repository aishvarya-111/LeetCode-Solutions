class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            count=0
            if i-1<0 or grid[i-1][j]!=1:
                count+=1
            if i+1>=n or grid[i+1][j]!=1:
                count+=1   
            if j-1<0 or grid[i][j-1]!=1:
                count+=1  
            if j+1>=m or grid[i][j+1]!=1:
                count+=1
               
            return count
        
        n = len(grid)
        m = len(grid[0])
       
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    c+=dfs(i,j)
        return c