from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        m = 0
        count = defaultdict(int)
        ans = 0
        while(j<len(s)):
            count[s[j]]+=1 
            m = max(count.values())
            j+=1
            if j-i-m>k:
                count[s[i]]-=1 
                m = max(count.values())
                i+=1 
            ans = max(ans,j-i)
        return ans