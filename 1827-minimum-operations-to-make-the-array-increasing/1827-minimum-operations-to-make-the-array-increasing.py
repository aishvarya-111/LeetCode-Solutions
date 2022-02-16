class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        c=0
        pv = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=pv:
                c+=pv+1-nums[i]
                nums[i] = pv+1
            pv = nums[i]
        return c
                