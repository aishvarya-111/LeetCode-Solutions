class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s,m=0,nums[0]
        for i in nums:
            if s<=0:
                s=0
            s+=i
            m = max(s,m)
        return m