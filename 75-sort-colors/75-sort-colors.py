class Solution:
    def sortColors(self, n: List[int]) -> None:
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
        l,m,h=0,0,len(n)-1
        while(m<=h):
            if n[m]==0:
                n[l],n[m]=n[m],n[l]
                m+=1
                l+=1
            elif n[m]==1:
                m+=1
            elif n[m]==2:
                n[m],n[h]=n[h],n[m]
                h-=1
        
            