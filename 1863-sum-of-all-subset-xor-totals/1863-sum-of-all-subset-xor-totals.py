class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        Len = 0
        for i in nums:
            ans |= i
            Len+=1
        return ans*(2**(Len-1))