class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = []
        t = 0
        for i in range(len(nums)):
            t = t+nums[i]
            s.append(t)
        return s