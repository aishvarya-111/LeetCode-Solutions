class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ss = sum(set(nums))
        s = (n*(n+1))//2 - ss
        m = sum(nums) - ss
        return [m,s]