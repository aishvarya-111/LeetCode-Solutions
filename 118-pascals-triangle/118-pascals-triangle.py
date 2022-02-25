class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        
        for i in range(numRows-2):
            l = res[-1]
            a = [1]
            for i in range(len(l)-1):
                a.append(l[i]+l[i+1])
            a.append(1)
            res.append(a)
        return res