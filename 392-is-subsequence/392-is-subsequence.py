class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n,m= len(s),len(t)
        x,i = 0,0
        
        while(x<n and i<m):
            if(s[x] == t[i]):
                x+=1
            i+=1
        if(x == n):
            return True
        return False
        