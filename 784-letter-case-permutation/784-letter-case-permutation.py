class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def dfs(s,t):
            if t == len(s):
                ans.append(s)
                return
            
            if s[t].isalpha():
                dfs(s[:t]+s[t].upper()+s[t+1:],t+1)
                dfs(s[:t]+s[t].lower()+s[t+1:],t+1)
            else:
                dfs(s,t+1)
        dfs(s,0)    
        return ans