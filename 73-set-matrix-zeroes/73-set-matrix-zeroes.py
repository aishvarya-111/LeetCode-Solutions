class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(m)
        c = len(m[0])
        flag = False
        for i in range(r):
            if m[i][0]==0:
                flag=True
            for j in range(1,c):
                if m[i][j]==0:
                    m[0][j]=0
                    m[i][0]=0
        
        for i in range(1,r):
            for j in range(1,c):
                if m[0][j]==0 or m[i][0]==0:
                    m[i][j]=0
        if m[0][0]==0:
            for j in range(c):
                m[0][j]=0
        if flag:
            for i in range(r):
                m[i][0]=0
        
        