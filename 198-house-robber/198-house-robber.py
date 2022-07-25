class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        dp = [0]*len(nums)
        dp[-1],dp[-2],dp[-3] = nums[-1],nums[-2],nums[-3]+nums[-1]
       
        for i in range(len(nums)-4,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],nums[i]+dp[i+3])
       
        return max(dp[0],dp[1])