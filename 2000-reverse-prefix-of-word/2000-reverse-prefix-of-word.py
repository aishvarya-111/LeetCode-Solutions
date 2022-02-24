class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = ""
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i]!=ch:
                s+=word[i]
            else:
                s+=word[i]
                break

        return s[::-1] + word[i+1:]