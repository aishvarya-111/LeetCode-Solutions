class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [[1],[1,1]]
        
        for i in range(rowIndex+1):
            l = res[-1]
            a = [1]
            for j in range(len(l)-1):
                a.append(l[j]+l[j+1])
            a.append(1)
            res.append(a)
        return res[rowIndex]