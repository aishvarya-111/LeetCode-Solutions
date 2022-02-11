class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a =[]
        for i in range(len(nums)):
            if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
                a.append(nums[i])
        return a
        