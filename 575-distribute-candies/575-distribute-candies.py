class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        candyType = list(set(candyType))
        if len(candyType) >= n//2:
            ans = n//2
        else:
            ans = len(candyType)
        return ans