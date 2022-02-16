class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if sorted(nums)==nums and len(nums)==len(set(nums)):
            return True
        for i in range(len(nums)-1):
            n = nums[:i]+nums[i+1:]
            if nums[i]>=nums[i+1] and sorted(n)==n and len(n)==len(set(n)):
                return True
        for i in range(1,len(nums)):
            n = nums[:i]+nums[i+1:]
            if nums[i]<=nums[i-1] and sorted(n)==n and len(n)==len(set(n)):
                return True
        return False
                