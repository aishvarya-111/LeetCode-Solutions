class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for k,v in d.items():
            if v==1:
                return k
