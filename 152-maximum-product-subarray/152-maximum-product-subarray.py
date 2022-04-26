class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        p = 1
        mi_val = 1
        mx_val = 1
        ans = max(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                mi_val = 1
                mx_val = 1
            curr = nums[i]
            x = min(curr,mi_val*curr,mx_val*curr)
            y = max(curr,mi_val*curr,mx_val*curr)
            mi_val,mx_val = x,y
            ans = max(ans,mx_val)
        return ans