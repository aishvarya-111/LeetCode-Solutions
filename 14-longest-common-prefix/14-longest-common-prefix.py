class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = max(strs)
        b = min(strs)
        i,j=0,0
        result = ""
        while(i<len(a) and i<len(b)):
            if(a[i]!=b[i]):
              break
            result = result + a[i]
            i=i+1
              
        return result
              