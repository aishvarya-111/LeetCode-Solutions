class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        c = nums[::-1]
        num = sorted(c)[::-1]
        num = num[:k]
        a = []
        for i in num:
            s = nums.index(i)
            a.append(s)
            nums[s] = 'x'
        a.sort()
        c = c[::-1]
        b = []
        for j in a:
            b.append(c[j])
        return b
        