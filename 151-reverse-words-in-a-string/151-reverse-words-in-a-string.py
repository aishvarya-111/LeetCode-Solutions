class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        i=0
        while(i<len(s)):
            while(i<len(s)and s[i]==" "):
                i+=1
            if i>=len(s):
                break
            j=i+1
            while(j<len(s) and s[j]!=" "):
                j+=1 
            if ans=="":
                ans = s[i:j]
            else:
                ans = s[i:j] + " "+ ans
            i = j+1
        return ans