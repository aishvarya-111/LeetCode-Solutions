class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        l,ls=[],0
        s = sum(beans)
        n = len(beans)
        for i in range(len(beans)):
            a = s - (beans[i]*n) + ls
            n-=1
            ls+=beans[i]
            s-=beans[i]
            l.append(a)
        return min(l)
        