class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            nums = int(num[i])
            if nums%2 != 0:
                return num[:i+1]
        return ""