class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """z,o,t=0,0,0
        for i in nums:
            if i==0:
                z+=1
            elif i==1:
                o+=1
            else:
                t+=1
        for i in range(z):
            nums[i]=0
        for i in range(z,z+o):
            nums[i]=1
        for i in range(z+o,z+o+t):
            nums[i]=2
        """
        l,m,h = 0,0,len(nums)-1
        for i in range(len(nums)):
            if nums[m]==0:
                nums[m],nums[l]= nums[l],nums[m]
                m+=1
                l+=1
            elif nums[m]==1:
                m+=1
            elif nums[m]==2:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1 
        
        
            