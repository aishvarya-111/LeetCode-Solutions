class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        ans=[]
        for i in range(n):
            a = [1]
            res=1
            for j in range(i):
                res*=(i-j)
                res/=(j+1)
                a.append(int(res))
            ans.append(a)
        return ans