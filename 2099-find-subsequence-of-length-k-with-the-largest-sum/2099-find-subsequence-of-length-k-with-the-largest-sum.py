class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = list(enumerate(nums))
        l = sorted(l, reverse=True, key=lambda x: x[1])
        l = l[:k]
        l.sort()
        return [i[1] for i in l]