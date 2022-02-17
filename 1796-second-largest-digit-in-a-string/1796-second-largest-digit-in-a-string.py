class Solution:
    def secondHighest(self, s: str) -> int:
        ans = -1
        a = []
        for i in s:
            if i.isdigit():
                a.append(int(i))
        a = sorted(set(a))
        if (len(a)>1):
            ans = a[-2]
        return ans