class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)==1:
            return 1
        
        ps,count = 0,1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count = 1
            ps = max(ps,count)   
        return ps