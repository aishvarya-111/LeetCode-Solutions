class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1 
        ans = []
      
        for k in d:
            if d[k]>(n//3):
                ans.append(k)
        return ans