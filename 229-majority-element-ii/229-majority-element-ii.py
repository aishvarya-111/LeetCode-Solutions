class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        n = len(nums)
        fs,ss = 0,0
        fm,sm = nums[0],nums[1] 
        for i in range(n):
            if fm==nums[i]:
                fs+=1 
            elif sm== nums[i]:
                ss+=1 
            elif fs==0:
                fm=nums[i]
                fs+=1 
            elif ss==0:
                sm = nums[i]
                ss+=1
            else:
                fs-=1 
                ss-=1 
                
        fs = 0
        ss = 0
        for i in range(n):
            if nums[i]==fm:
                fs+=1 
            elif nums[i]==sm:
                ss+=1
        ans = []
        if fs > n//3:
            ans.append(fm)
        if ss > n//3:
            ans.append(sm)
        return ans