class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1 
        ans = [0]*(len(nums))
        while(l<=r):
            a,b = abs(nums[l]),abs(nums[r])
            if a>b:
                ans[r-l] = a*a 
                l+=1
            else:
                ans[r-l]=b*b
                r-=1 
        return ans