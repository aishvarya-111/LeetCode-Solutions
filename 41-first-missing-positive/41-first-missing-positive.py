class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #nums.sort()
        #r = 1
        #for i in nums:
        #    if i==r:
         #       r+=1
        #return r
        nums = set(nums)
        for i in range(1,max(nums)+2):
            if i not in nums:
                return i
        return 1