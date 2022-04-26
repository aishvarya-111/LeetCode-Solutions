class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            s = abs(nums[i])
            if nums[s-1]>0:
                nums[s-1]*= -1 
        for i in range(len(nums)):
            if nums[i]>0:
                a.append(i+1)
        return a