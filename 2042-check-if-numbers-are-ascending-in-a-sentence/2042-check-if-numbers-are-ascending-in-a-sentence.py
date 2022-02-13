class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = list(s.split())
        pn = -1
        for i in l:
            if i.isnumeric() and int(i)>pn:
                pn = int(i)
            elif i.isnumeric() and int(i)<=pn:
                return False
        return True