class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=-float('inf')
        s=0
        for i in gain:
            s+=i
            n=max(n, s)
        return max(n,0)