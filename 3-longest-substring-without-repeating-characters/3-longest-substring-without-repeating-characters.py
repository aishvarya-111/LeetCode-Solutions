class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        ans = 0
        t = set()
        win=0
        l=0
        for i in range(len(s)):
            if s[i] not in t:
                t.add(s[i])
                win+=1 
            else:
                while s[i] in t:
                    t.remove(s[l])
                    l+=1
                    win-=1
                t.add(s[i])
                win+=1
            ans = max(win,ans)
        return ans