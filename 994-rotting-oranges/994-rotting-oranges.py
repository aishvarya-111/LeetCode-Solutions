class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time=0
        fresh,rot,minute =[0],[],0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rot.append([i,j])
                if grid[i][j]==1:
                    fresh[0]+=1 
                    
        def bfs(rt,ct,n,m,rot):
            
            if(rt<0 or rt==n or ct<0 or ct==m or grid[rt][ct]!=1):
                return
                   
            grid[rt][ct]=2
            rot.append([rt,ct])
            fresh[0]-=1
            
        sides = [[0,-1],[0,1],[1,0],[-1,0]]
       
        while rot and fresh[0]>0:
            t = len(rot)
            for i in range(t):
                r,c = rot.pop(0)
                bfs(r-1,c,n,m,rot)
                bfs(r+1,c,n,m,rot)
                bfs(r,c-1,n,m,rot)
                bfs(r,c+1,n,m,rot)
                
            minute+=1
            
        if fresh[0]!=0:
            return -1 
        return minute