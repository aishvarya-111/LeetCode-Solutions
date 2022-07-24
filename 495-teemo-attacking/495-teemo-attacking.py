class Solution:
    def findPoisonedDuration(self, time: List[int], d: int) -> int:
        c = 0
        for i in range(len(time)-1):
            c+= min(time[i+1]-time[i],d)
        return c+d