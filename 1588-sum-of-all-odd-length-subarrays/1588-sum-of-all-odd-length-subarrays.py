class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        a = 0
        n = len(arr)
        for i in range(len(arr)):
            t = (n-i)*(i+1)
            if t%2:
                t = t//2 + 1
            else:
                t = t//2 
            a+=(t*arr[i])
        return a
            