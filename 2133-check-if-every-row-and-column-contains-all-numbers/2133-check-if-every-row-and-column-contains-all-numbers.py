class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        p = [*range(1,n+1)]
        
        for i in matrix:
            if sorted(i)!=p:
                return False
        
        for j in range(n):
            row=[]
            for k in range(n):
                row.append(matrix[k][j])
            if sorted(row)!=p:
                return False
        return True