from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def com(ind,a):
            if len(a)==k:
                ans.append(a.copy())
                return
            
            for i in range(ind,n+1):
                a.append(i)
                com(i+1,a)
                a.pop()
        
        com(1,[])
        return ans