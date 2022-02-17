class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pc,c=0,0 
        for i in nums:
            if i == 1:
                c+=1
            else:
                pc = max(pc,c)
                c = 0
        return max(pc,c)