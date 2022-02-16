class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        for ch in s:
            if ch in {"a","e","i","o","u","A","E","I","O","U"}:
                vowel.append(ch)
        ans=[]
        for ch in s:
            if ch not in "aieouAEIOU":
                ans.append(ch)
            else :
                ans.append(vowel.pop())
        return "".join(ans)