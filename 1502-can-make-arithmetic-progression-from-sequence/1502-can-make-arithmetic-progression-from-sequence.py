class Solution:
    def canMakeArithmeticProgression(self, a: List[int]) -> bool:
        if len(a)<3:
            return True
        n = len(a)
        d = max(a)-min(a)
        if d%(n-1)!=0:
            return False
        d=d//(n-1)
        if d==0:
            return True
        h = set()
        m = min(a)
        for i in range(n):
            h.add(m)
            m+=d
        if len(h)!=n:
            return False
        print(h)
        for i in h:
            if i not in a:
                return False
        return True