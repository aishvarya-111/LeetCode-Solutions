class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,h = 0,n-1
        while l<=h:
            m = (l+h)//2
            if nums[m]==target:
                return m
            elif nums[l]<=nums[m]:
                if target>=nums[l] and target<=nums[m]:
                     h = m-1
                else:
                    l = m+1
            else:
                if target>=nums[m] and target<=nums[h]:
                    l = m+1
                else:
                    h = m-1 
        
        return -1