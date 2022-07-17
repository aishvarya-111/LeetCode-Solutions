class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums1)):
            d[nums1[i]]=i
        
        ans = [-1]*len(nums1) 
        s = []
        for i in range(len(nums2)):
            while s and nums2[i]>s[-1]:
                t = s.pop()
                ans[d[t]] = nums2[i]
            if nums2[i] in nums1:
                s.append(nums2[i])
        return ans