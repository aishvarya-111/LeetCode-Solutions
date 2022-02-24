class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j = 0
        for i in range(len(word)):
            if word[i]==ch:
                j=i+1
                break

        return word[:j][::-1] + word[j:]