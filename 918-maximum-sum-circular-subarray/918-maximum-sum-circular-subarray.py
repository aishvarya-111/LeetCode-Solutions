class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        def kadane(a):
            curr,end = 0,0
            for i in range(len(a)):
                curr = max(a[i],curr+a[i])
                end = max(end,curr)
            return end
        
        wrap = kadane(nums)
        s = sum(nums)
        for i in range(len(nums)):
            nums[i] = -nums[i]
        not_wrap = s + kadane(nums)
        return max(wrap,not_wrap)
        