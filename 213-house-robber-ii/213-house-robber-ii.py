class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(nums):
            n = len(nums) 
            dp=[-1]*n
            dp[0] = nums[0]
            for i in range(1,n):
                pick = nums[i]
                if i>1:
                    pick+=dp[i-2]
                notpick = dp[i-1]
                dp[i] = max(pick,notpick)
            return dp[n-1]
        
        a1 = nums[1:]
        a2 = nums[:len(nums)-1]
        return max(solve(a1),solve(a2))
        