class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i=0
        ls, rs = 0, sum(nums)
        while(i<len(nums)):
            rs-=nums[i]
            if ls==rs:
                return i
            ls+=nums[i]
            i+=1 
            
        return -1
        