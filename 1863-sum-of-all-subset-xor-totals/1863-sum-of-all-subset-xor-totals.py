class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(nums):
            s = 0
            for i in nums:
                s^=i
            return s
        
        n = pow(2,len(nums))
        a,h=[[]],0
        for i in range(1,n):
            s = bin(i)[2:]
            s = s[::-1]
            t =[]
            for j in range(len(s)):
                if(s[j]=='1'):
                    t.append(nums[j])
            h+=xor(t)
        return h