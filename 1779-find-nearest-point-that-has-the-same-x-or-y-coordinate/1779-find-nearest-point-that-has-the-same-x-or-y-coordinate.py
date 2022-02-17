class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx,mmd = -1,10**4
        for i in range(len(points)):
            if(x==points[i][0] or y==points[i][1]):
                md = abs(x-points[i][0])+abs(y-points[i][1])
                if(md<mmd):
                    mmd = md
                    idx = i
        return idx
                    
                