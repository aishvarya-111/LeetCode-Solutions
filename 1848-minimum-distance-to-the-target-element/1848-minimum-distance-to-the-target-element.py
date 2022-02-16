class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m = 1000
        for i in range(len(nums)):
            if nums[i]==target:
                m = min(m,abs(i-start))
        return m