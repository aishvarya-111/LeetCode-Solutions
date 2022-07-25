class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] 
        q = []
        
        if grid[0][0]==0:
            q = [[1,0,0]] 
            
        v = [[0]*n for i in range(n)]
        while q:
            dist,row,col = q.pop(0)
            if row == n-1 and col == n-1:
                return dist 
            for i,j in d:
                r = row + i
                c = col + j
                if r>=0 and r<n and c>=0 and c<n and grid[r][c]==0 and v[r][c] == 0:
                    q.append([dist+1,r,c])
                    v[r][c] = 1 
        return -1