class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1],reverse=True)
        res = 0 
        for i in boxTypes:
            if truckSize==0:
                break
            if truckSize>=i[0]:
                res+=(i[0]*i[1])
                truckSize-=i[0]
            else:
                res+=(truckSize*i[1])
                truckSize=0
        return res