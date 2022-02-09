class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=0
        d=[]
        for i in range(len(nums)):
            if nums[i]+k in nums[i+1:] and nums[i] not in d:
                d.append(nums[i])
                c+=1
        return c
        