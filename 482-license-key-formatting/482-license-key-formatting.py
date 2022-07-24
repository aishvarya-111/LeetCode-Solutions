class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        t = ""
        c=0 
        
        for j in range(len(s)-1,-1,-1):
            if c==k and s[j]!='-':
                t+='-'
                c=0
            if s[j]!='-':
                t+=s[j].capitalize()
                c+=1 
          
        return t[::-1]