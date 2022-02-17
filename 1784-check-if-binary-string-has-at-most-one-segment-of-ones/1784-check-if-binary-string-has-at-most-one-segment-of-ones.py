class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s.count('1')==1:
            return True
        c = s.count('1')
        count=0
        for i in range(0,len(s)):
            if i<len(s)-1 and s[i] == '1' and s[i+1]=='0':
                count+=1
                return c==count
            elif s[i]=='1':
                count+=1
        return c==count