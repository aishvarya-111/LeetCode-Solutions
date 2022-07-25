from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums,ans,ind):
            if ind==len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(ind,len(nums)):
                nums[i],nums[ind]=nums[ind],nums[i]
                perm(nums,ans,ind+1)
                nums[i],nums[ind]=nums[ind],nums[i]
            
        
        n = len(nums)
        ans =[]
        perm(nums,ans,0)
        return ans