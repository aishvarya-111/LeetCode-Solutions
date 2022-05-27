class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        d = 0
        for i in range(len(nums)):
            if i==0:
                if nums[i]>nums[i+1]:
                    d = 0
                    break
            elif i==len(nums)-1:
                if nums[i]>nums[i-1]:
                    d = i
                    break
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                d = i 
                break
        return d