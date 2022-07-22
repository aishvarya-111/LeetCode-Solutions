class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = [0]*(max(max(nums1),max(nums2))+1)
        for i in nums1:
            d[i]+=1
        ans = set()
        for i in nums2:
            if d[i]>0:
                ans.add(i)
        return ans