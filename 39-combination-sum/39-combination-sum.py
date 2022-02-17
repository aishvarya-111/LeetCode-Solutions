class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        
        def backtracking(i, target, path):
            if target == 0:
                ans.append(path)
                return
            if i == len(candidates) or target < candidates[i]:
                return
            backtracking(i, target - candidates[i], path + [candidates[i]]) 
            backtracking(i + 1, target, path) 
        ans = []
        backtracking(0, target, [])
        return ans