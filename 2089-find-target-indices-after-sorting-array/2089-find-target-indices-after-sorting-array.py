class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i,r = 0,[]
        while(i<len(nums) and nums[i]<=target):
            if nums[i]==target:
                r.append(i)
            i+=1
        return r