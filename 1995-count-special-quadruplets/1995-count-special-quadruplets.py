#from itertools import combinations
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count, ans, n = Counter(), 0, len(nums)
        for a in range(n-1, 0, -1):
            for b in range(a-1, -1, -1):
                ab = nums[a] + nums[b]
                ans += count[ab]
            for d in range(n-1, a, -1):
                da = nums[d] - nums[a]
                count[da] += 1
        return ans