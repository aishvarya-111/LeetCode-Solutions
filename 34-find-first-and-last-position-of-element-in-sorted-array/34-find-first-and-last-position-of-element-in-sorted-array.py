class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(nums,target,n):
            l,r = 0,n-1
            while(l<=r):
                m = (l+r)//2
                if nums[m]==target and (m==0 or nums[m-1]!=nums[m]):
                    return m
                elif nums[m]>=target:
                    r = m-1
                else:
                    l = m+1
            return -1
            
        def right(nums,target,n):
            l,r = 0,n-1
            while(l<=r):
                m = (l+r)//2
                if nums[m]==target and (m==n-1 or nums[m+1]!=nums[m]):
                    return m
                elif nums[m]>target:
                    r = m-1
                else:
                    l = m+1
                
            return -1
        
        l = left(nums,target,len(nums))
        r = right(nums,target,len(nums))
        return [l,r]