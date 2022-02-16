class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        a = ''
        for i in s:
            if i in v:
                a+=i
        a=a[::-1]
        c = 0
        for i in range(len(s)):
            if s[i] in v:
                s = s[:i]+a[c]+s[i+1:]
                c+=1
        return s