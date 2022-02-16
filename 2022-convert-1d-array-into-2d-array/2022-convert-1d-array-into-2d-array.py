class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        a = []
        for i in range(0,len(original),n):
            a.append(original[i:i+n])
        return a