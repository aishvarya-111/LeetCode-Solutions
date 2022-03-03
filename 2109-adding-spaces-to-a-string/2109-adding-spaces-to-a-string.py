class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = spaces[::-1]
        d = ""
        for i in range(len(s)):
            if len(spaces)>0 and spaces[-1] == i:
                d+=" "+ s[i]
                spaces.pop()
            else:
                d+=s[i]
        return d