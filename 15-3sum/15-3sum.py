class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                m = nums[i]+nums[j]+nums[k]
                if m==0:
                    res.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                elif m>0:
                    k-=1 
                else:
                    j+=1 
        return res