class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        for i in range(len(nums)):
            cc=0
            if nums[i]-1 not in s:
                t = nums[i]
                while(t in s):
                    t+=1 
                    cc+=1
            c = max(c,cc)
        return c