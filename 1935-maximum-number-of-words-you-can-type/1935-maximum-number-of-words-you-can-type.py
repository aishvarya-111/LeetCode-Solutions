class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = list(text.split())
        c=0
        for i in l:
            b = 0
            for j in brokenLetters:
                if j not in i:
                    b+=1
            if b == len(brokenLetters):
                c+=1
        return c
                