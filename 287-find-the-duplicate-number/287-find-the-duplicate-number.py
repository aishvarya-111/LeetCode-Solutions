class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - len(set(nums))
        m = (sum(nums) - sum(set(nums)))//n
        return m