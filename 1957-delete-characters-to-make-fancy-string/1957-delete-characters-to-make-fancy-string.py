class Solution:
    def makeFancyString(self, s: str) -> str:
        l = []
        for i in s:
            if len(l)<2:
                l.append(i)
            elif l[-2] != i or l[-1] != i:
                l.append(i)
        return "".join(l)