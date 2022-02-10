class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if(len(nums)==1 and nums[0]!=k):
            return 0
        d = {}
        s,count=0,0
        for i in nums:
            s+=i
            if s==k:
                count+=1
            if s-k in d:
                count+=d[s-k]    
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return count
                