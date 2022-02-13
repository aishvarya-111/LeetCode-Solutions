class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l=[]
        for j in range(len(colors)):
            for i in range(len(colors)-1,0,-1):
                if(colors[j]!=colors[i]):
                    l.append(abs(j-i))
                    break
        return max(l)