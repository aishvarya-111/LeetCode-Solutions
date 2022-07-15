class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n!=(r*c):
            return mat
        a = []
        for i in range(m):
            for j in range(n):
                a.append(mat[i][j])
        k = 0
        print(a)
        ans=[]
        for i in range(r):
            p = []
            for j in range(c):
                if k<len(a):
                    p.append(a[k])
                    k+=1
            ans.append(p)
        return ans