class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = []
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    
        if len(q)==n*m or len(q)==0:
            return mat
        
        v = [[0]*m for i in range(n)]
        
        def dfs(n,m,row,col,v,mat,node):
            if row < 0 or row >=n or col<0 or col >= m or v[row][col] or mat[row][col] == 0:
                return
            
            mat[row][col] = 1 + mat[node[0]][node[1]]
            q.append((row, col))
            v[row][col]=1
        
        
        while q:
            node = q.pop(0)
            row,col = node[0],node[1]
            dfs(n,m,row-1,col,v,mat,node)
            dfs(n,m,row+1,col,v,mat,node)
            dfs(n,m,row,col-1,v,mat,node)
            dfs(n,m,row,col+1,v,mat,node)
        
        return mat