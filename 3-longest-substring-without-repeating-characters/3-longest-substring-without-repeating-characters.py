class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        ans= 0
        d = ""
        for i in s:
            if i not in d:
                d+=i
            else:
                ind = d.index(i)
                d = d[ind+1:]+i
            ans = max(ans,len(d))
        return ans