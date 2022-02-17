class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mx = 0
        for i in rectangles:
            m = min(i[0],i[1])
            if m>mx:
                mx = m
                count=1
            elif m==mx:
                count+=1
        return count
                