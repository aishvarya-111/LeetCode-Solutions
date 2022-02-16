class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for k in words:
            if s[i:i+len(k)] != k:
                return False
            i+=len(k)
            if i==len(s):
                return True
        return False