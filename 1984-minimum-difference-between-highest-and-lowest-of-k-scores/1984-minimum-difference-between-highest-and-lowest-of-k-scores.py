class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        nums.sort(reverse=True)
        mi = nums[0]
        for i in range(len(nums)-k+1):
            m = nums[i] - nums[i+k-1]
            if m<mi:
                mi=m
        return mi