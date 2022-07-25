class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(arr, start, count):
            if start<0 or start>=len(arr) or count>=len(arr):
                return False
            if arr[start]==0:
                return True
            return dfs(arr, start+arr[start], count+1) or dfs(arr, start-arr[start], count+1)
        
        return dfs(arr, start, 0)