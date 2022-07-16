class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        a = (c[0][0])
        b = (c[0][1])
        cc = (c[1][0])
        d = (c[1][1])
        x = (a-cc)
        y = (b-d)
        
        for i in range(2,len(c)):
            e = (c[i][0]) - (c[i-1][0])
            g = (c[i][1]) - (c[i-1][1])
            if x*g != y*e:
                return False
        return True