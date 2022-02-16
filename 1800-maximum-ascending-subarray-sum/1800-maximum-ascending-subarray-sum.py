class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s,ps = nums[0],0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                ps = max(ps,s)
                s = 0
            s+=nums[i]
        return max(ps,s)