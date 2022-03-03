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
                ans = max(ans,len(d))
                ind = d.index(i)
                d = d[ind+1:]+i
            
        return max(ans,len(d))