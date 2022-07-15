class Solution:
    def canMakeArithmeticProgression(self, a: List[int]) -> bool:
        if len(a)<3:
            return True
        a.sort()
        for i in range(1,len(a)-1):
            if a[i]-a[i-1]!=a[i+1]-a[i]:
                return False
        return True