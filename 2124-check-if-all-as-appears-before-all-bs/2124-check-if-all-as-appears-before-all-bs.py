class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s:
            return True
        else:
            for i in range(0,len(s)-1):
                if(s[i]=='b' and s[i+1]=='a'):
                    return False
            return True