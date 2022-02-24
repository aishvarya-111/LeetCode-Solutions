class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for i in s:
            t+= str(ord(i)-96)
        for j in range(k):
            c = 0 
            for x in range(len(t)):
                c+= int(t[x])
            t = str(c)
        return c