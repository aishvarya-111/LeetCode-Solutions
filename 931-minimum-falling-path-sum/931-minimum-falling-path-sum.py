class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        for i in range(1,n):
            for j in range(n):
                temp = mat[i-1][j]
                if j>0:
                    temp = min(temp,mat[i-1][j-1])
                if j<n-1:
                    temp = min(temp,mat[i-1][j+1])
                mat[i][j]+=temp 
        
        return min(mat[n-1])