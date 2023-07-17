class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        y = m+n
        while m and n:
            if nums1[m-1]>=nums2[n-1]:
                nums1[y-1]=nums1[m-1]
                m=m-1
            else:
                nums1[y-1]=nums2[n-1]
                n=n-1
            y=y-1
            
        if n:
            for i in range(n):
                nums1[i]=nums2[i]
                
            
        