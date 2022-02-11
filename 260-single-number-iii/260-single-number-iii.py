class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums[0]
        dicts = {}
        for i in nums:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1                        
                
        s = []
        for k,v in dicts.items():
            if v == 1:
                s.append(k)
                
        return s
        