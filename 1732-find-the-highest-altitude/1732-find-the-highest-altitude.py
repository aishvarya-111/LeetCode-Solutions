class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ph,h = 0,0
        for i in gain:
            h+=i
            if h>ph:
                ph=h
        return ph