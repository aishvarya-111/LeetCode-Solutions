class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #d = {}
        #for each in nums:
            #if each in d:
                #return each 
            #else:
                #d[each] = 1
        return (sum(nums) - sum(set(nums)))//(len(nums)-len(set(nums)))