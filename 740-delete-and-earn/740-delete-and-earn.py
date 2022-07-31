class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dic = collections.defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        nums = sorted(list(set(nums)))
        prev = 0
        prev2 = 0
        for i in range(len(nums)):
            curr = nums[i]*dic[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                temp = prev
                prev= max(curr+prev2,prev)
                prev2 = temp
            else:
                temp = prev
                prev = curr+prev
                prev2 = temp
        return prev