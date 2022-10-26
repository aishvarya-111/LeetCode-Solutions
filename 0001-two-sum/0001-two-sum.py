class Solution(object):
    def twoSum(self, nums, target):

        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans = [d[target-nums[i]],i]
                break
            else:
                d[nums[i]] = i
        return ans