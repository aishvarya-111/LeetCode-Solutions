from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        d = sorted(d.items(),key=lambda x:x[0],reverse=True)
        d = sorted(d,key=lambda x:x[1])
        res = []
        for k,v in d:
            for i in range(v):
                res.append(k)
        return res