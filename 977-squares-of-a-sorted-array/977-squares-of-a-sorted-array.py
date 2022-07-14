class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [0]*(10**4+5)
        m = nums[0]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
            l[nums[i]]+=1
            m = max(m,nums[i])
        j=0   
        for i in range(m+1):
            while(l[i]!=0):
                nums[j] = i*i
                j+=1
                l[i]-=1
        return nums