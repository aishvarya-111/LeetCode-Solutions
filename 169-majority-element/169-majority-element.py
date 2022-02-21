class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        all_freq = {}
  
        for i in nums:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
         
        m = max(all_freq.values())
        
        for i,v in all_freq.items():
            if v==m:
                return i
        