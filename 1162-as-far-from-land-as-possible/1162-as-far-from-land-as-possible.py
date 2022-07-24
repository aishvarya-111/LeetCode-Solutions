class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    
        if len(q)==m*n or len(q)==0:
            return -1
                    
        def bfs(r,c,d,q):
            if r<0 or r>=n or c<0 or c>=m or grid[r][c]==1:
                return
            
            grid[r][c]=1
            q.append((r,c,d+1))
            
        
        for r,c,d in q:
            bfs(r-1,c,d,q)
            bfs(r+1,c,d,q)
            bfs(r,c-1,d,q)
            bfs(r,c+1,d,q)
        
        return q[-1][-1]