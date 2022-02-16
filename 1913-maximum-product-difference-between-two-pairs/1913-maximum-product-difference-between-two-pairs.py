class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')
        
        max1 = float('-inf')
        max2 = float('-inf')
        
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
                
            if n >= max1:
                max2 = max1
                max1 = n
            elif n >= max2:
                max2 = n
        
        return (max1*max2 - min1*min2)