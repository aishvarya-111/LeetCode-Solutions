class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s = 0
        for k,v in d.items():
            if v==1:
                s+=k
        return s