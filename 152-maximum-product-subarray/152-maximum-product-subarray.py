class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mi_val = 1
        mx_val = 1
        ans = nums[0]
        for i in range(len(nums)):
            curr = nums[i]
            x = min(curr,mi_val*curr,mx_val*curr)
            y = max(curr,mi_val*curr,mx_val*curr)
            mi_val,mx_val = x,y
            ans = max(ans,mx_val)
        return ans