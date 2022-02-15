class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        r = 1
        for i in nums:
            if i==r:
                r+=1
        return r
            