class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i=0
        ls, rs = 0, sum(nums)
        while(i<len(nums)):
            rs-=nums[i]
            if ls==rs:
                break
            ls+=nums[i]
            i+=1 
            
        if(i>=len(nums)):
            return -1
        else:
            return i
        