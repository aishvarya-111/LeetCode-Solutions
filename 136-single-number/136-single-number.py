class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        nums = set(nums)
        return sum(nums)*2 - s
            
            