class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        d,c = 0,0
        for i in range(2,len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                d+=1
                c+=d
            else:
                d=0
        return c