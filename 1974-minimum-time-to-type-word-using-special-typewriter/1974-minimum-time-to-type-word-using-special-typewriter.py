class Solution:
    def minTimeToType(self, word: str) -> int:
        c = 0
        temp = 'a'
        for i in word:
            d = abs(ord(i) - ord(temp)) 
            c+= min(d,26-d) + 1 
            temp = i
        return c