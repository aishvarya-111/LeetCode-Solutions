class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ls = 0
        s = sum(nums)
        for i in range(len(nums)):
            rs = s - ls - nums[i]
            if(rs==ls):
                return i
            ls+=nums[i]
        return -1