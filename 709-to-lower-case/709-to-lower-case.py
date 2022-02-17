class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        
        for x in s:
            if ord(x) >= 65 and ord(x) <= 90:
                ans += chr(ord(x) + 32)
            else:
                ans += x      
        return ans
    