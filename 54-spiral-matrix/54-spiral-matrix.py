class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat),len(mat[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        di = 0
        x,y = 0,0
        vis = [[0]*m for i in range(n)]
        ans = []
        for i in range(n*m):
            ans.append(mat[x][y])
            vis[x][y] = 1
            cr = x + dx[di]
            cy = y + dy[di]
            
            if cr>=0 and cy>=0 and cr<n and cy<m and vis[cr][cy]==0:
                x = cr
                y = cy
            else:
                di = (di+1)%4
                x+=dx[di]
                y+=dy[di]
        return ans