class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = sorted(nums)[::-1]
        if n == nums:
            return -1
        mn = nums[0]
        md = max(nums)
        for i in range(1,len(nums)):
            md = min(md,mn-nums[i])
            mn = min(mn,nums[i])
        return -md
            