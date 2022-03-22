class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end,nums):
            while(start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        
        n,k = len(nums) , k% len(nums)
        if k:
            reverse(0,n-1,nums)
            reverse(0,k-1,nums)
            reverse(k,n-1,nums)