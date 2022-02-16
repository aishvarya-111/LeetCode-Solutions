from itertools import combinations
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        for i,j,k,l in combinations(range(len(nums)), 4):
            if nums[i] + nums[j] + nums[k] == nums[l]:
                res += 1
        return res  