class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ""
        b = ""
        for i in range(len(s)):
            if s[i]=='#':
                a = a[:-1]
            else:
                a+=s[i]
                
        for i in range(len(t)):
            if t[i]=='#':
                b = b[:-1]
            else:
                b+=t[i]
        return True if(a==b) else False