class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            s = abs(nums[i])
            if nums[s-1]>0:
                nums[s-1] *= -1 
            else:
                res.append(abs(nums[i]))
        return res
            