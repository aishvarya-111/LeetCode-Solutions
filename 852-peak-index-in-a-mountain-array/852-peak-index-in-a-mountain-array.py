class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 1,len(arr)-1
        while(l<=r):
            m = (l+r)//2
            if arr[m]>arr[m-1] and arr[m]>arr[m+1]:
                return m
            elif arr[m]>arr[m-1] and arr[m]<arr[m+1]:
                l=m+1
            elif arr[m]<arr[m-1] and arr[m]>arr[m+1]:
                r = m-1
        return -1
        