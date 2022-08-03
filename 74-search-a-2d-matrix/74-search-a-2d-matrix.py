class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        l,r = 0,n-1
        while(l<m and r>=0):
            if target==mat[l][r]:
                return True
            elif target>mat[l][r]:
                l+=1
            else:
                r-=1 
        return False