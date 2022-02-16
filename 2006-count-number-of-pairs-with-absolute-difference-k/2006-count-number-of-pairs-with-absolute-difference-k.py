from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        for key,value in c.items():
            if key + k in c:
                ans += value * c[key + k]
        return ans