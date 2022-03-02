from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = list(permutations(nums))
        print(l)
        return l