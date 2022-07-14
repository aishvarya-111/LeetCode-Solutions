class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans = [d[target-nums[i]],i]
                break
            else:
                d[nums[i]] = i  
        return ans