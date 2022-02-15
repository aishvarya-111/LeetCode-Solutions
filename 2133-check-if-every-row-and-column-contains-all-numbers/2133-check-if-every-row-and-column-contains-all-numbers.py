class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        p = [*range(1,n+1)]
        
        for i in matrix:
            if sorted(i)!=p:
                return False
        
        for j in zip(*matrix):
            if sorted(j)!=p:
                return False
        return True