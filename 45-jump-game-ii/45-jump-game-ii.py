class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l,r,res = 0,0,0
        while(r<len(nums)-1):
            far = 0
            for i in range(l,r+1):
                far = max(far,i+nums[i])
            l = r+1
            r = far
            res+=1
        return res