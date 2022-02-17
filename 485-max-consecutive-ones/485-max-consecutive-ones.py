class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pc,c=0,0 
        for i in nums:
            if i == 1:
                c+=1
            else:
                c=0   
            pc = max(pc,c)
        return pc