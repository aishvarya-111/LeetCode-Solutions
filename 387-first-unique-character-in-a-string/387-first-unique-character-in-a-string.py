class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1 
        ans=""
        for k,v in d.items():
            if v==1:
                ans = k 
                break
                
        for i in range(len(s)):
            if ans==s[i]:
                return i
        return -1